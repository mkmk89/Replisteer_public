---
title: Replisteer
layout: hextra-home
---

<div class="hx:mt-6 hx:mb-6">
{{< hextra/hero-headline >}}
  Move data between Dataverse,&nbsp;<br class="hx:sm:block hx:hidden" />SQL Server and CSV files
{{< /hextra/hero-headline >}}
</div>

<div class="hx:mb-12">
{{< hextra/hero-subtitle >}}
  Design data migrations and integrations in XrmToolBox, check them with a dry run,&nbsp;<br class="hx:sm:block hx:hidden" />then run them on demand, from the command line or on a schedule.
{{< /hextra/hero-subtitle >}}
</div>

<div class="hx:mb-6">
{{< hextra/hero-button text="Get started" link="docs/getting-started" >}}
{{< hextra/hero-button text="Command line" link="docs/command-line" style="background: transparent; color: inherit; border: 1px solid currentColor;" >}}
</div>

<div class="hx:mt-6"></div>

{{< hextra/feature-grid >}}
  {{< hextra/feature-card
    title="Three kinds of systems"
    subtitle="Read from and write to Dataverse / Dynamics 365 environments, SQL Server and Azure SQL databases, and CSV files, in any combination."
    icon="switch-horizontal"
  >}}
  {{< hextra/feature-card
    title="Formulas like a spreadsheet"
    subtitle="Transform every value with more than 60 functions: text, numbers, dates, conditions, lookups in other systems, Dataverse lookups and party lists."
    icon="variable"
  >}}
  {{< hextra/feature-card
    title="Multi-step mappings"
    subtitle="Chain insert, update, upsert, delete and execute steps per source row, with conditions, failure branches and values passed from step to step."
    icon="view-list"
  >}}
  {{< hextra/feature-card
    title="Dry runs before real runs"
    subtitle="Validate the configuration and preview exactly what would be written, without touching the targets. Failed rows are listed with the reason."
    icon="eye"
  >}}
  {{< hextra/feature-card
    title="Runs without XrmToolBox"
    subtitle="The replisteer command line runner runs saved projects from scripts, pipelines and the Windows Task Scheduler. One file, nothing to install."
    icon="terminal"
    link="docs/command-line"
  >}}
  {{< hextra/feature-card
    title="Projects are files"
    subtitle="A project is one JSON file: share it, review it, keep it in source control. Credentials stay out of it: Dataverse uses your XrmToolBox connections."
    icon="document-text"
    link="docs/xrmtoolbox/project-files"
  >}}
{{< /hextra/feature-grid >}}
