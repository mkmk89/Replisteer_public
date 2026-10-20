---
title: Dataverse / Dynamics 365
linkTitle: Dataverse
weight: 1
---

The Dataverse connector reads with FetchXML and writes to tables or runs on-demand workflows, in Dataverse and Dynamics 365 (Sales, Customer Service, Field Service, …). In XrmToolBox it works with any environment XrmToolBox can connect to, online or on-premises.

## Connections

- **In XrmToolBox**, a Dataverse source or target uses an XrmToolBox connection: choose it with **Choose...** next to *Connection*. Any authentication XrmToolBox supports works.
- **Outside XrmToolBox** (the command line runner), the connection is a [Dataverse ServiceClient connection string](https://learn.microsoft.com/power-apps/developer/data-platform/xrm-tooling/use-connection-strings-xrm-tooling-connect). For unattended runs, use an app registration with a client secret or certificate:

  ```text
  AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=<application id>;ClientSecret=<client secret>
  AuthType=Certificate;Url=https://contoso.crm4.dynamics.com;ClientId=<application id>;Thumbprint=<certificate thumbprint>
  ```

  The app registration must be added to the environment as an **application user** with a security role that allows what the project does (Power Platform admin center > *Environments* > your environment > *Settings* > *Users + permissions* > *Application users*).

{{< deduplica "dataverse-connector" >}}

## Reading (source)

The query is FetchXML. See [Source: FetchXML](../../xrmtoolbox/source/#dataverse-fetchxml) for how attributes, lookups, choices and linked tables become fields.

### Source options

**Options...** on the Source tab:

| Option | Default | Meaning |
| --- | --- | --- |
| **Source page size** | 500 | Records per request (at most 5,000). A `count` attribute in the FetchXML wins. |

## Writing (target)

| Operation | What happens |
| --- | --- |
| Insert | One `Create` request. The new record's reference (`table:guid`) is available to later steps as `V_<step>_ID`. |
| Update | The records matching the criteria are retrieved, then each is updated. |
| Upsert | Like update; when nothing matches, a record is created. (Replisteer matches with its own criteria; it does not need alternate keys.) |
| Delete | Every matching record is deleted. |
| Execute | Runs an on-demand workflow: map `WorkflowId` (the workflow's id) and `EntityId` (the record, as a GUID or `table:guid`). Set the target's *Writes to* to *On-demand workflow*. |

When several records match an update or delete, they are sent in `ExecuteMultiple` batches; the first failure stops the step and is reported as `Request 3 of 200 failed: …`.

### Target options

**Options...** on the Targets tab:

| Option | Default | Meaning |
| --- | --- | --- |
| **Batch size** | 200 | Requests per `ExecuteMultiple` call when several records match (at most 1,000). |
| **Send date/time values as UTC** | off | Dates are sent as UTC instead of local time. Use it when the source dates are already UTC. |
| **Do not send empty values** | off | Columns whose value is null are left out of the request instead of being cleared. |
| **Do not send unchanged values (update)** | off | Before an update, the current values are read and columns that would not change are left out. Fewer changes means fewer plug-in executions and audit entries. |
| **Remove control characters from text** | off | Removes invisible control characters from text columns (multi-line text keeps line breaks and tabs). Helps with data copied from legacy systems. |
| **Bypass custom plug-ins and workflows** | off | Sets `BypassCustomPluginExecution` on every request, so custom synchronous plug-ins and real-time workflows do not run. Requires the *prvBypassCustomPlugins* privilege (System Administrators have it). |

## Values written to Dataverse columns

Formulas produce text, numbers, dates, TRUE/FALSE or null. The connector converts them to the column type, so values from CSV files and SQL text columns work without explicit conversions:

| Column type | Accepted values |
| --- | --- |
| Text, multi-line text | Any value, as text. |
| Whole number, decimal, float, currency | Numbers, or text holding a number with `.` as decimal separator (`"12.50"`). `"12,50"` is rejected with a hint to use `NUMBER(value, ",")`. |
| Yes/No | TRUE/FALSE, `"true"`/`"false"`, numbers (0 is No), or the labels in any language of the environment (`"Yes"`, `"Nein"`). |
| Date and time | Dates, or text in ISO format (`2024-01-31`, `2024-01-31 13:00`), `yyyy/MM/dd` or `dd.MM.yyyy`. Other formats: `DATETIME(value, "MM/dd/yyyy")`. |
| Choice (option set), status, status reason | The numeric value (`2`, `"2"`), or a label in any language of the environment (case-insensitive). |
| Choices (multi-select) | `"1;3"`, `"Red;Blue"` (`;` or `,` separated values or labels), or `ARRAY("Red", "Blue")`. |
| Lookup | `table:guid` (from a Dataverse source or `V_<step>_ID`), `CreateEntityReference("account", id)`, or a bare GUID when the lookup can only point to one table. |
| Customer, owner (polymorphic lookups) | `table:guid` or `CreateEntityReference(...)`: the table is required (`"team:…"`, `"account:…"`). |
| Party list (activity parties: To, Cc, Required attendees) | `CreatePartyList(CreateEntityReference("contact", id), …)`, an `ARRAY()` of references, or `table:guid;table:guid` text. |
| Unique identifier | A GUID, with or without braces; a `table:guid` gives its GUID. |

An empty value (null or empty text) **clears** the column, unless *Do not send empty values* is on. A value that cannot be converted fails the row with a message such as `Column 'revenue' expects a number, got 'abc'`.

## Lookups to other records

To link a record to another one, write a reference to the lookup column. The usual ways:

| Situation | Formula for the lookup column |
| --- | --- |
| The source is Dataverse: copy the reference as it is | `parentcustomerid` |
| Find the account by a business key in the target environment | `CreateEntityReference("account", LOOKUP("CRM", "account", "accountnumber", "accountid", customer_no))` |
| The account was created by step 1 of the same row | `V_1_ID` |
| A GUID from a SQL or CSV column, for a lookup to one table | `crm_accountid` |

When copying between environments, prefer looking records up by a business key: GUIDs usually differ between environments.

## Reading with LOOKUP

`LOOKUP("CRM", "<table>", "<search column>", "<result column>", value)` queries the table of a Dataverse target. Use logical names. Asking for the table's primary key (`accountid`) returns the GUID as text. `XLOOKUP` returns TRUE when exactly one record matches. Each call is one query; put lookups used by several steps in a [variable](../../xrmtoolbox/variables/) so they run once per row.
