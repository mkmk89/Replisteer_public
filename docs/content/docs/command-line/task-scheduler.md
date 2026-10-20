---
title: Windows Task Scheduler
weight: 5
---

The Windows Task Scheduler can run a project every night, every hour or at log-on, on any Windows computer. **Schedule...** in XrmToolBox prepares everything below for the open project.

{{% steps %}}

### Test the commands

Run `replisteer validate` and `replisteer preview` for the project in a Command Prompt until they succeed. Use a [connections file](../connections/#connections-file) for the connection strings.

### Create a batch file

Save the run command as a `.cmd` file next to the project, for example `accounts.run.cmd`:

```bat
@echo off
REM Runs the Replisteer project "Accounts nightly".
REM Exit codes: 0 succeeded, 1 failed, 2 some rows failed, 3 invalid project or connections.
"C:\Tools\Replisteer\replisteer.exe" run --project "C:\Projects\accounts.replisteer.json" --connections "C:\Projects\accounts.connections.json" --output "C:\Projects\accounts-last-run.log"
exit /b %ERRORLEVEL%
```

A batch file keeps the task's command short (`schtasks` accepts at most 261 characters) and lets you change the run without editing the task. In batch files, write `%%` for a literal `%`.

### Create the task

Either in **Task Scheduler** (*Create Basic Task > Daily > Start a program*, then select the `.cmd` file), or in a Command Prompt:

```bat
schtasks /Create /TN "Replisteer\Accounts nightly" /TR "\"C:\Projects\accounts.run.cmd\"" /SC DAILY /ST 02:00
```

The task runs as you, when you are signed in. To run it also when you are not signed in, add `/RU "%USERDOMAIN%\%USERNAME%" /RP` (it asks for your password), or in Task Scheduler choose *Run whether user is logged on or not*.

### Check the result

After a run, the task's **Last Run Result** in Task Scheduler is the runner's exit code:

| Last Run Result | Meaning |
| --- | --- |
| `0x0` | Succeeded. |
| `0x1` | Failed or cancelled. |
| `0x2` | Completed, some rows failed. |
| `0x3` | Invalid project or connections; nothing was written. |

The log file next to the project tells what happened.

{{% /steps %}}

## Good to know

- **Saved SQL Server passwords** are encrypted for the Windows account that saved the project. A task running as you can use them; a task running as another account (or `SYSTEM`) needs the connection strings in the connections file. See [Saved SQL Server passwords](../connections/#saved-sql-server-passwords).
- **Protect the connections file**: it contains secrets. Store it in a folder only the task's account can read.
- **Changes to the project** take effect at the next run: edit it in XrmToolBox and save it.
- **Keep a history** of runs by putting the date in the log file name; see [examples](../examples/#a-log-file-per-run).
- **Notifications**: Task Scheduler does not send e-mails. Check the exit code in the batch file and call your monitoring, or use the JSON result (`--output result.json`).
