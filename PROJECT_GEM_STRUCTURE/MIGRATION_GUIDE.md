# 📦 PROJECT GEM - Migration Guide

## Moving Your Existing Files into the New Structure

**Time Required:** 1-3 hours (depending on how much you have)
**Best Approach:** Do it in phases, starting with urgent items

---

## 🚨 PHASE 1: URGENT ITEMS (Do This First - 30 Minutes)

### Court & Legal Documents

**Current Location:** Scattered across Downloads, email attachments, desktop
**New Home:** `Documents/06_Legal/[Case_Folder]/`

**Action Steps:**

1. **Search your Google Drive for:**
   - "summons"
   - "court"
   - "hearing"
   - "LVNV"
   - "Hennepin"
   - "27-CR-25-22797"
   - "27DAFA24-5203"
   - "27-CO-25-4917"

2. **Move each document to its court case folder:**

   ```
   Documents/06_Legal/Court_Case_27-CR-25-22797/
   ├── 2025-XX-XX_Summons.pdf
   ├── 2025-XX-XX_Court_Order.pdf
   └── 2025-XX-XX_Hearing_Notice.pdf

   Documents/06_Legal/Court_Case_27-CO-25-4917/  (LVNV)
   ├── 2025-XX-XX_LVNV_Summons.pdf
   ├── 2025-XX-XX_Collection_Notice.pdf
   └── 2025-XX-XX_Court_Hearing_Notice.pdf

   Documents/06_Legal/OFP_Case_27DAFA24-5203/
   ├── 2025-XX-XX_OFP_Order.pdf
   └── 2025-XX-XX_OFP_Notice.pdf
   ```

3. **Rename files** using format: `YYYY-MM-DD_[Type]_[Description].pdf`

4. **Create Google Calendar events** with links to these folders:
   - Oct 22, 2025, 8:15 AM - "LVNV Court Hearing" - Link to folder
   - Dec 2, 2025, 9:00 AM - "Pre-trial Hearing" - Link to folder

### Benefits & Financial Crisis Documents

**Current Location:** Email, Downloads, random folders
**New Home:** Multiple locations based on type

**Social Security:**
- Search for: "SSA", "social security", "disability", "denial"
- Move to: `Documents/02_Personal/Social_Security/`
- Format: `2025-09-01_SSA_Denial_Letter.pdf`

**SNAP Benefits:**
- Search for: "SNAP", "food stamps", "EBT", "612-596-1300"
- Move to: `Documents/04_Household/Assistance/`
- Format: `2025-09-01_SNAP_Expired_Notice.pdf`

**Debt Collection:**
- Search for: "LVNV", "collection", "debt"
- Move to: `Documents/01_Finance/Debt_Collection/`
- Format: `2025-XX-XX_LVNV_Collection_Notice.pdf`

---

## 🎯 PHASE 2: HIGH PRIORITY (Next 1 Hour)

### Your Existing Google Drive Folders → New Structure

Based on the audit, here's where everything should go:

| **Current Folder** | **New Location** | **Notes** |
|-------------------|------------------|-----------|
| `Mxd-Mda` | `Documents/07_Creative_Projects/MXD-MDA_Brand/` | Your brand files |
| `Where's Crow` | `Documents/07_Creative_Projects/Wheres_Crow_Project/` | Story project |
| `Brand Profile & Guide` | `Documents/07_Creative_Projects/MXD-MDA_Brand/Brand_Guide/` | Brand assets |
| `Alchemy Archive` | `Documents/07_Creative_Projects/Alchemical_Nexus/` | Alchemical work |
| `Book of Skretz` | `Documents/07_Creative_Projects/Alchemical_Nexus/Book_of_Skretz/` | The book |
| `Marketing` | `Documents/07_Creative_Projects/MXD-MDA_Brand/Marketing/` | Marketing content |
| `Blog Post` | `Documents/07_Creative_Projects/MXD-MDA_Brand/Content/` | Blog articles |
| `04_ASSET_LIBRARY` | `Documents/07_Creative_Projects/MXD-MDA_Brand/Assets/` | Creative assets |
| `Images` | `Documents/07_Creative_Projects/MXD-MDA_Brand/Assets/Images/` | Image files |
| `Specs` | `Documents/07_Creative_Projects/MXD-MDA_Brand/Assets/Specs/` | Design specs |
| `Kredentials` | `Documents/02_Personal/Identification/` | ID documents |
| `Saved from Chrome` | `Documents/99_Archive/Web_Saves/` | Browser downloads |
| `Saved from Google app` | `Documents/99_Archive/Web_Saves/` | Mobile saves |
| `Opal` | `Documents/99_Archive/Old_Projects/` (if old) or appropriate folder | Unclear - review |
| `Arletta Cartela` | `Documents/99_Archive/Old_Projects/` (if old) or appropriate folder | Unclear - review |

### How to Move Folders in Google Drive:

**In Browser:**
1. Go to drive.google.com
2. Drag and drop folder into new location
3. Wait for sync

**On Desktop:**
1. Open File Explorer (Windows) or Finder (Mac)
2. Navigate to Google Drive folder
3. Cut (Ctrl+X / Cmd+X) and Paste (Ctrl+V / Cmd+V)
4. Google Drive will sync automatically

---

## 📋 PHASE 3: ROUTINE ORGANIZATION (Ongoing)

### Medical Records

**Current:** Email attachments, portal downloads
**New Home:** `Documents/03_Medical/2025/[Subfolder]/`

**Process:**

1. Download from patient portals
2. Rename: `YYYY-MM-DD_[Provider]_[Type].pdf`
3. Move to appropriate folder:
   - Bills/Insurance → `EOBs_Insurance/`
   - Test results → `Lab_Results/`
   - Visit summaries → `Doctor_Visits/`

### Financial Documents

**Current:** Email, bank websites
**New Home:** `Documents/01_Finance/2025/[Subfolder]/`

**Monthly Routine:**
1. Download bank statements → `Bank_Statements/`
2. Download credit card statements → `Credit_Cards/`
3. Save important receipts → `Receipts_Taxes/`
4. File pay stubs → `Pay_Stubs/`

**Format:** `2025-10_Chase_Statement.pdf`

---

## 🗂️ MIGRATION WORKFLOW

### Step-by-Step Process:

**1. Identify** → Search for files by keyword
**2. Review** → Confirm what it is and where it belongs
**3. Rename** → Use proper naming convention
**4. Move** → Drag to appropriate folder
**5. Verify** → Check it synced to cloud

### Batch Processing Tips:

**Select Multiple Files:**
- Hold Ctrl (Windows) or Cmd (Mac)
- Click each file to select
- Drag all at once to new folder

**Use Search to Find Similar Items:**
```
In Google Drive search:
- type:pdf
- after:2025-01-01
- owner:me
```

---

## 🚫 WHAT NOT TO MIGRATE

### Leave These Alone:

- **Google Photos** - Has its own organization
- **Gmail** - Keep in email unless you need offline access
- **Shared Drives** - Company/collaborative drives stay separate
- **App Data** - Backup folders from apps (don't touch)

### Archive Instead of Migrate:

If you find old files (2+ years) you haven't touched:
- Don't spend time organizing them
- Move entire old folder to `Documents/99_Archive/Old_Projects/`
- Name it: `Archive_[Original_Name]_[Date]`
- Example: `Archive_Random_Old_Files_20251101`

---

## 🎨 CREATIVE PROJECTS - DETAILED MIGRATION

### MXD-MDA Brand Files

**Organize by type:**

```
Documents/07_Creative_Projects/MXD-MDA_Brand/
├── Brand_Guide/
│   ├── Logo_Files/
│   │   ├── MXD_MDA_Logo_Primary.png
│   │   ├── MXD_MDA_Logo_White.png
│   │   └── MXD_MDA_Logo_Black.png
│   ├── Brand_Colors.pdf
│   ├── Typography_Guide.pdf
│   └── Brand_Standards_v2.pdf
│
├── Marketing/
│   ├── Social_Media/
│   │   ├── Instagram_Posts/
│   │   ├── LinkedIn_Content/
│   │   └── Content_Calendar.xlsx
│   ├── Email_Campaigns/
│   └── Marketing_Plan_2025.pdf
│
├── Content/
│   ├── Blog_Posts/
│   ├── Articles/
│   └── Thought_Leadership/
│
└── Assets/
    ├── Images/
    ├── Videos/
    ├── Templates/
    └── Design_Files/
```

**Migration Steps:**

1. **Audit current folders:**
   - `Mxd-Mda` - What's inside?
   - `04_ASSET_LIBRARY` - What types of assets?
   - `Brand Profile & Guide` - Logo files?

2. **Sort by type, not source:**
   - Don't keep old folder structure
   - Group by PURPOSE (marketing vs brand vs content)

3. **Delete duplicates:**
   - Search for "logo" - How many versions?
   - Keep ONLY current/latest versions
   - Archive old versions to `99_Archive/`

### Where's Crow Project

**Organize by production stage:**

```
Documents/07_Creative_Projects/Wheres_Crow_Project/
├── Business_Plan/
│   ├── Business_Model_Canvas.pdf
│   ├── Revenue_Strategy.pdf
│   └── Market_Research.pdf
│
├── Story_Development/
│   ├── Manuscript/
│   │   ├── Chapter_01_Draft.docx
│   │   ├── Chapter_02_Draft.docx
│   │   └── Full_Manuscript_v3.pdf
│   ├── Plot_Outlines/
│   ├── Character_Profiles/
│   └── World_Building/
│
└── Artwork/
    ├── Character_Designs/
    ├── Scene_Illustrations/
    ├── Cover_Art/
    └── Reference_Images/
```

### Alchemical Nexus

**Technical project structure:**

```
Documents/07_Creative_Projects/Alchemical_Nexus/
├── Book_of_Skretz/
│   ├── Original_Documents/
│   ├── Translations/
│   └── Research_Notes/
│
├── MVP_Development/
│   ├── Architecture_Docs/
│   ├── API_Documentation/
│   ├── Database_Schemas/
│   └── User_Flows/
│
└── Research/
    ├── Reference_Papers/
    ├── Inspiration/
    └── Competitive_Analysis/
```

---

## 📱 MOBILE WORKFLOW

### Uploading from Phone:

**Google Drive App:**

1. Open Google Drive app
2. Navigate to correct folder (e.g., `Documents/03_Medical/2025/Lab_Results/`)
3. Tap **+** button
4. Choose **Upload** → Select photo/file
5. Rename before uploading (use voice typing!)

**Example:**
- Take photo of court document
- Upload to `06_Legal/Court_Case_27-CR-25-22797/`
- Rename: `2025-11-01_Court_Summons_Photo.jpg`
- Later, create proper PDF version on computer

---

## 🔧 TROUBLESHOOTING MIGRATION

### "I have thousands of files, this is overwhelming!"

**Answer:** Don't migrate everything at once.

**Priority levels:**

1. **Week 1:** Legal documents (court deadlines!)
2. **Week 2:** Benefits, financial crisis docs
3. **Week 3:** Creative projects you're actively using
4. **Week 4:** Medical records from past year
5. **Month 2:** Everything else

**Rule:** If you haven't opened it in 6 months, archive it unorganized.

### "I don't know where something goes"

**Decision tree:**

1. **Is it legal/court-related?** → `06_Legal/`
2. **Is it about money?** → `01_Finance/`
3. **Is it medical?** → `03_Medical/`
4. **Is it creative work?** → `07_Creative_Projects/`
5. **Is it ID/personal?** → `02_Personal/`
6. **Is it home/utilities?** → `04_Household/`
7. **Still unsure?** → `99_Archive/Needs_Sorting/` (create this temp folder)

### "Files aren't syncing"

**Check:**
1. Google Drive icon in system tray/menu bar
2. Click icon → Check sync status
3. Pause & Resume sync if stuck
4. Check internet connection
5. Check available storage space

### "I accidentally deleted something important"

**Solution:**
1. Go to drive.google.com
2. Click **Trash** in left sidebar
3. Find deleted file
4. Right-click → **Restore**
5. You have 30 days before permanent deletion

---

## ✅ MIGRATION CHECKLIST

Print this and check off as you go:

### Phase 1 - Urgent (Day 1)
- [ ] Find all court documents
- [ ] Move to appropriate case folders in `06_Legal/`
- [ ] Rename with proper format
- [ ] Create calendar events with Drive links
- [ ] Find SSA/SNAP documents
- [ ] Move to `02_Personal/Social_Security/` or `04_Household/Assistance/`

### Phase 2 - High Priority (Week 1)
- [ ] Move existing Google Drive folders to new structure
- [ ] Migrate `Mxd-Mda` → `MXD-MDA_Brand/`
- [ ] Migrate `Where's Crow` → `Wheres_Crow_Project/`
- [ ] Migrate `Alchemy Archive` → `Alchemical_Nexus/`
- [ ] Archive browser download folders
- [ ] Move ID documents to `02_Personal/Identification/`

### Phase 3 - Medical (Week 2)
- [ ] Find recent medical records (past 6 months)
- [ ] Download from patient portals
- [ ] Move to `03_Medical/2025/[appropriate folder]/`
- [ ] Scan insurance cards → `Provider_Information/`

### Phase 4 - Financial (Week 2-3)
- [ ] Download recent bank statements
- [ ] Move to `01_Finance/2025/Bank_Statements/`
- [ ] Download credit card statements
- [ ] Move to `01_Finance/2025/Credit_Cards/`
- [ ] Gather tax documents
- [ ] Move to `01_Finance/Taxes/`

### Phase 5 - Creative (Week 3-4)
- [ ] Organize MXD-MDA brand files by type
- [ ] Sort Where's Crow materials by production stage
- [ ] Consolidate Alchemical Nexus documentation
- [ ] Delete duplicate files
- [ ] Archive old versions

### Phase 6 - Cleanup (Ongoing)
- [ ] Archive folders you no longer need
- [ ] Delete obvious duplicates
- [ ] Establish weekly filing routine
- [ ] Set up automated backups

---

## 📊 MEASURING SUCCESS

You'll know migration is working when:

✅ You can find your court documents in under 10 seconds
✅ Your Google Drive no longer has random unnamed folders
✅ New files go directly to the right place
✅ You stop losing important documents
✅ Your stress about "where did I put that?" disappears

---

## 🆘 NEED HELP?

**Stuck on something?**

1. Check the main README.md
2. Search Google Drive Help Center
3. Ask in a new chat session with specific questions

**Remember:** Progress > Perfection

You don't have to organize everything perfectly.
You just need to know where the important stuff is.

---

**You've got this! 🚀**

Start with Phase 1 (legal docs) TODAY.
Everything else can wait.
