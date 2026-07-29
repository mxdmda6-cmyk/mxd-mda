"""
llc_forms.py — Generate Minnesota LLC legal documents as PDFs using ReportLab.

Three documents are generated:
  1. Articles of Organization  (Minnesota-specific, MN SOS form equivalent)
  2. Operating Agreement       (standard single/multi-member LLC template)
  3. IRS Form SS-4             (EIN application, pre-filled for review)

All content is driven by the EntityConfig object from config_handler.py.
No raw strings are scattered across the codebase; every template section
lives in its own _section_* helper for easy maintenance.

Output directory:
    Set in config.yaml → output.directory
    Default: ./output/documents/

Dependency:
    pip install reportlab

IMPORTANT:
    Generated PDFs are for REVIEW purposes.  Have a Minnesota-licensed
    attorney verify Articles of Organization before filing.  The SS-4
    must be reviewed before IRS submission — never commit a copy with
    a real SSN filled in.
"""

from __future__ import annotations

import os
from datetime import date
from pathlib import Path
from typing import List

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    HRFlowable,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

from automation.modules.config_handler import EntityConfig, Member

# ── Style constants ──────────────────────────────────────────────────────────

_BASE_STYLES = getSampleStyleSheet()

_STYLE_TITLE = ParagraphStyle(
    "DocTitle",
    parent=_BASE_STYLES["Title"],
    fontSize=16,
    spaceAfter=6,
    alignment=TA_CENTER,
    textColor=colors.HexColor("#1a1a2e"),
)
_STYLE_HEADING = ParagraphStyle(
    "SectionHeading",
    parent=_BASE_STYLES["Heading2"],
    fontSize=12,
    spaceBefore=14,
    spaceAfter=4,
    textColor=colors.HexColor("#16213e"),
)
_STYLE_BODY = ParagraphStyle(
    "Body",
    parent=_BASE_STYLES["Normal"],
    fontSize=10,
    leading=14,
    spaceAfter=6,
    alignment=TA_JUSTIFY,
)
_STYLE_LABEL = ParagraphStyle(
    "FieldLabel",
    parent=_BASE_STYLES["Normal"],
    fontSize=9,
    textColor=colors.grey,
    spaceAfter=2,
)
_STYLE_CENTER = ParagraphStyle(
    "Centered",
    parent=_BASE_STYLES["Normal"],
    fontSize=10,
    alignment=TA_CENTER,
)
_STYLE_FOOTNOTE = ParagraphStyle(
    "Footnote",
    parent=_BASE_STYLES["Normal"],
    fontSize=8,
    textColor=colors.grey,
    alignment=TA_CENTER,
)


# ── Internal helpers ─────────────────────────────────────────────────────────

def _today() -> str:
    return date.today().strftime("%B %d, %Y")


def _hr() -> HRFlowable:
    return HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey, spaceAfter=6)


def _field_block(label: str, value: str) -> List:
    """Return a label + underlined value pair as ReportLab flowables."""
    return [
        Paragraph(label, _STYLE_LABEL),
        Paragraph(f"<u>{value}</u>", _STYLE_BODY),
        Spacer(1, 4),
    ]


def _signature_block(name: str, title: str) -> List:
    """Return a signature line block for one person."""
    return [
        Spacer(1, 24),
        HRFlowable(width=3 * inch, thickness=0.5, color=colors.black, spaceAfter=2),
        Paragraph(name, _STYLE_BODY),
        Paragraph(title, _STYLE_LABEL),
        Spacer(1, 4),
    ]


def _build_doc(output_path: Path, margin_mm: int) -> SimpleDocTemplate:
    m = margin_mm * mm
    return SimpleDocTemplate(
        str(output_path),
        pagesize=letter,
        leftMargin=m,
        rightMargin=m,
        topMargin=m,
        bottomMargin=m,
    )


def _footer_text(entity_name: str, doc_type: str) -> str:
    return f"{entity_name} | {doc_type} | Generated {_today()} — FOR REVIEW ONLY"


# ── 1. Articles of Organization ──────────────────────────────────────────────

def generate_articles_of_organization(cfg: EntityConfig, output_dir: Path) -> Path:
    """
    Generate a Minnesota-style Articles of Organization PDF.

    Minnesota Statutes § 322C.0201 requires:
      - LLC name (must include "LLC" or "Limited Liability Company")
      - Registered office address (physical MN address)
      - Registered agent name
      - Organizer name and address
      - Effective date (if not immediate)

    The generated PDF mirrors the MN SOS online form fields.
    Reference: https://www.sos.state.mn.us/business-liens/business-forms-fees/

    Args:
        cfg:        Parsed EntityConfig from config.yaml.
        output_dir: Directory where the PDF will be saved.

    Returns:
        Path to the generated PDF file.
    """
    output_path = output_dir / f"{cfg.name.replace(' ', '_')}_Articles_of_Organization.pdf"
    doc = _build_doc(output_path, cfg.output.pdf_margin_mm)
    story = []

    # ── Header ────────────────────────────────────────────────────
    story.append(Paragraph("STATE OF MINNESOTA", _STYLE_CENTER))
    story.append(Paragraph("OFFICE OF THE SECRETARY OF STATE", _STYLE_CENTER))
    story.append(Spacer(1, 6))
    story.append(Paragraph("ARTICLES OF ORGANIZATION", _STYLE_TITLE))
    story.append(Paragraph("LIMITED LIABILITY COMPANY", _STYLE_CENTER))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "Minnesota Statutes, Chapter 322C",
        ParagraphStyle("SmallCenter", parent=_STYLE_CENTER, fontSize=9, textColor=colors.grey),
    ))
    story.append(Spacer(1, 12))
    story.append(_hr())

    # ── Article I — Name ──────────────────────────────────────────
    story.append(Paragraph("ARTICLE I — NAME", _STYLE_HEADING))
    story.append(Paragraph(
        "The name of the Limited Liability Company is:",
        _STYLE_BODY,
    ))
    story.extend(_field_block("Legal name of LLC", cfg.name))
    story.append(Paragraph(
        "The name must contain the words 'Limited Liability Company' or the "
        "abbreviation 'L.L.C.' or 'LLC' (Minnesota Statutes § 322C.0108).",
        _STYLE_BODY,
    ))

    # ── Article II — Registered Agent ─────────────────────────────
    story.append(Paragraph("ARTICLE II — REGISTERED OFFICE AND AGENT", _STYLE_HEADING))
    story.append(Paragraph(
        "The LLC designates the following registered agent and registered office "
        "address for service of process in the State of Minnesota:",
        _STYLE_BODY,
    ))
    story.extend(_field_block("Registered Agent Name", cfg.registered_agent.name))
    story.extend(_field_block(
        "Registered Office Address (must be a physical MN address — no P.O. Box)",
        cfg.registered_agent.single_line(),
    ))

    # ── Article III — Principal Office ────────────────────────────
    story.append(Paragraph("ARTICLE III — PRINCIPAL OFFICE", _STYLE_HEADING))
    story.extend(_field_block(
        "Principal Office Address",
        cfg.principal_office.single_line(),
    ))

    # ── Article IV — Management ───────────────────────────────────
    story.append(Paragraph("ARTICLE IV — MANAGEMENT", _STYLE_HEADING))
    management_structure = (
        "member-managed" if len(cfg.members) <= 2 else "manager-managed"
    )
    story.append(Paragraph(
        f"The LLC will be <b>{management_structure}</b>. "
        "All members (or designated managers) have authority to bind the company.",
        _STYLE_BODY,
    ))

    # ── Article V — Members ───────────────────────────────────────
    story.append(Paragraph("ARTICLE V — INITIAL MEMBERS", _STYLE_HEADING))
    member_data = [["Member Name", "Title", "Ownership %", "Address"]]
    for m in cfg.members:
        member_data.append([
            m.name,
            m.title,
            f"{m.ownership_percentage:.0f}%",
            m.address,
        ])
    member_table = Table(member_data, colWidths=[1.6 * inch, 1.4 * inch, 0.9 * inch, 2.8 * inch])
    member_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#1a1a2e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.lightgrey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f5")]),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(member_table)

    # ── Article VI — Duration ─────────────────────────────────────
    story.append(Paragraph("ARTICLE VI — DURATION", _STYLE_HEADING))
    story.append(Paragraph(
        "The LLC shall have a perpetual existence unless dissolved in accordance "
        "with Minnesota Statutes, Chapter 322C.",
        _STYLE_BODY,
    ))

    # ── Article VII — Purpose ─────────────────────────────────────
    story.append(Paragraph("ARTICLE VII — PURPOSE", _STYLE_HEADING))
    story.append(Paragraph(
        "The purpose of the LLC is to engage in any lawful business activity "
        "permitted under the laws of the State of Minnesota.",
        _STYLE_BODY,
    ))

    # ── Organizer Signature ───────────────────────────────────────
    story.append(Spacer(1, 12))
    story.append(_hr())
    story.append(Paragraph("ORGANIZER'S SIGNATURE", _STYLE_HEADING))
    story.append(Paragraph(
        "The undersigned, acting as organizer of the above-named Limited Liability "
        "Company, adopts the foregoing Articles of Organization.",
        _STYLE_BODY,
    ))
    story.extend(_field_block("Date", _today()))
    organizer_name = cfg.organizer.get("name", cfg.members[0].name if cfg.members else "")
    organizer_title = cfg.organizer.get("title", "Organizer")
    story.extend(_signature_block(organizer_name, organizer_title))

    # ── Footer ────────────────────────────────────────────────────
    story.append(Spacer(1, 20))
    story.append(_hr())
    story.append(Paragraph(_footer_text(cfg.name, "Articles of Organization"), _STYLE_FOOTNOTE))
    story.append(Paragraph(
        "IMPORTANT: This document is generated for review. File at "
        "https://www.sos.state.mn.us (fee $155 online). Consult a Minnesota attorney before filing.",
        _STYLE_FOOTNOTE,
    ))

    doc.build(story)
    return output_path


# ── 2. Operating Agreement ───────────────────────────────────────────────────

def generate_operating_agreement(cfg: EntityConfig, output_dir: Path) -> Path:
    """
    Generate a Minnesota LLC Operating Agreement PDF.

    Covers standard provisions for a member-managed LLC:
      - Capital contributions
      - Profit/loss allocation
      - Voting rights
      - Member withdrawal and buyout
      - Dissolution

    Args:
        cfg:        Parsed EntityConfig from config.yaml.
        output_dir: Directory where the PDF will be saved.

    Returns:
        Path to the generated PDF file.
    """
    output_path = output_dir / f"{cfg.name.replace(' ', '_')}_Operating_Agreement.pdf"
    doc = _build_doc(output_path, cfg.output.pdf_margin_mm)
    story = []

    # ── Header ────────────────────────────────────────────────────
    story.append(Paragraph("OPERATING AGREEMENT", _STYLE_TITLE))
    story.append(Paragraph(f"OF {cfg.name.upper()}", _STYLE_CENTER))
    story.append(Paragraph(
        f"A Minnesota Limited Liability Company",
        ParagraphStyle("SmallCenter", parent=_STYLE_CENTER, fontSize=9, textColor=colors.grey),
    ))
    story.append(Spacer(1, 8))
    story.append(_hr())
    story.append(Paragraph(
        f"This Operating Agreement ('Agreement') is entered into as of {_today()}, "
        f"by and among the Members listed herein, for the purpose of forming and "
        f"operating {cfg.name}, a limited liability company organized under the "
        f"laws of the State of Minnesota (Minnesota Statutes, Chapter 322C).",
        _STYLE_BODY,
    ))

    # ── Section 1 — Formation ─────────────────────────────────────
    story.append(Paragraph("SECTION 1 — FORMATION", _STYLE_HEADING))
    story.extend(_field_block("Company Name", cfg.name))
    story.extend(_field_block("State of Formation", cfg.state))
    story.extend(_field_block(
        "Principal Office",
        cfg.principal_office.single_line(),
    ))
    story.extend(_field_block(
        "Registered Agent",
        cfg.registered_agent.single_line(),
    ))

    # ── Section 2 — Members & Ownership ──────────────────────────
    story.append(Paragraph("SECTION 2 — MEMBERS AND OWNERSHIP", _STYLE_HEADING))
    story.append(Paragraph(
        "The initial members of the LLC and their respective ownership interests are:",
        _STYLE_BODY,
    ))
    ownership_data = [
        ["Member Name", "Title", "Ownership Interest", "Initial Contribution"],
    ]
    for m in cfg.members:
        ownership_data.append([
            m.name,
            m.title,
            f"{m.ownership_percentage:.1f}%",
            "As agreed in Schedule A",
        ])
    ownership_table = Table(
        ownership_data,
        colWidths=[1.8 * inch, 1.4 * inch, 1.4 * inch, 2.1 * inch],
    )
    ownership_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#16213e")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 9),
        ("GRID", (0, 0), (-1, -1), 0.3, colors.lightgrey),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#f5f5f5")]),
        ("PADDING", (0, 0), (-1, -1), 5),
    ]))
    story.append(ownership_table)

    # ── Section 3 — Management ────────────────────────────────────
    story.append(Paragraph("SECTION 3 — MANAGEMENT", _STYLE_HEADING))
    managing_members = [m for m in cfg.members if "managing" in m.title.lower()]
    if managing_members:
        mm_names = ", ".join(m.name for m in managing_members)
        story.append(Paragraph(
            f"The LLC shall be managed by its Managing Member(s): <b>{mm_names}</b>. "
            "The Managing Member(s) shall have authority to bind the company, execute "
            "contracts, open bank accounts, and make day-to-day business decisions without "
            "requiring consent of all members.",
            _STYLE_BODY,
        ))
    else:
        story.append(Paragraph(
            "The LLC shall be member-managed. All members shall share equally in "
            "management authority proportional to their ownership interest.",
            _STYLE_BODY,
        ))
    story.append(Paragraph(
        "Major decisions (defined as any single transaction exceeding $10,000, sale of "
        "company assets, admission of new members, or dissolution) require approval by "
        "members holding a majority of ownership interests.",
        _STYLE_BODY,
    ))

    # ── Section 4 — Profits, Losses, Distributions ───────────────
    story.append(Paragraph("SECTION 4 — PROFITS, LOSSES, AND DISTRIBUTIONS", _STYLE_HEADING))
    story.append(Paragraph(
        "Profits and losses of the LLC shall be allocated among the members in "
        "proportion to their respective ownership interests as set forth in Section 2. "
        "Distributions shall be made at such times and in such amounts as determined "
        "by the Managing Member(s), subject to the LLC maintaining adequate reserves.",
        _STYLE_BODY,
    ))

    # ── Section 5 — Books and Records ────────────────────────────
    story.append(Paragraph("SECTION 5 — BOOKS, RECORDS, AND FISCAL YEAR", _STYLE_HEADING))
    story.append(Paragraph(
        f"The fiscal year of the LLC shall end on the last day of "
        f"{cfg.ein_application.fiscal_year_end_month}. The LLC shall maintain complete "
        f"and accurate books of account at its principal office. Each member shall have "
        f"the right to inspect the books upon reasonable notice.",
        _STYLE_BODY,
    ))

    # ── Section 6 — Transfers ─────────────────────────────────────
    story.append(Paragraph("SECTION 6 — TRANSFER OF MEMBERSHIP INTERESTS", _STYLE_HEADING))
    story.append(Paragraph(
        "No member may sell, assign, pledge, or otherwise transfer their membership "
        "interest without the prior written consent of members holding a majority of "
        "ownership interests. Existing members shall have a right of first refusal on "
        "any proposed transfer, exercisable within thirty (30) days of written notice.",
        _STYLE_BODY,
    ))

    # ── Section 7 — Dissolution ───────────────────────────────────
    story.append(Paragraph("SECTION 7 — DISSOLUTION", _STYLE_HEADING))
    story.append(Paragraph(
        "The LLC shall be dissolved upon: (a) the vote of members holding at least "
        "two-thirds (2/3) of all ownership interests; (b) entry of a judicial decree "
        "of dissolution; or (c) any event requiring dissolution under Minnesota Statutes "
        "§ 322C.0701. Upon dissolution, assets shall be distributed per § 322C.0708.",
        _STYLE_BODY,
    ))

    # ── Section 8 — Indemnification ───────────────────────────────
    story.append(Paragraph("SECTION 8 — INDEMNIFICATION", _STYLE_HEADING))
    story.append(Paragraph(
        "The LLC shall indemnify and hold harmless each member and manager from claims "
        "arising out of the conduct of LLC business, to the fullest extent permitted "
        "by Minnesota Statutes § 322C.0408, except for acts of gross negligence, "
        "willful misconduct, or breach of this Agreement.",
        _STYLE_BODY,
    ))

    # ── Section 9 — Amendments ────────────────────────────────────
    story.append(Paragraph("SECTION 9 — AMENDMENTS", _STYLE_HEADING))
    story.append(Paragraph(
        "This Agreement may be amended only by a written instrument signed by members "
        "holding a majority of ownership interests.",
        _STYLE_BODY,
    ))

    # ── Section 10 — Governing Law ────────────────────────────────
    story.append(Paragraph("SECTION 10 — GOVERNING LAW", _STYLE_HEADING))
    story.append(Paragraph(
        "This Agreement shall be governed by and construed in accordance with the "
        "laws of the State of Minnesota, without regard to conflict-of-law principles.",
        _STYLE_BODY,
    ))

    # ── Signature Blocks ──────────────────────────────────────────
    story.append(Spacer(1, 12))
    story.append(_hr())
    story.append(Paragraph("SIGNATURES", _STYLE_HEADING))
    story.append(Paragraph(
        "IN WITNESS WHEREOF, the members have executed this Operating Agreement "
        "as of the date first written above.",
        _STYLE_BODY,
    ))
    for m in cfg.members:
        story.extend(_signature_block(m.name, m.title))
        story.extend(_field_block("Date", "________________"))

    # ── Footer ────────────────────────────────────────────────────
    story.append(Spacer(1, 20))
    story.append(_hr())
    story.append(Paragraph(_footer_text(cfg.name, "Operating Agreement"), _STYLE_FOOTNOTE))
    story.append(Paragraph(
        "IMPORTANT: Have a Minnesota attorney review before all parties sign.",
        _STYLE_FOOTNOTE,
    ))

    doc.build(story)
    return output_path


# ── 3. IRS Form SS-4 (EIN Application) ──────────────────────────────────────

def generate_ss4_application(cfg: EntityConfig, output_dir: Path) -> Path:
    """
    Generate a pre-filled IRS Form SS-4 (Application for EIN) for review.

    This is NOT the official IRS form — it is a plain-text representation
    of SS-4 fields populated from config.yaml.  The fastest way to apply
    for an EIN is online: https://www.irs.gov/businesses/small-businesses-self-employed/
    apply-for-an-employer-identification-number-ein-online

    SSN/ITIN fields are populated with the placeholder from config.yaml
    (default: XXX-XX-XXXX).  NEVER commit a version with a real SSN.

    Args:
        cfg:        Parsed EntityConfig from config.yaml.
        output_dir: Directory where the PDF will be saved.

    Returns:
        Path to the generated PDF file.
    """
    ein = cfg.ein_application
    output_path = output_dir / f"{cfg.name.replace(' ', '_')}_SS4_EIN_Application.pdf"
    doc = _build_doc(output_path, cfg.output.pdf_margin_mm)
    story = []

    # ── Header ────────────────────────────────────────────────────
    story.append(Paragraph("INTERNAL REVENUE SERVICE", _STYLE_CENTER))
    story.append(Paragraph("APPLICATION FOR EMPLOYER IDENTIFICATION NUMBER", _STYLE_TITLE))
    story.append(Paragraph("(IRS Form SS-4) — PRE-FILLED DRAFT FOR REVIEW", _STYLE_CENTER))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "OMB No. 1545-0003  |  Apply online at irs.gov for fastest processing",
        ParagraphStyle("SmallCenter", parent=_STYLE_CENTER, fontSize=8, textColor=colors.grey),
    ))
    story.append(Spacer(1, 8))
    story.append(_hr())

    # ── Line 1 — Legal Name ───────────────────────────────────────
    story.append(Paragraph("PART I — ENTITY IDENTIFICATION", _STYLE_HEADING))
    story.extend(_field_block("Line 1: Legal name of entity", cfg.name))
    story.extend(_field_block("Line 2: Trade name / DBA (if different)", "(none)"))

    # ── Lines 4–6 — Address ───────────────────────────────────────
    story.extend(_field_block(
        "Line 4a: Mailing address — street",
        cfg.principal_office.address,
    ))
    story.extend(_field_block(
        "Line 4b: City, state, ZIP",
        f"{cfg.principal_office.city}, {cfg.principal_office.state} {cfg.principal_office.zip}",
    ))
    story.extend(_field_block("Line 5: County and state where principal business is located",
        f"Ramsey County, {cfg.state}"))

    # ── Line 7 — Responsible Party ────────────────────────────────
    story.append(Paragraph("PART II — RESPONSIBLE PARTY", _STYLE_HEADING))
    story.append(Paragraph(
        "The 'responsible party' is the individual who controls, manages, or directs "
        "the entity and/or the disposition of the entity's funds or assets.",
        _STYLE_BODY,
    ))
    story.extend(_field_block("Line 7a: Responsible party name", ein.responsible_party_name))
    story.extend(_field_block(
        "Line 7b: SSN / ITIN of responsible party",
        ein.responsible_party_ssn,  # placeholder — fill locally before submission
    ))
    story.append(Paragraph(
        "⚠  The SSN/ITIN above is a placeholder. Fill it in your local, "
        ".gitignored copy of this config before submitting. Never commit a real SSN.",
        ParagraphStyle(
            "Warning", parent=_STYLE_BODY, textColor=colors.HexColor("#c0392b"), fontSize=9
        ),
    ))

    # ── Lines 8–9 — Entity Type ───────────────────────────────────
    story.append(Paragraph("PART III — ENTITY TYPE AND REASON FOR APPLYING", _STYLE_HEADING))
    story.extend(_field_block("Line 8a: Entity type", "Limited Liability Company (LLC)"))
    story.extend(_field_block(
        "Line 8b: Number of LLC members",
        str(len(cfg.members)),
    ))
    story.extend(_field_block(
        "Line 8c: If LLC, indicate how entity is classified for federal tax purposes",
        "Partnership" if len(cfg.members) > 1 else "Disregarded entity (single-member LLC)",
    ))
    story.extend(_field_block("Line 9a: Reason for applying", ein.reason_for_applying))
    story.extend(_field_block(
        "Line 10: Date business started or acquired (MM/DD/YYYY)",
        ein.business_start_date,
    ))
    story.extend(_field_block(
        "Line 11: Closing month of accounting year",
        ein.fiscal_year_end_month,
    ))

    # ── Lines 12–15 — Business Activity ──────────────────────────
    story.append(Paragraph("PART IV — BUSINESS ACTIVITY", _STYLE_HEADING))
    story.extend(_field_block(
        "Line 12: First date wages or annuities were paid (if none, skip)",
        "N/A — no employees",
    ))
    story.extend(_field_block(
        "Line 13: Highest number of employees expected in next 12 months",
        str(ein.expected_employees),
    ))
    story.extend(_field_block(
        "Line 14: Check one box that best describes principal activity",
        ein.principal_activity,
    ))
    story.extend(_field_block(
        "Line 15: Describe specific products or services provided",
        ein.specific_products_services,
    ))

    # ── Third-Party Designee ──────────────────────────────────────
    story.append(Paragraph("THIRD-PARTY DESIGNEE (optional)", _STYLE_HEADING))
    story.extend(_field_block("Designee name", "(leave blank if applying directly)"))
    story.extend(_field_block("Designee phone", ""))
    story.extend(_field_block("Designee fax", ""))

    # ── Signature ─────────────────────────────────────────────────
    story.append(Paragraph("SIGNATURE", _STYLE_HEADING))
    story.append(Paragraph(
        "Under penalties of perjury, I declare that I have examined this application, "
        "and to the best of my knowledge and belief, it is true, correct, and complete.",
        _STYLE_BODY,
    ))
    story.extend(_signature_block(ein.responsible_party_name, "Responsible Party / Applicant"))
    story.extend(_field_block("Date", "________________"))
    story.extend(_field_block("Applicant telephone number", "(___) ___-____"))
    story.extend(_field_block("Applicant fax number (optional)", ""))

    # ── Footer ────────────────────────────────────────────────────
    story.append(Spacer(1, 20))
    story.append(_hr())
    story.append(Paragraph(_footer_text(cfg.name, "IRS SS-4 EIN Application — DRAFT"), _STYLE_FOOTNOTE))
    story.append(Paragraph(
        "Apply online (fastest): https://www.irs.gov | "
        "Review SS-4 instructions: https://www.irs.gov/pub/irs-pdf/iss4.pdf",
        _STYLE_FOOTNOTE,
    ))
    story.append(Paragraph(
        "CAUTION: This is a draft for review only. The responsible party's SSN "
        "must be filled in immediately before submission. Never store real SSNs in "
        "version control.",
        ParagraphStyle(
            "Caution", parent=_STYLE_FOOTNOTE, textColor=colors.HexColor("#c0392b")
        ),
    ))

    doc.build(story)
    return output_path


# ── Public entry point ───────────────────────────────────────────────────────

def generate_all_llc_documents(cfg: EntityConfig) -> dict[str, Path]:
    """
    Generate all three LLC documents and return a dict mapping document
    type → output path.

    Args:
        cfg: Parsed EntityConfig from config.yaml.

    Returns:
        {
            "articles":          Path to Articles of Organization PDF,
            "operating_agreement": Path to Operating Agreement PDF,
            "ss4":               Path to SS-4 EIN Application PDF,
        }
    """
    output_dir = Path(cfg.output.directory)
    output_dir.mkdir(parents=True, exist_ok=True)

    paths = {
        "articles": generate_articles_of_organization(cfg, output_dir),
        "operating_agreement": generate_operating_agreement(cfg, output_dir),
        "ss4": generate_ss4_application(cfg, output_dir),
    }
    return paths
