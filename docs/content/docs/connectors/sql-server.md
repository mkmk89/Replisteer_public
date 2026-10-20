---
title: SQL Server
weight: 2
---

The SQL Server connector works with SQL Server, Azure SQL Database and Azure SQL Managed Instance. It reads with any query and writes to tables, views or stored procedures. All values are sent as typed parameters, never pasted into SQL text.

## The connection dialog

**Configure...** on the Source or Targets tab opens the connection dialog:

| Setting | Meaning |
| --- | --- |
| **Server** | Server name, `server\instance`, `server,port`, or `myserver.database.windows.net` for Azure SQL. |
| **Authentication** | SQL Server authentication (user name and password) or Windows authentication. |
| **User name**, **Password** | For SQL Server authentication. |
| **Database** | The database. **List databases** reads the list from the server. |
| **Encrypt connection** | Encrypts the connection (required by Azure SQL). |
| **Trust server certificate** | Accepts the server's certificate without validating it. Needed for servers with a self-signed certificate, such as a local development server or container. |
| **Connect timeout (s)** | How long to wait for the connection. |
| **Command timeout (s)** | How long a query or write may take (default 30). Increase it for slow source queries. |
| **Edit the connection string directly** | Shows the connection string itself, for options the dialog does not have. |

**Test connection** checks the settings. Passwords are saved in the project file encrypted for your Windows account, or not at all; see [Project files](../../xrmtoolbox/project-files/#passwords-and-secrets).

Outside XrmToolBox the connection is a standard connection string:

```text
Server=sql.contoso.com;Database=dw;User ID=replisteer;Password=<password>;Encrypt=true
Server=myserver.database.windows.net;Database=dw;User ID=replisteer;Password=<password>;Encrypt=true
Server=localhost,1433;Database=dw;Integrated Security=true;TrustServerCertificate=true
```

## Reading (source)

Any query that returns rows: `SELECT`, views, or `EXEC` of a stored procedure. Each column is a field named like the column. See [Source: SQL query](../../xrmtoolbox/source/#sql-server-sql-query).

## Writing (target)

Set the target's *Writes to* to **Table or view** (insert, update, upsert, delete) or **Stored procedure** (execute). The object name may include the schema and database: `dbo.Contacts`, `staging.[Customer Import]`. Names are quoted, so spaces and reserved words are fine.

| Operation | SQL |
| --- | --- |
| Insert | `INSERT INTO … VALUES (…)`. The identity of the new row (`SCOPE_IDENTITY()`) is available to later steps as `V_<step>_ID`; it is empty for tables without an identity column. |
| Update | `UPDATE … SET … WHERE <criteria>`. Columns with *Overwrite* cleared are only set where they are `NULL`. |
| Upsert | The update; when it matches no rows, the insert. |
| Delete | `DELETE FROM … WHERE <criteria>`. |
| Execute | Calls the stored procedure. Map every parameter by name, with or without `@` (`CustomerId` or `@CustomerId`). |

Criteria are combined with `AND`. A criterion with a null value becomes `column IS NULL`.

{{< callout type="info" >}}
Each step is a separate statement in its own implicit transaction. To make several writes atomic, or to apply set-based logic, write them in a stored procedure and call it with an Execute step.
{{< /callout >}}

## Values written to SQL columns

Values are converted to the type of the column (or parameter):

| SQL type | Accepted values |
| --- | --- |
| `char`, `varchar`, `nchar`, `nvarchar`, `text`, `xml` | Any value, as text. |
| `bit` | TRUE/FALSE, `"true"`/`"false"`, numbers (0 is false). |
| `tinyint`, `smallint`, `int`, `bigint` | Whole numbers, or text holding one. |
| `decimal`, `numeric`, `money`, `float`, `real` | Numbers, or text holding a number with `.` as decimal separator. |
| `date`, `datetime`, `datetime2`, `smalldatetime`, `datetimeoffset`, `time` | Dates, or text in ISO format, `yyyy/MM/dd` or `dd.MM.yyyy`. |
| `uniqueidentifier` | A GUID, or `table:guid` (its GUID). |
| `binary`, `varbinary` | Base64 text. |

Null writes `NULL`. Empty text writes `NULL` to non-text columns, but an empty string to text columns; use `IF(ISNULL(x), NULL, x)` to write `NULL` instead. A value that cannot be converted fails the row: `Value 'abc' cannot be converted to SQL type Int`.

## Reading with LOOKUP

`LOOKUP("Warehouse", "dbo.Customers", "CustomerNo", "Id", customer_no)` runs `SELECT TOP (1) [Id] FROM [dbo].[Customers] WHERE [CustomerNo] = @value` on the target's database.
