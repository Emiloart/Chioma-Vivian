"""
Generates assets/Mogaha-Chioma-Vivian-CV.pdf for the portfolio's
"Download CV" button. Content matches the verified CV exactly.
"""
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem, HRFlowable
)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

INK = HexColor("#2A2420")
COFFEE = HexColor("#3B2A1E")
MUTED = HexColor("#6B6258")
SKY = HexColor("#2D7AA6")

styles = {
    "name": ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=22, textColor=COFFEE, spaceAfter=2),
    "title": ParagraphStyle("title", fontName="Helvetica-Bold", fontSize=11.5, textColor=SKY, spaceAfter=4),
    "contact": ParagraphStyle("contact", fontName="Helvetica", fontSize=9.5, textColor=MUTED, spaceAfter=12),
    "h2": ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5, textColor=COFFEE, spaceBefore=12, spaceAfter=6, letterSpacing=0.6),
    "body": ParagraphStyle("body", fontName="Helvetica", fontSize=9.8, textColor=INK, leading=14, spaceAfter=6),
    "bullet": ParagraphStyle("bullet", fontName="Helvetica", fontSize=9.8, textColor=INK, leading=13.5),
    "role": ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=10.3, textColor=INK, spaceBefore=6, spaceAfter=1),
    "org": ParagraphStyle("org", fontName="Helvetica-Oblique", fontSize=9.6, textColor=MUTED, spaceAfter=4),
    "link": ParagraphStyle("link", fontName="Helvetica", fontSize=9.3, textColor=SKY, spaceAfter=6),
}

doc = SimpleDocTemplate(
    "assets/Mogaha-Chioma-Vivian-CV.pdf",
    pagesize=LETTER,
    topMargin=0.55 * inch, bottomMargin=0.55 * inch,
    leftMargin=0.65 * inch, rightMargin=0.65 * inch,
)

def rule():
    return HRFlowable(width="100%", thickness=0.75, color=HexColor("#D9CBB4"), spaceAfter=8)

def bullets(items):
    return ListFlowable(
        [ListItem(Paragraph(i, styles["bullet"]), leftIndent=10, bulletColor=SKY) for i in items],
        bulletType="bullet", start="•", leftIndent=14, spaceAfter=6,
    )

story = []

story.append(Paragraph("Mogaha Chioma Vivian", styles["name"]))
story.append(Paragraph("Customer Support Specialist &nbsp;·&nbsp; IT Support &nbsp;·&nbsp; Computer Science Graduate", styles["title"]))
story.append(Paragraph("Anambra, Nigeria &nbsp;|&nbsp; mogahachioma03@gmail.com &nbsp;|&nbsp; +234 806 993 2553", styles["contact"]))
story.append(rule())

story.append(Paragraph("PROFILE", styles["h2"]))
story.append(Paragraph(
    "Computer Science graduate with hands-on customer support experience in the cryptocurrency sector at "
    "BITUNIX, where I worked omnichannel queues across live chat and Zendesk before moving into the retention "
    "team, engaging users directly through Discord. I'm skilled at translating technical account issues into "
    "clear, calm guidance, and at building the kind of trust that keeps a user engaged rather than lost.",
    styles["body"]))
story.append(Paragraph(
    "At Pa-cent Technologies, I brought that same clarity to teaching non-technical learners everyday "
    "software, helping them build real confidence rather than just complete a session.",
    styles["body"]))
story.append(Paragraph(
    "I'm looking for a remote or hybrid role in customer support, technical support, or operations, ideally "
    "within FinTech, Web3, or SaaS, where technical grounding and clear communication both matter.",
    styles["body"]))

story.append(Paragraph("CORE STRENGTHS", styles["h2"]))
story.append(bullets([
    "Omnichannel customer support &amp; retention, live chat, Zendesk, Discord community engagement",
    "Technical onboarding and one-on-one training for non-technical users",
    "HTML5 &amp; CSS3 fundamentals",
    "Microsoft Office &amp; Google Workspace, documentation, reporting, presentations",
    "Accurate data entry, records management, and plain-language technical communication",
]))

story.append(Paragraph("PROFESSIONAL EXPERIENCE", styles["h2"]))
story.append(Paragraph("Customer Service Representative", styles["role"]))
story.append(Paragraph("BITUNIX", styles["org"]))
story.append(bullets([
    "Managed omnichannel support queues across live chat and Zendesk, resolving issues on first contact "
    "where possible and escalating what genuinely needed a specialist.",
    "Logged and tracked every interaction in Zendesk to keep accurate, consistent records across shifts "
    "and handoffs.",
    "Worked directly with teammates on escalated cases rather than just passing them along.",
]))
story.append(Paragraph("Retention Team", styles["role"]))
story.append(Paragraph("BITUNIX", styles["org"]))
story.append(bullets([
    "Moved into the retention team, engaging users directly through Discord to support re-engagement and "
    "reduce churn.",
    "Used direct, community-based communication to rebuild trust with users experiencing friction, rather "
    "than relying on ticket replies alone.",
]))
story.append(Paragraph("IT Skills Facilitator", styles["role"]))
story.append(Paragraph("Pa-cent Technologies Limited", styles["org"]))
story.append(bullets([
    "Taught non-technical learners the Microsoft Office tools and everyday software they would actually "
    "use, not a generic curriculum.",
    "Broke down technical concepts into language people could act on immediately.",
    "Worked one-on-one with learners who needed extra support to build real, lasting confidence, not just "
    "pass a session.",
]))

story.append(Paragraph("PROJECTS", styles["h2"]))
story.append(Paragraph("FM University of Science and Art &nbsp;—&nbsp; Multi-Page Website", styles["role"]))
story.append(Paragraph(
    "Designed and built a full multi-page website (home, about, courses, blog, contact) using HTML and CSS, "
    "structuring content across academic programmes and campus facilities.", styles["body"]))
story.append(Paragraph(
    '<link href="https://mogahachioma03-arch.github.io/FM-University/course.html">'
    'mogahachioma03-arch.github.io/FM-University/course.html</link>', styles["link"]))

story.append(Paragraph(
    "Design and Implementation of an Expert System for Land Ownership Verification and Property Dispute "
    "Resolution", styles["role"]))
story.append(Paragraph(
    "Researched and designed an expert system for land ownership verification and property dispute "
    "resolution.", styles["body"]))
story.append(Paragraph(
    '<link href="https://eu.wps.com/cms/docs/d/cbRadn45tyVbmXuD?sa=601.1074">Full project documentation</link>',
    styles["link"]))

story.append(Paragraph("EDUCATION", styles["h2"]))
story.append(Paragraph("Bachelor of Science (B.Sc.), Computer Science", styles["role"]))
story.append(Paragraph("Nnamdi Azikiwe University &nbsp;—&nbsp; 2025", styles["org"]))

story.append(Paragraph("TOOLS &amp; TECHNOLOGIES", styles["h2"]))
story.append(Paragraph(
    "Microsoft Word, Excel, PowerPoint &nbsp;·&nbsp; Google Workspace &nbsp;·&nbsp; HTML5, CSS3 "
    "&nbsp;·&nbsp; Zendesk, Discord &nbsp;·&nbsp; Computer Graphics fundamentals", styles["body"]))

story.append(Paragraph("CERTIFICATIONS", styles["h2"]))
story.append(Paragraph(
    "Certificate of Completion, Diploma Programme (2017), Computer Application, Disk &amp; Virus Management, "
    "Desktop Publishing, Word Processing, Database Management, Computer Graphics, Internet Usage.",
    styles["body"]))

doc.build(story)
print("done")
