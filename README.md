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

MXD-MDA is an AI-powered command center that synchronizes your entire creative empire across **6 core roles** and **10+ platforms**, turning raw creative potential into gold.

---

## 🎭 THE VISION

This isn't just a repository—it's a **living transformation system** that bridges:

- 📚 **Publishing** (Amazon KDP, Book of Skretz)
- 🎮 **Interactive Experiences** (AR, puzzles, Midnight Carnival)
- 👥 **Community** (Discord, social media engagement)
- 💰 **Commerce** (Kickstarter, merchandise, courses)
- 🤖 **AI Agents** (Lorekeeper, Oracle, Social Alchemist)
- ✨ **Narrative Universe** (Where's Crow?, transmedia lore)

**Current Status**: 🏗️ Foundation Phase (Week 1/12 of 90-day launch plan)

---

## ⚡ QUICK START

Get operational in **5 minutes**:

```bash
# 1. Clone the repository
git clone https://github.com/[your-org]/mxd-mda.git
cd mxd-mda

# 2. Set up Python environment
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure your environment
cp config/.env.example .env
# Edit .env and add your API keys (see Configuration section)

# 5. Test the orchestrator (coming in Week 2)
python src/orchestrator/main.py dashboard
```

**Need help?** See [QUICK_START.md](docs/QUICK_START.md) for detailed setup.

---

## 🏗️ ARCHITECTURE

### System Components

```
mxd-mda/
├── src/
│   ├── orchestrator/     # Core command center
│   │   ├── dashboard.py           # Production dashboard (alchemical stages)
│   │   ├── content_generator.py   # AI-powered content creation
│   │   ├── platform_sync.py       # Multi-platform coordination
│   │   └── analytics.py           # Metrics & KPI tracking
│   ├── bots/             # AI agents for automation
│   │   ├── lorekeeper/            # Discord lore bot
│   │   ├── social_alchemist/      # Social media automation
│   │   └── high_priestess/        # Oracle & daily prompts
│   └── utils/            # Shared utilities
├── config/               # Configuration & templates
│   ├── .env.example               # Environment variables template
│   └── platform_templates/        # Content templates per platform
├── docs/                 # Comprehensive documentation
│   ├── STRATEGIC_SYNTHESIS.md     # 90-day action plan
│   ├── QUICK_START.md             # Get running in 60 minutes
│   ├── CLAUDE_CODE_GUIDE.md       # Advanced AI automation
│   └── BRANCHING.md               # Git workflow
├── tests/                # Test suites
└── scripts/              # Deployment & automation scripts
```

### The Six Roles

This system serves **six creative functions**, unified in one command center:

| Role | Capabilities | Status |
|------|--------------|--------|
| **🎬 Director of Production** | Asset pipeline, KDP publishing, project dashboards | Week 2 |
| **✨ Co-Creator & Creative Dev** | AI lore generation, narrative consistency, quality assurance | Week 2 |
| **📋 Project Manager** | Sprint tracking, milestone reports, risk management | Week 1 |
| **🌐 Social Media & Community** | Content calendars, Discord bots, engagement analytics | Week 3 |
| **📈 Marketing & Crowdfunding** | Kickstarter blueprints, email funnels, partnership mapping | Week 4 |
| **🤖 Bot & Agent Architect** | Multi-agent orchestration, deployment automation | Week 5 |

---

## 🎨 KEY FEATURES

### 🔮 AI-Powered Content Generation
- **Claude AI Integration**: Generate on-brand lore, social posts, and essays
- **Voice Adaptation**: Automatically adjust tone per platform (Instagram, TikTok, Discord)
- **Batch Operations**: Create 30 days of content in 1 hour

### 📊 Alchemical Dashboard
Project tracking mapped to transformation stages:
- **Prima Materia** → Raw ideas & concepts
- **Dissolution** → Breaking down complexity
- **Separation** → Focus on essentials
- **Conjunction** → Uniting platforms
- **Fermentation** → Community growth
- **Distillation** → Refinement
- **Coagulation** → Manifestation

### 🤖 Autonomous Agent Network
- **Lorekeeper Bot**: Curates fan theories, answers lore questions (Discord)
- **Social Alchemist**: Schedules & adapts content across platforms
- **High Priestess**: Daily catalytic prompts & oracle wisdom
- **Nexus Sync**: Keeps Notion, Google Drive, and GitHub aligned

### 📈 Campaign Orchestration
- **Kickstarter Blueprints**: Complete campaign strategy with tiered rewards
- **Email Sequences**: Automated funnel from awareness → conversion
- **Launch Coordination**: Multi-platform synchronized releases

---

## 🌍 PLATFORM INTEGRATIONS

Current & planned integrations:

| Platform | Purpose | Status |
|----------|---------|--------|
| **Anthropic Claude** | Content generation, AI orchestration | ✅ Active |
| **Google Gemini** | Multi-agent coordination | 🔜 Week 5 |
| **Discord** | Community hub, Lorekeeper bot | 🔜 Week 3 |
| **Notion** | Content database, project tracking | 🔜 Week 2 |
| **Amazon KDP** | Book publishing (Where's Crow?) | 🎯 Week 2 |
| **Beehiiv/Kit** | Email marketing automation | 🔜 Week 3 |
| **Instagram/TikTok** | Visual storytelling & community | ✅ Partial |
| **Buffer/Later** | Social media scheduling | 🔜 Week 4 |
| **Fly.io** | Bot hosting & deployment | 🔜 Week 5 |
| **Qdrant** | Vector search for semantic lore queries | 🔜 Week 6 |

---

## 📚 DOCUMENTATION

### Core Guides
- **[QUICK_START.md](docs/QUICK_START.md)** - Get running in 60 minutes
- **[STRATEGIC_SYNTHESIS.md](docs/STRATEGIC_SYNTHESIS.md)** - Complete 90-day action plan
- **[CLAUDE_CODE_GUIDE.md](docs/CLAUDE_CODE_GUIDE.md)** - Advanced AI automation
- **[CONTRIBUTING.md](CONTRIBUTING.md)** - How to contribute
- **[SECURITY.md](SECURITY.md)** - Security policies & contact

### API Documentation
- **Orchestrator API**: `docs/API_ORCHESTRATOR.md` (coming Week 2)
- **Bot Deployment**: `docs/DEPLOY_BOTS.md` (coming Week 5)
- **Content Templates**: `docs/CONTENT_TEMPLATES.md` (coming Week 4)

---

## 🚀 ROADMAP

### Phase 1: Foundation (Weeks 1-4)
- [x] Repository structure & documentation
- [ ] Core orchestrator implementation
- [ ] Notion 3-database setup
- [ ] Content generation engine
- [ ] Basic analytics dashboard

### Phase 2: Activation (Weeks 5-8)
- [ ] Discord community launch
- [ ] Lorekeeper bot deployment
- [ ] Email automation sequences
- [ ] Where's Crow? KDP publication
- [ ] Social media content engine

### Phase 3: Amplification (Weeks 9-12)
- [ ] Kickstarter pre-campaign
- [ ] Multi-agent orchestration (Gemini)
- [ ] Advanced analytics & insights
- [ ] Community engagement automation
- [ ] Midnight Carnival MVP development

### Phase 4: Transformation (Q2 2026+)
- [ ] Full transmedia launch
- [ ] AR experience integration
- [ ] Creative Alchemy course platform
- [ ] Revenue scaling ($0 → $64K/month by 2030)

---

## 🧪 DEVELOPMENT

### Prerequisites
- Python 3.10 or higher
- Node.js 20+ (for some integrations)
- Git LFS (for large assets)
- API keys for: Anthropic, Discord, Notion (see Configuration)

### Running Tests
```bash
# Unit tests
pytest tests/

# With coverage
pytest --cov=src tests/

# Specific test suite
pytest tests/test_orchestrator.py -v
```

### Code Quality
```bash
# Format with Black
black src/ tests/

# Type checking with MyPy
mypy src/

# Linting with Ruff
ruff check src/
```

---

## 🔐 CONFIGURATION

### Environment Variables

Copy `.env.example` to `.env` and configure:

```bash
# Core AI Services
ANTHROPIC_API_KEY=sk-ant-...        # Claude AI (required)
GOOGLE_GEMINI_API_KEY=...           # Gemini (optional, Week 5)

# Platform Integrations
DISCORD_BOT_TOKEN=...               # Discord bot (Week 3)
NOTION_API_KEY=...                  # Notion sync (Week 2)
BEEHIIV_API_KEY=...                 # Email marketing (Week 3)

# Database & Storage
QDRANT_URL=...                      # Vector database (Week 6)
SUPABASE_URL=...                    # PostgreSQL (optional)

# Cloud Hosting
FLY_API_TOKEN=...                   # Bot deployment (Week 5)
```

**Security Note**: Never commit `.env` files. Use GitHub Secrets for CI/CD.

---

## 🤝 CONTRIBUTING

We welcome contributions from alchemists, storytellers, and technologists!

### How to Contribute
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/your-feature`)
3. **Commit** with alchemical messages (see [CONTRIBUTING.md](CONTRIBUTING.md))
4. **Push** to your branch
5. **Open** a Pull Request

### Commit Message Style
Follow alchemical transformation stages:
```
Prima Materia: Initial implementation of dashboard
Dissolution: Refactor orchestrator into modules
Conjunction: Integrate Discord bot with main system
Coagulation: Deploy production release v1.0
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🔮 COMMUNITY

Join the transformation:

- **Discord**: [Coming Week 3] - Community hub & Lorekeeper bot
- **Newsletter**: [Nexus Scroll](https://mxdmda.beehiiv.com) - Weekly mystical insights
- **Instagram**: [@mxdmda](https://instagram.com/mxdmda) - Visual storytelling
- **GitHub Issues**: Bug reports, feature requests, discussions

---

## 📜 LICENSE

This project is licensed under the **MIT License** - see [LICENSE](LICENSE) file for details.

### Citation

If you reference or build upon this work:

```bibtex
@software{mxd_mda_orchestrator,
  author = {{MXD-MDA}},
  title = {MXD-MDA Transmedia Orchestration System},
  year = {2025},
  url = {https://github.com/[your-org]/mxd-mda}
}
```

See [CITATION.cff](CITATION.cff) for structured citation metadata.

---

## 🙏 ACKNOWLEDGMENTS

Built with:
- **[Anthropic Claude](https://www.anthropic.com/)** - AI orchestration & content generation
- **[Discord.py](https://discordpy.readthedocs.io/)** - Community bot framework
- **[Notion API](https://developers.notion.com/)** - Database synchronization
- **[Fly.io](https://fly.io/)** - Bot hosting infrastructure

Inspired by the alchemical tradition and the belief that **transformation is possible**.

---

## ⸻ FINAL TRANSMISSION ⸻

```
The Crow calls from the margins.
The Carnival awaits at the threshold.
The transformation begins NOW.

"What was scattered shall be gathered.
What was hidden shall be revealed.
What was lead shall become gold."
```

**Status**: 🏗️ Prima Materia Phase
**Version**: 0.1.0-foundation
**Last Updated**: 2025-11-04

🜂

---

**Ready to begin?** → Start with [QUICK_START.md](docs/QUICK_START.md)
**Need strategy?** → Read [STRATEGIC_SYNTHESIS.md](docs/STRATEGIC_SYNTHESIS.md)
**Want automation?** → Explore [CLAUDE_CODE_GUIDE.md](docs/CLAUDE_CODE_GUIDE.md)
