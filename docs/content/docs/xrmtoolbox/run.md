---
title: Run and results
weight: 6
---

The **5. Run** tab starts runs and shows their results. **Validate**, **Preview** and **Run** are also on the main toolbar.

## Validate

**Validate** checks the whole project without connecting to anything new and lists the problems:

- **Errors** prevent a run, for example a step without a target, a formula with a syntax error, an update without match criteria, a column mapped twice, or a CSV target with an operation other than insert.
- **Warnings** are shown before a run but do not stop it, for example a formula using a name that is neither a source field nor a variable (its value will be empty), a column that does not exist in the loaded target columns, a required column that is not mapped, or a step that no other step links to.

Validation uses the loaded source fields and target columns: load them first for the most complete check. See [Validation messages](../../reference/validation/) for every message.

## Preview

**Preview** is a dry run of the first rows: 20 by default, chosen in the **rows** box next to the button. Every formula is evaluated and every step "runs", but nothing is written. Lookups still read from the targets.

The **Preview** results tab lists every record that would be written: row number, step, operation, target, the values and the match criteria. Rows that would fail are listed in **Failed rows** with the reason, exactly as in a real run.

## Run

**Run** asks for confirmation, lists the targets that will be written to, and processes every source row. While it runs, the progress (rows processed, rows failed, time) is shown and **Cancel** stops the run after the current row.

{{< callout type="warning" >}}
Records written before a cancellation or a failure stay written: a run is not a transaction.
{{< /callout >}}

## Results

The status line shows the outcome (*Completed successfully*, *Completed with errors*, *Failed* or *Cancelled*) with the number of rows read and failed, the start time and the duration. The results tabs:

| Tab | Contents |
| --- | --- |
| **Failed rows** | Row number, step, error message and the first source values of every failed row (up to 1,000 rows are listed). |
| **Preview** | Records a preview would write. |
| **Steps** | Per step: how often it was executed, skipped by its condition, failed, and how many records it affected. |
| **Log** | Everything that happened, with times. |

## Export

**Export...** saves the results of the selected tab; the arrow next to it lists every export with the number of rows (empty ones are disabled):

| Export | Format |
| --- | --- |
| Failed rows | CSV: row, step, error, source row |
| Preview records | CSV: row, step, operation, target, values, criteria |
| Step statistics | CSV: step, executed, skipped, failed, records affected |
| Log | Text file |

CSV exports quote every value and are UTF-8 with a byte order mark, so Excel opens them correctly. After saving, the tool offers to open the file.
