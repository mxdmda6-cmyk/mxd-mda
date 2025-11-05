# 📝 FILE NAMING CONVENTIONS - Quick Reference

## Universal Format

```
YYYY-MM-DD_[Source]_[Type]_[Description].pdf
```

**Why this format?**
- ✅ Sorts chronologically automatically
- ✅ Easy to search by date, source, or type
- ✅ Clear at a glance what the document is
- ✅ No "final_v2_FINAL_use_this_one.pdf" madness

---

## 📅 Date Format: YYYY-MM-DD

**Always use:** `2025-11-01` (never `11-01-2025` or `11/01/25`)

**Why?**
- Sorts correctly when alphabetized
- International standard (ISO 8601)
- No confusion between US/European date formats

**Examples:**
- `2025-11-01` ✅
- `11-01-2025` ❌
- `11/01/25` ❌

**What if I don't know the exact date?**
- Use first of month: `2025-10-01`
- Use first of year: `2025-01-01`
- Use document date, not when you saved it

---

## 🏛️ Category-Specific Formats

### Legal Documents

```
YYYY-MM-DD_[Court/Case]_[Document_Type].pdf
```

**Examples:**
- `2025-10-15_Hennepin_Court_Summons.pdf`
- `2025-10-22_LVNV_Collection_Notice.pdf`
- `2025-11-01_Court_27CR2522797_Hearing_Notice.pdf`
- `2025-12-02_Pretrial_Order.pdf`

**Common Types:**
- Summons, Notice, Order, Complaint, Motion, Filing, Exhibit, Evidence

---

### Financial Documents

```
YYYY-MM_[Institution]_[Account_Type]_Statement.pdf
```

**Examples:**
- `2025-10_Chase_Checking_Statement.pdf`
- `2025-10_Discover_Credit_Card_Statement.pdf`
- `2025-10-15_LVNV_Collection_Letter.pdf`
- `2025-Q3_Tax_Return.pdf`

**For receipts:**
```
YYYY-MM-DD_[Vendor]_[Amount]_[Category].pdf
```
- `2025-10-15_Target_48.53_Groceries.pdf`
- `2025-11-01_Gas_Station_35.00_Auto.pdf`

---

### Medical Documents

```
YYYY-MM-DD_[Provider]_[Type].pdf
```

**Examples:**
- `2025-10-15_Hennepin_Healthcare_Lab_Results.pdf`
- `2025-10-20_Dr_Smith_Visit_Summary.pdf`
- `2025-10-25_BCBS_EOB_Invoice_12345.pdf`
- `2025-09-01_HealthPartners_Insurance_Card.pdf`

**Common Types:**
- Lab_Results, Visit_Summary, Prescription, EOB, Bill, Insurance_Card, Referral

---

### Personal Documents

```
[Document_Type]_[Name/ID]_[Date].pdf
```

**Examples:**
- `Drivers_License_MN_2025-Expires-2030.pdf`
- `SSN_Card_Scan.pdf`
- `Birth_Certificate_Original.pdf`
- `Passport_US_Expires_2029.pdf`

**SSA/Benefits:**
```
YYYY-MM-DD_[Agency]_[Type].pdf
```
- `2025-09-01_SSA_Denial_Letter.pdf`
- `2025-10-01_SNAP_Benefits_Expired_Notice.pdf`
- `2025-08-15_Disability_Application.pdf`

---

### Creative Project Files

```
[Project]_[Type]_[Version]_[Date].extension
```

**Examples:**
- `MXD_MDA_Logo_Primary_v3_2025-10.png`
- `MXD_MDA_Brand_Guide_v2_2025-11-01.pdf`
- `Wheres_Crow_Chapter_01_Draft_2025-10.docx`
- `Wheres_Crow_Cover_Art_Final_2025-11.jpg`
- `Alchemical_Nexus_Architecture_Diagram_v1.pdf`

**Version naming:**
- `v1`, `v2`, `v3` (not `version1`, `draft`, `final`)
- `Final` only when ACTUALLY final
- `Draft` for work-in-progress

**Bad naming:**
- ❌ `logo_final_FINAL_use_this_v3.png`
- ❌ `document1.pdf`
- ❌ `untitled.docx`

**Good naming:**
- ✅ `MXD_MDA_Logo_Primary_v4_2025-11.png`
- ✅ `Brand_Guide_Final_2025-11-01.pdf`

---

### Work/Contract Documents

```
YYYY-MM-DD_[Client/Company]_[Type].pdf
```

**Examples:**
- `2025-09-01_Acme_Corp_Contract.pdf`
- `2025-10-15_Freelance_Invoice_Oct.pdf`
- `2025-11-01_Resume_Creative_Director.pdf`
- `2025-10-20_Portfolio_Web_Design.pdf`

---

## 🚫 Characters to NEVER Use in File Names

**Avoid these characters:**
```
❌ / \ : * ? " < > |
```

**Why?**
- They break Windows/Mac file systems
- Cause sync errors
- Create upload failures

**Use instead:**
```
✅ Use: _ (underscore) or - (dash)
✅ Use: Spaces (but sparingly)
```

---

## 📏 Length Guidelines

**File name length:**
- **Ideal:** 30-50 characters
- **Maximum:** 100 characters
- **Minimum:** Be descriptive enough to know what it is

**Too short:**
- ❌ `doc.pdf` (What is this?)
- ❌ `court.pdf` (Which court case?)

**Too long:**
- ❌ `2025-10-15_Hennepin_County_District_Court_Case_Number_27-CR-25-22797_Pre_Trial_Hearing_Notice_Received_Via_Mail.pdf`
- ✅ `2025-10-15_Court_27CR2522797_Pretrial_Notice.pdf`

---

## 🔤 Capitalization

**Choose ONE style and stick with it:**

**Option 1: Snake_Case (Recommended)**
```
2025-10-15_Court_Summons_LVNV.pdf
Drivers_License_MN.pdf
Brand_Guide_Final.pdf
```

**Option 2: lowercase-with-dashes**
```
2025-10-15-court-summons-lvnv.pdf
drivers-license-mn.pdf
brand-guide-final.pdf
```

**Option 3: CamelCase**
```
2025-10-15-CourtSummonsLVNV.pdf
DriversLicenseMN.pdf
BrandGuideFinal.pdf
```

**Pick ONE. Don't mix styles.**

---

## 🔢 Version Numbers

**For creative work that evolves:**

```
[Project]_[Type]_v[Number]_[Date].extension
```

**Examples:**
- `Brand_Guide_v1_2025-09.pdf` (First version)
- `Brand_Guide_v2_2025-10.pdf` (Updated)
- `Brand_Guide_v3_2025-11.pdf` (Current)
- `Brand_Guide_Final_2025-11-01.pdf` (Published)

**Rules:**
- Start at v1 (not v0)
- Increment by 1 each time
- Add `_Final` only when truly done
- Keep old versions in `99_Archive/`

---

## 📂 Special Cases

### Scanned Documents

```
[Original_Name]_Scanned_YYYY-MM-DD.pdf
```

**Examples:**
- `Birth_Certificate_Scanned_2025-10-15.pdf`
- `Court_Summons_Scanned_2025-10-22.pdf`

### Downloaded from Email

```
YYYY-MM-DD_[Subject]_[Sender].pdf
```

**Examples:**
- `2025-10-15_SSA_Denial_Letter_Social_Security.pdf`
- `2025-10-22_Court_Notice_Hennepin_County.pdf`

### Photos of Documents (temporary)

```
YYYY-MM-DD_[Type]_Photo.jpg
```

**Examples:**
- `2025-10-15_Court_Summons_Photo.jpg`
- `2025-10-20_Medical_Bill_Photo.jpg`

**Note:** Replace with scanned PDF version later

---

## ✅ QUICK CHECKLIST

Before saving ANY file, ask yourself:

- [ ] Does the filename include a date in YYYY-MM-DD format?
- [ ] Can I tell what this is without opening it?
- [ ] Does it sort chronologically with similar files?
- [ ] Did I avoid special characters (/, \, :, *, ?, ", <, >, |)?
- [ ] Is it between 30-100 characters?
- [ ] Am I using consistent capitalization?
- [ ] If it's a new version, did I increment the version number?

---

## 🎯 Examples by Scenario

### "I just downloaded a court summons from my email"

**Original name:** `document-14875.pdf`

**Rename to:** `2025-10-22_Hennepin_Court_Summons_LVNV.pdf`

**Why?**
- Date: When you received it
- Source: Hennepin Court
- Type: Summons
- Detail: Related to LVNV case

---

### "I scanned my Social Security denial letter"

**Original name:** `scan001.pdf`

**Rename to:** `2025-09-01_SSA_Denial_Letter.pdf`

**Why?**
- Date: Letter date (not scan date)
- Source: SSA
- Type: Denial Letter

---

### "I'm saving a new version of my brand guide"

**Previous name:** `MXD_MDA_Brand_Guide_v2_2025-10.pdf`

**New name:** `MXD_MDA_Brand_Guide_v3_2025-11.pdf`

**Why?**
- Incremented version number (v2 → v3)
- Updated month (Oct → Nov)
- Kept consistent format

---

### "I took a photo of a medical bill on my phone"

**Phone name:** `IMG_20251015_143052.jpg`

**Upload as:** `2025-10-15_Medical_Bill_Photo.jpg`

**Later replace with:** `2025-10-15_Hennepin_Healthcare_Bill_12345.pdf`

---

## 🧰 TOOLS FOR BATCH RENAMING

### Windows:
- Built-in: Select multiple files → F2 → Rename
- PowerRename (PowerToys - free from Microsoft)

### Mac:
- Built-in: Select multiple files → Right-click → Rename Items
- NameChanger (free app)

### Both:
- Bulk Rename Utility (free)
- Advanced Renamer (free)

---

## 🏆 THE GOLDEN RULE

> **"If you can't find it in 30 seconds, your naming system failed."**

Good file naming is about **future you** being able to find stuff quickly.

Not about making it look pretty.

Not about being clever.

**About being FINDABLE.**

---

## 💡 REAL-WORLD NAMING EXAMPLES

### Legal:
```
2025-10-22_Court_Summons_LVNV.pdf
2025-11-15_Attorney_Contract_Johnson_Law.pdf
2025-12-02_Pretrial_Hearing_Notice.pdf
```

### Medical:
```
2025-10-15_Lab_Results_Hennepin_Healthcare.pdf
2025-10-20_Insurance_EOB_October.pdf
2025-09-15_Prescription_Adderall.pdf
```

### Financial:
```
2025-10_Chase_Checking_Statement.pdf
2025-10_Discover_Credit_Card_Statement.pdf
2025-10-15_LVNV_Collection_Notice.pdf
2025-Q3_2025_Tax_Documents.pdf
```

### Creative:
```
MXD_MDA_Logo_Primary_v3.png
MXD_MDA_Brand_Colors_v2.pdf
Wheres_Crow_Chapter_01_Draft.docx
Alchemical_Nexus_Wireframes_v1.pdf
```

---

**You've got this! Start naming files consistently TODAY and future you will thank you. 🎯**
