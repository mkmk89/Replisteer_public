---
title: Examples
weight: 6
---

## A log file per run

A batch file that keeps one log per day:

```bat
@echo off
for /f %%d in ('powershell -NoProfile -Command "Get-Date -Format yyyy-MM-dd"') do set TODAY=%%d
"C:\Tools\Replisteer\replisteer.exe" run --project "C:\Projects\accounts.replisteer.json" ^
  --connections "C:\Projects\accounts.connections.json" ^
  --output "C:\Logs\accounts-%TODAY%.log"
exit /b %ERRORLEVEL%
```

## PowerShell

```powershell
$runner  = 'C:\Tools\Replisteer\replisteer.exe'
$project = 'C:\Projects\accounts.replisteer.json'
$result  = "C:\Logs\accounts-$(Get-Date -Format yyyy-MM-dd-HHmm).json"

& $runner run --project $project --connections 'C:\Projects\accounts.connections.json' --output $result --quiet
$code = $LASTEXITCODE

$summary = Get-Content $result -Raw | ConvertFrom-Json
switch ($code) {
    0 { Write-Host "OK: $($summary.summary)" }
    2 { Write-Warning "$($summary.result.rowsFailed) row(s) failed: $($summary.summary)" }
    default { Write-Error "Run failed ($code): $($summary.summary)" }
}
exit $code
```

## Several projects in order

Run a chain of projects and stop at the first that does not complete:

```bat
@echo off
set R=C:\Tools\Replisteer\replisteer.exe
set C=--connections C:\Projects\prod.connections.json
for %%p in (accounts contacts opportunities) do (
  "%R%" run --project C:\Projects\%%p.replisteer.json %C% --output C:\Logs\%%p.log
  if errorlevel 1 if not errorlevel 2 (echo %%p failed & exit /b 1)
  if errorlevel 3 (echo %%p is not valid & exit /b 3)
)
```

One connections file can serve several projects: it lists connections by name, and each project uses the names it has.

## Azure DevOps pipeline

Run a migration as a deployment step, with the connection strings in secret pipeline variables:

```yaml
steps:
  - pwsh: |
      Invoke-WebRequest {{< download-url "replisteer-win-x64.zip" >}} -OutFile replisteer.zip
      Expand-Archive replisteer.zip -DestinationPath replisteer
      ./replisteer/replisteer.exe validate --project migration/accounts.replisteer.json
      ./replisteer/replisteer.exe run --project migration/accounts.replisteer.json --output $(Build.ArtifactStagingDirectory)/accounts.json
    displayName: Migrate accounts
    env:
      Connection__CRM__ConnectionString: $(CrmConnectionString)
      Connection__Legacy__ConnectionString: $(LegacyConnectionString)
  - publish: $(Build.ArtifactStagingDirectory)
    artifact: migration-results
    condition: always()
```

## GitHub Actions

```yaml
jobs:
  migrate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Get the runner
        run: |
          mkdir -p "$HOME/replisteer"
          curl -sSL {{< download-url "replisteer-linux-x64.tar.gz" >}} | tar -xz -C "$HOME/replisteer"
          echo "$HOME/replisteer" >> "$GITHUB_PATH"
      - name: Migrate accounts
        env:
          Connection__CRM__ConnectionString: ${{ secrets.CRM_CONNECTION_STRING }}
        run: |
          replisteer validate --project migration/accounts.replisteer.json
          replisteer run --project migration/accounts.replisteer.json --output results/accounts.json
      - uses: actions/upload-artifact@v4
        if: always()
        with:
          name: migration-results
          path: results/
```

## Linux cron

```bash
# crontab -e: every night at 02:00
0 2 * * * /opt/replisteer/replisteer run --project /srv/replisteer/accounts.replisteer.json --connections /srv/replisteer/connections.json --output /var/log/replisteer/accounts.log --quiet
```

## A different input file every day

Give a CSV source another path than the one saved in the project:

```bat
replisteer run --project import.replisteer.json --source "D:\Incoming\orders-%DATE:~-4%%DATE:~3,2%%DATE:~0,2%.csv"
```

(`%DATE%` depends on the regional settings of the computer; adjust the offsets, or build the name in PowerShell.)
