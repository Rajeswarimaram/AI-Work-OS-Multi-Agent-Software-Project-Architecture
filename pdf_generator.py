import os
from xml.sax.saxutils import escape
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph, SimpleDocTemplate

OUTPUT_FOLDER = "output"
PDF_FILE = os.path.join(
    OUTPUT_FOLDER,
    "AI_WorkOS_Report.pdf"
)
def format_text(content: str | None) -> str:
    """Escapes special characters and
    formats multiline text for PDF."""
    if content is None:
        return ""
    return escape(
        str(content)
    ).replace(
        "\n",
        "<br/>"
    )
def pdf_generator(project_report: dict) -> None:
    """Generates the final project
    report in PDF format."""
    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )
    pdf_document = SimpleDocTemplate(
        PDF_FILE
    )
    pdf_styles = getSampleStyleSheet()

    title_style = pdf_styles["Heading1"]
    title_style.alignment = TA_CENTER

    heading_style = pdf_styles["Heading2"]

    normal_style = pdf_styles["BodyText"]

    pdf_story = []


    # Title
    pdf_story.append(
        Paragraph(
            "AI WorkOS",
            title_style
        )
    )

    pdf_story.append(
        Paragraph(
            "Adaptive Multi-Agent Task Automation Platform",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            "<br/><br/>",
            normal_style
        )
    )

    # Project Information
    pdf_story.append(
        Paragraph(
            "Project Information",
            heading_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Project:</b> {format_text(project_report.get('project'))}",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Task Type:</b> {format_text(project_report.get('task_type'))}",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Status:</b> {format_text(project_report.get('status'))}",
            normal_style
        )
    )

    confidence = project_report.get(
        "confidence",
        {}
    )

    pdf_story.append(
        Paragraph(
            f"<b>Confidence Score:</b> {confidence.get('score', 0)}%",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Rating:</b> {format_text(confidence.get('rating'))}",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            "<br/>",
            normal_style
        )
    )

    # Research Report
    pdf_story.append(
        Paragraph(
            "Research Report",
            heading_style
        )
    )

    pdf_story.append(
        Paragraph(
            format_text(
                project_report.get(
                    "research_report"
                )
            ),
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            "<br/>",
            normal_style
        )
    )

    # Implementation Report
    pdf_story.append(
        Paragraph(
            "Implementation Report",
            heading_style
        )
    )

    pdf_story.append(
        Paragraph(
            format_text(
                project_report.get(
                    "implementation_report"
                )
            ),
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            "<br/>",
            normal_style
        )
    )
    # Expert Review
    project_review = project_report.get(
        "review_report",
        {}
    )

    pdf_story.append(
        Paragraph(
            "Expert Review",
            heading_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Overall Score:</b> {project_review.get('overall_score', 0)}",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Industry Rating:</b> {format_text(project_review.get('industry_rating'))}",
            normal_style
        )
    )

    pdf_story.append(
        Paragraph(
            f"<b>Final Verdict:</b><br/>{format_text(project_review.get('final_verdict'))}",
            normal_style
        )
    )
    pdf_document.build(
        pdf_story
    )
    print("PDF Report Generated Successfully")
    print(f"Saved at: {PDF_FILE}")