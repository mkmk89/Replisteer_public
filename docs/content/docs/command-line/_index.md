---
title: Command line runner
linkTitle: Command line
weight: 5
---

`replisteer` runs projects saved by the XrmToolBox tool, without XrmToolBox. Use it to run projects by hand, from scripts, from CI/CD pipelines, or on a schedule with the Windows Task Scheduler. It has no user interface: it prints what happens and exits with a code that tells how the run went.

```text
C:\> replisteer run --project accounts.replisteer.json --connections accounts.connections.json
08:00:01 replisteer 1.2026.10.1: run 'Accounts nightly'
08:00:01   Source 'Source': SQL Server sql01, erp
08:00:01   Target 'CRM': Dataverse https://contoso.crm4.dynamics.com
08:00:02 Opening connections
08:00:04 Reading source rows
08:01:30 Step 1 'Upsert account': executed 1,204, skipped 0, failed 2, records affected 1,202
08:01:30 Failed rows (2):
08:01:30   row 87, step 'Upsert account': Column 'revenue' expects a number, got 'n/a'
08:01:30   row 311, step 'Upsert account': Column 'parentaccountid' can reference account; ...
08:01:30 Completed with errors: 1,204 row(s) read, 2 failed, 00:01:28.
```

## Get it

Download [replisteer-win-x64.zip]({{< download-url "replisteer-win-x64.zip" >}}) (Windows) or [replisteer-linux-x64.tar.gz]({{< download-url "replisteer-linux-x64.tar.gz" >}}) (Linux) and extract it. It is a single program file with .NET included: nothing to install, no administrator rights needed. See [Installation](../getting-started/installation/#the-command-line-runner).

## Quick start

{{% steps %}}

### Save the project

Design and test the project in XrmToolBox, then save it. The runner reads the saved file.

### Check it

```bat
replisteer validate --project C:\Projects\accounts.replisteer.json
```

The runner tells you which connections need a connection string and how to give them. Dataverse connections always do: XrmToolBox connections only exist in XrmToolBox.

### Give the connection strings

Put them in a [connections file](connections/#connections-file), or on the command line:

```bat
replisteer validate --project C:\Projects\accounts.replisteer.json --target "CRM=AuthType=ClientSecret;Url=https://contoso.crm4.dynamics.com;ClientId=...;ClientSecret=..."
```

### Preview, then run

```bat
replisteer preview --project C:\Projects\accounts.replisteer.json --connections C:\Projects\accounts.connections.json
replisteer run --project C:\Projects\accounts.replisteer.json --connections C:\Projects\accounts.connections.json --output C:\Logs\accounts.log
```

{{% /steps %}}

{{< callout type="info" >}}
In XrmToolBox, **Schedule...** on the toolbar writes these commands for the open project, creates the connections file template and a batch file, and gives the Task Scheduler command. See [Schedule dialog](../xrmtoolbox/schedule/).
{{< /callout >}}

## In this section

{{< cards >}}
  {{< card link="commands" title="Commands" icon="terminal" subtitle="run, preview, validate, help, version" >}}
  {{< card link="options" title="Options" icon="adjustments" subtitle="Every option, and the built-in help" >}}
  {{< card link="connections" title="Connection strings" icon="key" subtitle="Where they come from: options, connections file, environment, project" >}}
  {{< card link="output" title="Output and exit codes" icon="document-text" subtitle="Console output, result files and exit codes" >}}
  {{< card link="task-scheduler" title="Windows Task Scheduler" icon="clock" subtitle="Run a project every night on Windows" >}}
  {{< card link="examples" title="Examples" icon="code" subtitle="PowerShell, Azure DevOps, GitHub Actions, Linux cron" >}}
{{< /cards >}}
