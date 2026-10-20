---
title: Schedule dialog
weight: 7
---

**Schedule...** on the toolbar explains how to run the open project without XrmToolBox and writes everything needed for it. It does not change the project.

{{% steps %}}

### Get the runner

The first line links to the download of the [command line runner](../../command-line/). Unzip it, for example to `C:\Tools\Replisteer`.

### Runner

The path of `replisteer.exe`. **Browse...** selects it; the tool remembers it.

### Project file

The runner reads the **saved** project file. When the project was never saved, or has unsaved changes, a warning says so and **Save project** saves it.

### Connections

Dataverse connections always need a connection string outside XrmToolBox, and SQL Server connections need one when their password is not saved in the project. Choose where they go:

- **In a connections file** (recommended): a JSON file next to the project, `<project>.connections.json`. **Save template...** creates it with a `<...>` placeholder for every value you need to fill in, and offers to open it in Notepad. Command lines stay free of secrets.
- **On the command line**: the commands contain `--source` / `--target` options with placeholders.

When the project needs no connection strings (for example SQL Server with Windows authentication and CSV files), this choice is disabled.

{{% /steps %}}

## Tabs

| Tab | Contents |
| --- | --- |
| **Commands** | The `validate`, `preview` and `run` commands for this project, ready to paste into a Command Prompt. **Copy commands** copies them; **Save run as .cmd file...** saves the run command as a batch file for the Task Scheduler. |
| **Connection strings** | For every connection: whether the runner needs a connection string, and what it looks like. For Dataverse it explains the app registration (client secret) to use for unattended runs. |
| **Task Scheduler** | The steps to schedule the batch file, the `schtasks` command for a daily task, and what the task's *Last Run Result* means. |
| **All options** | The complete help of the runner. |

The generated batch file runs the project and saves the log next to it as `<project>-last-run.log`. See [Windows Task Scheduler](../../command-line/task-scheduler/) for the details.
