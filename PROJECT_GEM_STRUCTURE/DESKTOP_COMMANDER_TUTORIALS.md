# 🎮 DESKTOP COMMANDER MASTERY GUIDE
## From Beginner to Power User
**Created for:** MXD-MDA Command Center Operations
**Version:** Tailored for Windows File Organization
**Last Updated:** November 1, 2025

---

## 🌟 WHAT IS DESKTOP COMMANDER?

Desktop Commander is your **AI-powered file system assistant** that turns complex file operations into simple commands. Think of it as having a genius organizer who never sleeps, never forgets, and can process thousands of files in seconds.

**What makes it special:**
- ✅ Natural language commands
- ✅ Batch operations on hundreds of files at once
- ✅ Cross-platform file management (C:, D:, OneDrive, Google Drive)
- ✅ Smart search and duplicate detection
- ✅ Automated organization and renaming
- ✅ Integration with cloud services

---

## 🚀 QUICK START: YOUR FIRST 5 COMMANDS

### 1. **Find All Your PDFs**

```javascript
// Find every PDF on your computer
const pdfs = await dc.glob('**/*.pdf');
console.log(`Found ${pdfs.length} PDF files`);

// Show first 10
pdfs.slice(0, 10).forEach(file => {
  console.log(file);
});
```

**What this does:**
- Searches entire C: drive
- Lists all .pdf files
- Shows you where they are

**Why it's useful:**
- Find that court document you misplaced
- Locate all receipts for tax time
- See where duplicates might exist

---

### 2. **Search for Specific Content**

```javascript
// Find files containing "LVNV" or "court"
const legalFiles = await dc.search({
  query: 'LVNV OR court',
  fileTypes: ['pdf', 'doc', 'docx'],
  drives: ['C:', 'D:', 'Google Drive']
});

console.log('Legal files found:');
legalFiles.forEach(file => {
  console.log(`📄 ${file.path}`);
  console.log(`   Size: ${file.size}`);
  console.log(`   Modified: ${file.modified}\n`);
});
```

**What this does:**
- Searches file content (not just names)
- Checks multiple drives at once
- Shows file metadata

**Real-world use:**
- "Find all files mentioning my court case"
- "Locate every document with 'SNAP' in it"
- "Show me all my bank statements"

---

### 3. **Move Files to Organized Folders**

```javascript
// Move all court documents to legal folder
const courtDocs = await dc.glob('**/*court*.pdf');

for (const doc of courtDocs) {
  await dc.moveFile({
    source: doc,
    destination: 'My Drive (mxdmda6@gmail.com)/Documents/06_Legal/Unsorted/',
    createFolder: true  // Creates folder if doesn't exist
  });
  console.log(`Moved: ${doc}`);
}
```

**What this does:**
- Finds files by keyword in filename
- Moves them to organized location
- Creates folders automatically if needed

**Use cases:**
- Organize scattered downloads
- Move creative assets to project folders
- Clean up desktop chaos

---

### 4. **Find and Delete Duplicates**

```javascript
// Find duplicate files (same content, different names)
const duplicates = await dc.findDuplicates({
  directory: 'C:\\Users\\AMBER\\',
  recursive: true,
  minFileSize: 1024  // Ignore tiny files
});

console.log(`Found ${duplicates.length} groups of duplicates\n`);

duplicates.forEach((group, index) => {
  console.log(`Group ${index + 1}:`);
  group.files.forEach(file => {
    console.log(`  - ${file.path} (${file.size} bytes)`);
  });
  console.log(`  Keep: ${group.files[0].path}`);
  console.log(`  Delete: ${group.files.slice(1).length} copies\n`);
});

// Optional: Auto-delete duplicates (CAREFUL!)
// await dc.deleteDuplicates(duplicates, { keepNewest: true });
```

**What this does:**
- Compares file content (not just names)
- Groups identical files together
- Shows which to keep/delete

**Why it matters:**
- Free up storage space
- Reduce confusion about which file is "the real one"
- Clean up after multiple downloads

---

### 5. **Auto-Rename with Smart Patterns**

```javascript
// Rename files to Project GEM standard
const messyFiles = await dc.glob('Downloads/*.pdf');

for (const file of messyFiles) {
  const metadata = await dc.extractMetadata(file);

  const newName = await dc.rename({
    source: file,
    pattern: '{date}_{source}_{type}.pdf',
    metadata: {
      date: metadata.createdDate.toISOString().split('T')[0],  // YYYY-MM-DD
      source: detectSource(metadata),  // "Court", "Bank", etc.
      type: detectType(metadata)       // "Summons", "Statement"
    }
  });

  console.log(`Renamed: ${path.basename(file)}`);
  console.log(`     To: ${newName}\n`);
}

// Helper functions
function detectSource(metadata) {
  if (metadata.content.includes('Hennepin')) return 'Hennepin_Court';
  if (metadata.content.includes('LVNV')) return 'LVNV';
  if (metadata.content.includes('Chase')) return 'Chase_Bank';
  return 'Unknown_Source';
}

function detectType(metadata) {
  if (metadata.content.includes('Summons')) return 'Summons';
  if (metadata.content.includes('Statement')) return 'Statement';
  if (metadata.content.includes('Notice')) return 'Notice';
  return 'Document';
}
```

**What this does:**
- Reads PDF content to understand what it is
- Renames files with consistent format
- Follows Project GEM naming convention

**Transform this:**
```
document(1).pdf
scan0001.pdf
IMG_20251015_143052.pdf
```

**Into this:**
```
2025-10-15_Hennepin_Court_Summons.pdf
2025-10-22_LVNV_Collection_Notice.pdf
2025-10-15_Medical_Bill.pdf
```

---

## 💪 INTERMEDIATE COMMANDS

### **6. Organize Google Drive Folder Chaos**

```javascript
// List all folders in Google Drive
const driveFolders = await dc.listFolders('My Drive (mxdmda6@gmail.com)');

console.log('Current Google Drive structure:');
driveFolders.forEach(folder => {
  console.log(`📁 ${folder.name}`);
  console.log(`   Items: ${folder.itemCount}`);
  console.log(`   Size: ${folder.size}\n`);
});

// Find duplicate folders (e.g., multiple "Where's Crow" folders)
const duplicateFolders = driveFolders
  .reduce((acc, folder) => {
    const name = folder.name.toLowerCase();
    if (!acc[name]) acc[name] = [];
    acc[name].push(folder);
    return acc;
  }, {});

Object.entries(duplicateFolders)
  .filter(([_, folders]) => folders.length > 1)
  .forEach(([name, folders]) => {
    console.log(`\n⚠️ Found ${folders.length} folders named "${name}":`);
    folders.forEach((f, i) => {
      console.log(`  ${i + 1}. ${f.id} (${f.itemCount} items, ${f.modified})`);
    });
  });
```

**What this does:**
- Maps your entire Google Drive
- Finds duplicate folder names
- Shows what's in each

**Use it to:**
- Identify which "Where's Crow" folder has the most recent files
- Consolidate 3 crow folders into 1
- Clean up Drive before deploying Project GEM

---

### **7. Migrate Files from Old Locations**

```javascript
// Migrate from OneDrive to Google Drive with Project GEM structure
const migrationMap = {
  'court': 'Documents/06_Legal/Unsorted/',
  'medical': 'Documents/03_Medical/2025/Unsorted/',
  'crow': 'Documents/07_Creative_Projects/Wheres_Crow_Project/Unsorted/',
  'mxd': 'Documents/07_Creative_Projects/MXD-MDA_Brand/Unsorted/',
  'bank': 'Documents/01_Finance/2025/Unsorted/'
};

// Scan OneDrive
const oneDriveFiles = await dc.glob('OneDrive/**/*.{pdf,doc,docx,png,jpg}');

console.log(`Found ${oneDriveFiles.length} files in OneDrive\n`);

for (const file of oneDriveFiles) {
  const filename = path.basename(file).toLowerCase();
  let destination = 'Documents/99_Archive/Migrated_from_OneDrive/';

  // Detect where it should go
  for (const [keyword, folder] of Object.entries(migrationMap)) {
    if (filename.includes(keyword)) {
      destination = folder;
      break;
    }
  }

  // Copy (don't delete original yet)
  await dc.copyFile({
    source: file,
    destination: `My Drive (mxdmda6@gmail.com)/${destination}`,
    createFolder: true
  });

  console.log(`Migrated: ${path.basename(file)}`);
  console.log(`      To: ${destination}`);
}
```

**What this does:**
- Scans OneDrive for important files
- Intelligently routes them to Project GEM folders
- Keeps originals safe until you verify

---

### **8. Create Project Snapshots**

```javascript
// Snapshot your Where's Crow project for version control
const projectName = 'Wheres_Crow';
const snapshotDate = new Date().toISOString().split('T')[0];

const snapshot = await dc.createSnapshot({
  source: `Documents/07_Creative_Projects/Wheres_Crow_Project/`,
  destination: `Documents/99_Archive/Snapshots/${projectName}_${snapshotDate}/`,
  exclude: ['*.tmp', 'node_modules', '.git'],
  compress: true
});

console.log(`Snapshot created: ${snapshot.path}`);
console.log(`Size: ${snapshot.size}`);
console.log(`Files backed up: ${snapshot.fileCount}`);
```

**What this does:**
- Creates dated backup of entire project
- Compresses to save space
- Lets you roll back if something breaks

**Use before:**
- Major manuscript edits
- Reorganizing folder structure
- Sharing files with collaborators

---

## 🔥 ADVANCED AUTOMATION

### **9. Daily Auto-Organization Script**

```javascript
// Run this every morning to auto-organize yesterday's work
async function dailyCleanup() {
  console.log('🧹 Starting daily cleanup...\n');

  // 1. Organize Downloads
  const downloads = await dc.glob('Downloads/*');
  console.log(`Found ${downloads.length} files in Downloads`);

  for (const file of downloads) {
    const ext = path.extname(file).toLowerCase();
    const filename = path.basename(file).toLowerCase();

    let destination;

    // Route by content
    if (filename.includes('court') || filename.includes('legal')) {
      destination = 'Documents/06_Legal/Unsorted/';
    } else if (ext === '.pdf' && filename.includes('statement')) {
      destination = 'Documents/01_Finance/2025/Unsorted/';
    } else if (ext === '.pdf') {
      destination = 'Documents/99_Archive/Downloaded_PDFs/';
    } else if (['.jpg', '.png', '.gif'].includes(ext)) {
      destination = 'Documents/99_Archive/Downloaded_Images/';
    } else {
      destination = 'Documents/99_Archive/Misc_Downloads/';
    }

    await dc.moveFile({
      source: file,
      destination: `My Drive (mxdmda6@gmail.com)/${destination}`,
      createFolder: true
    });
  }

  // 2. Clean Desktop
  const desktopFiles = await dc.glob('Desktop/*');
  console.log(`\nCleaning ${desktopFiles.length} files from Desktop`);

  for (const file of desktopFiles) {
    const isOld = await dc.isOlderThan(file, { days: 7 });
    if (isOld) {
      await dc.moveFile({
        source: file,
        destination: `Documents/99_Archive/Old_Desktop_Files/`
      });
    }
  }

  // 3. Backup recent work
  const recentCreative = await dc.find({
    directory: 'Documents/07_Creative_Projects/',
    modifiedWithin: { days: 1 },
    recursive: true
  });

  if (recentCreative.length > 0) {
    console.log(`\n📸 Backing up ${recentCreative.length} recently modified files`);
    await dc.createSnapshot({
      files: recentCreative,
      destination: `Documents/99_Archive/Daily_Backups/${new Date().toISOString().split('T')[0]}/`
    });
  }

  console.log('\n✅ Daily cleanup complete!');
}

// Schedule to run every day at 8 AM
dc.schedule({
  task: dailyCleanup,
  cron: '0 8 * * *'  // Every day at 8 AM
});
```

**What this does:**
- Auto-organizes Downloads folder
- Cleans old files from Desktop
- Backs up recent creative work
- Runs automatically while you sleep

---

### **10. Smart Document Scanner**

```javascript
// Scan a directory and categorize every file
async function intelligentCategorization(directory) {
  const files = await dc.glob(`${directory}/**/*`);

  const categories = {
    legal: [],
    financial: [],
    medical: [],
    creative: [],
    personal: [],
    unknown: []
  };

  for (const file of files) {
    const analysis = await dc.analyzeFile(file);

    // Use AI to read content and categorize
    const category = await analyzeContent(analysis);
    categories[category].push(file);
  }

  // Generate report
  console.log('\n📊 CATEGORIZATION REPORT\n');
  for (const [category, fileList] of Object.entries(categories)) {
    if (fileList.length > 0) {
      console.log(`\n${category.toUpperCase()} (${fileList.length} files):`);
      fileList.slice(0, 5).forEach(f => console.log(`  - ${path.basename(f)}`));
      if (fileList.length > 5) {
        console.log(`  ... and ${fileList.length - 5} more`);
      }
    }
  }

  return categories;
}

async function analyzeContent(analysis) {
  const content = analysis.content.toLowerCase();

  if (content.match(/court|summons|hearing|legal|attorney|judge/i)) return 'legal';
  if (content.match(/bank|statement|invoice|payment|\$\d+/i)) return 'financial';
  if (content.match(/medical|doctor|hospital|prescription|patient/i)) return 'medical';
  if (content.match(/crow|mxd|brand|story|character|chapter/i)) return 'creative';
  if (content.match(/birthday|family|personal|journal/i)) return 'personal';

  return 'unknown';
}

// Run on your Downloads or Desktop
const results = await intelligentCategorization('Downloads');

// Optionally: Auto-move files to correct folders
for (const [category, files] of Object.entries(results)) {
  if (category === 'unknown') continue;

  for (const file of files) {
    let destination;
    switch(category) {
      case 'legal': destination = 'Documents/06_Legal/Unsorted/'; break;
      case 'financial': destination = 'Documents/01_Finance/2025/Unsorted/'; break;
      case 'medical': destination = 'Documents/03_Medical/2025/Unsorted/'; break;
      case 'creative': destination = 'Documents/07_Creative_Projects/Unsorted/'; break;
      case 'personal': destination = 'Documents/02_Personal/Unsorted/'; break;
    }

    await dc.moveFile({ source: file, destination });
  }
}
```

**What this does:**
- Reads file content with AI
- Categorizes automatically
- Moves files to correct Project GEM folders

---

## 🎯 REAL-WORLD WORKFLOWS

### **Workflow 1: Court Document Preparation**

**Scenario:** Dec 2 pre-trial hearing - gather all documents

```javascript
async function prepareForCourt(caseNumber) {
  console.log(`⚖️ Preparing documents for case: ${caseNumber}\n`);

  // 1. Find ALL related files
  const caseFiles = await dc.search({
    query: caseNumber,
    drives: ['C:', 'D:', 'Google Drive', 'OneDrive'],
    fileTypes: ['pdf', 'doc', 'docx', 'jpg', 'png']
  });

  console.log(`Found ${caseFiles.length} files related to case\n`);

  // 2. Copy everything to case folder
  const caseFolder = `Documents/06_Legal/Court_Case_${caseNumber}/`;

  for (const file of caseFiles) {
    await dc.copyFile({
      source: file.path,
      destination: `My Drive (mxdmda6@gmail.com)/${caseFolder}`,
      createFolder: true
    });
    console.log(`✓ Added: ${path.basename(file.path)}`);
  }

  // 3. Create checklist
  const checklist = `
# Court Hearing Checklist - ${caseNumber}
Date: ${new Date().toLocaleDateString()}

## Documents Prepared:
${caseFiles.map(f => `- [ ] ${path.basename(f.path)}`).join('\n')}

## Pre-Hearing Tasks:
- [ ] Review all documents
- [ ] Prepare questions for judge
- [ ] Contact attorney
- [ ] Print physical copies
- [ ] Set 3 alarms for hearing day

## Day Of:
- [ ] Arrive 30 minutes early
- [ ] Have case number memorized
- [ ] Bring phone charger
- [ ] Bring water/snacks
`;

  await dc.writeFile({
    path: `${caseFolder}/COURT_PREP_CHECKLIST.md`,
    content: checklist
  });

  console.log(`\n✅ All documents ready in: ${caseFolder}`);
  console.log(`📋 Checklist created`);
}

// Run it
await prepareForCourt('27-CR-25-22797');
```

---

### **Workflow 2: Where's Crow Asset Consolidation**

```javascript
async function consolidateWheresCrow() {
  console.log('🦅 Consolidating Where\'s Crow project files...\n');

  // 1. Find ALL Crow-related files across all drives
  const crowFiles = await dc.search({
    query: "crow OR Where's Crow",
    drives: ['C:', 'D:', 'Google Drive', 'OneDrive'],
    fileTypes: ['txt', 'doc', 'docx', 'pdf', 'png', 'jpg', 'epub']
  });

  console.log(`Found ${crowFiles.length} Crow-related files\n`);

  // 2. Categorize by type
  const categories = {
    'Story_Development/Manuscript/': ['.txt', '.doc', '.docx'],
    'Artwork/': ['.png', '.jpg', '.jpeg', '.gif'],
    'Business_Plan/': ['business', 'plan', 'revenue', 'market'],
    'Unsorted/': []
  };

  for (const file of crowFiles) {
    let destination = 'Documents/07_Creative_Projects/Wheres_Crow_Project/';

    const ext = path.extname(file.path).toLowerCase();
    const filename = path.basename(file.path).toLowerCase();

    // Route by extension
    for (const [folder, extensions] of Object.entries(categories)) {
      if (extensions.includes(ext)) {
        destination += folder;
        break;
      }
      // Route by keyword in filename
      if (extensions.some(keyword => filename.includes(keyword))) {
        destination += folder;
        break;
      }
    }

    if (!destination.includes('/')) {
      destination += 'Unsorted/';
    }

    await dc.moveFile({
      source: file.path,
      destination: `My Drive (mxdmda6@gmail.com)/${destination}`,
      createFolder: true
    });

    console.log(`Moved: ${path.basename(file.path)}`);
    console.log(`   To: ${destination}`);
  }

  console.log('\n✅ Where\'s Crow consolidation complete!');

  // 3. Generate project status report
  const projectFolder = 'Documents/07_Creative_Projects/Wheres_Crow_Project/';
  const stats = await dc.getFolderStats(projectFolder);

  console.log(`\n📊 PROJECT STATUS:`);
  console.log(`Total files: ${stats.fileCount}`);
  console.log(`Total size: ${stats.size}`);
  console.log(`Last modified: ${stats.lastModified}`);
}

await consolidateWheresCrow();
```

---

### **Workflow 3: Monthly Organization Routine**

```javascript
async function monthlyMaintenance() {
  console.log('🗓️ Starting monthly maintenance...\n');

  // 1. Find files not filed properly (still in Unsorted folders)
  const unsortedFolders = [
    'Documents/06_Legal/Unsorted/',
    'Documents/01_Finance/2025/Unsorted/',
    'Documents/03_Medical/2025/Unsorted/',
    'Documents/07_Creative_Projects/Unsorted/'
  ];

  for (const folder of unsortedFolders) {
    const files = await dc.glob(`${folder}*`);
    if (files.length > 0) {
      console.log(`⚠️ ${files.length} files still in: ${folder}`);
    }
  }

  // 2. Archive files older than 6 months
  const oldFiles = await dc.find({
    directory: 'Documents/',
    olderThan: { months: 6 },
    exclude: ['07_Creative_Projects', '06_Legal']  // Don't auto-archive these
  });

  console.log(`\n📦 Found ${oldFiles.length} files ready for archiving`);

  for (const file of oldFiles) {
    const archiveDate = new Date().toISOString().split('T')[0];
    await dc.moveFile({
      source: file,
      destination: `Documents/99_Archive/Auto_Archived_${archiveDate}/`
    });
  }

  // 3. Find and merge duplicate creative files
  const creativeDupes = await dc.findDuplicates({
    directory: 'Documents/07_Creative_Projects/',
    recursive: true
  });

  if (creativeDupes.length > 0) {
    console.log(`\n⚠️ Found ${creativeDupes.length} duplicate groups in creative projects`);
    console.log(`Review these manually before deleting`);
  }

  // 4. Generate storage report
  const storageReport = await dc.getStorageReport('Documents/');

  console.log(`\n💾 STORAGE REPORT:`);
  Object.entries(storageReport).forEach(([category, size]) => {
    console.log(`${category}: ${size}`);
  });

  console.log('\n✅ Monthly maintenance complete!');
}

// Schedule for first day of every month
dc.schedule({
  task: monthlyMaintenance,
  cron: '0 9 1 * *'  // 9 AM on the 1st of each month
});
```

---

## 🎓 LEARN BY DOING: 30-DAY CHALLENGE

### **Week 1: Basics**
- [ ] Day 1: Run glob command to find all PDFs
- [ ] Day 2: Search for specific keywords in files
- [ ] Day 3: Move 10 files to organized folders
- [ ] Day 4: Rename 5 files with standard format
- [ ] Day 5: Find duplicate files
- [ ] Day 6: Create your first snapshot backup
- [ ] Day 7: Review and celebrate progress

### **Week 2: Intermediate**
- [ ] Day 8: Audit Google Drive folders
- [ ] Day 9: Consolidate one duplicate folder pair
- [ ] Day 10: Set up OneDrive → Google Drive migration
- [ ] Day 11: Create custom categorization script
- [ ] Day 12: Organize Downloads folder
- [ ] Day 13: Clean Desktop using automation
- [ ] Day 14: Review and optimize scripts

### **Week 3: Advanced**
- [ ] Day 15: Build court document preparation workflow
- [ ] Day 16: Create Where's Crow consolidation script
- [ ] Day 17: Set up daily auto-organization
- [ ] Day 18: Implement smart document scanner
- [ ] Day 19: Schedule automated backups
- [ ] Day 20: Create project snapshot system
- [ ] Day 21: Review all automations

### **Week 4: Mastery**
- [ ] Day 22: Build monthly maintenance routine
- [ ] Day 23: Create custom Dashboard
- [ ] Day 24: Integrate with Google Calendar
- [ ] Day 25: Set up notification system
- [ ] Day 26: Fine-tune all scripts
- [ ] Day 27: Document your custom workflows
- [ ] Day 28: Teach someone else what you learned
- [ ] Day 29: Celebrate your mastery
- [ ] Day 30: Plan next automation projects

---

## 🆘 TROUBLESHOOTING

**Command not working?**
- Check syntax (case-sensitive!)
- Verify paths exist
- Use `console.log()` to debug
- Check Desktop Commander console for errors

**File not found?**
- Use absolute paths
- Check drive letter is correct
- Verify file still exists
- Try glob pattern to find it

**Permission errors?**
- Run Desktop Commander as Administrator
- Check file/folder isn't locked by another program
- Verify you have write access

**Automation not running?**
- Check cron schedule format
- Verify Desktop Commander is running
- Check system time zone
- Review logs for errors

---

## 🎯 NEXT STEPS

**After mastering these tutorials:**

1. **Create Your Own Workflows**
   - What repetitive tasks do you do daily?
   - Can Desktop Commander automate them?
   - Write custom scripts for your needs

2. **Join the Community**
   - Share your scripts
   - Learn from others
   - Contribute improvements

3. **Keep Exploring**
   - Desktop Commander has many more features
   - Try integrations with other tools
   - Build increasingly complex automations

---

**Remember:** The best automation is the one you actually use.

**Start small. Build momentum. Automate everything. ⚂**
