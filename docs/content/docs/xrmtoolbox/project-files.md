---
title: Project files
weight: 8
---

A project is one file. The tool saves JSON by default (`*.replisteer.json`); XML (`*.replisteer.xml`) is supported too: choose it in **Save as...**. Both contain the same information; the tool and the command line runner read either.

## What is in the file

```json
{
  "formatVersion": 2,
  "name": "Import contacts",
  "source": {
    "id": 0,
    "name": "Source",
    "adapter": "Csv",
    "csv": { "filePath": "C:\\Data\\contacts.csv", "delimiter": "Auto", "hasHeader": true, "encoding": "utf-8" }
  },
  "targets": [
    {
      "id": 1,
      "name": "CRM",
      "adapter": "Dataverse",
      "dataverse": {
        "xrmToolBoxConnectionId": "7c4c3f39-…",
        "xrmToolBoxConnectionName": "Contoso production",
        "organizationUrl": "https://contoso.crm4.dynamics.com",
        "targetKind": "Table",
        "tableName": "contact",
        "batchSize": 200
      }
    }
  ],
  "variables": [],
  "steps": [
    {
      "id": 1,
      "name": "Upsert contact",
      "isStartingStep": true,
      "targetId": 1,
      "operation": "Upsert",
      "mappings": [ { "targetColumn": "lastname", "formula": "TRIM(lastname)", "overwrite": true } ],
      "matchCriteria": [ { "targetColumn": "emailaddress1", "formula": "LOWERCASE(TRIM(email))" } ]
    }
  ]
}
```

The file is plain text and works well in source control: keep projects next to the code or scripts that use them and review changes like any other file. (The example is shortened; the tool writes every setting.)

## Passwords and secrets

| Connection | What the file contains |
| --- | --- |
| Dataverse | Only which XrmToolBox connection to use (id, name and URL). Never credentials. |
| SQL Server | The connection string. With *Save SQL Server passwords in project files* checked (the default), the whole connection string is encrypted with Windows DPAPI for your Windows account (`"connectionString": "dpapi:…"`). When cleared, the password is removed before saving. |
| CSV | The file path. |

Encrypted connection strings can be read by the same Windows account on the same computer: by the tool, and by the [command line runner](../../command-line/connections/#saved-sql-server-passwords) when it runs as you. Anyone else opening the file (another user, another computer) gets the connection without its password and has to provide it.

{{< callout type="info" >}}
To share a project or commit it to source control, clear *Save SQL Server passwords in project files* on the Project tab before saving. Others enter the password in the connection dialog, and the runner gets it from a connections file or an environment variable.
{{< /callout >}}

## Opening projects

**Open** (Ctrl+O) opens a project; the arrow next to it lists the ten most recent files. After opening:

- Dataverse connections are linked to your XrmToolBox connections by id, then by name, then by URL. Any that cannot be linked are listed in the notice strip; choose them on the Source and Targets tabs.
- Passwords that could not be decrypted (saved by another user or on another computer) are reported; enter them again in the connection dialog.

## Projects from the original Replisteer

Project files of the original Replisteer client (`ProjectDetails` XML) open too: choose the file in **Open** (filter *XML*). The project is converted, a summary of the conversion is shown, and the project opens as a new, unsaved project so the original file stays untouched. Things that no longer exist are reported:

- OData connections become CSV placeholders that keep their steps and mappings; point them to a new connection.
- Schedules are not imported: projects run on demand in the tool, and on a schedule with the [command line runner](../../command-line/task-scheduler/).
