---
title: Options
weight: 2
---

| Option | Value | Commands | Meaning |
| --- | --- | --- | --- |
| `-p`, `--project` | file, JSON, or `-` | all | **Required.** The project file saved by the XrmToolBox tool (`.replisteer.json` or `.replisteer.xml`), the JSON / XML content itself, or `-` to read it from standard input. |
| `-s`, `--source` | connection string | all | Connection string of the source. |
| `-t`, `--target` | `<name>=<connection string>` | all | Connection string of a target, by target name or id. Repeat it for every target. When the project has one target, the name can be left out. |
| `-c`, `--connections` | file | all | JSON file with connection strings by connection name. See [Connections file](../connections/#connections-file). |
| `-r`, `--rows` | number | run, preview | preview: number of rows (default 20). run: process at most this many rows. |
| `-o`, `--output` | file | all | Also save the result to a file: `.json`, `.csv`, `.txt` or `.log`. See [Result files](../output/#result-files). |
| `-q`, `--quiet` | | all | Print only problems and the final summary. |
| `-h`, `--help`, `/?` | | | Show the help. |

Options are written as `--option value`; long names also as `--option=value`. Option and command names are case-insensitive.

## Quoting values

Values with spaces, `;`, `&`, `|`, `<` or `>` must be in double quotes. Connection strings always contain `;`, so always quote them:

```bat
replisteer run --project "C:\My Projects\accounts.replisteer.json" --target "CRM=AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=...;ClientSecret=..."
```

In **PowerShell**, double-quoted strings expand `$` and backticks: use single quotes for connection strings that contain them (`'...;Password=pa$$word'`), or a connections file.

In **batch files**, `%` starts a variable: write `%%` for a literal `%`.

## Pasting a project

`--project` also accepts the project's JSON or XML content, which is convenient in pipelines that generate projects. Reading it from standard input avoids quoting problems:

```bash
cat accounts.replisteer.json | replisteer run --project - --connections connections.json
```

## Target names

`--target` and the [connections file](../connections/#connections-file) find targets by:

1. their **id** (`--target "2=..."`), as shown on the Targets tab;
2. their **name**, ignoring case (`--target "crm prod=..."` matches *CRM Prod*);
3. their name with every character other than letters and digits written as `_` (`--target "CRM_Prod=..."`), like the environment variables.

An unknown name is an error that lists the targets of the project.

## Built-in help

This is the output of `replisteer help`:

{{< generated "replisteer-help.txt" >}}
