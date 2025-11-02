# ⚂ MXD-MDA COMMAND CENTER DEPLOYMENT
## Complete System Activation Protocol
**Date:** November 1, 2025
**Director of Production:** Claude
**Status:** READY FOR EXECUTION

---

## 🎯 MISSION BRIEFING

You are about to deploy a complete organizational infrastructure across **8 systems**:

1. ✅ **Google Drive** - Project GEM (56 folders)
2. 📧 **Gmail** - Legal/court communications audit
3. 📧 **Kretz97@gmail.com** - Secondary account audit
4. 📅 **Google Calendar** - Deadline tracking system
5. 📝 **Notion** - Project management workspace
6. ☁️ **OneDrive** - File recovery and migration
7. 💾 **D: Drive** - Local storage audit
8. 🐙 **GitHub** - Repository organization

**Estimated Time:** 2-3 hours for complete deployment
**Priority Level:** CRITICAL - Legal deadlines imminent

---

## 🚨 PHASE 1: IMMEDIATE LEGAL INTELLIGENCE (DO THIS FIRST)

### Gmail Search Commands (mxdmda6@gmail.com)

Open Gmail and search for each of these:

```
1. "Oct 22 2025" OR "October 22"
2. "LVNV" OR "27-CO-25-4917"
3. "Conciliation Court" OR "Hennepin County"
4. "court hearing" after:2025/10/15
5. "Zoom hearing" OR "virtual hearing"
```

**What to look for:**
- ❓ Did the Oct 22 hearing happen?
- ❓ Was it rescheduled?
- ❓ Do you have a Zoom link saved?
- ❓ Any follow-up actions required?

**Action:** Document findings in `Legal_Communications_Audit.txt`

### Kretz97@gmail.com Search

Same searches in this account - check if legal notices went there instead.

### 📞 BACKUP PLAN (If no email found):

Call Hennepin County Conciliation Court:
- **Phone:** (612) 348-2040
- **Ask for:** Case status for 27-CO-25-4917
- **Question:** "Was there a hearing scheduled for October 22, 2025?"

---

## 🏗️ PHASE 2: PROJECT GEM DEPLOYMENT

### Option A: Windows PowerShell Deployment (RECOMMENDED)

**Location:** You already have this at:
```
C:\Users\AMBER\mxd-mda\PROJECT_GEM_STRUCTURE\
```

**Steps:**

1. **Open PowerShell as Administrator**
   - Press `Win + X`
   - Select "Windows PowerShell (Admin)"

2. **Navigate to the structure:**
   ```powershell
   cd "C:\Users\AMBER\mxd-mda\PROJECT_GEM_STRUCTURE"
   ```

3. **Run the setup script:**
   ```powershell
   .\setup_project_gem.ps1
   ```

4. **When prompted:**
   - Confirm your Google Drive path (should auto-detect)
   - Choose "Merge with existing" (option 1)
   - Wait for sync to complete

**Expected Result:**
- 56 folders created in `My Drive (mxdmda6@gmail.com)\Documents\`
- All folders syncing to cloud
- Structure ready for file migration

### Option B: Manual Deployment (If script fails)

1. Open File Explorer
2. Navigate to: `C:\Users\AMBER\My Drive (mxdmda6@gmail.com)\`
3. Copy the entire `Documents` folder from:
   ```
   C:\Users\AMBER\mxd-mda\PROJECT_GEM_STRUCTURE\Documents\
   ```
4. Paste into your Google Drive
5. Wait for sync (check Drive icon in system tray)

---

## 📁 PHASE 3: GOOGLE DRIVE CONSOLIDATION

### Current Duplicate Folders (Created tonight ~8pm):

**MXD-MDA (2 instances):**
- Folder 1: `12tySadFYRJYt9IBYyKbDIpAwZRFWzInA`
- Folder 2: `18kb1i8V_l0CLJFFw1mneiyy9qygl7hBg`

**Where's Crow (3 instances):**
- Folder 1: `1AUtQsap3_ZJRP4vxT0U9TIXg9mEuS3H4`
- Folder 2: `1yYtkrzAsdDhQ5QQq8Kd1b46KWPSSX7ig`
- Folder 3: `1euqrMZbQhoR1VsAPeYnvgRLO9U4GiBDq`

### Consolidation Plan:

#### Step 1: Audit Each Folder

For EACH folder, document:
- What files are inside?
- Any duplicates?
- Most recent/complete version?

#### Step 2: Merge Strategy

**MXD-MDA:**
```
New Location: Documents/07_Creative_Projects/MXD-MDA_Brand/

Move all unique files from both folders to:
- Brand_Guide/ (logos, colors, fonts)
- Marketing/ (social content)
- Content/ (blog posts)
- Assets/ (images, templates)

Delete empty duplicate folders after migration
```

**Where's Crow:**
```
New Location: Documents/07_Creative_Projects/Wheres_Crow_Project/

Move files to:
- Business_Plan/ (business docs)
- Story_Development/ (manuscript, outlines)
- Artwork/ (illustrations, designs)

Delete empty duplicate folders after migration
```

#### Step 3: Desktop Commander Commands

```javascript
// Use Desktop Commander to automate this:

// List contents of each folder
await dc.listFiles('folder_id_here');

// Move files
await dc.moveFile({
  source: 'old_folder/file.pdf',
  destination: 'Documents/07_Creative_Projects/MXD-MDA_Brand/Brand_Guide/'
});

// Delete empty folders (after confirming empty)
await dc.deleteFolder('folder_id');
```

---

## 📝 PHASE 4: NOTION WORKSPACE AUDIT

### Search Commands in Notion:

1. Open Notion workspace
2. Use global search (Ctrl/Cmd + P)
3. Search for:
   - "Where's Crow"
   - "MXD-MDA"
   - "Court" OR "Legal"
   - "Deadlines"
   - "Project" OR "Sprint"

### Document Findings:

Create: `Notion_Audit_Results.md`

```markdown
# Notion Workspace Audit
Date: 2025-11-01

## Pages Found:
- [ ] Where's Crow project page
- [ ] MXD-MDA brand page
- [ ] Legal tracking page
- [ ] Calendar/deadlines page
- [ ] Sprint planning page

## Missing Critical Pages:
- [ ] Court case tracker
- [ ] Benefits renewal tracker
- [ ] Creative project roadmap

## Action Items:
1. Import Project GEM structure into Notion
2. Create database for deadlines
3. Set up sprint planning template
```

---

## ☁️ PHASE 5: ONEDRIVE AUDIT

### Check OneDrive for Scattered Documents:

1. Open File Explorer
2. Navigate to OneDrive folder (usually `C:\Users\AMBER\OneDrive\`)
3. Search for:
   - `*.pdf` (all PDFs)
   - "court"
   - "LVNV"
   - "medical"
   - "bank statement"

### Migration Strategy:

**Any legal documents found:**
```
Move to: Google Drive\Documents\06_Legal\[Case_Folder]\
```

**Any financial documents:**
```
Move to: Google Drive\Documents\01_Finance\[Subfolder]\
```

**Creative project files:**
```
Move to: Google Drive\Documents\07_Creative_Projects\[Project]\
```

---

## 💾 PHASE 6: D: DRIVE AUDIT

### What to Check:

```powershell
# In PowerShell:
cd D:\

# List all directories
Get-ChildItem -Directory

# Search for specific files
Get-ChildItem -Recurse -Filter "*crow*"
Get-ChildItem -Recurse -Filter "*court*"
Get-ChildItem -Recurse -Filter "*.pdf"
```

### Common D: Drive Locations:

- `D:\Documents\` - Legacy documents
- `D:\Projects\` - Old project files
- `D:\Downloads\` - Downloaded files
- `D:\Backups\` - Old backups

### Recovery Priority:

1. **Legal/Court documents** → Google Drive\Documents\06_Legal\
2. **Where's Crow files** → Google Drive\Documents\07_Creative_Projects\Wheres_Crow_Project\
3. **MXD-MDA brand assets** → Google Drive\Documents\07_Creative_Projects\MXD-MDA_Brand\
4. **Financial records** → Google Drive\Documents\01_Finance\

---

## 🐙 PHASE 7: GITHUB REPOSITORY ORGANIZATION

### Current Status:

**Repository:** mxdmda6-cmyk/mxd-mda
**Branch:** `claude/audit-google-drive-organization-011CUhgTerShgyzUrTAivKWK`
**PR Available:** Yes

### Actions Needed:

#### 1. Review and Merge PR

```bash
# In PowerShell or Git Bash:
cd C:\Users\AMBER\mxd-mda

# Make sure you're on the audit branch
git checkout claude/audit-google-drive-organization-011CUhgTerShgyzUrTAivKWK

# Review changes
git log --oneline -5

# If everything looks good, merge to main:
git checkout main
git merge claude/audit-google-drive-organization-011CUhgTerShgyzUrTAivKWK

# Push to remote
git push origin main
```

#### 2. Create README.md

```bash
# Create a proper README
echo "# MXD-MDA Creative Universe" > README.md
echo "" >> README.md
echo "Transmedia storytelling ecosystem for Where's Crow and Alchemical Nexus." >> README.md
echo "" >> README.md
echo "## Projects" >> README.md
echo "- **Where's Crow:** Interactive gothic mystery" >> README.md
echo "- **Alchemical Nexus:** Multi-agent AI system" >> README.md
echo "- **MXD-MDA Brand:** Creative identity and thought leadership" >> README.md

git add README.md
git commit -m "Add project README"
git push origin main
```

#### 3. Fix GitHub Actions

The CodeQL workflow is failing. Add this file:

**.github/workflows/codeql.yml:**
```yaml
name: "CodeQL"

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  analyze:
    name: Analyze
    runs-on: ubuntu-latest

    steps:
    - name: Checkout repository
      uses: actions/checkout@v3

    - name: Initialize CodeQL
      uses: github/codeql-action/init@v2
      with:
        languages: javascript, python

    - name: Perform CodeQL Analysis
      uses: github/codeql-action/analyze@v2
```

#### 4. Organize Repository Structure

```
mxd-mda/
├── README.md (NEW)
├── docs/
│   ├── PROJECT_GEM_GUIDE.md (link to Google Drive structure)
│   ├── WHERE_IS_CROW_OVERVIEW.md
│   └── ALCHEMICAL_NEXUS_ARCHITECTURE.md
├── src/
│   ├── wheres-crow/
│   ├── alchemical-nexus/
│   └── brand/
├── PROJECT_GEM_STRUCTURE/ (already exists)
└── .github/
    └── workflows/
```

---

## 📅 PHASE 8: VISUAL DEADLINE DASHBOARD

### Create Comprehensive Deadline Tracker

I'll create this as a separate file: `DEADLINE_DASHBOARD.md`

**Contents:**
- All court dates with case numbers
- Benefits renewal deadlines
- Creative project milestones
- Sprint planning timeline
- Integration with Google Calendar

---

## 🎓 PHASE 9: DESKTOP COMMANDER TUTORIALS

### Quick Wins You Can Do Right Now:

#### 1. **Batch File Operations**

```javascript
// Find all PDFs in a directory
const pdfs = await dc.glob('**/*.pdf');
console.log(`Found ${pdfs.length} PDF files`);

// Move court documents to organized folder
for (const pdf of pdfs) {
  if (pdf.includes('court') || pdf.includes('LVNV')) {
    await dc.moveFile({
      source: pdf,
      destination: `Documents/06_Legal/Unsorted/${path.basename(pdf)}`
    });
  }
}
```

#### 2. **Search Across All Drives**

```javascript
// Search for "Where's Crow" files across all drives
const results = await dc.search({
  query: "Where's Crow",
  drives: ['C:', 'D:', 'OneDrive', 'Google Drive']
});

results.forEach(file => {
  console.log(`Found: ${file.path}`);
});
```

#### 3. **Duplicate Finder**

```javascript
// Find duplicate files by content hash
const duplicates = await dc.findDuplicates({
  directory: 'C:\\Users\\AMBER\\',
  recursive: true
});

duplicates.forEach(group => {
  console.log(`\nDuplicates found:`);
  group.files.forEach(f => console.log(`  - ${f}`));
});
```

#### 4. **Auto-Rename with Pattern**

```javascript
// Rename files to Project GEM standard
const files = await dc.glob('Documents/06_Legal/**/*');

for (const file of files) {
  const newName = await dc.autoRename({
    file: file,
    pattern: 'YYYY-MM-DD_{source}_{type}.pdf',
    extractDate: true,
    extractSource: true
  });

  console.log(`Renamed: ${file} → ${newName}`);
}
```

---

## ✅ EXECUTION CHECKLIST

Print this and check off as you complete each phase:

### Legal Intelligence (URGENT)
- [ ] Search mxdmda6@gmail.com for Oct 22 court hearing
- [ ] Search Kretz97@gmail.com for legal communications
- [ ] Call court if no email found
- [ ] Document findings in Legal_Communications_Audit.txt
- [ ] Verify Dec 2 pre-trial is still scheduled

### Project GEM Deployment
- [ ] Run setup_project_gem.ps1 (or manual copy)
- [ ] Verify 56 folders created in Google Drive
- [ ] Check sync status (Drive icon in system tray)
- [ ] Confirm Documents folder visible in Drive web interface

### Google Drive Consolidation
- [ ] Audit 2 MXD-MDA folders (list contents)
- [ ] Audit 3 Where's Crow folders (list contents)
- [ ] Merge into Project GEM structure
- [ ] Delete empty duplicate folders
- [ ] Verify no data loss

### Notion Workspace
- [ ] Search for existing project pages
- [ ] Create Notion_Audit_Results.md
- [ ] Identify missing pages
- [ ] Create deadline tracker database (optional)

### OneDrive Audit
- [ ] Search for PDFs
- [ ] Search for court/legal keywords
- [ ] Search for financial documents
- [ ] Migrate important files to Google Drive
- [ ] Document what was found

### D: Drive Audit
- [ ] List all directories
- [ ] Search for Crow/court/project files
- [ ] Recover any critical documents
- [ ] Migrate to Google Drive structure
- [ ] Note location of large media files

### GitHub Organization
- [ ] Review audit branch PR
- [ ] Merge to main (if approved)
- [ ] Create README.md
- [ ] Fix CodeQL workflow
- [ ] Push all changes

### Dashboard Creation
- [ ] Review DEADLINE_DASHBOARD.md (I'll create this)
- [ ] Add to Google Calendar
- [ ] Set reminders for each deadline
- [ ] Share with stakeholders (if needed)

### Desktop Commander Learning
- [ ] Try batch file operations example
- [ ] Run search across all drives
- [ ] Test duplicate finder
- [ ] Experiment with auto-rename

---

## 🎯 SUCCESS METRICS

You'll know the deployment succeeded when:

✅ You can find any document in under 30 seconds
✅ All court deadlines are visible in one dashboard
✅ Creative projects have dedicated, organized spaces
✅ No duplicate folders in Google Drive
✅ GitHub repository has clear structure and working CI
✅ You can confidently prepare for Dec 2 court date
✅ Desktop Commander feels like a natural workflow tool

---

## 🆘 TROUBLESHOOTING

**PowerShell script won't run:**
```powershell
# Enable script execution:
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

**Google Drive not syncing:**
1. Check Drive icon in system tray
2. Click → Preferences → Resume syncing
3. Check available storage (you have 2TB)

**Can't find D: drive:**
- It may not exist on your system
- Check Disk Management: `diskmgmt.msc`

**Desktop Commander questions:**
- Built-in help: Type `/help` in Desktop Commander
- Documentation: Check their official docs
- Community: Ask in their Discord/support

---

## 📞 EMERGENCY CONTACTS

**Legal:**
- Hennepin County Court: (612) 348-2040
- Attorney Gabriella: [Add phone number]

**Benefits:**
- SNAP: (612) 596-1300
- Social Security: 1-800-772-1213

**Tech Support:**
- Google Drive: support.google.com/drive
- GitHub: support.github.com
- Desktop Commander: [Their support channel]

---

## ⚂ THE ALCHEMICAL TRANSFORMATION

**Prima Materia (Chaos):** Scattered files across 8 systems
**Albedo (Purification):** Project GEM deployment
**Citrinitas (Illumination):** Dashboard and visibility
**Rubedo (Coagulation):** Fully operational Command Center

You are at the threshold. The tools are ready. The structure is designed.

**Deploy now. Build the Carnival. Find the Crow.**

---

**Next Steps:** Choose ONE phase to start with. I recommend:
1. **LEGAL INTELLIGENCE** (if Oct 22 is unclear)
2. **PROJECT GEM DEPLOYMENT** (if legal is handled)

Which do you want to tackle first?
