---
title: Variables
weight: 4
---

**Calculated variables** are values computed once per source row, before the first step runs. Steps (and later variables) use them by name, like source fields. Use them for values needed by several steps or mappings, or to keep long formulas readable.

| Column | Meaning |
| --- | --- |
| **Name** | Letters, digits and `_`, starting with a letter or `_`. Unique within the project. |
| **Formula** | Any [formula](../../formulas/). **...** opens the formula editor. |

The toolbar adds, removes and reorders variables. They are calculated **in the order of the list**, so a variable can use the variables above it.

## Example

| Name | Formula |
| --- | --- |
| `Email` | `LOWERCASE(TRIM(email))` |
| `AccountId` | `LOOKUP("CRM", "account", "accountnumber", "accountid", TRIM(customer_no))` |
| `IsNew` | `ISNULL(LOOKUP("CRM", "contact", "emailaddress1", "contactid", Email))` |

A step can then map `emailaddress1` to `Email`, use `IsNew` as its *Run only if* condition, and link the contact with `CreateEntityReference("account", AccountId)`.

## Things to know

- A variable that fails (for example a conversion error) marks the row as failed and its steps do not run. The failure is listed with the variable's name.
- When a variable has the same name as a source field, formulas see the variable. Validation warns about this.
- Variables are evaluated for every row, also in a preview. A `LOOKUP` in a variable runs once per row, not once per step.
