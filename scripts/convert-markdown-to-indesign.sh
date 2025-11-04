#!/usr/bin/env bash
#
# convert-markdown-to-indesign.sh
# Converts Markdown files to IDML format for Adobe InDesign import
#
# USAGE: ./scripts/convert-markdown-to-indesign.sh <input.md> [output.idml]
#
# NOTE: This is a stub script for the MVP. Full implementation requires:
#   - Pandoc installation with IDML support
#   - Custom Pandoc filters for InDesign styles
#   - Template IDML file with predefined styles
#
# TODO: Install and configure required tools before production use

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Script configuration
SCRIPT_NAME=$(basename "$0")
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$SCRIPT_DIR")"

# Display usage information
usage() {
    cat <<EOF
Usage: $SCRIPT_NAME <input.md> [output.idml]

Converts Markdown files to IDML format for Adobe InDesign import.

Arguments:
    input.md     Path to input Markdown file
    output.idml  Optional output IDML file path (defaults to input name with .idml extension)

Example:
    $SCRIPT_NAME chapters/01-calcination.md
    $SCRIPT_NAME chapters/01-calcination.md output/chapter-01.idml

EOF
    exit 1
}

# Safety checks
safety_checks() {
    echo -e "${YELLOW}Running safety checks...${NC}"
    
    # Check if input file is provided
    if [ $# -eq 0 ]; then
        echo -e "${RED}Error: No input file specified${NC}"
        usage
    fi
    
    # Check if input file exists
    if [ ! -f "$1" ]; then
        echo -e "${RED}Error: Input file '$1' not found${NC}"
        exit 1
    fi
    
    # Check if input file is readable
    if [ ! -r "$1" ]; then
        echo -e "${RED}Error: Input file '$1' is not readable${NC}"
        exit 1
    fi
    
    # Verify it's a Markdown file (basic check)
    if [[ ! "$1" =~ \.(md|markdown)$ ]]; then
        echo -e "${YELLOW}Warning: Input file does not have .md or .markdown extension${NC}"
        read -p "Continue anyway? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo "Cancelled by user"
            exit 0
        fi
    fi
    
    echo -e "${GREEN}✓ Safety checks passed${NC}\n"
}

# Main conversion function (currently stubbed)
convert_markdown_to_idml() {
    local input_file="$1"
    local output_file="${2:-${input_file%.md}.idml}"
    
    echo "=========================================="
    echo "Markdown to InDesign IDML Conversion"
    echo "=========================================="
    echo "Input:  $input_file"
    echo "Output: $output_file"
    echo ""
    
    # TODO: Check for Pandoc installation
    echo -e "${YELLOW}Checking for required tools...${NC}"
    if ! command -v pandoc &> /dev/null; then
        echo -e "${RED}✗ Pandoc is not installed${NC}"
        echo "  Install Pandoc: https://pandoc.org/installing.html"
        echo "  Recommended: pandoc version 2.19 or later"
        exit 1
    else
        echo -e "${GREEN}✓ Pandoc found: $(pandoc --version | head -n1)${NC}"
    fi
    
    # TODO: Check for IDML support in Pandoc
    echo -e "${YELLOW}Checking Pandoc IDML support...${NC}"
    if pandoc --list-output-formats | grep -q "idml"; then
        echo -e "${GREEN}✓ IDML output format supported${NC}"
    else
        echo -e "${RED}✗ IDML output format not supported in this Pandoc installation${NC}"
        echo "  Note: IDML support may require custom Pandoc build or extensions"
        echo "  Alternative: Convert to .docx first, then import to InDesign"
    fi
    
    # TODO: Conversion pipeline (commented out until tools are configured)
    echo ""
    echo -e "${YELLOW}Conversion pipeline (STUBBED - implementation pending):${NC}"
    echo "  1. Parse Markdown with metadata extraction"
    echo "  2. Apply custom Pandoc filters for InDesign styles"
    echo "  3. Generate IDML with template integration"
    echo "  4. Validate IDML structure"
    echo "  5. Output file ready for InDesign import"
    echo ""
    
    # Placeholder: Show what would be executed
    echo -e "${YELLOW}Would execute:${NC}"
    echo "  pandoc \"$input_file\" \\"
    echo "    --from markdown+smart \\"
    echo "    --to idml \\"
    echo "    --template=\"templates/indesign-template.idml\" \\"
    echo "    --lua-filter=\"filters/indesign-styles.lua\" \\"
    echo "    --output=\"$output_file\""
    echo ""
    
    # For MVP: Suggest manual workaround
    echo -e "${GREEN}Manual workaround for MVP:${NC}"
    echo "  1. Convert to .docx: pandoc \"$input_file\" -o \"${input_file%.md}.docx\""
    echo "  2. Import .docx into InDesign"
    echo "  3. Apply paragraph and character styles manually"
    echo "  4. Add AR markers and finalize layout"
    echo ""
    
    # TODO: Actual conversion command (uncomment when tools are ready)
    # pandoc "$input_file" \
    #     --from markdown+smart \
    #     --to idml \
    #     --template="$PROJECT_ROOT/templates/indesign-template.idml" \
    #     --lua-filter="$PROJECT_ROOT/filters/indesign-styles.lua" \
    #     --output="$output_file"
    
    # TODO: Post-processing validation
    # echo -e "${GREEN}✓ Conversion complete: $output_file${NC}"
    
    echo -e "${YELLOW}⚠ MVP Status: Manual conversion required${NC}"
    echo "This script will be fully automated in a future sprint."
}

# Main execution
main() {
    safety_checks "$@"
    convert_markdown_to_idml "$@"
}

main "$@"
