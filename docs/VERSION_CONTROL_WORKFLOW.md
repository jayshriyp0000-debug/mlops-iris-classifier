# Version Control Workflow for MLOps Iris Classifier

## 1. Branching Model

The project uses Git branches to manage development.

- main: Stable version of the project.
- develop: Development branch.
- feature branches: Used for adding new features.
- conflict-demo-a and conflict-demo-b: Used to demonstrate merge conflicts.

## 2. Commit Convention

Meaningful commit messages are used.

Examples:

- chore: initialize project structure
- feat: add classification report
- docs: add version control workflow documentation
- merge: resolve README conflict

## 3. Pull Request Review

Feature branches are pushed to GitHub and a Pull Request is created.

The Pull Request is reviewed before merging into the develop branch.

## 4. Conflict Resolution

When two branches modify the same part of a file, Git may create a merge conflict.

The conflict is resolved manually by selecting the correct content and removing conflict markers.

After resolving the conflict:

git add README.md

git commit -m "merge: resolve README conflict between version A and B"

## 5. .gitignore Policy

The .gitignore file prevents unnecessary files from being tracked.

Examples include:

- Python cache files
- Virtual environments
- Data files
- Model files
- IDE files
- Environment files

## 6. Verification Checklist

- Git repository initialized
- Main and develop branches created
- Feature branch created
- Pull Request created
- Merge conflict demonstrated
- Conflict successfully resolved
- Training script executed successfully
- Model generated successfully
- Documentation added