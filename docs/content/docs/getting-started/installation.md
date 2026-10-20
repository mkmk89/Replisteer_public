---
title: Installation
weight: 1
---

Replisteer has two parts. Most people only need the first one; the second runs projects without XrmToolBox.

## The XrmToolBox tool

Requirements:

- Windows with **.NET Framework 4.8** (included in current Windows 10 and 11).
- **XrmToolBox 1.2023.10.67** or later. XrmToolBox is free; download it from [xrmtoolbox.com](https://www.xrmtoolbox.com/). The portable version needs no installation.

{{% steps %}}

### Open the Tool Library

Start XrmToolBox and open **Configuration > Tool Library**.

### Install Replisteer

Search for **Replisteer**, select *Replisteer: Data Migration (ETL)* and click **Install**. XrmToolBox downloads the tool and asks to restart.

### Open the tool

After the restart, open **Tools** and start *Replisteer: Data Migration (ETL)*. A Dataverse connection is only needed for Dataverse sources and targets; you can connect at any time from the tool.

{{% /steps %}}

{{< callout type="info" >}}
Older XrmToolBox versions do not show the tool in the Tool Library. If the tool was copied into the plugins folder by hand, it shows a message asking to update XrmToolBox instead of opening.
{{< /callout >}}

Updates appear in the Tool Library like for any other tool.

## The command line runner

The runner runs saved projects without XrmToolBox: by hand, from scripts and pipelines, or with the Windows Task Scheduler. See [Command line runner](../../command-line/).

1. Download the archive for your system:
   - **Windows:** [replisteer-win-x64.zip]({{< download-url "replisteer-win-x64.zip" >}})
   - **Linux:** [replisteer-linux-x64.tar.gz]({{< download-url "replisteer-linux-x64.tar.gz" >}})
2. Extract it to a folder, for example `C:\Tools\Replisteer`. The archive contains one program file and a `README.txt` with the help.
3. Check that it works:

   ```bat
   C:\Tools\Replisteer\replisteer.exe version
   ```

The program includes .NET; nothing else needs to be installed.

{{< callout type="warning" >}}
The runner is not code-signed yet. The first time you run it, Windows may show *Windows protected your PC*: choose **More info > Run anyway**, or unblock the downloaded zip file first (right-click > **Properties** > **Unblock**).
{{< /callout >}}

On Linux, the archive keeps the executable permission:

```bash
mkdir -p ~/replisteer && tar -xzf replisteer-linux-x64.tar.gz -C ~/replisteer
~/replisteer/replisteer version
```

## Version compatibility

Projects are plain files with a format version. The tool and the runner read projects saved by the same or an older version. Keep both on the same release to be safe; the runner prints its version with `replisteer version`.
