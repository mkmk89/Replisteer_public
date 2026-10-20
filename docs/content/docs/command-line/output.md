---
title: Output and exit codes
weight: 4
---

## Console output

Every line starts with the local time. The runner prints:

- the command, the project and where each connection points (never secrets);
- the log of the run: connecting, reading, progress every 10 seconds on long runs, and the statistics per step;
- **failed rows**: the first 20, each with the row number, the step and the reason (the full list goes to `--output`);
- for `preview`, every record that would be written;
- the **summary** as the last line, for example `Completed with errors: 1,204 row(s) read, 2 failed, 00:01:28.`

Problems (errors, warnings and failed rows) go to **standard error**, everything else to standard output, so `2> errors.txt` captures just the problems. `--quiet` leaves out everything but problems and the summary.

## Exit codes

| Code | `run` / `preview` | `validate` |
| --- | --- | --- |
| **0** | Succeeded: every row was processed without errors. | No errors (warnings are allowed). |
| **1** | Failed or cancelled: the run could not complete, for example a connection failed, a step stopped the run, or Ctrl+C. | — |
| **2** | Completed, but some rows failed. | — |
| **3** | Nothing was run: invalid command line, project file or connection strings, or the project has errors. | The project or a connection has errors. |

Scripts and schedulers use the exit code to tell success from failure:

```bat
replisteer run --project accounts.replisteer.json --connections accounts.connections.json --output accounts.log
if %ERRORLEVEL% GEQ 3 echo The project or its connections are wrong & exit /b %ERRORLEVEL%
if %ERRORLEVEL% EQU 2 echo Some rows failed, see accounts.log
```

## Result files

`--output <file>` saves the result too. The format follows the extension:

| Extension | Contents |
| --- | --- |
| `.json` | Everything: the summary, exit code, validation issues, status, times, counts, steps, failed rows and preview records. For automation and monitoring. |
| `.csv` | `run`: the failed rows. `preview`: the records that would be written. `validate`: the problems. Every value quoted, UTF-8 with BOM for Excel. |
| `.txt`, `.log` | The complete log, as printed (without `--quiet` filtering). |

The folder is created when it does not exist. The file is replaced on every run; put a date in the name to keep history (see [examples](../examples/)).

### JSON result

```json
{
  "runner": "replisteer 1.2026.10.1",
  "command": "run",
  "project": "Accounts nightly",
  "summary": "Completed with errors: 1,204 row(s) read, 2 failed, 00:01:28.",
  "issues": [],
  "exitCode": 2,
  "result": {
    "status": "CompletedWithErrors",
    "startedUtc": "2026-10-20T06:00:02.1234567Z",
    "endedUtc": "2026-10-20T06:01:30.4567890Z",
    "duration": "00:01:28.3333323",
    "wasDryRun": false,
    "rowsRead": 1204,
    "rowsFailed": 2,
    "message": null,
    "failures": [
      {
        "rowNumber": 87,
        "stepId": 1,
        "stepName": "Upsert account",
        "message": "Column 'revenue' expects a number, got 'n/a'",
        "sourcePreview": "AccountNo=C-0087, Name=Northwind, Revenue=n/a"
      }
    ],
    "failuresTruncated": false,
    "steps": [
      { "stepId": 1, "stepName": "Upsert account", "executed": 1204, "skipped": 0, "failed": 2, "recordsAffected": 1202 }
    ],
    "preview": [],
    "durationSeconds": 88.3
  }
}
```

| Field | Meaning |
| --- | --- |
| `exitCode` | The exit code of the run. |
| `issues` | Validation errors and warnings (`severity`, `area`, `message`). |
| `valid` | `validate` only: TRUE when there are no errors (there is no `result` then). |
| `result.status` | `Succeeded`, `CompletedWithErrors`, `Failed` or `Cancelled`. |
| `result.message` | Why a run failed or stopped. |
| `result.failures` | Failed rows (up to 1,000; `failuresTruncated` is TRUE when there were more). |
| `result.steps` | Per step: executed, skipped by their condition, failed, records affected. |
| `result.preview` | `preview` only: the records that would be written. |
