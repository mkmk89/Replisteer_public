---
title: Connection strings
weight: 3
---

Outside XrmToolBox, every connection of the project (the source and **every** target, including targets only used by `LOOKUP()`) needs what it needs to connect. The runner looks in these places, in this order, and uses the first it finds:

1. `--source` and `--target` options.
2. The `--connections` file.
3. Environment variables: `Connection__<name>__ConnectionString`.
4. The project file itself.

When a connection has none, the runner stops before connecting to anything and says how to give it:

```text
Error: Target 'CRM Prod' (Dataverse) needs a connection string: Dataverse connections of the XrmToolBox tool cannot be used outside XrmToolBox. Give it with --target "CRM Prod=<connection string>", in the --connections file, or as Connection__CRM_Prod__ConnectionString.
Error:   e.g. AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=<application id>;ClientSecret=<client secret>
Nothing was run. See 'replisteer help' for all options.
```

## What each connection needs

| Connector | Connection string | When it is needed |
| --- | --- | --- |
| Dataverse | [ServiceClient connection string](#dataverse) | Always. |
| SQL Server | [SQL connection string](#sql-server) | When the project has no usable one: saved without password, or encrypted for another Windows account. |
| CSV file | The file path | Only to use another file than the one saved in the project. |

### Dataverse

A [Dataverse ServiceClient connection string](https://learn.microsoft.com/power-apps/developer/data-platform/xrm-tooling/use-connection-strings-xrm-tooling-connect). For scheduled and unattended runs use an **app registration** (service principal):

```text
AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=<application id>;ClientSecret=<client secret>
AuthType=Certificate;Url=https://contoso.crm4.dynamics.com;ClientId=<application id>;Thumbprint=<certificate thumbprint>
```

{{% details title="Setting up an app registration" closed="true" %}}

1. In the Azure portal, open **Microsoft Entra ID > App registrations > New registration**. Give it a name (for example `Replisteer`) and register it. Copy the **Application (client) ID**.
2. Under **Certificates & secrets**, create a **client secret** and copy its value (or upload a certificate).
3. In the [Power Platform admin center](https://admin.powerplatform.microsoft.com/), open the environment, then **Settings > Users + permissions > Application users > New app user**. Add the app registration and give it a security role that allows what the project reads and writes.
4. Use the environment URL, the application id and the secret in the connection string.

Client secrets expire: note the expiry date, and run `replisteer validate` after replacing one.

{{% /details %}}

The ServiceClient also supports interactive sign-in with a user account (`AuthType=OAuth`, with `LoginPrompt=Auto`), which needs someone to sign in and so only suits attended runs; see Microsoft's connection string documentation for its options.

### SQL Server

A standard SQL Server connection string:

```text
Server=sql01;Database=erp;User ID=replisteer;Password=<password>;Encrypt=true;TrustServerCertificate=true
Server=myserver.database.windows.net;Database=dw;User ID=replisteer;Password=<password>;Encrypt=true
Server=sql01;Database=erp;Integrated Security=true;TrustServerCertificate=true
```

With `Integrated Security=true` the runner signs in as the Windows account it runs as.

### Saved SQL Server passwords

The XrmToolBox tool saves SQL Server connection strings encrypted for your Windows account (unless that is turned off on its Project tab). The runner decrypts them when it runs **on Windows, as the same Windows account**, so a project you saved can run on your computer, or in a Task Scheduler task running as you, without repeating the password.

Anywhere else (another account, another computer, Linux) the saved value cannot be read and the runner asks for the connection string:

```text
Error: Target 'Warehouse' (SQL Server) needs a connection string: its saved password is encrypted for the Windows account that saved the project (and can only be read there). ...
```

### CSV files

The value is the file path. Without one, the path saved in the project is used: give one to read or write another file, for example a dated file name from a script.

## The options

```bat
replisteer run --project accounts.replisteer.json ^
  --source "Server=sql01;Database=erp;User ID=replisteer;Password=..." ^
  --target "CRM=AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=...;ClientSecret=..." ^
  --target "Export=D:\Exports\accounts.csv"
```

`--target` takes `<target name or id>=<connection string>`. With a single target, the name can be left out. See [target names](../options/#target-names).

{{< callout type="warning" >}}
Command lines can be seen by other users and administrators of the computer (Task Manager, process lists, Task Scheduler). Prefer a connections file or environment variables for secrets.
{{< /callout >}}

## Connections file

A JSON file with connection strings by connection name, given with `--connections`:

```json
{
  "Source": "Server=sql01;Database=erp;User ID=replisteer;Password=...",
  "CRM": "AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=...;ClientSecret=...",
  "Export": "D:\\Exports\\accounts.csv"
}
```

- Keys are connection names (or target ids, or the name with `_` for other characters). `Source`, or the source's name, is the source.
- Only connections that need one have to be listed; an unknown name is an error.
- Backslashes in JSON are written twice (`D:\\Exports`).
- **Schedule...** in XrmToolBox creates this file with placeholders for exactly the connections that need one.

Keep the file private: store it where only the account running the project can read it.

## Environment variables

`Connection__<connection name>__ConnectionString`, with every character other than letters and digits in the name written as `_`:

```bat
set Connection__CRM__ConnectionString=AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=...;ClientSecret=...
set Connection__Legacy_ERP__ConnectionString=Server=sql01;Database=erp;Integrated Security=true
replisteer run --project accounts.replisteer.json
```

Environment variables suit CI/CD pipelines, where secrets are usually provided that way.

## Secrets are never printed

The runner prints where each connection points (the environment URL, server and database, or file), never passwords or secrets, also in error messages and result files.
