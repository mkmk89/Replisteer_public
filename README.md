# Replisteer

Replisteer moves and synchronises data between **Dataverse / Dynamics 365**, **SQL Server** and **CSV files**: read rows from a source, transform them with formulas, and write them to one or more targets with insert, update, upsert, delete and execute steps.

- **[Documentation](https://mkmk89.github.io/Replisteer_public/)**: user guide, formula reference and command line runner.
- **XrmToolBox tool:** install *Replisteer: Data Migration (ETL)* from the XrmToolBox Tool Library.
- **Command line runner:** download `replisteer-win-x64.zip` or `replisteer-linux-x64.tar.gz` from the [latest release](https://github.com/mkmk89/Replisteer_public/releases/latest).

## Questions, problems and ideas

[Open an issue](https://github.com/mkmk89/Replisteer_public/issues/new/choose). For problems, include the version (`replisteer version`, or the tool's version in XrmToolBox) and the messages, with connection details and personal data removed.

## License

Replisteer is free to use, also commercially, under the [PolyForm Perimeter License 1.0.0](LICENSE.md) with an additional permission: use it for anything, including paid work for your clients, but do not offer Replisteer itself (sold, repackaged or hosted) as a product or service of your own. See the license for the exact terms.

## This repository

It contains the [documentation site](docs/) (built and published by [.github/workflows/docs.yml](.github/workflows/docs.yml)) and the releases with the runner downloads; the source code of Replisteer is not public. Corrections to the documentation are welcome as pull requests. Some pages are generated from the source and are replaced on every release: the function reference (`docs/content/docs/formulas/functions.md`) and the files in `docs/assets/generated/`.

Preview the site locally with [Hugo](https://gohugo.io/) (extended, 0.158 or later) and Go: `cd docs && hugo server`, then open http://localhost:1313/Replisteer_public/.
