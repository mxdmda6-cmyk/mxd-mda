# 🗺️ MXD-MDA Project Master Map

**🚨 SINGLE SOURCE OF TRUTH — Check Here FIRST Before Creating Any Folders/Files**

**Last Updated:** November 2, 2025
**Version:** 1.0
**Owner:** Prime Alchemist (Strategic Lead)

---

## 📍 Purpose

This document is the **definitive reference** for where EVERY MXD-MDA asset, document, and resource lives.

**Rules:**
1. **ALWAYS check this map FIRST** before creating new folders
2. **If it's not listed here, it doesn't officially exist**
3. **Update this map IMMEDIATELY** when creating new canonical locations
4. **ONE location per asset type** — no duplicates

---

## 🏠 Core Infrastructure Locations

### GitHub Repository (Code & Documentation Hub)
**URL:** `https://github.com/[username]/mxd-mda` *(Update with actual URL)*
**Local Path:** `C:\Users\AMBER\mxd-mda\`

**What Lives Here:**
- Strategic planning documents (`docs/`)
- Production checklists and workflows (`docs/projects/`)
- Technical code for AI agents (`src/agents/`)
- Automation scripts (`scripts/`)
- This Master Map document

**Key Directories:**
- `docs/operations/` → Q4 sprint calendar, weekly reviews, risk register
- `docs/projects/wheres-crow/` → Where's Crow production checklist
- `docs/projects/book-of-skretz/` → Book of Skretz project files
- `docs/projects/alchemical-nexus/` → AI agent system documentation
- `docs/brand/` → Brand Bible, voice/tone guides
- `src/` → Source code for agents and tools
- `tests/` → Test suites

**Branch Strategy:**
- Main development: Create feature branches with pattern `claude/[project-name]-[session-id]`
- Always push to feature branch first, merge to main via PR

---

### Google Drive (Asset Storage & Collaboration)
**Master Folder:** `MXD-MDA Master` *(Add direct link after consolidation)*

**Canonical Structure:**
```
📁 MXD-MDA Master/
├── 📁 01_Active_Projects/
│   ├── 📁 Where's_Crow_MASTER/
│   │   ├── 📁 Manuscript/              [Manuscript versions, drafts]
│   │   ├── 📁 Art_Assets/              [Character designs, illustrations]
│   │   ├── 📁 Production_Specs/        [KDP specs, EPUB requirements]
│   │   └── 📁 Marketing_Assets/        [Kickstarter materials, social graphics]
│   ├── 📁 Book_of_Skretz_MASTER/
│   │   ├── 📁 Poems/                   [Individual poem files]
│   │   ├── 📁 Layout_Design/           [Book layout, typography]
│   │   └── 📁 Cover_Art/               [Cover design iterations]
│   ├── 📁 Alchemical_Nexus_MASTER/
│   │   ├── 📁 System_Design/           [Architecture diagrams, workflows]
│   │   ├── 📁 Agent_Prompts/           [Prompt templates, personas]
│   │   └── 📁 Integration_Specs/       [API docs, integration plans]
│   └── 📁 Heartbreak_by_Design_MASTER/
│       ├── 📁 Manuscript/              [Catalyst Arc chronicle]
│       └── 📁 Reference_Materials/     [Journey documentation]
├── 📁 02_Brand_Assets/
│   ├── 📁 Brand_Bible/                 [Core identity documents]
│   ├── 📁 Logos_Icons/                 [Logo variations, icons, symbols]
│   ├── 📁 Color_Palettes/              [Brand colors, hex codes]
│   ├── 📁 Typography/                  [Font files, usage guidelines]
│   └── 📁 Templates/                   [Social media, email, doc templates]
├── 📁 03_Operations/
│   ├── 📁 Strategy_Docs/               [5-year roadmap, business plans]
│   ├── 📁 Financial_Tracking/          [Budget, revenue, expenses]
│   ├── 📁 Meeting_Notes/               [Strategy sessions, reviews]
│   └── 📁 Legal_Admin/                 [Contracts, copyrights, ISBNs]
└── 📁 99_Archive/
    └── [Dated archived folders]        [Old duplicates, deprecated files]
```

**Quick Links (Add After Consolidation):**
- Where's Crow Master Folder: *[Direct link]*
- Book of Skretz Master Folder: *[Direct link]*
- Brand Assets: *[Direct link]*

---

### Notion (Task Management & Knowledge Base)
**Master Hub Page:** `MXD-MDA MASTER HUB` *(Add direct link)*

**Canonical Structure:**
```
🏠 MXD-MDA MASTER HUB
├── 🎯 MISSION CONTROL
│   ├── Prime Dashboard                 [Current sprint, today's focus]
│   ├── Weekly Review Ritual            [Template + review history]
│   └── Unified Task Tracker            [ONE database, all tasks]
│       ├── View: By Role
│       ├── View: By Project
│       ├── View: By Due Date
│       └── View: By Status
├── 📚 PROJECT WORKSPACES
│   ├── Where's Crow                    [Links to GitHub checklist + Drive assets]
│   ├── Book of Skretz                  [Poems tracker, publication plan]
│   ├── Alchemical Nexus                [Agent development roadmap]
│   ├── Creative Alchemy Workshops      [Course content, community planning]
│   └── Heartbreak by Design            [Catalyst Arc documentation]
├── 🗂️ KNOWLEDGE BASE
│   ├── Aetheric Core (Lore DB)         [Crow mythology, character profiles, world-building]
│   ├── Brand Bible                     [Mission, vision, voice, visual identity]
│   ├── Content Pipeline                [Editorial calendar, post queue, content ideas]
│   └── Research Archive                [Articles, references, inspiration]
├── 📊 ANALYTICS & STRATEGY
│   ├── Risk Register                   [Project risks, mitigation strategies]
│   ├── Revenue Tracking                [Income sources, projections, actuals]
│   ├── Milestone Progress              [OKR tracking, quarterly reviews]
│   └── Metrics Dashboard               [KPIs, weekly stats]
└── 🔗 EXTERNAL LINKS
    ├── GitHub Repo                     [Link to mxd-mda repo]
    ├── Google Drive Master             [Link to Drive master folder]
    ├── Discord Community               [Link when launched]
    ├── Beehiiv Email List              [Link to email platform]
    ├── Social Media Accounts           [Instagram, TikTok, Twitter/X]
    └── Website                         [mxd-mda.com or equivalent]
```

**Quick Links (Add After Consolidation):**
- Master Hub: *[Direct link]*
- Prime Dashboard: *[Direct link]*
- Unified Task Tracker: *[Direct link]*
- Aetheric Core (Lore DB): *[Direct link]*

---

### Local Development Environment
**Path:** `C:\Users\AMBER\mxd-mda\`

**What Lives Here:**
- Git clone of GitHub repo (always synced)
- MXD MDA Orchestrator.py *(To be moved to `src/agents/orchestrator.py`)*
- Local-only files (should be minimal — commit to Git ASAP)

**Workflow:**
1. Always `git pull` before starting work
2. Make changes locally
3. Commit frequently with clear messages
4. Push to feature branch regularly (don't let local diverge)

---

## 📚 Project-Specific Locations

### Where's Crow 🐦‍⬛

**Primary Assets:**
- **Manuscript:** Google Drive → `01_Active_Projects/Where's_Crow_MASTER/Manuscript/`
- **Art Assets:** Google Drive → `01_Active_Projects/Where's_Crow_MASTER/Art_Assets/`
- **Production Checklist:** GitHub → `docs/projects/wheres-crow/PRODUCTION_CHECKLIST.md`
- **MVP Code:** GitHub (to be created) → `src/projects/midnight-carnival-mvp/`
- **Kickstarter Materials:** Google Drive → `01_Active_Projects/Where's_Crow_MASTER/Marketing_Assets/Kickstarter/`
- **Notion Project Page:** Notion → `PROJECT WORKSPACES/Where's Crow`

**Key Documents:**
- Manuscript v1.0-FINAL: *[Link when available]*
- Art Asset Inventory Spreadsheet: *[Link when available]*
- KDP Submission Checklist: *[Link when available]*
- Kickstarter Campaign Draft: *[Link when available]*

---

### Book of Skretz 📖

**Primary Assets:**
- **Poems:** GitHub → `poems/` *(Already exists in repo)*
- **Poetry Collection (Master):** Google Drive → `01_Active_Projects/Book_of_Skretz_MASTER/Poems/`
- **Layout Design:** Google Drive → `01_Active_Projects/Book_of_Skretz_MASTER/Layout_Design/`
- **Publication Plan:** GitHub → `docs/projects/book-of-skretz/PUBLICATION_PLAN.md` *(To be created)*
- **Notion Project Page:** Notion → `PROJECT WORKSPACES/Book of Skretz`

**Key Documents:**
- Poetry Tracker (Notion): *[Link when available]*
- Publication Timeline: *[Link when available]*

---

### Alchemical Nexus 🜁 (Multi-Agent AI System)

**Primary Assets:**
- **System Architecture:** GitHub → `docs/projects/alchemical-nexus/ARCHITECTURE.md` *(To be created)*
- **Agent Prompts:** Google Drive → `01_Active_Projects/Alchemical_Nexus_MASTER/Agent_Prompts/`
- **Source Code:** GitHub → `src/agents/alchemical-nexus/`
- **Technical Docs:** Google Drive → `01_Active_Projects/Alchemical_Nexus_MASTER/System_Design/`
- **Notion Project Page:** Notion → `PROJECT WORKSPACES/Alchemical Nexus`

**Key Documents:**
- Technical Architecture: *[Link when available]*
- Agent Development Roadmap: *[Link when available]*

---

### Heartbreak by Design 💔 (Catalyst Arc Chronicle)

**Primary Assets:**
- **Manuscript:** Google Drive → `01_Active_Projects/Heartbreak_by_Design_MASTER/Manuscript/`
- **Reference Materials:** Google Drive → `01_Active_Projects/Heartbreak_by_Design_MASTER/Reference_Materials/`
- **Transformation Arc Timeline:** Notion → `KNOWLEDGE BASE/Aetheric Core/Catalyst Arc`
- **Notion Project Page:** Notion → `PROJECT WORKSPACES/Heartbreak by Design`

**Key Documents:**
- Catalyst Arc Chronicle: *[Link when available]*
- Transformation Timeline: *[Link when available]*

---

### Creative Case Manager (CCM Agent) 🤖

**Primary Assets:**
- **System Design:** GitHub → `src/agents/ccm-agent/`
- **Technical Documentation:** GitHub → `docs/technical/CCM_AGENT_SPEC.md` *(To be created)*
- **Notion Project Page:** Notion → *(To be created)*

**Status:** Phase 2 (2027-2028) — Paused until Where's Crow MVP complete

---

## 🎨 Brand & Marketing Assets

### Brand Identity
**Location:** Google Drive → `02_Brand_Assets/`

**Key Files:**
- Brand Bible (Master Document): *[Link]*
- Logo Package (all variations): *[Link]*
- Color Palette Hex Codes: *[Link]*
- Typography Guide: *[Link]*
- Voice & Tone Guidelines: GitHub → `docs/brand/VOICE_TONE_GUIDE.md` *(To be created)*

---

### Social Media
**Platforms:**
- **Instagram:** *[Username/Link]*
- **TikTok:** *[Username/Link]*
- **Twitter/X:** *[Username/Link]*
- **Discord:** *[Invite link when launched]*

**Content Storage:**
- **Content Calendar:** Notion → `KNOWLEDGE BASE/Content Pipeline/Editorial Calendar`
- **Post Graphics:** Google Drive → `02_Brand_Assets/Templates/Social_Media/`
- **Content Backlog:** Notion → `KNOWLEDGE BASE/Content Pipeline/Content Ideas`

---

### Email Marketing
**Platform:** Beehiiv *(or Mailchimp/ConvertKit)*
**Link:** *[Add when set up]*

**Email Sequences Stored:**
- GitHub → `docs/marketing/EMAIL_SEQUENCES.md` *(To be created)*

---

## 🛠️ Technical Infrastructure

### Make.com Workflows
**Account:** *[Add login/link]*
**Workflows Stored:** Make.com platform (documented in GitHub)
**Documentation:** GitHub → `docs/technical/AUTOMATION_WORKFLOWS.md` *(To be created)*

---

### APIs & Integrations
**Documentation:** GitHub → `docs/technical/API_DOCUMENTATION.md` *(To be created)*

**Active Integrations:**
- Notion API: *[Status]*
- Google Drive API: *[Status]*
- Discord Bot: *[Status — planned]*
- Beehiiv API: *[Status — planned]*

---

## 🔄 Workflow: Before Creating Anything New

### The "Master Map Check" Protocol

**Step 1: PAUSE** ⏸️
Before creating a new folder, document, or file...

**Step 2: CHECK THIS MAP** 🔍
Ask yourself:
- Does a folder for this project/asset type already exist?
- Where is the canonical location for this type of file?
- Have I looked at the Master Map in the last week?

**Step 3: DECIDE** ✅
- **If location exists:** Use existing location
- **If location doesn't exist:** Proceed to Step 4

**Step 4: UPDATE MAP FIRST** 📝
- Open this document
- Add new location to appropriate section
- Commit change to Git
- THEN create the folder/file

**Step 5: SHARE** 📢
- Update Notion Master Hub with link
- Add to relevant project pages
- Tell all "roles" where new asset lives

---

## 📅 Weekly Audit Ritual

**Every Friday (part of Weekly Review):**

1. **Google Drive Audit:**
   - [ ] Are there any new folders outside the Master structure?
   - [ ] Have any assets been saved in wrong locations?
   - [ ] Are there duplicate files?

2. **Notion Audit:**
   - [ ] Are there orphaned pages not linked from Master Hub?
   - [ ] Have any new pages been created without proper categorization?
   - [ ] Are all links in Master Hub still working?

3. **Git Repo Audit:**
   - [ ] Are there uncommitted local files?
   - [ ] Have any files been created outside the documented structure?
   - [ ] Are there merge conflicts or outdated branches?

4. **Update Master Map:**
   - [ ] Add any new canonical locations
   - [ ] Update "Last Updated" date
   - [ ] Commit changes to Git

---

## 🚨 Duplicate Prevention Rules

**If you find yourself about to create a folder/file and you're NOT SURE if it already exists:**

1. **STOP** — Do not create yet
2. **Search** — Use Google Drive search, Notion search, file explorer search
3. **Ask** — Review this Master Map (you're reading it now!)
4. **Document** — If truly new, add to Master Map first
5. **Create** — Only after confirming no duplicate exists

**If you accidentally create a duplicate:**
1. Immediately identify which version is more complete/recent
2. Move content from duplicate to canonical location
3. Archive duplicate (don't delete) with clear naming: `Archive_YYYY-MM-DD_[FolderName]`
4. Update Master Map if needed

---

## 🎯 Success Metrics

**This Master Map is working when:**
- ✅ You can find any asset in < 2 minutes
- ✅ You never create duplicate folders
- ✅ New projects have clear homes from day 1
- ✅ All team "roles" know where to look for their resources
- ✅ You spend time creating, not searching

---

## 📞 Who Owns What

| Asset Type | Primary Owner (Role) | Backup Owner |
|------------|---------------------|--------------|
| **Manuscript Files** | Creative Development | Director of Production |
| **Art Assets** | Creative Development | Director of Production |
| **Production Checklists** | Director of Production | Project Manager |
| **Marketing Materials** | Marketing & Crowdfunding | Social Media Manager |
| **Technical Code** | Bot & Agent Architect | (Solo for now) |
| **Strategic Docs** | Prime Alchemist | Project Manager |
| **Social Media Content** | Social Media Manager | Marketing & Crowdfunding |
| **Notion Organization** | Project Manager | Prime Alchemist |
| **Brand Assets** | Creative Development | Social Media Manager |

---

## 🔮 Future Locations (Planned but Not Yet Created)

**Q1 2026:**
- Kickstarter Campaign Page (Kickstarter.com)
- Discord Community Server (Discord.com)
- Website (mxd-mda.com or equivalent)

**Q2 2026+:**
- Course Platform (Teachable? Thinkific?)
- Podcast Hosting (Spotify, Apple Podcasts)
- YouTube Channel

**Update this section as new platforms are added!**

---

## 📝 Change Log

**Version 1.0 (November 2, 2025):**
- Initial Master Map created
- Defined canonical locations for all active projects
- Established weekly audit ritual
- Documented duplicate prevention protocol

**Future updates will be logged here.**

---

## 🆘 When You're Lost

**Can't find something? Follow this troubleshooting process:**

1. **Check this Master Map** — Is there a link in the project-specific section?
2. **Search Google Drive** — Use search function with project name
3. **Search Notion** — Check Master Hub and use global search
4. **Check GitHub** — Look in `docs/projects/[project-name]/`
5. **Ask Your Past Self** — Check meeting notes, weekly reviews for clues
6. **Still lost?** → Time to consolidate! Asset might be in duplicate folder that needs archiving

---

**"One map. One truth. Infinite clarity."** 🗺️

---

**Last Updated:** November 2, 2025
**Next Review:** November 8, 2025 (During weekly audit ritual)
**Version:** 1.0

---

## 🔗 Quick Reference Links

**Essential Daily Links (Bookmark These!):**
- [ ] This Master Map (GitHub): *[Link to this file]*
- [ ] Notion Master Hub: *[Link]*
- [ ] Prime Dashboard (Today's Focus): *[Link]*
- [ ] Google Drive Master Folder: *[Link]*
- [ ] Unified Task Tracker: *[Link]*

**Update these links after consolidation is complete!**
