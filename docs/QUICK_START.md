# 🜂 MXD-MDA QUICK START GUIDE

Get the orchestration system running in **5 minutes**.

---

## ⚡ Prerequisites

- **Python 3.10+** installed
- **Git** installed
- **Text editor** (VS Code, Cursor, etc.)
- **Anthropic API key** ([get one here](https://console.anthropic.com/))

---

## 🚀 5-Minute Setup

### Step 1: Clone & Navigate (30 seconds)

```bash
git clone https://github.com/[your-org]/mxd-mda.git
cd mxd-mda
```

### Step 2: Create Virtual Environment (1 minute)

```bash
# Create venv
python3 -m venv .venv

# Activate it
source .venv/bin/activate  # On Mac/Linux
# OR
.venv\Scripts\activate     # On Windows
```

### Step 3: Install Core Dependencies (2 minutes)

```bash
# Minimal install for Week 1
pip install anthropic python-dotenv pydantic rich typer

# OR full install (takes longer)
pip install -r requirements.txt
```

### Step 4: Configure Environment (1 minute)

```bash
# Copy template
cp config/.env.example .env

# Edit .env and add your API key
# ANTHROPIC_API_KEY=sk-ant-api03-YOUR_KEY_HERE
```

**Using nano/vim:**
```bash
nano .env  # or vim .env
# Add: ANTHROPIC_API_KEY=sk-ant-YOUR_KEY
# Save & exit
```

**Using VS Code:**
```bash
code .env
# Add key, save file
```

### Step 5: Test the System (30 seconds)

```bash
python src/orchestrator/main.py test
python src/orchestrator/main.py dashboard
python src/orchestrator/main.py version
```

You should see:
```
✅ Orchestrator system initialized successfully!
```

---

## ✅ You're Ready!

**What you have now:**
- ✅ Repository structure in place
- ✅ Python environment configured
- ✅ Core dependencies installed
- ✅ API key configured
- ✅ Orchestrator tested & working

---

## 🎯 Next Steps

### Immediate (Next 30 minutes)
1. **Read the README**: `cat README.md` or open in browser
2. **Explore structure**: `tree -L 2` or `ls -R`
3. **Review configuration**: `cat config/.env.example`

### This Week (Week 1 Goals)
- [ ] Read [STRATEGIC_SYNTHESIS.md](STRATEGIC_SYNTHESIS.md)
- [ ] Plan your Notion database structure
- [ ] Set up Discord server (if ready)
- [ ] Test content generation (Week 2)

### Week 2 Goals
- [ ] Implement core orchestrator features
- [ ] Create Notion databases
- [ ] Test dashboard functionality
- [ ] Generate first AI content

---

## 🔧 Troubleshooting

### "Python not found"
```bash
# Try python3 instead
python3 --version

# Install Python 3.10+ from python.org
```

### "pip not found"
```bash
# Use python -m pip instead
python -m pip install --upgrade pip
```

### "Permission denied"
```bash
# Don't use sudo! Use venv instead
python3 -m venv .venv
source .venv/bin/activate
```

### "Module not found"
```bash
# Ensure venv is activated (you should see (.venv) in prompt)
source .venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### "API key error"
```bash
# Verify .env file exists
ls -la .env

# Check key format (should start with sk-ant-api03-)
cat .env | grep ANTHROPIC

# Ensure no spaces around the = sign
# CORRECT: ANTHROPIC_API_KEY=sk-ant-...
# WRONG:   ANTHROPIC_API_KEY = sk-ant-...
```

---

## 📚 Documentation Reference

- **[README.md](../README.md)** - System overview & architecture
- **[STRATEGIC_SYNTHESIS.md](STRATEGIC_SYNTHESIS.md)** - 90-day action plan
- **[CLAUDE_CODE_GUIDE.md](CLAUDE_CODE_GUIDE.md)** - Advanced automation
- **[CONTRIBUTING.md](../CONTRIBUTING.md)** - Contribution guidelines
- **[SECURITY.md](../SECURITY.md)** - Security policies

---

## 🎨 Pro Tips

### Activate venv automatically (optional)
Add to your `.bashrc` or `.zshrc`:
```bash
# Auto-activate venv when cd into project
cd() {
  builtin cd "$@"
  if [[ -f .venv/bin/activate ]]; then
    source .venv/bin/activate
  fi
}
```

### Use aliases for common commands
```bash
# Add to .bashrc/.zshrc
alias mxd-dashboard="python src/orchestrator/main.py dashboard"
alias mxd-test="python src/orchestrator/main.py test"
```

### Keep dependencies updated
```bash
# Check for updates
pip list --outdated

# Update specific package
pip install --upgrade anthropic

# Update all
pip install --upgrade -r requirements.txt
```

---

## 🜂 The Journey Begins

```
Prima Materia Phase Complete ✅

You've established the foundation.
The transformation has begun.

"Find Crow. Find Yourself."
```

**Next**: Read [STRATEGIC_SYNTHESIS.md](STRATEGIC_SYNTHESIS.md) to understand the full 90-day plan.

---

**Questions?** Open a GitHub issue or check the [Community](../README.md#community) section.
