#!/bin/bash

# PROJECT GEM - Automated Google Drive Setup Script
# For Mac and Linux
# Created: November 1, 2025

set -e  # Exit on error

echo "================================================"
echo "  PROJECT GEM - Google Drive Organization Setup"
echo "================================================"
echo ""

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Function to detect Google Drive path
detect_google_drive() {
    echo "🔍 Detecting Google Drive Desktop location..."

    # Common Google Drive paths
    POSSIBLE_PATHS=(
        "$HOME/Google Drive/My Drive"
        "$HOME/GoogleDrive/My Drive"
        "$HOME/Google Drive"
        "$HOME/GoogleDrive"
        "/Volumes/GoogleDrive"
    )

    for path in "${POSSIBLE_PATHS[@]}"; do
        if [ -d "$path" ]; then
            echo -e "${GREEN}✅ Found Google Drive at: $path${NC}"
            GDRIVE_PATH="$path"
            return 0
        fi
    done

    return 1
}

# Function to create folder structure
create_structure() {
    local BASE_PATH="$1"

    echo ""
    echo "📁 Creating Project GEM folder structure..."
    echo "   Location: $BASE_PATH"
    echo ""

    # Create all directories
    mkdir -p "$BASE_PATH/Documents/01_Finance/2025"/{Bank_Statements,Credit_Cards,Receipts_Taxes,Pay_Stubs}
    mkdir -p "$BASE_PATH/Documents/01_Finance"/{Investments,Taxes,Debt_Collection}

    mkdir -p "$BASE_PATH/Documents/02_Personal"/{Identification,Education,Journal_Entries,Family_Records,Social_Security,Fitness_and_Health}

    mkdir -p "$BASE_PATH/Documents/03_Medical/2025"/{EOBs_Insurance,Lab_Results,Doctor_Visits}
    mkdir -p "$BASE_PATH/Documents/03_Medical"/{Medical_History,Provider_Information}

    mkdir -p "$BASE_PATH/Documents/04_Household"/{Auto,Mortgage_or_Lease,Utilities,Manuals_Warranties,Assistance}

    mkdir -p "$BASE_PATH/Documents/05_Work"/{Contracts,Resume_CV,Projects}

    mkdir -p "$BASE_PATH/Documents/06_Legal"/{Court_Case_27-CR-25-22797,OFP_Case_27DAFA24-5203,Court_Case_27-CO-25-4917}

    mkdir -p "$BASE_PATH/Documents/07_Creative_Projects/MXD-MDA_Brand"/{Brand_Guide,Marketing,Content,Assets}
    mkdir -p "$BASE_PATH/Documents/07_Creative_Projects/Wheres_Crow_Project"/{Business_Plan,Artwork,Story_Development}
    mkdir -p "$BASE_PATH/Documents/07_Creative_Projects/Alchemical_Nexus"/{Book_of_Skretz,MVP_Development,Research}

    mkdir -p "$BASE_PATH/Documents/99_Archive"/{Old_Projects,Web_Saves,Deprecated_Files}

    echo -e "${GREEN}✅ All 57 folders created successfully!${NC}"
}

# Function to create .gitkeep files (keeps empty folders in sync)
create_gitkeep_files() {
    local BASE_PATH="$1"
    echo ""
    echo "📌 Creating .gitkeep files to preserve empty folders..."
    find "$BASE_PATH/Documents" -type d -exec touch {}/.gitkeep \;
    echo -e "${GREEN}✅ .gitkeep files created${NC}"
}

# Function to count folders
count_folders() {
    local BASE_PATH="$1"
    local COUNT=$(find "$BASE_PATH/Documents" -type d | wc -l)
    echo -e "${GREEN}📊 Total folders created: $COUNT${NC}"
}

# Main execution
echo "This script will set up the complete Project GEM folder structure"
echo "in your Google Drive Desktop folder."
echo ""

# Try to detect Google Drive
if detect_google_drive; then
    echo ""
    echo -e "${YELLOW}📍 Detected Google Drive location:${NC}"
    echo "   $GDRIVE_PATH"
    echo ""
    read -p "Is this correct? (y/n): " -n 1 -r
    echo ""

    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo ""
        echo "Please enter the full path to your Google Drive folder:"
        read -r GDRIVE_PATH

        if [ ! -d "$GDRIVE_PATH" ]; then
            echo -e "${RED}❌ Error: Directory does not exist: $GDRIVE_PATH${NC}"
            exit 1
        fi
    fi
else
    echo -e "${YELLOW}⚠️  Could not automatically detect Google Drive${NC}"
    echo ""
    echo "Please enter the full path to your Google Drive folder:"
    echo "Common locations:"
    echo "  • macOS: /Users/[YourName]/Google Drive/My Drive"
    echo "  • Linux: /home/[YourName]/Google Drive"
    echo ""
    read -r GDRIVE_PATH

    if [ ! -d "$GDRIVE_PATH" ]; then
        echo -e "${RED}❌ Error: Directory does not exist: $GDRIVE_PATH${NC}"
        exit 1
    fi
fi

# Check if Documents folder already exists
if [ -d "$GDRIVE_PATH/Documents" ]; then
    echo ""
    echo -e "${YELLOW}⚠️  Warning: 'Documents' folder already exists!${NC}"
    echo ""
    echo "Options:"
    echo "  1) Merge with existing (recommended - won't overwrite files)"
    echo "  2) Rename existing to 'Documents_OLD' and create fresh"
    echo "  3) Cancel and exit"
    echo ""
    read -p "Choose option (1/2/3): " -n 1 -r
    echo ""

    case $REPLY in
        1)
            echo "Merging with existing structure..."
            ;;
        2)
            echo "Renaming existing to Documents_OLD..."
            mv "$GDRIVE_PATH/Documents" "$GDRIVE_PATH/Documents_OLD_$(date +%Y%m%d_%H%M%S)"
            ;;
        3)
            echo "Exiting..."
            exit 0
            ;;
        *)
            echo "Invalid option. Exiting..."
            exit 1
            ;;
    esac
fi

# Create the structure
echo ""
echo "🚀 Starting creation process..."
echo ""

create_structure "$GDRIVE_PATH"
create_gitkeep_files "$GDRIVE_PATH"
count_folders "$GDRIVE_PATH"

echo ""
echo "================================================"
echo -e "${GREEN}✨ SUCCESS! Project GEM structure deployed!${NC}"
echo "================================================"
echo ""
echo "📂 Your folders are now syncing to Google Drive cloud"
echo ""
echo "Next steps:"
echo "  1. Wait for Google Drive to finish syncing (check status icon)"
echo "  2. Open Google Drive in browser to verify folders appear"
echo "  3. Start uploading documents to appropriate folders"
echo "  4. See MIGRATION_GUIDE.md for help organizing existing files"
echo ""
echo "🎯 Priority folders to populate first:"
echo "   • 06_Legal/ - Court documents (URGENT - Oct 22 & Dec 2 deadlines)"
echo "   • 01_Finance/Debt_Collection/ - LVNV and collection notices"
echo "   • 02_Personal/Social_Security/ - SSA denial and appeals"
echo "   • 03_Medical/ - Recent medical records and insurance info"
echo ""
echo "💡 Pro tip: Bookmark the Documents folder in your browser for quick access!"
echo ""
echo -e "${GREEN}You've got this! 🚀${NC}"
echo ""
