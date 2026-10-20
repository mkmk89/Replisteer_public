---
title: Documentation
linkTitle: Documentation
weight: 1
---

{{< logo >}}

Replisteer moves and synchronises data between **Dataverse / Dynamics 365** environments, **SQL Server** databases and **CSV files**. You read rows from a *source*, transform them with *formulas*, and write them to one or more *targets* through a chain of *steps* that insert, update, upsert, delete or execute.

Typical uses:

- **Data migration** – load accounts, contacts, products or history from a legacy SQL database or Excel/CSV exports into Dataverse, with lookups to records created earlier in the same run.
- **Environment to environment** – copy configuration or reference data from one Dataverse environment to another (development to test to production), matched on a business key instead of GUIDs.
- **Integration and reporting** – export Dataverse data to a SQL Server table or a CSV file every night, or keep a SQL table in sync with upserts.
- **Data fixes** – update or delete records matching a query, with a preview of every change before it is made.

## Two ways to run a project

| | What it is | Use it to |
| --- | --- | --- |
| [XrmToolBox tool](xrmtoolbox/) | *Replisteer: Data Migration (ETL)* in the XrmToolBox Tool Library. | Design projects, preview them and run them interactively. |
| [Command line runner](command-line/) | `replisteer.exe` (Windows) or `replisteer` (Linux): one self-contained file. | Run saved projects from scripts, CI/CD pipelines or the Windows Task Scheduler. |

Both use the same engine: a project behaves the same wherever it runs. Projects are designed in XrmToolBox and saved as local files (`*.replisteer.json`), which the runner reads.

## Where to start

{{< cards >}}
  {{< card link="getting-started/installation" title="Installation" icon="download" subtitle="Install the XrmToolBox tool and, if you need it, the runner." >}}
  {{< card link="getting-started/first-project" title="Your first project" icon="academic-cap" subtitle="Import a CSV file into Dataverse contacts, step by step." >}}
  {{< card link="getting-started/concepts" title="Concepts" icon="light-bulb" subtitle="Sources, targets, variables, steps, mappings and match criteria." >}}
  {{< card link="formulas" title="Formulas" icon="variable" subtitle="The formula language and every function." >}}
  {{< card link="command-line" title="Command line" icon="terminal" subtitle="Run projects without XrmToolBox." >}}
  {{< card link="reference/troubleshooting" title="Troubleshooting" icon="support" subtitle="Common problems and how to solve them." >}}
{{< /cards >}}
