---
title: Steps
weight: 5
---

The **4. Steps** tab defines what is written for every source row. The list on the left shows the steps in the order they run: the first step has a green flag, the others the icon of their operation. Select a step to edit it.

| Toolbar | What it does |
| --- | --- |
| **Add step** | Adds a step. A new step continues the chain: it becomes the *Then* step of the last step. |
| **Remove** | Removes the selected step. Links to it from other steps are cleared. |
| **Set as first** | Makes the selected step the first step. Links pointing *to* it are removed, because nothing may continue with the first step. |

## Step settings

| Setting | Meaning |
| --- | --- |
| **Name** | Shown in results and logs. |
| **Target** | The target the step writes to. |
| **Operation** | Insert, Update, Upsert, Delete or Execute. The available operations depend on what the target [writes to](../targets/#what-a-target-writes-to). |
| **Run only if** | Optional condition formula. When it is not TRUE (FALSE or null), the step is skipped and the chain continues with *Then*. |
| **Then** | The step that runs after this one succeeds or is skipped, or *(finish the row)*. |
| **If it fails** | *Continue with* a step (choose it in the next drop-down, or *(finish the row)*), *Skip the rest of the row*, or *Stop the run*. |
| **List failed rows in the run results** | When checked (the default), a failure of this step is listed with the row and the reason. Clear it for steps that are expected to fail sometimes, for example an insert that is allowed to hit a duplicate. |

### Operations

- **Insert** creates one record from the field mappings.
- **Update** updates every record that matches the match criteria. When nothing matches, the step succeeds without changes.
- **Upsert** updates every matching record, or inserts one when nothing matches.
- **Delete** deletes every record that matches the match criteria.
- **Execute** runs a stored procedure (SQL Server) or an on-demand workflow (Dataverse). The field mappings are the parameters.

## Field mappings

Each row of **Field mappings** sets one target column (or procedure parameter for Execute):

| Column | Meaning |
| --- | --- |
| **Target column** | The column. The drop-down lists the target's columns once they are loaded; an unknown name is shown in red with a tooltip. |
| **Value (formula)** | A [formula](../../formulas/) giving the value. `NULL` clears the column. |
| **...** | Opens the formula editor. |
| **Overwrite** | Update and upsert only. When cleared, the column is only filled when it is empty in the target, so existing values are kept. |

A column can be mapped only once per step; a duplicate row is marked with a red icon. Select rows and click **Remove** (or press **Delete**) to remove them.

**Map same names** adds a mapping for every writable target column that has a source field with the same name (ignoring case). **Load fields** loads the source fields and the target columns.

## Match criteria

Update, upsert and delete steps find their records with **Match criteria**: every row is a *target column equals formula* condition, and a record matches when **all** of them are true. A criterion whose value is null matches records where the column is empty.

| Target column | Equals (formula) |
| --- | --- |
| `accountnumber` | `TRIM(customer_no)` |
| `statecode` | `0` |

At least one criterion is required, so a step can never affect every record of a table by mistake.

{{< callout type="info" >}}
Match on a business key that identifies records in both systems (an account number, an e-mail address, an external id column), not on GUIDs that differ between environments.
{{< /callout >}}

## The field panel

The panel on the right lists everything a formula can use at this step, grouped by kind:

- **Target columns** of the step's target.
- **Source fields**.
- **Calculated variables**.
- **Previous steps**: values written by steps that can run before this one (`V_<step>_<column>`) and ids of records they created (`V_<step>_ID`).

Drag a target column onto the *Target column* cell of a mapping, and anything else onto a *Value* cell. Double-click a target column to add a mapping for it, or a source field to add a mapping to the column with the same name.

## Example: account and contact in one row

| Step | Target / operation | Mappings and criteria |
| --- | --- | --- |
| 1 `Account` | CRM `account`, Upsert | criteria `accountnumber` = `customer_no`; mappings `name` = `company`, `accountnumber` = `customer_no` |
| 2 `Contact` | CRM `contact`, Upsert | criteria `emailaddress1` = `LOWERCASE(email)`; mappings `lastname` = `lastname`, `parentcustomerid` = `CreateEntityReference("account", LOOKUP("CRM", "account", "accountnumber", "accountid", customer_no))` |

When step 1 *inserts* the account, `V_1_ID` holds its reference (`account:<guid>`) and step 2 can map `parentcustomerid` = `V_1_ID` directly. After an *update*, `V_1_ID` is empty, which is why the example looks the account up instead. Both work for both cases: `COALESCE(V_1_ID, CreateEntityReference("account", LOOKUP(…)))`.
