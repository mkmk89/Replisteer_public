---
title: Project tab
weight: 1
---

The **Project** tab holds the settings of the project as a whole.

| Setting | Meaning |
| --- | --- |
| **Project name** | Shown in the toolbar, in run logs and as the default file name. |
| **Description** | Free text, saved with the project. Useful for notes about what the project does and when to run it. |
| **File** | Where the project is saved; empty until the first save. |
| **Save SQL Server passwords in project files** | When checked (the default), SQL Server passwords are saved encrypted for your Windows account. When cleared, project files are saved without passwords; enter them again after opening the file. This is a setting of the tool, not of one project. |

{{< callout type="info" >}}
Encrypted passwords can only be read by the same Windows account on the same computer (Windows DPAPI). Another user opening the file, or the runner on a server, needs the password again. See [Project files](../project-files/#passwords-and-secrets).
{{< /callout >}}

## Dataverse environments

The list shows the XrmToolBox connections the project uses: the main connection of the tool (the one selected in XrmToolBox when the tool opened) and every additional environment, with its URL and which source or targets use it.

- **Connect another environment...** opens the XrmToolBox connection dialog and adds the environment, so a source or target can use it.
- **Remove** removes an additional environment from the tool. When a source or target still uses it, the tool asks first; those connections then need to be linked again.

The project file only stores which XrmToolBox connection each source or target uses (its id, name and URL), never credentials. When you open a project on another computer, Replisteer links the connections by id, then by name, then by URL. Connections it cannot link are listed in the notice strip; choose them on the Source and Targets tabs.
