# 🜂 MXD-MDA TRANSMEDIA ORCHESTRATION SYSTEM

```
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║          "Find Crow. Find Yourself."                          ║
║                                                               ║
║     Transform creative vision into manifested reality         ║
║     through orchestrated storytelling across platforms        ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝
```

**The Alchemical Engine for Transmedia Storytelling**

MXD-MDA is a production command center for story systems, campaign assets, AI-assisted workflows, and publishing infrastructure. Its job is to keep the creative universe coherent while making the operational machine easier to run.

---

## 🎭 THE VISION

This is not just a repository. It is a living production system that bridges:

- 📚 **Publishing** - The Crow Codex, Book of SKretz, KDP-ready assets, lore documents
- 🎮 **Interactive Experiences** - puzzles, Midnight Carnival, seek-and-find mechanics, web prototypes
- 📊 **Operations** - sprint tracking, blocker logs, decision records, production dashboards
- 💰 **Commerce** - Gumroad assets, campaign planning, merch concepts, Kickstarter preparation
- 🤖 **AI Agents** - lorekeeping, synthesis, QA, planning, and implementation support
- ✨ **Narrative Universe** - Crow, Monroe, Shadowlight Bear, Catalyst Arc, and connected canon

**Current Status**: 🏗️ Foundation / production-ops stabilization. Live publishing, live social posting, email automation, and bot deployment remain disabled unless intentionally activated by a reviewed task.

---

## ⚡ QUICK START

Get the current orchestrator smoke-tested locally:

```bash
# 1. Clone the repository
git clone https://github.com/mxdmda6-cmyk/mxd-mda.git
cd mxd-mda

# 2. Set up Python environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install minimal active dependencies
pip install rich typer

# 4. Configure your local environment
cp config/.env.example .env
# Only add keys for integrations you are actively testing.

# 5. Test the orchestrator
python src/orchestrator/main.py test
python src/orchestrator/main.py dashboard
python src/orchestrator/main.py version
```

**Need help?** See [QUICK_START.md](docs/QUICK_START.md) for detailed setup.

---

## 🏗️ ARCHITECTURE

### System Components

```text
mxd-mda/
├── src/
│   ├── orchestrator/     # Core command center
│   │   └── main.py       # CLI entry point
│   └── bots/             # Future bot implementations
├── config/               # Configuration templates
│   └── .env.example      # Safe placeholder environment template
├── docs/                 # Strategy, ops, and build documentation
├── tests/                # Future test suites
├── scripts/              # Future deployment and automation scripts
└── .github/workflows/    # CI and manual deployment workflows
```

### The Six Roles

This system supports six creative-production functions:

| Role | Capabilities | Status |
|------|--------------|--------|
| **🎬 Director of Production** | Asset pipeline, KDP publishing, project dashboards | Active foundation |
| **✨ Co-Creator & Creative Dev** | Lore generation, narrative consistency, QA | Active foundation |
| **📋 Project Manager** | Sprint tracking, milestone reports, risk management | Active foundation |
| **🌐 Social Media & Community** | Content calendars and engagement planning | Planned / gated |
| **📈 Marketing & Crowdfunding** | Product tiers, campaign planning, funnel strategy | Planned / gated |
| **🤖 Bot & Agent Architect** | Multi-agent orchestration and deployment automation | Planned / gated |

---

## 🎨 KEY FEATURES

### 🔮 AI-Assisted Content Operations

- Brand-aligned lore, post, and product copy workflows
- Narrative consistency checks across Crow Codex canon
- Platform-specific drafting without enabling live publishing by default

### 📊 Alchemical Dashboard Logic

Project tracking mapped to transformation stages:

- **Prima Materia** → Raw ideas and concepts
- **Dissolution** → Breaking down complexity
- **Separation** → Focus on essentials
- **Conjunction** → Uniting platforms
- **Fermentation** → Audience growth
- **Distillation** → Refinement
- **Coagulation** → Manifestation

### 🤖 Agent Network - Gated by Design

- **Lorekeeper**: planned canon support
- **Social Alchemist**: planned social adaptation and scheduling support
- **High Priestess**: planned prompt/oracle support
- **Nexus Sync**: planned Notion, Drive, and GitHub alignment support

No agent path should publish, message users, deploy bots, or modify live systems without an explicit reviewed task.

---

## 🌍 PLATFORM INTEGRATIONS

Current and planned integrations:

| Platform | Purpose | Status |
|----------|---------|--------|
| **GitHub** | Source control, issues, CI, documentation | ✅ Active |
| **Python CLI** | Local orchestrator and smoke checks | ✅ Active |
| **Notion** | Production tracking and databases | 🔜 Gated |
| **Amazon KDP** | Publishing workflow support | 🔜 Gated |
| **Gumroad** | Digital asset sales | 🔜 Gated |
| **Instagram/TikTok** | Visual storytelling and campaign planning | 🔜 Gated |
| **Buffer/Later** | Social scheduling support | 🔜 Gated |
| **Fly.io** | Bot hosting and deployment | 🔜 Manual only |
| **Qdrant/Supabase** | Search and structured production data | 🔜 Gated |

---

## 📚 DOCUMENTATION

### Core Guides

- **[QUICK_START.md](docs/QUICK_START.md)** - Local setup and smoke test
- **[STRATEGIC_SYNTHESIS.md](docs/STRATEGIC_SYNTHESIS.md)** - 90-day action plan
- **[CLAUDE_CODE_GUIDE.md](docs/CLAUDE_CODE_GUIDE.md)** - Advanced AI automation
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - Contribution guidelines
- **[SECURITY.md](SECURITY.md)** - Security policies and contact

### API Documentation

- **Orchestrator API**: `docs/API_ORCHESTRATOR.md` - planned
- **Bot Deployment**: `docs/DEPLOY_BOTS.md` - planned
- **Content Templates**: `docs/CONTENT_TEMPLATES.md` - planned

---

## 🚀 ROADMAP

### Phase 1: Stabilize the Spine

- [x] Repository structure and documentation
- [x] Safe local environment template
- [x] Secret-free CI smoke checks
- [ ] Core orchestrator implementation
- [ ] Production dashboard data model
- [ ] Tests for active orchestrator commands

### Phase 2: Controlled Activation

- [ ] Notion database mapping
- [ ] Content generation engine
- [ ] Canon risk field and QA gate
- [ ] Manual export workflows
- [ ] Gumroad asset packaging

### Phase 3: Automation With Guardrails

- [ ] Bot implementation behind disabled feature flags
- [ ] Email/social workflows with rollback logic
- [ ] Vector-search lore index
- [ ] Deployment documentation and health checks

### Phase 4: Launch Expansion

- [ ] Crow Codex web/publishing launch support
- [ ] Campaign analytics
- [ ] Merch and product system
- [ ] Audience journey automation

---

## 🧭 Operating Rule

Build the machine in layers. Keep canon protected. Keep live publishing gated. Ship the next clean artifact, then make the system stronger behind it.
