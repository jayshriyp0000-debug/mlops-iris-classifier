# DVC Workflow

## Remote Configuration

A local folder was configured as the default DVC remote:

~/dvc-remote-storage

## Dataset Versioning Workflow

For every dataset change, the following workflow was used:

dvc add
git add
git commit
dvc push

DVC tracks the actual dataset while Git tracks the DVC metafile.

## Dataset Versions

Version 1:
150 rows

Version 2:
170 rows

## Comparing Versions

The `dvc diff` command was used to compare dataset versions.

## Restoring Versions

`git checkout` was used to restore the required DVC metafile.

`dvc checkout` was then used to restore the actual dataset corresponding to that metafile.

Version 1 was restored to 150 rows and Version 2 was restored to 170 rows.