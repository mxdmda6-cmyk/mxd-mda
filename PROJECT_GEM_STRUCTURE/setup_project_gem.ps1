# PROJECT GEM - Automated Google Drive Setup Script
# For Windows (PowerShell)
# Created: November 1, 2025

Write-Host "================================================" -ForegroundColor Cyan
Write-Host "  PROJECT GEM - Google Drive Organization Setup" -ForegroundColor Cyan
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""

# Function to detect Google Drive path
function Find-GoogleDrive {
    Write-Host "🔍 Detecting Google Drive Desktop location..." -ForegroundColor Yellow

    $possiblePaths = @(
        "$env:USERPROFILE\Google Drive\My Drive",
        "$env:USERPROFILE\GoogleDrive\My Drive",
        "$env:USERPROFILE\Google Drive",
        "$env:USERPROFILE\GoogleDrive",
        "G:\My Drive",
        "G:\"
    )

    foreach ($path in $possiblePaths) {
        if (Test-Path $path) {
            Write-Host "✅ Found Google Drive at: $path" -ForegroundColor Green
            return $path
        }
    }

    return $null
}

# Function to create folder structure
function New-ProjectGemStructure {
    param(
        [string]$BasePath
    )

    Write-Host ""
    Write-Host "📁 Creating Project GEM folder structure..." -ForegroundColor Yellow
    Write-Host "   Location: $BasePath" -ForegroundColor Gray
    Write-Host ""

    $folders = @(
        # Finance
        "Documents\01_Finance\2025\Bank_Statements",
        "Documents\01_Finance\2025\Credit_Cards",
        "Documents\01_Finance\2025\Receipts_Taxes",
        "Documents\01_Finance\2025\Pay_Stubs",
        "Documents\01_Finance\Investments",
        "Documents\01_Finance\Taxes",
        "Documents\01_Finance\Debt_Collection",

        # Personal
        "Documents\02_Personal\Identification",
        "Documents\02_Personal\Education",
        "Documents\02_Personal\Journal_Entries",
        "Documents\02_Personal\Family_Records",
        "Documents\02_Personal\Social_Security",
        "Documents\02_Personal\Fitness_and_Health",

        # Medical
        "Documents\03_Medical\2025\EOBs_Insurance",
        "Documents\03_Medical\2025\Lab_Results",
        "Documents\03_Medical\2025\Doctor_Visits",
        "Documents\03_Medical\Medical_History",
        "Documents\03_Medical\Provider_Information",

        # Household
        "Documents\04_Household\Auto",
        "Documents\04_Household\Mortgage_or_Lease",
        "Documents\04_Household\Utilities",
        "Documents\04_Household\Manuals_Warranties",
        "Documents\04_Household\Assistance",

        # Work
        "Documents\05_Work\Contracts",
        "Documents\05_Work\Resume_CV",
        "Documents\05_Work\Projects",

        # Legal
        "Documents\06_Legal\Court_Case_27-CR-25-22797",
        "Documents\06_Legal\OFP_Case_27DAFA24-5203",
        "Documents\06_Legal\Court_Case_27-CO-25-4917",

        # Creative Projects
        "Documents\07_Creative_Projects\MXD-MDA_Brand\Brand_Guide",
        "Documents\07_Creative_Projects\MXD-MDA_Brand\Marketing",
        "Documents\07_Creative_Projects\MXD-MDA_Brand\Content",
        "Documents\07_Creative_Projects\MXD-MDA_Brand\Assets",
        "Documents\07_Creative_Projects\Wheres_Crow_Project\Business_Plan",
        "Documents\07_Creative_Projects\Wheres_Crow_Project\Artwork",
        "Documents\07_Creative_Projects\Wheres_Crow_Project\Story_Development",
        "Documents\07_Creative_Projects\Alchemical_Nexus\Book_of_Skretz",
        "Documents\07_Creative_Projects\Alchemical_Nexus\MVP_Development",
        "Documents\07_Creative_Projects\Alchemical_Nexus\Research",

        # Archive
        "Documents\99_Archive\Old_Projects",
        "Documents\99_Archive\Web_Saves",
        "Documents\99_Archive\Deprecated_Files"
    )

    $createdCount = 0
    foreach ($folder in $folders) {
        $fullPath = Join-Path $BasePath $folder
        if (-not (Test-Path $fullPath)) {
            New-Item -Path $fullPath -ItemType Directory -Force | Out-Null
            $createdCount++
        }
    }

    Write-Host "✅ Created $createdCount new folders!" -ForegroundColor Green
}

# Function to create placeholder files
function New-PlaceholderFiles {
    param(
        [string]$BasePath
    )

    Write-Host ""
    Write-Host "📌 Creating placeholder files to preserve empty folders..." -ForegroundColor Yellow

    Get-ChildItem -Path "$BasePath\Documents" -Recurse -Directory | ForEach-Object {
        $placeholderPath = Join-Path $_.FullName ".gitkeep"
        if (-not (Test-Path $placeholderPath)) {
            New-Item -Path $placeholderPath -ItemType File -Force | Out-Null
        }
    }

    Write-Host "✅ Placeholder files created" -ForegroundColor Green
}

# Main execution
Write-Host "This script will set up the complete Project GEM folder structure"
Write-Host "in your Google Drive Desktop folder."
Write-Host ""

# Try to detect Google Drive
$gdrivePath = Find-GoogleDrive

if ($gdrivePath) {
    Write-Host ""
    Write-Host "📍 Detected Google Drive location:" -ForegroundColor Yellow
    Write-Host "   $gdrivePath" -ForegroundColor Gray
    Write-Host ""

    $confirm = Read-Host "Is this correct? (Y/N)"

    if ($confirm -ne "Y" -and $confirm -ne "y") {
        Write-Host ""
        Write-Host "Please enter the full path to your Google Drive folder:"
        $gdrivePath = Read-Host

        if (-not (Test-Path $gdrivePath)) {
            Write-Host "❌ Error: Directory does not exist: $gdrivePath" -ForegroundColor Red
            exit 1
        }
    }
} else {
    Write-Host "⚠️  Could not automatically detect Google Drive" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Please enter the full path to your Google Drive folder:"
    Write-Host "Common location: C:\Users\YourName\Google Drive\My Drive" -ForegroundColor Gray
    Write-Host ""
    $gdrivePath = Read-Host

    if (-not (Test-Path $gdrivePath)) {
        Write-Host "❌ Error: Directory does not exist: $gdrivePath" -ForegroundColor Red
        exit 1
    }
}

# Check if Documents folder already exists
$documentsPath = Join-Path $gdrivePath "Documents"

if (Test-Path $documentsPath) {
    Write-Host ""
    Write-Host "⚠️  Warning: 'Documents' folder already exists!" -ForegroundColor Yellow
    Write-Host ""
    Write-Host "Options:"
    Write-Host "  1) Merge with existing (recommended - won't overwrite files)"
    Write-Host "  2) Rename existing to 'Documents_OLD' and create fresh"
    Write-Host "  3) Cancel and exit"
    Write-Host ""
    $choice = Read-Host "Choose option (1/2/3)"

    switch ($choice) {
        "1" {
            Write-Host "Merging with existing structure..." -ForegroundColor Yellow
        }
        "2" {
            $timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
            $newName = "Documents_OLD_$timestamp"
            Write-Host "Renaming existing to $newName..." -ForegroundColor Yellow
            Rename-Item -Path $documentsPath -NewName $newName
        }
        "3" {
            Write-Host "Exiting..." -ForegroundColor Gray
            exit 0
        }
        default {
            Write-Host "Invalid option. Exiting..." -ForegroundColor Red
            exit 1
        }
    }
}

# Create the structure
Write-Host ""
Write-Host "🚀 Starting creation process..." -ForegroundColor Cyan
Write-Host ""

New-ProjectGemStructure -BasePath $gdrivePath
New-PlaceholderFiles -BasePath $gdrivePath

# Count total folders
$totalFolders = (Get-ChildItem -Path "$gdrivePath\Documents" -Recurse -Directory).Count
Write-Host ""
Write-Host "📊 Total folders: $totalFolders" -ForegroundColor Green

Write-Host ""
Write-Host "================================================" -ForegroundColor Cyan
Write-Host "✨ SUCCESS! Project GEM structure deployed!" -ForegroundColor Green
Write-Host "================================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📂 Your folders are now syncing to Google Drive cloud"
Write-Host ""
Write-Host "Next steps:"
Write-Host "  1. Check Google Drive sync status (system tray icon)" -ForegroundColor Yellow
Write-Host "  2. Open Google Drive in browser to verify folders appear" -ForegroundColor Yellow
Write-Host "  3. Start uploading documents to appropriate folders" -ForegroundColor Yellow
Write-Host "  4. See MIGRATION_GUIDE.md for organizing existing files" -ForegroundColor Yellow
Write-Host ""
Write-Host "🎯 Priority folders to populate first:"
Write-Host "   • 06_Legal\ - Court documents (URGENT - Oct 22 & Dec 2 deadlines)" -ForegroundColor Red
Write-Host "   • 01_Finance\Debt_Collection\ - LVNV and collection notices" -ForegroundColor Yellow
Write-Host "   • 02_Personal\Social_Security\ - SSA denial and appeals" -ForegroundColor Yellow
Write-Host "   • 03_Medical\ - Recent medical records and insurance info" -ForegroundColor Yellow
Write-Host ""
Write-Host "💡 Pro tip: Pin the Documents folder to Quick Access in File Explorer!" -ForegroundColor Cyan
Write-Host ""
Write-Host "You've got this! 🚀" -ForegroundColor Green
Write-Host ""

# Open the Documents folder in File Explorer
$openFolder = Read-Host "Open Documents folder in File Explorer? (Y/N)"
if ($openFolder -eq "Y" -or $openFolder -eq "y") {
    Start-Process explorer.exe -ArgumentList $documentsPath
}
