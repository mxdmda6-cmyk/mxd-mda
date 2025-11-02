# 🗂️ MXD-MDA Infrastructure Consolidation Roadmap

**🚨 PRIORITY 1 STRATEGIC INITIATIVE**

**Created:** November 2, 2025
**Target Completion:** November 8, 2025 (End of Week 1)
**Owner:** Prime Alchemist + Director of Production

---

## 📍 Problem Statement

**Critical Issue Identified:**
- **3x "Where's Crow" folders** created November 1, 2025
- **2x "MXD-MDA" folders** created November 1, 2025
- Documents scattered across **multiple Google Drive locations**
- **50+ Notion pages** across multiple workspaces
- **No single source of truth** for asset locations
- **Version control chaos** — don't know which file is canonical

**Impact:**
- ⏱️ Time wasted searching for assets (estimated 2-4 hours/week)
- 🔄 Duplicate work across platforms
- 😰 Cognitive overhead and decision fatigue
- 🚧 Blocks Q4 2025 milestone progress
- ⚠️ Risk of working on wrong versions

---

## 🎯 Success Criteria

By November 8, 2025:
1. ✅ ONE canonical folder per project in Google Drive
2. ✅ ONE Master Hub in Notion linking to all resources
3. ✅ PROJECT_MASTER_MAP.md documenting every official location
4. ✅ All duplicate folders archived (not deleted) with clear labels
5. ✅ New workflow established: "Check Master Map FIRST before creating anything"

---

## 🗓️ 4-Hour Consolidation Sprint Plan

### Phase 1: AUDIT (60 minutes)

**Goal:** Create comprehensive inventory of all assets across all platforms

#### Google Drive Audit
- [ ] List all folders with "Where's Crow" in the name
  - Document: creation date, contents, last modified
  - Identify which has most complete/recent content
- [ ] List all folders with "MXD-MDA" in the name
  - Document: creation date, contents, last modified
  - Identify master folder
- [ ] List all other project folders (Book of Skretz, Alchemical Nexus, etc.)
- [ ] Screenshot folder structure for reference

**Deliverable:** Google Drive Audit Spreadsheet

#### Notion Audit
- [ ] List all workspaces you have access to
- [ ] Within each workspace, count pages and identify purpose:
  - Prime Dashboard
  - Aetheric Core
  - Production System
  - MXD-MDA Operations
  - Risk Crucible
  - Task Trackers (multiple!)
- [ ] Identify most recent/complete version of each type

**Deliverable:** Notion Page Inventory Document

#### Local Files Audit
- [ ] Check C:\Users\AMBER\mxd-mda\ for:
  - Orphaned files not in Git
  - MXD MDA Orchestrator.py location
  - Any local-only assets
- [ ] Compare local with GitHub repo

**Deliverable:** Local Files Status Report

---

### Phase 2: DESIGNATE CANONICAL LOCATIONS (45 minutes)

**Goal:** Make ONE definitive choice per project/asset type

#### Google Drive Canonical Structure
```
📁 MXD-MDA Master (CANONICAL) [Created: Nov 2025]
├── 📁 01_Active_Projects/
│   ├── 📁 Where's_Crow_MASTER/
│   │   ├── 📁 Manuscript/
│   │   │   └── [All manuscript versions here]
│   │   ├── 📁 Art_Assets/
│   │   │   ├── 📁 Character_Designs/
│   │   │   ├── 📁 Scene_Illustrations/
│   │   │   └── 📁 Style_References/
│   │   ├── 📁 Production_Specs/
│   │   │   └── [KDP specs, EPUB3 requirements, etc.]
│   │   └── 📁 Marketing_Assets/
│   │       └── [Kickstarter materials, social media graphics]
│   ├── 📁 Book_of_Skretz_MASTER/
│   ├── 📁 Alchemical_Nexus_MASTER/
│   └── 📁 Heartbreak_by_Design_MASTER/
├── 📁 02_Brand_Assets/
│   ├── 📁 Brand_Bible/
│   ├── 📁 Logos_Icons/
│   └── 📁 Templates/
├── 📁 03_Operations/
│   ├── 📁 Strategy_Docs/
│   ├── 📁 Financial_Tracking/
│   └── 📁 Meeting_Notes/
└── 📁 99_Archive/
    ├── 📁 Archive_2025-11-01_WheresCrow_Duplicate1/
    ├── 📁 Archive_2025-11-01_WheresCrow_Duplicate2/
    └── 📁 Archive_2025-11-01_MXDMDA_Duplicate/
```

#### Notion Canonical Structure
```
🏠 MXD-MDA MASTER HUB (Top-level page)
├── 🎯 MISSION CONTROL
│   ├── Prime Dashboard (Current sprint, today's focus)
│   ├── Weekly Review Ritual (Template + history)
│   └── Unified Task Tracker (ONE tracker to rule them all)
├── 📚 PROJECT WORKSPACES
│   ├── Where's Crow → [Links to production checklist in GitHub]
│   ├── Book of Skretz → [Links to poems folder]
│   ├── Alchemical Nexus → [Links to technical docs]
│   └── Heartbreak by Design → [Links to Catalyst Arc lore]
├── 🗂️ KNOWLEDGE BASE
│   ├── Aetheric Core (Lore database)
│   ├── Brand Bible (Voice, tone, visual identity)
│   └── Content Pipeline (Editorial calendar, post queue)
├── 📊 ANALYTICS & STRATEGY
│   ├── Risk Register
│   ├── Revenue Tracking
│   └── Milestone Progress
└── 🔗 EXTERNAL LINKS
    ├── GitHub Repo (mxd-mda)
    ├── Google Drive Master Folder
    ├── Discord Community
    └── Social Media Accounts
```

**Decisions to Make:**
- [ ] Which "Where's Crow" folder becomes MASTER?
- [ ] Which Notion page becomes MASTER HUB?
- [ ] Which task tracker becomes the ONE tracker?

---

### Phase 3: MIGRATION (90 minutes)

**Goal:** Move all assets to canonical locations

#### Google Drive Migration
1. [ ] Create "MXD-MDA Master" folder if it doesn't exist
2. [ ] Set up subfolder structure (01_Active_Projects, 02_Brand_Assets, etc.)
3. [ ] **MOVE** (not copy) all files from duplicates to master
   - Use Google Drive's MOVE function to preserve modification dates
   - Check for conflicts (same filename); rename with version numbers if needed
4. [ ] Rename duplicate folders with prefix "Archive_2025-11-01_"
5. [ ] Move archived folders to 99_Archive/
6. [ ] Add README.txt in each archived folder explaining why it was archived

**Migration Checklist per Project:**
- [ ] Where's Crow manuscript files → Where's_Crow_MASTER/Manuscript/
- [ ] Where's Crow art assets → Where's_Crow_MASTER/Art_Assets/
- [ ] Brand Bible documents → 02_Brand_Assets/Brand_Bible/
- [ ] Strategy documents → 03_Operations/Strategy_Docs/

#### Notion Migration
1. [ ] Create "MXD-MDA MASTER HUB" top-level page
2. [ ] Build out section structure (copy template from above)
3. [ ] **MOVE** pages from scattered workspaces into proper sections
   - Use Notion's move function
   - Update any internal links that break
4. [ ] Create ONE Unified Task Tracker using database
   - Swim lanes: By Role (Production, Creative Dev, Marketing, etc.)
   - Views: By Status, By Project, By Due Date, By Role
5. [ ] Archive old dashboards/trackers (move to "Archive" section, don't delete)
6. [ ] Update all bookmarks/shortcuts to point to Master Hub

---

### Phase 4: DOCUMENTATION (45 minutes)

**Goal:** Create the "Master Map" so this never happens again

#### Create PROJECT_MASTER_MAP.md
```markdown
# 🗺️ MXD-MDA Project Master Map

**Last Updated:** [Date]

## Where Everything Lives

### Google Drive
- **Master Folder:** [Direct link]
  - Where's Crow: [Direct link to Where's_Crow_MASTER/]
  - Book of Skretz: [Direct link]
  - Brand Assets: [Direct link]

### Notion
- **Master Hub:** [Direct link]
  - Prime Dashboard: [Direct link]
  - Task Tracker: [Direct link]
  - Aetheric Core: [Direct link]

### GitHub
- **Repo:** https://github.com/[username]/mxd-mda
  - Docs: /docs/
  - Code: /src/
  - Production Checklists: /docs/projects/

### Local Development
- **Path:** C:\Users\AMBER\mxd-mda\
  - Always sync with GitHub before working
  - Never create local-only files (commit immediately)

## Rules for Creating New Assets

1. **ALWAYS check this map FIRST**
2. **Ask:** "Does a folder for this already exist?"
3. **If yes:** Add to existing folder
4. **If no:** Update this map BEFORE creating new folder
5. **Share location immediately** in all relevant places
```

#### Update All References
- [ ] Pin Master Map in Notion Master Hub
- [ ] Add Master Map link to Google Drive Master folder description
- [ ] Add Master Map link to GitHub repo README.md
- [ ] Create browser bookmarks for all canonical locations

---

## 🛡️ Prevention Protocol

**New Workflow (Effective November 9, 2025):**

### Before Creating ANY New Folder/Page:
1. ⏸️ STOP
2. 🔍 Check PROJECT_MASTER_MAP.md
3. ❓ Ask: "Does this belong in an existing location?"
4. ✅ If yes → Use existing location
5. ✅ If no → Update Master Map FIRST, then create

### Weekly Audit Ritual (Every Friday):
- [ ] Review Google Drive: any new folders outside Master structure?
- [ ] Review Notion: any orphaned pages not linked from Master Hub?
- [ ] Review local files: anything not committed to Git?
- [ ] If found → Consolidate immediately; update Master Map

---

## 📊 Progress Tracking

### Consolidation Sprint Checklist

**Phase 1: Audit** (Target: 60 min)
- [ ] Google Drive audit complete
- [ ] Notion audit complete
- [ ] Local files audit complete
- [ ] Audit deliverables created

**Phase 2: Designate** (Target: 45 min)
- [ ] Canonical Google Drive structure decided
- [ ] Canonical Notion structure decided
- [ ] All designation decisions documented

**Phase 3: Migration** (Target: 90 min)
- [ ] Google Drive files migrated to master locations
- [ ] Duplicate Google Drive folders archived
- [ ] Notion pages migrated to Master Hub
- [ ] Old Notion dashboards archived
- [ ] All internal links updated

**Phase 4: Documentation** (Target: 45 min)
- [ ] PROJECT_MASTER_MAP.md created
- [ ] Master Map linked from all platforms
- [ ] Browser bookmarks updated
- [ ] Prevention protocol established

### Weekly Audit Log
| Date | Platform | Issues Found | Actions Taken |
|------|----------|--------------|---------------|
| Nov 8 | Initial consolidation | 3x Crow folders, 2x MXD folders | Consolidated to master structure |
| Nov 15 | | | |
| Nov 22 | | | |
| Nov 29 | | | |

---

## 🎯 Success Validation

**After consolidation is complete, test these scenarios:**

1. ✅ "I need to find the latest Where's Crow manuscript"
   - Can you find it in < 2 minutes using Master Map?

2. ✅ "I want to add a new character design for Crow"
   - Do you know exactly where to save it without hesitation?

3. ✅ "What are today's priorities across all roles?"
   - Can you check ONE location and see everything?

4. ✅ "I need to review last week's progress"
   - Is there ONE place with the complete picture?

5. ✅ "A new project idea emerges"
   - Do you check Master Map before creating any folders?

**If all 5 are ✅ → Consolidation successful!**

---

## 🔮 Future State Vision

**3 Months from Now (February 2026):**
- Every asset has ONE home
- Zero time wasted searching for files
- New team members can onboard by reading Master Map
- Project handoffs are seamless (everything is documented)
- Cognitive load reduced by 50%
- You spend time creating, not organizing

---

**"From chaos to clarity. From scattered to sovereign. This is alchemy."** 🜁

---

## 📝 Notes & Learnings

**What caused the duplication?**
- [To be filled in during audit]

**What systems broke down?**
- [To be filled in during audit]

**How do we prevent this long-term?**
- Weekly audit ritual
- Master Map as single source of truth
- "Check first, create second" protocol
- Real-time documentation (not batched)

**Post-Consolidation Debrief:**
- [To be filled in after completion on Nov 8]
