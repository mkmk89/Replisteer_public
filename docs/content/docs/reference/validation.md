---
title: Validation messages
weight: 1
---

**Validate** in XrmToolBox, `replisteer validate`, and every run check the project. **Errors** prevent a run; **warnings** are reported but do not stop it. Each message names the area: *Source*, *Target 'name'*, *Step 'name'*, *Variable 'name'* or *Steps*.

## Connections

| Message | Severity | What to do |
| --- | --- | --- |
| The project has no source | Error | Configure the Source tab. |
| The connection has no name | Error | Give the source or target a name. |
| Connection names must be unique | Error | Rename one of the connections with the same name. |
| The connection is not configured | Error | Choose (Dataverse) or configure (SQL Server) the connection. |
| No CSV file is selected | Error | Select the file in the CSV dialog. |
| The source query is empty | Error | Enter the FetchXML or SQL query. |
| Target ids must be unique positive numbers | Error | Only happens with hand-edited project files: fix the `id` of the targets. |
| Target '…' has no table / file configured | Error | Choose the table, procedure, workflow or file the target writes to. |
| Not linked to an open XrmToolBox connection; choose an environment | Error | XrmToolBox only: choose the Dataverse connection with **Choose...**. |

## Steps

| Message | Severity | What to do |
| --- | --- | --- |
| The project has no steps | Error | Add a step. |
| No step is marked as the starting step | Error | Select a step and click **Set as first**. |
| Only one step can be the starting step | Error | Hand-edited files only: keep one `isStartingStep`. |
| Step ids must be unique positive numbers | Error | Hand-edited files only. |
| A step cannot continue with itself | Error | Choose another *Then* / *If it fails* step. |
| The next step … does not exist | Error | Choose an existing step. |
| A step cannot continue with the starting step | Error | Rows always start with the first step; link to another step. |
| The step has no target connection | Error | Choose the step's target. |
| Map at least one target column | Error | Insert, update, upsert and execute need at least one mapping. |
| A field mapping has no target column | Error | Fill in or remove the empty mapping row. |
| Column '…' is mapped more than once | Error | Remove the duplicate row (it is marked with a red icon). |
| … needs at least one match criterion, otherwise it would affect every record | Error | Add a match criterion to the update, upsert or delete step. |
| A match criterion has no target column | Error | Fill in or remove the empty criterion. |
| CSV files can only be written with Insert (rows are appended) | Error | Use Insert for CSV targets. |
| Execute needs a target configured as a stored procedure or an on-demand workflow | Error | Change the target's *Writes to*, or the operation. |
| … needs a target table; target '…' is configured for Execute | Error | Change the target's *Writes to* to a table, or use Execute. |
| Column '…' does not exist in … | Warning | The column is not in the loaded target columns: check the spelling, or **Load columns** again. A run fails the rows with an unknown column. |
| Required column '…' is not mapped | Warning | Map it, unless the target fills it itself (for example a default value or a plug-in). |
| The step is never executed; link it from another step | Warning | Link it with *Then* or *If it fails* of another step, or remove it. |

## Formulas and variables

| Message | Severity | What to do |
| --- | --- | --- |
| … has no formula | Error | Enter a formula (for a value that should be empty, write `NULL`). |
| … : *syntax error* (at position *n*) | Error | Fix the formula; the formula editor shows the error while typing. |
| … uses '…', which is not a source field or variable (it will be empty) | Warning | Check the spelling, load the source fields, or use brackets for names with spaces: `[First Name]`. |
| Variable names must start with a letter or '_' and contain only letters, digits and '_' | Error | Rename the variable. |
| The variable name is used more than once | Error | Rename one of them. |
| A source field has the same name; formulas will see the variable | Warning | Rename the variable if you need the source field. |

## Command line only

The runner checks the command line and the connection strings before anything else; see [Connection strings](../../command-line/connections/). These messages end with *Nothing was run.* and exit code 3.

| Message | What to do |
| --- | --- |
| --project is required | Give the project file. |
| The project file does not exist: … | Check the path (relative paths are relative to the current folder). |
| The project could not be read: … | The file is not a Replisteer project, or it is damaged. |
| Unknown command / option '…' | See `replisteer help`. |
| --rows must be a whole number greater than 0 | Fix the value. |
| Unexpected argument '…'. Values with spaces or ';' must be in double quotes | Quote the value. |
| --target: no target named '…' | Use a name or id from the list in the message. |
| --target: say which target the connection string is for | With several targets, write `--target "<name>=<connection string>"`. |
| … needs a connection string: … | Give it with `--source` / `--target`, the connections file, or an environment variable. |
| --connections: no connection named '…' in the project | Fix the key in the connections file. |
