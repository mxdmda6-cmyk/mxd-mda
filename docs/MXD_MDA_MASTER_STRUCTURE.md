# 🜁 MXD-MDA Master Repository Structure

**Last Updated:** November 2, 2025
**Status:** Strategic Reorganization in Progress
**Branch:** `claude/mxd-mda-strategic-review-011CUjMFomgYZphRsBDrsmLE`

---

## 📋 Repository Purpose

This repository serves as the **operational hub** for the MXD-MDA transmedia ecosystem, housing:
- Strategic planning documents
- Production workflows and checklists
- Technical infrastructure for AI agents
- Project coordination tools
- Brand assets and guidelines

---

## 🗂️ Current Directory Structure

```
mxd-mda/
├── .github/                    # GitHub workflows and actions
├── .devcontainer/             # Development environment config
├── docs/                      # Strategic documentation (THIS IS YOUR HUB)
│   ├── MXD_MDA_MASTER_STRUCTURE.md (this file)
│   ├── CONSOLIDATION_ROADMAP.md
│   ├── PROJECT_MASTER_MAP.md
│   ├── operations/
│   │   ├── Q4_2025_SPRINT_CALENDAR.md
│   │   ├── WEEKLY_REVIEW_TEMPLATE.md
│   │   └── RISK_REGISTER.md
│   ├── projects/
│   │   ├── wheres-crow/
│   │   │   ├── PRODUCTION_CHECKLIST.md
│   │   │   ├── MANUSCRIPT_STATUS.md
│   │   │   ├── ART_ASSET_INVENTORY.md
│   │   │   └── KICKSTARTER_PREP.md
│   │   ├── book-of-skretz/
│   │   ├── alchemical-nexus/
│   │   └── heartbreak-by-design/
│   ├── brand/
│   │   ├── BRAND_BIBLE_SUMMARY.md
│   │   ├── VOICE_TONE_GUIDE.md
│   │   └── VISUAL_IDENTITY.md
│   └── technical/
│       ├── TECH_STACK.md
│       ├── AGENT_ARCHITECTURE.md
│       └── API_DOCUMENTATION.md
├── src/                       # Source code for AI agents and tools
│   ├── agents/               # AI agent implementations
│   ├── automation/           # Make.com workflows and scripts
│   ├── utils/                # Shared utilities
│   └── __init__.py
├── tests/                     # Test suites
├── scripts/                   # Automation and utility scripts
├── assets/                    # Shared assets (to be created)
│   ├── brand/
│   ├── templates/
│   └── media/
└── README.md                  # Repository overview
```

---

## 🎯 Strategic Integration

### This Repo Connects To:

1. **Google Drive** → Canonical asset storage
   - One "Where's Crow" master folder
   - One "MXD-MDA Operations" folder
   - Archive of historical duplicates

2. **Notion Workspace** → Task management & knowledge base
   - Master Hub links to this repo's docs/
   - Project pages reference production checklists here
   - Git commit messages sync with Notion updates

3. **Local Development** → C:\Users\AMBER\mxd-mda\
   - This repo is cloned locally
   - MXD MDA Orchestrator.py should be moved to src/agents/
   - Regular sync with remote branches

4. **GitHub Projects** → Sprint tracking
   - Q4 2025 Milestones tracked in GitHub Projects
   - Issues tagged by role (Production, Creative Dev, Marketing, etc.)

---

## 🔄 Workflow: How to Use This Structure

### Daily Operations
1. Check `docs/operations/Q4_2025_SPRINT_CALENDAR.md` for today's priorities
2. Update relevant project checklists in `docs/projects/[project-name]/`
3. Commit changes with clear messages referencing role & project
4. Push to feature branch (following git safety protocol)

### Weekly Reviews
1. Run through `docs/operations/WEEKLY_REVIEW_TEMPLATE.md`
2. Update `docs/operations/RISK_REGISTER.md`
3. Sync with Notion Master Hub
4. Plan next week's sprints

### Project Launches
1. Create new folder in `docs/projects/[project-name]/`
2. Copy templates from `assets/templates/`
3. Link in `docs/PROJECT_MASTER_MAP.md`
4. Set milestones in GitHub Projects

---

## 🚨 Critical Rules

1. **NO MORE DUPLICATE FOLDERS** — Always check PROJECT_MASTER_MAP.md first
2. **ONE SOURCE OF TRUTH** — If it's not linked in the Master Map, it doesn't exist
3. **VERSION EVERYTHING** — All production files get version numbers (v1.0, v1.1, etc.)
4. **DOCUMENT AS YOU GO** — Don't wait until Friday; update checklists in real-time
5. **BRANCH NAMING** — Always use `claude/[project-name]-[session-id]` format

---

## 📊 Success Metrics

This structure is working when:
- ✅ You can find any asset in < 2 minutes
- ✅ All team roles know where to look for their tasks
- ✅ No duplicate work happening across platforms
- ✅ Weekly reviews take < 30 minutes
- ✅ New projects launch with clear documentation

---

## 🔮 Next Steps

1. ✅ Create this master structure document
2. ⏳ Build out all templates in `docs/operations/` and `docs/projects/`
3. ⏳ Consolidate Google Drive folders using CONSOLIDATION_ROADMAP.md
4. ⏳ Link Notion Master Hub to this repo's docs/
5. ⏳ Move MXD MDA Orchestrator.py to src/agents/
6. ⏳ Set up GitHub Projects board for Q4 2025 milestones

---

**"One structure. One truth. Infinite gold."** 🜁
