# MXD-MDA Integration Guide
## Alchemical Transmedia Production Pipeline

*Version 1.0 - MVP Foundation*

---

## 📖 Overview

This guide provides step-by-step instructions for integrating content across the MXD-MDA production pipeline, from initial Markdown drafts through InDesign layout, EPUB validation, AR marker integration, and AI-powered story generation.

---

## 🔄 Markdown → InDesign Workflow

### Step 1: Markdown Authoring
**Creating Story Content**

1. **File Structure:**
   ```
   content/
   ├── chapters/
   │   ├── 01-calcination.md
   │   ├── 02-dissolution.md
   │   └── ...
   ├── meta/
   │   └── metadata.yaml
   └── assets/
       ├── images/
       └── fonts/
   ```

2. **Markdown Conventions:**
   - TODO: Define heading hierarchy (# = Chapter, ## = Section, etc.)
   - TODO: Image reference syntax
   - TODO: Special formatting markers for InDesign import
   - TODO: Metadata frontmatter format

### Step 2: Conversion to InDesign
**Using Pandoc and IDML**

1. **Run Conversion Script:**
   ```bash
   ./scripts/convert-markdown-to-indesign.sh chapters/01-calcination.md
   ```

2. **Manual InDesign Refinement:**
   - TODO: Import IDML into InDesign template
   - TODO: Apply character and paragraph styles
   - TODO: Position images and adjust layout
   - TODO: Add AR markers and QR codes
   - TODO: Review page breaks and widow/orphan control

3. **Quality Checks:**
   - [ ] Verify all styles applied correctly
   - [ ] Check image resolution and placement
   - [ ] Validate AR marker visibility
   - [ ] Proof-read formatted text
   - [ ] Test interactive elements

### Step 3: Export for Distribution
**Multi-Format Output**

- **Print PDF:**
  - TODO: Export preset (bleed, crop marks, color profile)
  - TODO: Preflight checklist
  
- **EPUB3:**
  - TODO: Export settings for reflowable EPUB
  - TODO: Fixed-layout considerations (if applicable)
  
- **KDP Package:**
  - TODO: Specific requirements for Amazon

---

## ✅ EPUB3 Validation Checklist

### Pre-Validation Setup
- [ ] EPUB3 file generated from InDesign or Pandoc
- [ ] EPUBCheck 5.1.0+ installed locally or via CI
- [ ] Test file(s) placed in `docs/` or `artifacts/` directory

### Validation Process

1. **Local Validation:**
   ```bash
   ./scripts/validate-epub.sh
   ```

2. **CI/CD Validation:**
   - Automatic validation on PR via GitHub Actions
   - Check `.github/workflows/epub-validation.yml` status

3. **Common Validation Errors:**
   - TODO: Document typical issues and fixes
   - TODO: Metadata requirements
   - TODO: Navigation document structure
   - TODO: Accessibility requirements (alt text, semantic markup)

### Post-Validation Actions
- [ ] Fix any errors identified by EPUBCheck
- [ ] Re-run validation until clean pass
- [ ] Test EPUB in multiple readers (Calibre, iBooks, Kindle Previewer)
- [ ] Verify accessibility features

---

## 🎯 AR Marker Workflow

### QR Code Generation
**Linking Physical and Digital Experiences**

1. **Define QR Code Targets:**
   - TODO: List of landing pages/AR experiences
   - TODO: URL structure with tracking parameters
   - Example: `${PUBLIC_SITE_URL}/ar/chapter-1?marker=calcination`

2. **Generate QR Codes:**
   - Tool: TODO (qrencode, online generator, custom script)
   - Specifications:
     - TODO: Error correction level (L, M, Q, H)
     - TODO: Output format (SVG, PNG)
     - TODO: Size and resolution for print

3. **Visual Integration:**
   - TODO: QR code placement in layouts
   - TODO: Branding and customization
   - TODO: Accessibility labels

### AR Overlay Triggers
**Image Recognition and Geolocation**

1. **Image Recognition Setup:**
   - TODO: Define target images (book covers, specific illustrations)
   - TODO: AR provider configuration (8th Wall, Vuforia, etc.)
   - TODO: Overlay content (3D models, videos, animations)

2. **Geolocation-Based Triggers (Optional):**
   - TODO: Define trigger locations
   - TODO: Privacy and permission handling
   - TODO: Fallback for users without location access

3. **Testing AR Experiences:**
   - [ ] Test QR codes in print and digital formats
   - [ ] Verify image recognition accuracy
   - [ ] Check overlay content rendering
   - [ ] Test on multiple devices (iOS, Android)

---

## 🤖 AI Agent API Integration

### FastAPI Endpoint Structure
**Server-Side Story Generation**

1. **Base Configuration:**
   ```
   FASTAPI_BASE_URL=http://localhost:8000
   ```

2. **Available Endpoints:**
   - TODO: `POST /generate/story` - Generate narrative based on alchemical stage
   - TODO: `POST /refine/dialogue` - Improve character dialogue
   - TODO: `GET /analyze/consistency` - Check plot consistency
   - TODO: Authentication and rate limiting details

3. **Gemini API Integration:**
   - API Key: Set `GEMINI_API_KEY` in .env
   - TODO: Prompt engineering guidelines
   - TODO: Response parsing and formatting
   - TODO: Error handling and fallbacks

### Web Tool Integration
**Alchemical Story Architect**

1. **Client-Side Setup:**
   - Open `web/alchemical-story-architect.html`
   - Currently stubbed - no live API calls in MVP

2. **Future Integration Steps:**
   - TODO: Add authentication flow
   - TODO: Connect to FastAPI backend
   - TODO: Handle API responses and errors
   - TODO: Save generated content locally or to backend

---

## 🧪 Integration Testing: Test Chapter Workflow

### Complete Pipeline Test

**Goal:** Validate the entire workflow from Markdown to published EPUB with AR markers

1. **Prepare Test Content:**
   - [ ] Create test chapter Markdown file (1-2 pages)
   - [ ] Include sample metadata
   - [ ] Add placeholder image reference

2. **Execute Conversion:**
   - [ ] Run `convert-markdown-to-indesign.sh`
   - [ ] Import into InDesign template
   - [ ] Apply basic styling

3. **Add AR Elements:**
   - [ ] Generate test QR code
   - [ ] Place QR code in InDesign layout
   - [ ] Note AR trigger specifications

4. **Export and Validate:**
   - [ ] Export EPUB3 from InDesign
   - [ ] Run `validate-epub.sh`
   - [ ] Fix any validation errors
   - [ ] Confirm EPUB displays correctly in reader

5. **AI Story Generation Test:**
   - [ ] Open Story Architect web tool
   - [ ] Select test alchemical stage
   - [ ] Generate sample prompt
   - [ ] Export Markdown output
   - [ ] (Future) Integrate with FastAPI endpoint

6. **Document Results:**
   - [ ] Note any issues or blockers
   - [ ] Record time taken for each step
   - [ ] Identify areas for automation
   - [ ] Update this guide with learnings

---

## 🛠️ Required Tools and Dependencies

### Software Requirements
- **Pandoc:** Markdown conversion (v2.19+)
- **Adobe InDesign:** Layout and design (2024+)
- **EPUBCheck:** EPUB validation (5.1.0+)
- **Java:** Runtime for EPUBCheck (v17+)
- **Python:** Scripts and automation (3.10+)
- **Node.js:** Web tools and build processes (18+)

### Installation Guides
- TODO: Provide installation instructions for each tool
- TODO: Platform-specific notes (macOS, Windows, Linux)
- TODO: Docker containerization option

---

## 📊 Quality Metrics

### Production KPIs
- TODO: Time from Markdown draft to validated EPUB
- TODO: Validation error rate
- TODO: AR marker engagement rates
- TODO: AI-generated content usage

### Quality Standards
- TODO: Define acceptable validation error threshold
- TODO: Accessibility compliance requirements
- TODO: Cross-platform compatibility targets

---

## 🚨 Troubleshooting

### Common Issues

**Markdown Conversion Problems:**
- TODO: Document common Pandoc errors
- TODO: Character encoding issues
- TODO: Image path resolution

**EPUB Validation Failures:**
- TODO: Missing metadata fields
- TODO: Invalid HTML structure
- TODO: Accessibility errors

**AR Integration Challenges:**
- TODO: QR code scanning issues
- TODO: AR overlay not triggering
- TODO: Device compatibility

**API Connection Issues:**
- TODO: Environment variable configuration
- TODO: CORS and authentication errors
- TODO: Rate limiting and throttling

---

## 📖 Additional Resources

- **Pandoc Documentation:** https://pandoc.org/MANUAL.html
- **EPUB3 Specification:** https://www.w3.org/TR/epub-33/
- **EPUBCheck:** https://github.com/w3c/epubcheck
- **InDesign Scripting:** TODO: Link to resources
- **AR Development:** TODO: Link to AR provider docs

---

## 🔄 Document Status

**Current Version:** 1.0 - MVP Skeleton  
**Last Updated:** 2025-11-03  
**Status:** 🚧 In Development - Awaiting team input and first test run

**Next Steps:**
1. Complete first test chapter workflow
2. Document actual tool versions and configurations
3. Create video walkthrough of integration process
4. Build automation scripts for repetitive tasks
5. Establish SLAs for each pipeline stage

---

*"Integration is not merely connection—it is the conscious transmutation of separate elements into a unified whole."*
