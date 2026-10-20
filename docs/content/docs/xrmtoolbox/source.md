---
title: Source
weight: 2
---

The **1. Source** tab defines where rows are read from. Every row of the source runs through the steps once.

| Setting | Meaning |
| --- | --- |
| **Name** | The name of the source connection (default `Source`). The command line runner uses it to find its connection string. |
| **Source type** | *Dataverse / Dynamics 365*, *SQL Server* or *CSV file*. |
| **Connection** | Which environment, database or file to read. **Choose...** (Dataverse) or **Configure...** (SQL Server, CSV) changes it. |
| **Options...** | Dataverse only: the page size used to read records (see [Dataverse](../../connectors/dataverse/#source-options)). |
| **Query** | FetchXML for Dataverse, a SQL query for SQL Server. A CSV source has no query: every row of the file is read. |

**Insert query for a table...** lists the tables (or views) of the connection and writes a query that reads all their columns, as a starting point. **Load fields** reads the field list of the query, without reading its rows, and fills **Source fields** with the name, type and display name of every field the query returns. Load the fields before mapping: the field panel of the Steps tab, *Map same names* and the validation of formulas use them.

## Dataverse: FetchXML

Write the query as FetchXML, for example in [FetchXML Builder](https://fetchxmlbuilder.com/) (another XrmToolBox tool) and paste it here:

```xml
<fetch>
  <entity name="contact">
    <attribute name="fullname" />
    <attribute name="emailaddress1" />
    <attribute name="parentcustomerid" />
    <attribute name="statecode" />
    <filter>
      <condition attribute="statecode" operator="eq" value="0" />
    </filter>
    <link-entity name="account" from="accountid" to="parentcustomerid" link-type="outer" alias="acc">
      <attribute name="accountnumber" />
    </link-entity>
  </entity>
</fetch>
```

How the result becomes source fields:

- Every attribute is a field with its logical name: `fullname`, `emailaddress1`.
- **Lookups** have the value `table:guid` (for example `account:b9564ad3-…`), which can be written to another lookup column as it is. A second field `<name>name` holds the display name of the referenced record: `parentcustomeridname`.
- **Choices**, **yes/no** columns and **multi-select choices** have their numeric value (`1;3` for multi-select). The `<name>name` field holds the label in the user's language: `statecodename`.
- **Linked tables** are prefixed with their alias: `acc.accountnumber`. Give every `link-entity` an explicit `alias` so the names stay stable; without one Replisteer uses `<table><n>`, for example `account1`.
- Columns with an `alias` attribute (including aggregates) use the alias as their name.
- The primary key of the main table is always available as `<table>id`, for example `contactid`, even when it is not selected.

{{< deduplica "source-fetchxml" >}}

**Paging.** Replisteer reads all records page by page. The page size is the `count` attribute of the FetchXML when present, otherwise the page size in **Options...** (500 by default), and at most 5,000. Queries with `top` or `aggregate="true"` are read in a single request.

## SQL Server: SQL query

Any query that returns rows works: a `SELECT`, a view, or a stored procedure call (`EXEC dbo.GetChanges`).

```sql
SELECT c.Id, c.FirstName, c.LastName, c.Email, a.AccountNumber
FROM dbo.Contacts AS c
LEFT JOIN dbo.Accounts AS a ON a.Id = c.AccountId
WHERE c.ModifiedOn >= DATEADD(day, -1, SYSUTCDATETIME())
```

Every column of the result is a field with its column name; give computed columns an alias (`AS FullName`). *Load fields* asks SQL Server for the columns without running the query; procedures that build their result in temporary tables sometimes cannot answer that. The run itself still works, map the columns by name. Values keep their SQL types: numbers stay numbers, dates stay dates. The command timeout of the connection (30 seconds by default) applies to the query.

## CSV file

The whole file is read; there is no query. With a header row the fields are named after the header (blank names become `Column3`, repeated names get `_2`, `_3`). Without a header they are `Column1`, `Column2`, and so on. Every value is text; see [CSV files](../../connectors/csv/) for how text that holds numbers and dates behaves in formulas.
