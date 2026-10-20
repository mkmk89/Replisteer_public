---
title: Targets
weight: 3
---

The **2. Targets** tab lists the systems the project writes to. Add a target with **Add target** and choose its type; **Remove** deletes the selected one. The list shows each target with the icon of its type.

| Setting | Meaning |
| --- | --- |
| **Name** | Unique name of the target. Formulas read from the target with `LOOKUP("<name>", …)`, and the command line runner matches connection strings by this name. |
| **Target type** | Dataverse / Dynamics 365, SQL Server or CSV file (chosen when the target is added). |
| **Connection** | The environment, database or file. |
| **Options...** | Dataverse only: write options such as batch size, UTC dates, skipping empty or unchanged values and bypassing plug-ins. See [Dataverse](../../connectors/dataverse/#target-options). |
| **Writes to** | What the steps write to; it decides which operations are possible (below). |
| **Table** (or procedure / workflow) | The table, view or stored procedure. **Browse...** lists them. |

Every target has an id (1, 2, 3, …), shown in the hint under the settings. Formulas can use the id instead of the name: `LOOKUP(1, …)`.

## What a target writes to

| Target type | Writes to | Operations |
| --- | --- | --- |
| Dataverse | **Table** | Insert, update, upsert, delete |
| Dataverse | **On-demand workflow** | Execute: runs a workflow for a record (map `WorkflowId` and `EntityId`) |
| SQL Server | **Table or view** | Insert, update, upsert, delete |
| SQL Server | **Stored procedure** | Execute: calls the procedure with the mapped parameters |
| CSV file | **CSV file** | Insert: appends rows |

## Target columns

**Load columns** reads the columns of the table, procedure or file and lists them with their type, display name, and whether they are required or read-only. The list feeds the column drop-downs of the Steps tab, marks unknown column names in red, and lets **Validate** check mappings.

A new CSV file has no columns yet: its header is written from the mapped columns of the first row.

## Lookup-only targets

A target does not have to be written to. A target that no step uses can still be read by formulas, for example a SQL table of code mappings or a CSV file with translations:

```text
LOOKUP("Country codes", "", "Code", "Name", country)
```

{{< callout type="info" >}}
Every target is opened when a run starts, including targets only used by `LOOKUP()`. Outside XrmToolBox, each of them needs a connection string.
{{< /callout >}}
