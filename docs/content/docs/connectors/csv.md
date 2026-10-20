---
title: CSV files
weight: 3
---

CSV files work as a source (every row is read) and as a target (rows are inserted). They are also handy as lookup tables. Files follow [RFC 4180](https://www.rfc-editor.org/rfc/rfc4180): values containing the delimiter, quotes or line breaks are enclosed in double quotes, and quotes inside them are doubled.

## The CSV dialog

**Configure...** on the Source or Targets tab:

| Setting | Default | Meaning |
| --- | --- | --- |
| **File** | | The file. **Browse...** selects it. A target file does not have to exist yet. |
| **Delimiter** | Auto | *Auto* detects comma, semicolon, tab or pipe from the first line (a new target file uses comma). Or choose one. |
| **Encoding** | UTF-8 | UTF-8, UTF-8 with BOM (best for Excel), UTF-16, Windows-1250, Windows-1252, ISO-8859-2, ISO-8859-1. A byte order mark in the file wins when reading. |
| **First row contains column names** | on | Without a header, columns are named `Column1`, `Column2`, … |
| **When writing** | Append | Target only: *Append rows to the file*, or *Replace the file at the start of each run*. |
| **Quotes** | Quote every value | Target only: *Quote every value* (`"a","b"`), or *Quote only values that need it* (`a,"b, c"`). |

**Preview file** shows the detected delimiter, the columns and the first row.

## Reading (source)

Every row of the file is read, blank lines are skipped. An empty unquoted value is null; a quoted empty value (`""`) is empty text.

All values are text, but text that holds numbers or dates works where numbers and dates are expected:

| Formula | Result for `qty = "3"`, `price = "2.50"`, `born = "1990-02-03"` |
| --- | --- |
| `qty * price` | `7.5` |
| `qty + 1` | `4` (`+` adds when both sides are numbers) |
| `born + 1` | 1990-02-04 |
| `price > 2` | TRUE (compared as numbers) |
| `qty & "x"` | `"3x"` (`&` always joins text) |

The connectors convert text to the column type when writing, so `"2.50"` can be written to a currency column directly.

Numbers with a decimal comma, such as `1,5`, are never guessed (it could be one and a half or fifteen). Convert them with `NUMBER(price, ",")`. Dates in other formats than `2024-01-31`, `2024/01/31` and `31.01.2024` are converted with `DATETIME(date, "MM/dd/yyyy")`.

## Writing (target)

CSV targets only support **Insert**: every insert writes one line.

- **A new file** (or *Replace the file*) gets a header row with the mapped columns of the first row, in mapping order. With *Replace the file*, the existing file is replaced when the first row is written, so a run that writes nothing leaves it untouched.
- **Append to an existing file** keeps its header and rows as they are and adds rows below. Mapped columns must exist in its header (case-insensitive); columns that are not mapped stay empty.
- **Values** are written as text: numbers with `.` as decimal separator, dates as ISO 8601 (`1990-02-03T00:00:00`). Use `FORMAT()` for other formats: `FORMAT(amount, "0.00")`, `FORMAT(date, "dd.MM.yyyy")`.
- **Nulls** are written as nothing (`"a",,"c"`), empty text as `""`, so both read back the same way.

The target's folder must exist and be writable; the file is checked when the run starts, before any row is processed.

## Lookup tables

A CSV target can be read with `LOOKUP` while the steps write to other targets. The table argument is ignored (the file is the table):

```text
LOOKUP("Country codes", "", "code", "name", country_code)
```

Rows written to the file during the run are found by later lookups.
