# MXD-MDA Exports

This directory is reserved for generated local exports.

## Dashboard Exports

Run:

```bash
python src/orchestrator/main.py export-dashboard
```

or:

```bash
npm run dashboard:export
```

The command writes a timestamped JSON file using this naming pattern:

```text
MXD_MDA_DASHBOARD_YYYYMMDDTHHMMSSZ_v01.json
```

## Git Discipline

Generated export files are intentionally ignored by Git. Keep this README tracked so the folder has a documented purpose, but do not commit generated operational exports unless a release task explicitly requires it.

## Safety Rule

Dashboard exports are read-only snapshots. They must not trigger publishing, social posting, email automation, bot deployment, or Notion writes.
