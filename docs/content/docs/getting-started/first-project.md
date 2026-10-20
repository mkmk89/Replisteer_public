---
title: Your first project
weight: 2
---

This walkthrough imports contacts from a CSV file into Dataverse. Existing contacts (matched by e-mail address) are updated, new ones are created, and each contact is linked to its account by the account name. It takes about ten minutes and touches every part of the tool.

## Before you start

You need XrmToolBox with Replisteer [installed](../installation/), an XrmToolBox connection to a Dataverse environment you may write to (a trial or development environment is best for trying things out), and a CSV file. Save this one as `contacts.csv`:

```text
firstname;lastname;email;company;birthdate
Jane;Doe;jane.doe@example.com;Contoso Ltd;1990-02-03
John;Smith;JOHN.SMITH@example.com ;Fabrikam Inc;
Anna;Kowalska;anna.k@example.com;Contoso Ltd;31.12.1985
```

## Build the project

{{% steps %}}

### Start a new project

Open *Replisteer: Data Migration (ETL)* in XrmToolBox. A new, empty project opens on the **Project** tab. Enter a **Project name**, for example `Import contacts`.

### Configure the source

Open the **1. Source** tab.

1. Set **Source type** to *CSV file*.
2. Click **Configure...** and select `contacts.csv`. Leave the delimiter on *Auto* (it detects the `;`), the encoding on *UTF-8* and *First row contains column names* checked. **Preview file** shows the detected delimiter, the columns and the first row. Click **OK**.
3. Click **Load fields**. The field list shows `firstname`, `lastname`, `email`, `company` and `birthdate`.

A CSV source needs no query: every row of the file is read.

### Add the Dataverse target

Open the **2. Targets** tab.

1. Click **Add target > Dataverse / Dynamics 365**.
2. Change the **Name** to `CRM`. Formulas use this name to look up data in the target.
3. Next to **Connection**, click **Choose...** and pick your XrmToolBox connection (or *Connect to an environment...* to add one).
4. Leave **Writes to** on *Table*, click **Browse...** next to **Table** and pick `contact`.
5. Click **Load columns** to read the contact columns.

### Add a step

Open the **4. Steps** tab and click **Add step**.

1. Set **Name** to `Upsert contact`, **Target** to *CRM (contact)* and **Operation** to *Upsert (update, or insert if none match)*.
2. In **Match criteria**, add a row: **Target column** `emailaddress1`, **Equals (formula)** `LOWERCASE(TRIM(email))`. An upsert updates every contact with that e-mail address, or creates one when there is none.
3. In **Field mappings**, add these rows. Type the column names, pick them from the drop-down, or drag fields from the panel on the right:

   | Target column | Value (formula) |
   | --- | --- |
   | `firstname` | `TRIM(firstname)` |
   | `lastname` | `TRIM(lastname)` |
   | `emailaddress1` | `LOWERCASE(TRIM(email))` |
   | `birthdate` | `DATETIME(birthdate)` |
   | `parentcustomerid` | `CreateEntityReference("account", LOOKUP("CRM", "account", "name", "accountid", company))` |

The **...** button on each row opens the formula editor, which lists every field and function and checks the formula as you type.

The last mapping looks up the account by name in the same environment and links the contact to it. `parentcustomerid` can point to an account or a contact, so `CreateEntityReference` says which table the id belongs to. When no account has that name, `LOOKUP` returns nothing and the column stays empty.

{{% /steps %}}

## Check it

{{% steps %}}

### Validate

Open the **5. Run** tab and click **Validate**. It lists problems in the configuration, for example a misspelled column or a formula error. Warnings, such as a required column that is not mapped, do not stop a run.

### Preview

Click **Preview**. Replisteer reads the first rows (20 by default; change it next to the button), evaluates every formula and shows what it *would* write in the **Preview** results tab, without changing anything in Dataverse. Check the values: the e-mail of John is trimmed and lower-cased, and both date formats became dates.

{{< callout type="info" >}}
A preview still reads from the targets: `LOOKUP` queries the accounts, so the preview shows the real account references.
{{< /callout >}}

### Run

Click **Run** (or press **F5**) and confirm. When the run finishes, the results show how many rows were read and failed, statistics per step and the full log. Rows that failed are listed with the reason. **Export...** saves any of these as a file.

{{% /steps %}}

## Save it

Press **Ctrl+S** and save the project, for example as `contacts.replisteer.json`. The file contains the whole project; reopen it later with **Open**, or the recent-files list next to it.

## Next steps

- Run the same project every night without XrmToolBox: click **Schedule...** in the toolbar, or read [Command line runner](../../command-line/).
- Learn how the parts fit together in [Concepts](../concepts/).
- Browse the [formula functions](../../formulas/functions/) and [recipes](../../formulas/recipes/).
