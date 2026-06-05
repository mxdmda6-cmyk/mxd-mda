# 🜂 MXD-MDA QUICK START GUIDE

Get the orchestration system running locally without touching live publishing, bots, or automation.

---

## ⚡ Prerequisites

- **Python 3.10+** installed
- **Git** installed
- **Text editor** such as VS Code, Cursor, or similar
- Optional: **Anthropic API key** for future AI-generation features

---

## 🚀 5-Minute Setup

### Step 1: Clone & Navigate

```bash
git clone https://github.com/mxdmda6-cmyk/mxd-mda.git
cd mxd-mda
```

### Step 2: Create Virtual Environment

```bash
# Create venv
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # Mac/Linux
# OR
.venv\Scripts\activate     # Windows
```

### Step 3: Install Core Dependencies

```bash
# Minimal install for the current orchestrator and tests
pip install -r requirements-minimal.txt

# Optional full install for integration development
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
cp config/.env.example .env
```

Only fill in keys for integrations you are actively testing. Keep all live-posting, Discord, email automation, and vector-search feature flags disabled unless a separate implementation task explicitly turns them on.

### Step 5: Test the System

```bash
python src/orchestrator/main.py doctor
python src/orchestrator/main.py dashboard
python src/orchestrator/main.py version
pytest -q
```

You should see the doctor check complete safely and the pytest suite pass.

---

## ✅ You're Ready

What you have now:

- ✅ Repository structure in place
- ✅ Python environment configured
- ✅ Core dependencies installed
- ✅ Orchestrator smoke-tested locally
- ✅ Test suite ready
- ✅ No live deployment or publishing trigger activated

---

## 🎯 Next Steps

### Immediate

1. Read the README: `cat README.md` or open it in your editor.
2. Explore structure: `tree -L 2` or `find . -maxdepth 2 -type f`.
3. Review configuration: `cat config/.env.example`.
4. Run full local QA when dev tools are installed: `npm run qa`.

### Current Operating Priorities

- [ ] Keep the production dashboard and sprint docs current.
- [ ] Implement orchestrator features behind disabled-by-default flags.
- [ ] Add tests before enabling automation paths.
- [ ] Keep bot deployment manual until infrastructure is confirmed.

---

## 🔧 Troubleshooting

### "Python not found"

```bash
python3 --version
```

Install Python 3.10+ if needed.

### "pip not found"

```bash
python -m pip install --upgrade pip
```

### "Permission denied"

```bash
# Do not use sudo for project dependencies. Use venv instead.
python3 -m venv .venv
source .venv/bin/activate
```

### "Module not found"

```bash
source .venv/bin/activate
pip install -r requirements-minimal.txt
```

### "pytest not found"

```bash
pip install -r requirements-minimal.txt
```

### "API key error"

```bash
ls -la .env
```

Confirm the integration you are testing has a real key in `.env`. Do not paste real keys into docs, screenshots, GitHub issues, or chat.

---

## 📚 Documentation Reference

- **[README.md](../README.md)** - System overview and architecture
- **[STRATEGIC_SYNTHESIS.md](STRATEGIC_SYNTHESIS.md)** - 90-day action plan
- **[CLAUDE_CODE_GUIDE.md](CLAUDE_CODE_GUIDE.md)** - Advanced automation
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Contribution guidelines
- **[SECURITY.md](../SECURITY.md)** - Security policies

---

## 🎨 Pro Tips

### Use aliases for common commands

```bash
alias mxd-dashboard="python src/orchestrator/main.py dashboard"
alias mxd-doctor="python src/orchestrator/main.py doctor"
```

### Keep dependencies tight

```bash
pip list --outdated
pip install --upgrade -r requirements-minimal.txt
```

---

## 🜂 The Journey Begins

```text
Foundation smoke test complete ✅

The machine turns only when you choose to turn the key.

"Find Crow. Find Yourself."
```

**Next**: Read [STRATEGIC_SYNTHESIS.md](STRATEGIC_SYNTHESIS.md) to understand the full 90-day plan.
