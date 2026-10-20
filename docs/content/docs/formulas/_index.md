---
title: Formulas
weight: 4
---

Formulas calculate the values written to targets, the match criteria, step conditions and calculated variables. They look like spreadsheet formulas:

```text
TRIM(firstname + " " + lastname)
IF(ISNULL(email), "n/a", LOWERCASE(email))
LOOKUP("CRM", "account", "accountnumber", "accountid", AccountNo)
```

The [function reference](functions/) lists every function. The formula editor (the **...** button next to every formula) shows the same reference, lists every field, variable and previous-step value you can use, inserts them with a double-click, and checks the formula while you type.

## Values

| Kind | Written as | Examples |
| --- | --- | --- |
| Text | In double or single quotes; double the quote to include it | `"Contoso"`, `'it''s'`, `"say ""hi"""` |
| Number | Digits with `.` as decimal separator | `42`, `-3.5` |
| Date and time | Between `#` signs | `#2024-01-31#`, `#2024-01-31 13:00#` |
| Boolean | | `TRUE`, `FALSE` |
| Null | No value; writing it clears the column | `NULL` |

## Names

A name refers to a **source field**, a **calculated variable** or a **value from a previous step**:

- Names are case-insensitive: `Email`, `email` and `EMAIL` are the same.
- Names with spaces or other special characters go in brackets: `[First Name]`, `[order-no]`.
- Linked-table columns from FetchXML keep their alias prefix: `acc.accountnumber`.
- `V_<step id>_<column>` is the value a previous step wrote to a column (`V_1_name`); `V_<step id>_ID` the id of the record it created.

A name that does not exist gives null (validation warns about it).

## Operators

| Operator | Meaning |
| --- | --- |
| `+` | Adds numbers, adds days to a date, otherwise joins text |
| `-` | Subtracts numbers or days; date − date is the number of days between them |
| `*` `/` `%` (or `MOD`) | Multiply, divide, remainder |
| `&` | Always joins as text |
| `=` `<>` (or `!=`) `<` `<=` `>` `>=` | Comparisons |
| `AND` `OR` `NOT` | Logic |

Precedence, from lowest: `OR`, `AND`, `NOT`, comparisons for equality, comparisons for order, `+ - &`, `* / % MOD`, unary minus. Use parentheses when in doubt.

## Nulls

A missing or empty source value is **null**. The rules are designed so that empty data rarely needs special handling:

- `+` joining text treats null as empty text: `firstname + " " + lastname` works when one is empty. Wrap it in `TRIM()` to drop the space.
- Arithmetic with null gives null: `price * qty` is null when either is missing.
- `=` treats null and empty text as equal: `email = ""` is TRUE for a missing e-mail.
- A condition that is null counts as FALSE.
- Number and date functions give null for a null argument (`ROUND(NULL, 2)`, `ADDDAYS(NULL, 1)`). Text functions treat null as empty text: `UPPERCASE(NULL)` and `TRIM(NULL)` are `""`, and `LEN(NULL)` is 0. `ISNULL()` is TRUE for both.
- Targets treat the two slightly differently. Dataverse clears the column for both. SQL Server writes `NULL` for null, and for empty text in non-text columns; text columns get an empty string. A CSV target writes null as nothing and empty text as `""`. Use `IF(ISNULL(x), NULL, x)` when a SQL text column must be `NULL`.
- A formula that only names a field (`email`) passes the value through unchanged, including null.

`ISNULL(x)`, `ISNOTNULL(x)` and `COALESCE(a, b, …)` test and replace nulls.

## Text that holds numbers and dates

Values from CSV files, and text columns from SQL Server, are text even when they contain numbers or dates. Formulas handle them like a spreadsheet does:

- `+`, `-`, `*`, `/` calculate when both sides hold numbers: `"3" * "2.5"` is `7.5`. With one side text that is not a number, `+` joins: `"Order " + 42` is `"Order 42"`. `&` always joins.
- `<`, `>` and the other order comparisons compare numbers and dates by value, other text alphabetically.
- `=` compares a number with text by value (`42 = "42"` is TRUE) but two texts exactly (`"007" = "7"` is FALSE).
- Numbers in text use `.` as decimal separator and no thousands separators. `"12,50"` is not a number: convert it with `NUMBER("12,50", ",")`.
- Dates in text are recognised in ISO format (`2024-01-31`, `2024-01-31 13:00`), `yyyy/MM/dd` and `dd.MM.yyyy`. Other formats: `DATETIME(value, "MM/dd/yyyy")`.

Formulas never depend on the language settings of the computer: the same project gives the same result everywhere.

## Writing to targets

The target connector converts the result to the type of the column: text `"2.50"` to a currency column, `"Yes"` to a yes/no column, a choice label to its value, `table:guid` to a lookup. See the type tables for [Dataverse](../connectors/dataverse/#values-written-to-dataverse-columns), [SQL Server](../connectors/sql-server/#values-written-to-sql-columns) and [CSV](../connectors/csv/#writing-target).

## Errors

A formula with a syntax error is reported by **Validate** with its position, and the project does not run. A formula that fails while running (a conversion that is not possible, a lookup to a missing target) fails the step for that row; the run continues with the other rows and the failure is listed with the reason, for example:

```text
Column 'Salary': NUMBER: argument 1 must be a number, got Text 'abc' (at position 1)
```
