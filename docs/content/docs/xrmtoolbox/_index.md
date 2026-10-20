---
title: XrmToolBox tool
weight: 2
---

The XrmToolBox tool, *Replisteer: Data Migration (ETL)*, is where projects are designed, checked and run interactively.

## The window

The **toolbar** at the top works on the whole project:

| Button | Shortcut | What it does |
| --- | --- | --- |
| **New** | Ctrl+N | Starts a new project. |
| **Open** | Ctrl+O | Opens a project file. The arrow lists recently used files. |
| **Save** / **Save as...** | Ctrl+S | Saves the project file. |
| **Load all schemas** | | Loads the fields of the source and the columns of every target in one go. Connections that are not set up yet, or fail, are listed at the end. |
| **Validate** | | Checks the configuration and lists problems. |
| **Preview** | Ctrl+F5 | Dry run on the first rows: evaluates everything, writes nothing. |
| **Run** | F5 | Runs the project and writes to the targets. |
| **Cancel** | | Shown while something runs: stops after the current row. |
| **Schedule...** | | Explains how to run the project without XrmToolBox and writes the commands. |
| **Documentation** | F1 | Opens this documentation at the page for the current tab. |

The Replisteer logo at the left end of the toolbar opens this documentation. The right end of the toolbar shows the project name, a `*` when there are unsaved changes, and the file name.

The **tabs** follow the order in which a project is usually built:

| Tab | Contents |
| --- | --- |
| [Project](project/) | Name, description, file, password handling and the Dataverse environments the project uses. |
| [1. Source](source/) | Where rows are read from, and the query. |
| [2. Targets](targets/) | The systems written to. |
| [3. Variables](variables/) | Values calculated once per row. |
| [4. Steps](steps/) | What is written for every row, and in which order. |
| [5. Run](run/) | Validate, preview, run and the results. |

A yellow strip above the tabs shows notices, for example connections that still need to be linked after opening a project. Click it to close it.

A banner along the bottom of the tool, and links to deduplica.net (the author's tool for finding duplicates in Dataverse), may show news and offers.

## Unsaved changes

The tool asks before discarding unsaved changes: when you start a new project, open another one, close the tool or its tab, or close XrmToolBox. Choose **Yes** to save, **No** to discard or **Cancel** to stay. This also happens when XrmToolBox is set to close tools silently. Undocking the tab into its own window, or docking it back, keeps the project and its changes.

## Connections

- **Dataverse** connections are XrmToolBox connections. The source and every target pick one with **Choose...**: the main connection of the tool, another connected environment, or *Connect to an environment...* to add one. A project can read from one environment and write to several others. The [Project tab](project/) lists the environments in use.
- **SQL Server** connections are configured in their own dialog: server, SQL or Windows authentication, database and security options. See [SQL Server](../connectors/sql-server/).
- **CSV files** are configured with the file and its format. See [CSV files](../connectors/csv/).

## Pages in this section

{{< cards >}}
  {{< card link="project" title="Project tab" >}}
  {{< card link="source" title="Source" >}}
  {{< card link="targets" title="Targets" >}}
  {{< card link="variables" title="Variables" >}}
  {{< card link="steps" title="Steps" >}}
  {{< card link="run" title="Run and results" >}}
  {{< card link="schedule" title="Schedule dialog" >}}
  {{< card link="project-files" title="Project files" >}}
{{< /cards >}}
