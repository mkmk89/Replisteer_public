---
title: Commands
weight: 1
---

```text
replisteer <command> --project <file> [options]
```

## run

Runs the project: reads every source row and writes to the targets, exactly like **Run** in XrmToolBox.

```bat
replisteer run --project accounts.replisteer.json --connections accounts.connections.json
```

- `--rows <n>` processes at most *n* rows, useful for a first real run on a small batch.
- The project is [validated](#validate) first, without connecting: when it has errors, nothing runs and the exit code is 3.
- Progress is printed every 10 seconds on long runs.
- **Ctrl+C** stops the run after the current row (the exit code is 1, *Cancelled*); a second Ctrl+C ends the process immediately.

## preview

A dry run of the first rows, like **Preview** in XrmToolBox: every formula is evaluated and every step "runs", but nothing is written. Lookups still read from the targets.

```bat
replisteer preview --project accounts.replisteer.json --connections accounts.connections.json --rows 5
```

```text
08:00:03 Would write (5):
08:00:03   row 1, Upsert account: Upsert CRM / account: name = Contoso Ltd; accountnumber = C-0001 where accountnumber = C-0001
08:00:03   row 2, Upsert account: Upsert CRM / account: name = Fabrikam; accountnumber = C-0002 where accountnumber = C-0002
...
08:00:03 Preview Succeeded: 5 row(s) read, 0 failed, 00:00:01.
```

`--rows` defaults to 20. Rows that would fail are listed with the reason, as in a real run.

## validate

Checks the project and every connection without writing anything:

1. Reads the project and matches the connection strings to its connections.
2. Opens every connection (the source and all targets) and reads their fields and columns.
3. Runs the same checks as **Validate** in XrmToolBox, using those fields: formulas, mappings, match criteria, step links, and columns that do not exist in the target.

```text
C:\> replisteer validate --project accounts.replisteer.json --connections accounts.connections.json
08:00:01 replisteer 1.2026.10.1: validate 'Accounts nightly'
08:00:01   Source 'Source': SQL Server sql01, erp
08:00:01   Target 'CRM': Dataverse https://contoso.crm4.dynamics.com
08:00:02   Source: connected, 14 field(s)
08:00:04   Target 'CRM': connected, 312 field(s)
08:00:04 Warning: Step 'Upsert account': Required column 'name' is not mapped
08:00:04 The project is valid (1 warning(s)).
```

The exit code is 0 when there are no errors (warnings are fine) and 3 when there are. Use it before scheduling a project, and after changing connection strings or credentials.

## help

```bat
replisteer help
```

Prints all [options](../options/). `replisteer` without a command, `replisteer --help`, `-h` and `/?` do the same, also after a command (`replisteer run --help`).

## version

```bat
replisteer version
```

Prints the version, for example `replisteer 1.2026.10.1`.
