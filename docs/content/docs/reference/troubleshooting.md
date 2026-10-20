---
title: Troubleshooting
weight: 2
---

## In XrmToolBox

{{% details title="The tool does not appear in the Tool Library" closed="true" %}}
Replisteer needs XrmToolBox 1.2023.10.67 or later. Update XrmToolBox (*Help > Check for updates*, or download the latest version).
{{% /details %}}

{{% details title="Column names are red, or 'Column ... does not exist'" closed="true" %}}
The name is not in the loaded target columns. Click **Load columns** (Targets tab) or **Load fields** (Steps tab), and check the spelling: Dataverse columns use logical names (`emailaddress1`, not *Email*).
{{% /details %}}

{{% details title="A formula uses a field that 'will be empty'" closed="true" %}}
The name is not a source field or variable. Load the source fields (Source tab, **Load fields**) and check the spelling. Names with spaces or special characters need brackets: `[First Name]`. Linked-table columns of FetchXML keep their alias: `acc.accountnumber`.
{{% /details %}}

{{% details title="'... expects a number, got 12,50'" closed="true" %}}
The value uses a decimal comma. Convert it: `NUMBER(price, ",")`. Numbers in text use `.` as decimal separator; Replisteer never guesses because `1,500` could be one and a half or fifteen hundred.
{{% /details %}}

{{% details title="A lookup column fails: 'can reference account, contact; use CreateEntityReference'" closed="true" %}}
The column can point to several tables (customer, owner, regarding), so a bare GUID is not enough. Say which table: `CreateEntityReference("account", id)`.
{{% /details %}}

{{% details title="An update or upsert changes nothing" closed="true" %}}
No record matches all match criteria. Preview the step and compare the criteria values with the target data: text must match exactly (the comparison in Dataverse follows its own rules for case), and `"007"` is not `"7"`. Trim and normalise values in the criteria, for example `LOWERCASE(TRIM(email))`.
{{% /details %}}

{{% details title="An upsert creates duplicates" closed="true" %}}
Upserts match on the criteria you give. Make sure they identify one record (a business key), and that the inserted record gets the same values the criteria look for: map the key column too.
{{% /details %}}

{{% details title="Plug-ins slow a migration down, or fail it" closed="true" %}}
On the target's **Options...**, check *Bypass custom plug-ins and workflows* (requires the *prvBypassCustomPlugins* privilege) and *Do not send unchanged values*, which avoids updates that change nothing.
{{% /details %}}

{{% details title="Passwords are missing after opening a project" closed="true" %}}
The project was saved by another Windows account, on another computer, or without passwords. Enter them again in the SQL Server connection dialog. See [Passwords and secrets](../../xrmtoolbox/project-files/#passwords-and-secrets).
{{% /details %}}

## Command line

{{% details title="Windows protected your PC" closed="true" %}}
The runner is not code-signed yet. Choose **More info > Run anyway**, or unblock the downloaded zip before extracting it (right-click > **Properties** > **Unblock**).
{{% /details %}}

{{% details title="'needs a connection string'" closed="true" %}}
Outside XrmToolBox every Dataverse connection needs a connection string, and SQL Server connections need one when their password is not readable. The message says the exact option and environment variable to use. See [Connection strings](../../command-line/connections/).
{{% /details %}}

{{% details title="Connecting to Dataverse fails" closed="true" %}}
Check the `Url` (the environment address, `https://<org>.crm<n>.dynamics.com`), the application id and the secret (secrets expire). The app registration must be an application user of the environment with a security role. `replisteer validate` tests the connection without writing anything.
{{% /details %}}

{{% details title="SQL Server: 'The certificate chain was issued by an authority that is not trusted'" closed="true" %}}
The server uses a certificate the computer does not trust (common for on-premises and development servers). Add `TrustServerCertificate=true` to the connection string, or install the server's certificate.
{{% /details %}}

{{% details title="The scheduled task shows 0x3" closed="true" %}}
The project or its connections are not valid and nothing ran. Run the task's command in a Command Prompt to see the message, or open the log file.
{{% /details %}}


## Still stuck?

[Open an issue](https://github.com/mkmk89/Replisteer_public/issues/new/choose) on GitHub. Run with `--output result.json` (or export the log in XrmToolBox) and include the messages. Remove connection details first: Replisteer never writes secrets to its output, but your data may be in the source values of failed rows.
