---
title: Function reference
weight: 2
---

<!-- Generated from the function catalog by GeneratedDocsTests; do not edit (run the tests with REPLISTEER_UPDATE_DOCS=1). -->

Every value, operator and function of the formula language. The formula editor in XrmToolBox shows the same descriptions. The [formula language](../) page explains how values, nulls and conversions work.

## Values

| Syntax | Meaning |
| --- | --- |
| `"text"` | Text in double or single quotes. Double the quote to include it: "say ""hi""". |
| `#2024-01-31 13:00#` | A date/time value. |
| `TRUE` | Boolean true. |
| `FALSE` | Boolean false. |
| `NULL` | No value; clears the target column. |
| `[Field name]` | A field whose name contains spaces or other special characters. |
| `name`, `alias.name` | A source field, calculated variable or previous step value (case-insensitive). |
| `V_<step id>_<column>` | The value a previous step wrote to a column, e.g. `V_1_name`. |
| `V_<step id>_ID` | The id of the record a previous insert / upsert step created (Dataverse: `table:guid`, SQL Server: identity). |

## Operators

| Operator | Meaning |
| --- | --- |
| `+` | Adds numbers (also numbers stored as text, e.g. from CSV files), adds days to a date, otherwise joins text (null counts as empty text). Use &amp; to always join. |
| `-` | Subtracts numbers, subtracts days from a date, or returns the number of days between two dates (also when they are stored as text). |
| `*` | Multiplies numbers. |
| `/` | Divides numbers. |
| `%` | Remainder of a division (also MOD). |
| `&` | Joins two values as text. |
| `=` | TRUE when both values are equal. A number equals text with the same value; two texts must match exactly ("007" &lt;&gt; "7"). Null equals empty text. |
| `<>` | TRUE when the values are different (also !=). |
| `<` | TRUE when the left value is lower. Texts holding numbers or dates are compared by value, other texts alphabetically. |
| `<=` | TRUE when the left value is lower or equal. |
| `>` | TRUE when the left value is greater. |
| `>=` | TRUE when the left value is greater or equal. |
| `AND` | TRUE when both conditions are TRUE. |
| `OR` | TRUE when any condition is TRUE. |
| `NOT` | Reverses a condition: NOT ISNULL(name). |

Precedence, lowest first: `OR`, `AND`, `NOT`, `= <> !=`, `< <= > >=`, `+ - &`, `* / % MOD`, unary `-`.

## Conversion functions

### ARRAY

```text
ARRAY(<value>, [<value>], ...)
```

Creates an array that can be used with SUM(), MIN() etc. Written to a target as JSON text. Example: SUM(ARRAY(1, 2, 3)) = 6

### DATETIME

```text
DATETIME(<text>, [<format>])
```

Converts text to a date/time. Without a format ISO dates (2024-01-31 13:00), yyyy/MM/dd and dd.MM.yyyy are recognised. Empty text gives null. Example: DATETIME("31/01/2024", "dd/MM/yyyy")

### NEWGUID

```text
NEWGUID()
```

Returns a new random GUID as text.

### NUMBER

```text
NUMBER(<text>, [<decimal separator>])
```

Converts text to a number. The decimal separator is '.' unless given; thousands separators (space, apostrophe, or the other of '.' and ',') are ignored. Empty text gives null. Example: NUMBER("1 234,5", ",") = 1234.5

### TEXT

```text
TEXT(<value>)
```

Converts a value to text. Example: TEXT(123) = "123"

## Data functions

### LOOKUP

```text
LOOKUP(<target id or name>, <table>, <search column>, <result column>, <value to find>)
```

Reads a value from a target: returns &lt;result column&gt; of the first record of &lt;table&gt; where &lt;search column&gt; equals the value, or null when nothing is found. For CSV targets &lt;table&gt; is ignored (the file is the table). Example: LOOKUP(1, "account", "accountnumber", "accountid", ACCOUNTNO)

### XLOOKUP

```text
XLOOKUP(<target id or name>, <table>, <search column>, <result column>, <value to find>)
```

Returns TRUE when exactly one record of &lt;table&gt; has &lt;search column&gt; equal to the value.

## Dataverse functions

### CreateEntityReference

```text
CreateEntityReference("<table logical name>", <guid>)
```

Creates a lookup value for a Dataverse lookup column. Example: CreateEntityReference("account", "b9564ad3-6eb0-4003-9134-72d906f73d9c")

### CreatePartyList

```text
CreatePartyList(<lookup>, [<lookup>], ...)
```

Creates a party list value (e.g. email To/Cc) from lookup values or an ARRAY() of them.

### GetGuid

```text
GetGuid(<lookup>)
```

Returns the GUID of a lookup value. Example: GetGuid(parentcustomerid)

## Date and time functions

### ADDDAYS

```text
ADDDAYS(<date>, <number of days>)
```

Adds days to a date (use a negative number to subtract).

### ADDHOURS

```text
ADDHOURS(<date>, <number of hours>)
```

Adds hours to a date (use a negative number to subtract).

### ADDMINUTES

```text
ADDMINUTES(<date>, <number of minutes>)
```

Adds minutes to a date (use a negative number to subtract).

### ADDMONTHS

```text
ADDMONTHS(<date>, <number of months>)
```

Adds months to a date (use a negative number to subtract).

### ADDSECONDS

```text
ADDSECONDS(<date>, <number of seconds>)
```

Adds seconds to a date (use a negative number to subtract).

### ADDYEARS

```text
ADDYEARS(<date>, <number of years>)
```

Adds years to a date (use a negative number to subtract).

### DATEDIFFDAYS

```text
DATEDIFFDAYS(<start date>, <end date>, [<allow fractions>])
```

Returns the number of days between two dates. Without fractions the result is truncated to whole days.

### DATEDIFFHOURS

```text
DATEDIFFHOURS(<start date>, <end date>, [<allow fractions>])
```

Returns the number of hours between two dates. Without fractions the result is truncated to whole hours.

### DATEDIFFMINUTES

```text
DATEDIFFMINUTES(<start date>, <end date>, [<allow fractions>])
```

Returns the number of minutes between two dates. Without fractions the result is truncated to whole minutes.

### DATEDIFFSECONDS

```text
DATEDIFFSECONDS(<start date>, <end date>, [<allow fractions>])
```

Returns the number of seconds between two dates. Without fractions the result is truncated to whole seconds.

### DAY

```text
DAY(<date>)
```

Returns the day of the month (1-31) of a date.

### HOUR

```text
HOUR(<date>)
```

Returns the hour (0-23) of a date.

### MINUTE

```text
MINUTE(<date>)
```

Returns the minute (0-59) of a date.

### MONTH

```text
MONTH(<date>)
```

Returns the month (1-12) of a date.

### NOW

```text
NOW()
```

Returns the current date and time in UTC.

### SECOND

```text
SECOND(<date>)
```

Returns the second (0-59) of a date.

### TODAY

```text
TODAY()
```

Returns the current local date without time.

### YEAR

```text
YEAR(<date>)
```

Returns the year of a date.

## Logical functions

### COALESCE

```text
COALESCE(<value>, <value>, ...)
```

Returns the first value that is not null or empty text.

### IF

```text
IF(<condition>, <value if true>, <value if false>)
```

Returns the second argument when the condition is TRUE, otherwise the third. Only the returned branch is evaluated. Example: IF(1 = 1, "Yes", "No") = "Yes"

### ISARRAY

```text
ISARRAY(<value>)
```

Returns TRUE when the value is an array.

### ISDATETIME

```text
ISDATETIME(<value>)
```

Returns TRUE when the value is a date/time or text in a recognised date format (2024-01-31, 2024/01/31, 31.01.2024, optionally with time).

### ISNOTNULL

```text
ISNOTNULL(<value>)
```

Returns TRUE when the value is neither null nor empty text.

### ISNULL

```text
ISNULL(<value>)
```

Returns TRUE when the value is null or empty text.

### ISNUMBER

```text
ISNUMBER(<value>)
```

Returns TRUE when the value is a number or text that converts to one ('.' as decimal separator). Example: ISNUMBER("12.5") = TRUE, ISNUMBER("12,5") = FALSE

### ISTEXT

```text
ISTEXT(<value>)
```

Returns TRUE when the value is text.

## Math functions

### ABS

```text
ABS(<number>)
```

Returns the absolute value.

### AVG

```text
AVG(<array of numbers>)
```

Returns the average of the numbers in an array or of the arguments. Null values are ignored. Example: AVG(ARRAY(1, 2, 3))

### CEILING

```text
CEILING(<number>)
```

Returns the smallest integer greater than or equal to the number.

### COUNT

```text
COUNT(<array>)
```

Returns the number of items in the array (or the number of arguments).

### EXP

```text
EXP(<number>)
```

Returns e raised to the given power.

### FLOOR

```text
FLOOR(<number>)
```

Returns the largest integer less than or equal to the number.

### LOG

```text
LOG(<number>)
```

Returns the natural (base e) logarithm.

### MAX

```text
MAX(<array of numbers>)
```

Returns the maximum of the numbers in an array or of the arguments. Null values are ignored. Example: MAX(ARRAY(1, 2, 3))

### MIN

```text
MIN(<array of numbers>)
```

Returns the minimum of the numbers in an array or of the arguments. Null values are ignored. Example: MIN(ARRAY(1, 2, 3))

### POW

```text
POW(<number>, <power>)
```

Returns a number raised to a power. Example: POW(2, 3) = 8

### RND

```text
RND()
```

Returns a random number greater than or equal to 0 and less than 1.

### ROUND

```text
ROUND(<number>, [<decimals>])
```

Rounds a number to the given number of decimals (half away from zero). Example: ROUND(2.145, 2) = 2.15

### SQRT

```text
SQRT(<number>)
```

Returns the square root.

### SUM

```text
SUM(<array of numbers>)
```

Returns the sum of the numbers in an array or of the arguments. Null values are ignored. Example: SUM(ARRAY(1, 2, 3))

## Text functions

### CHR

```text
CHR(<character code>)
```

Returns the character with the given Unicode code. Example: CHR(10) is a line break.

### CONTAINS

```text
CONTAINS(<text>, <text to find>)
```

Returns TRUE when the text contains the other text (case-insensitive).

### FORMAT

```text
FORMAT(<value>, [<format>])
```

Formats a number or date with a .NET format string (invariant culture); text holding a number or date (e.g. from a CSV file) is formatted the same way. Example: FORMAT(15, "0.00") = "15.00", FORMAT(#2024-01-05#, "dd.MM.yyyy") = "05.01.2024", FORMAT("42", "000000") = "000042"

### LEFT

```text
LEFT(<text>, <number of characters>)
```

Returns the given number of characters from the start of the text.

### LEN

```text
LEN(<text>)
```

Returns the number of characters in the text.

### LOWERCASE

```text
LOWERCASE(<text>)
```

Converts text to lower case.

### MID

```text
MID(<text>, <start>, [<number of characters>])
```

Returns part of the text starting at a 1-based position. Example: MID("abcdef", 2, 3) = "bcd"

### NULL

```text
NULL()
```

Returns null, which clears the target column.

### REPLACE

```text
REPLACE(<text>, <text to find>, <replacement>)
```

Replaces every occurrence of a text. Example: REPLACE("a-b-c", "-", "") = "abc"

### RIGHT

```text
RIGHT(<text>, <number of characters>)
```

Returns the given number of characters from the end of the text.

### TRIM

```text
TRIM(<text>)
```

Removes leading and trailing white space.

### UPPERCASE

```text
UPPERCASE(<text>)
```

Converts text to upper case.
