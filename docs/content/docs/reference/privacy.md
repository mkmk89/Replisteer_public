---
title: Privacy and usage statistics
linkTitle: Privacy
weight: 3
---

## What stays on your computer

Replisteer works between your computer and your systems. Your data, queries, formulas, project files and connection details are never sent anywhere else.

## Anonymous usage statistics

The XrmToolBox tool sends **anonymous usage statistics** to Azure Application Insights, to show how Replisteer is used and what to improve, **only when you allowed XrmToolBox to collect anonymous statistics** (XrmToolBox asks on first start; change it in XrmToolBox *Settings*). Organisations can turn statistics off for everyone with the XrmToolBox policy for IT administrators.

What is sent:

| Event | Contents |
| --- | --- |
| The tool is opened | Nothing more than the common fields below. |
| A run or preview finished | Run or preview, the result status, the source type and target types (Dataverse, SQL Server, CSV), the operations used (insert, update, …), and the numbers of rows, failed rows, steps, targets, variables and mappings, and the duration. |

Every event also carries the version of the tool and of XrmToolBox and a random installation id (created on first use, not derived from you, your computer or your organisation).

What is **never** sent: names of projects, connections, tables or columns, queries, formulas, connection strings or any part of them, environment URLs, user names, and any data.

The command line runner sends no statistics.

## Banner

When the XrmToolBox tool opens, it asks `ads.owware.com` for the banner shown at the bottom of the tool (and loads its image), and whether to show links to deduplica.net. These requests contain nothing about you, your projects or your environments; as with any web request, the server sees your IP address. Without an answer there is no banner and there are no links; the tool works the same. Links to deduplica.net carry UTM parameters that only say where in Replisteer they were clicked. It also asks `api.replisteer.com` whether optional online services for running projects are offered. That request contains only a random number, used once, which lets the tool check that the answer is genuine. Without a genuine answer the tool shows nothing about these services. This documentation site asks the same question when a page opens, to decide whether to show its *Cloud* menu link; that request also contains only a random number.
