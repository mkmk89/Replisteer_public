---
title: Recipes
weight: 3
---

Formulas for common tasks. Field names are examples; use your own.

## Text

| Task | Formula |
| --- | --- |
| Full name from two fields, without extra spaces | `TRIM(firstname + " " + lastname)` |
| Clean an e-mail address | `LOWERCASE(TRIM(email))` |
| Default for an empty value | `COALESCE(phone, mobile, "unknown")` |
| First 100 characters (column length limits) | `LEFT(description, 100)` |
| Remove dashes from a number | `REPLACE(tax_id, "-", "")` |
| Postal code from "00-950 Warsaw" | `LEFT(address_line, 6)` |
| Text with a line break | `street + CHR(10) + city` |
| Zero-padded code | `FORMAT(customer_no, "000000")` |

## Numbers

| Task | Formula |
| --- | --- |
| Decimal comma from a CSV file or Excel | `NUMBER(amount, ",")` |
| Round to two decimals | `ROUND(price * qty, 2)` |
| Percentage to a fraction | `discount / 100` |
| Sum of several fields, ignoring empty ones | `SUM(ARRAY(q1, q2, q3, q4))` |
| Empty instead of zero | `IF(amount = 0, NULL, amount)` |

## Dates

| Task | Formula |
| --- | --- |
| Date in a fixed format | `DATETIME(birth_date, "MM/dd/yyyy")` |
| End of a 30-day trial | `ADDDAYS(start_date, 30)` |
| Age in years | `FLOOR(DATEDIFFDAYS(birthdate, TODAY()) / 365.25)` |
| Today as text for a file or a name | `FORMAT(TODAY(), "yyyy-MM-dd")` |
| Only dates in the future | `IF(due_date > NOW(), due_date, NULL)` |

## Conditions

As the *Run only if* condition of a step:

| Task | Condition |
| --- | --- |
| Only rows with an e-mail address | `ISNOTNULL(email)` |
| Only active customers | `status = "Active"` |
| Only when the record does not exist yet | `ISNULL(LOOKUP("CRM", "contact", "emailaddress1", "contactid", email))` |
| Only large orders from Poland | `amount >= 1000 AND country = "PL"` |

## Choices and yes/no

| Task | Formula |
| --- | --- |
| Map codes to a choice value | `IF(type = "C", 1, IF(type = "S", 2, 3))` |
| A choice by its label | `"Preferred Customer"` (the label is converted to its value) |
| Yes/no from "Y"/"N" | `flag = "Y"` |
| Several values of a multi-select choice | `"Red;Blue"` |

## Lookups and references

| Task | Formula |
| --- | --- |
| Link to an account found by its number | `CreateEntityReference("account", LOOKUP("CRM", "account", "accountnumber", "accountid", customer_no))` |
| Link to the record created by step 1 | `V_1_ID` |
| Owner by the user's e-mail | `CreateEntityReference("systemuser", LOOKUP("CRM", "systemuser", "internalemailaddress", "systemuserid", owner_email))` |
| A value from a mapping table in SQL Server | `LOOKUP("Warehouse", "dbo.CountryMap", "OldCode", "NewCode", country)` |
| A value from a CSV lookup file | `LOOKUP("Codes", "", "code", "name", code)` |
| E-mail recipients (party list) | `CreatePartyList(CreateEntityReference("contact", contact_id), CreateEntityReference("systemuser", user_id))` |
| GUID of a lookup, for a SQL column | `GetGuid(parentcustomerid)` |

## Ids

| Task | Formula |
| --- | --- |
| A new GUID for each row | `NEWGUID()` |
| A key from two fields | `UPPERCASE(country) & "-" & customer_no` |
