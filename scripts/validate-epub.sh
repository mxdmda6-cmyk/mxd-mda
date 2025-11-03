#!/usr/bin/env bash
#
# validate-epub.sh
# Validates EPUB files using EPUBCheck
#
# USAGE: ./scripts/validate-epub.sh [path/to/file.epub]
#
# If no file is specified, searches for all .epub files in docs/ and artifacts/
# directories and validates them all.

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Script configuration
SCRIPT_NAME=$(basename "$0")
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# EPUBCheck configuration
EPUBCHECK_VERSION="5.1.0"
EPUBCHECK_URL="https://github.com/w3c/epubcheck/releases/download/v${EPUBCHECK_VERSION}/epubcheck-${EPUBCHECK_VERSION}.zip"
EPUBCHECK_DIR="$PROJECT_ROOT/.cache/epubcheck"
EPUBCHECK_JAR="$EPUBCHECK_DIR/epubcheck-${EPUBCHECK_VERSION}/epubcheck.jar"

# Display usage information
usage() {
    cat <<EOF
Usage: $SCRIPT_NAME [path/to/file.epub]

Validates EPUB files using EPUBCheck ${EPUBCHECK_VERSION}.

Options:
    path/to/file.epub  Validate a specific EPUB file
    (no arguments)     Validate all .epub files in docs/ and artifacts/ directories

Examples:
    $SCRIPT_NAME                              # Validate all EPUB files
    $SCRIPT_NAME docs/my-book.epub           # Validate specific file

Environment Variables:
    SKIP_DOWNLOAD=1   Skip EPUBCheck download if already present

EOF
}

# Download EPUBCheck if not present
download_epubcheck() {
    if [ -f "$EPUBCHECK_JAR" ]; then
        echo -e "${GREEN}✓ EPUBCheck found: $EPUBCHECK_JAR${NC}"
        return 0
    fi
    
    if [ "${SKIP_DOWNLOAD:-0}" = "1" ]; then
        echo -e "${RED}✗ EPUBCheck not found and SKIP_DOWNLOAD=1${NC}"
        exit 1
    fi
    
    echo -e "${YELLOW}Downloading EPUBCheck ${EPUBCHECK_VERSION}...${NC}"
    mkdir -p "$EPUBCHECK_DIR"
    
    # Download EPUBCheck
    if command -v wget &> /dev/null; then
        wget -q -O "$EPUBCHECK_DIR/epubcheck.zip" "$EPUBCHECK_URL"
    elif command -v curl &> /dev/null; then
        curl -sL -o "$EPUBCHECK_DIR/epubcheck.zip" "$EPUBCHECK_URL"
    else
        echo -e "${RED}✗ Neither wget nor curl found. Cannot download EPUBCheck.${NC}"
        echo "Please install wget or curl, or manually download EPUBCheck from:"
        echo "$EPUBCHECK_URL"
        exit 1
    fi
    
    # Extract
    echo -e "${YELLOW}Extracting EPUBCheck...${NC}"
    unzip -q "$EPUBCHECK_DIR/epubcheck.zip" -d "$EPUBCHECK_DIR"
    rm "$EPUBCHECK_DIR/epubcheck.zip"
    
    if [ -f "$EPUBCHECK_JAR" ]; then
        echo -e "${GREEN}✓ EPUBCheck downloaded successfully${NC}"
    else
        echo -e "${RED}✗ Failed to extract EPUBCheck${NC}"
        exit 1
    fi
}

# Check Java installation
check_java() {
    if ! command -v java &> /dev/null; then
        echo -e "${RED}✗ Java is not installed${NC}"
        echo "EPUBCheck requires Java 17 or later."
        echo "Install Java from: https://adoptium.net/"
        exit 1
    fi
    
    # Extract major version number (works for both old format "1.8.0" and new format "11.0.1")
    local java_version=$(java -version 2>&1 | head -n1 | cut -d'"' -f2)
    local major_version=$(echo "$java_version" | cut -d'.' -f1)
    
    # Handle old Java versioning (1.x.y format)
    if [ "$major_version" = "1" ]; then
        major_version=$(echo "$java_version" | cut -d'.' -f2)
    fi
    
    if [ "$major_version" -lt 11 ]; then
        echo -e "${YELLOW}⚠ Warning: Java version may be too old (found: $java_version, recommended: 17+)${NC}"
    else
        echo -e "${GREEN}✓ Java found: $(java -version 2>&1 | head -n1)${NC}"
    fi
}

# Validate a single EPUB file
validate_epub_file() {
    local epub_file="$1"
    
    echo ""
    echo "=========================================="
    echo -e "${BLUE}Validating: $epub_file${NC}"
    echo "=========================================="
    
    if [ ! -f "$epub_file" ]; then
        echo -e "${RED}✗ File not found: $epub_file${NC}"
        return 1
    fi
    
    # Run EPUBCheck
    if java -jar "$EPUBCHECK_JAR" "$epub_file"; then
        echo -e "${GREEN}✓ Validation PASSED for $epub_file${NC}"
        return 0
    else
        echo -e "${RED}✗ Validation FAILED for $epub_file${NC}"
        return 1
    fi
}

# Find and validate all EPUB files in specified directories
validate_all_epubs() {
    local search_dirs=("docs" "artifacts")
    local epub_files=()
    local validation_failed=0
    
    echo -e "${YELLOW}Searching for EPUB files...${NC}"
    
    for dir in "${search_dirs[@]}"; do
        if [ -d "$PROJECT_ROOT/$dir" ]; then
            while IFS= read -r -d '' file; do
                epub_files+=("$file")
            done < <(find "$PROJECT_ROOT/$dir" -type f -name "*.epub" -print0 2>/dev/null || true)
        fi
    done
    
    if [ ${#epub_files[@]} -eq 0 ]; then
        echo -e "${YELLOW}No EPUB files found in ${search_dirs[*]}${NC}"
        echo "This is expected if you haven't created any EPUB files yet."
        echo ""
        echo "To test this script, place .epub files in:"
        echo "  - $PROJECT_ROOT/docs/"
        echo "  - $PROJECT_ROOT/artifacts/"
        exit 0
    fi
    
    echo -e "${GREEN}Found ${#epub_files[@]} EPUB file(s)${NC}"
    
    for epub_file in "${epub_files[@]}"; do
        if ! validate_epub_file "$epub_file"; then
            validation_failed=1
        fi
    done
    
    echo ""
    echo "=========================================="
    if [ $validation_failed -eq 0 ]; then
        echo -e "${GREEN}✓ All EPUB files validated successfully!${NC}"
        exit 0
    else
        echo -e "${RED}✗ One or more EPUB files failed validation${NC}"
        echo "Please fix the validation errors and run this script again."
        exit 1
    fi
}

# Main execution
main() {
    echo "=========================================="
    echo "EPUB Validation Script"
    echo "=========================================="
    echo ""
    
    # Check prerequisites
    check_java
    download_epubcheck
    echo ""
    
    # Validate based on arguments
    if [ $# -eq 0 ]; then
        validate_all_epubs
    elif [ "$1" = "-h" ] || [ "$1" = "--help" ]; then
        usage
        exit 0
    else
        # Validate specific file
        if validate_epub_file "$1"; then
            exit 0
        else
            exit 1
        fi
    fi
}

main "$@"
