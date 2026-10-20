---
title: Connectors
weight: 3
---

A connector is the kind of system a source or target talks to. Every project uses one connector for its source and any mix of connectors for its targets.

| | Dataverse / Dynamics 365 | SQL Server | CSV file |
| --- | --- | --- | --- |
| Source | FetchXML query | SQL query | Every row of the file |
| Insert | ✓ | ✓ | ✓ (appends a row) |
| Update, upsert, delete | ✓ | ✓ | — |
| Execute | On-demand workflow | Stored procedure | — |
| `LOOKUP()` | ✓ | ✓ | ✓ |
| Connection in XrmToolBox | XrmToolBox connection | Connection dialog | File and format |
| Connection outside XrmToolBox | ServiceClient connection string | SQL connection string | File path |

{{< cards >}}
  {{< card link="dataverse" title="Dataverse / Dynamics 365" subtitle="FetchXML, lookups, choices, party lists, workflows and write options." >}}
  {{< card link="sql-server" title="SQL Server" subtitle="Queries, tables, stored procedures, types and identities." >}}
  {{< card link="csv" title="CSV files" subtitle="Delimiters, encodings, headers, quoting and append or replace." >}}
{{< /cards >}}
