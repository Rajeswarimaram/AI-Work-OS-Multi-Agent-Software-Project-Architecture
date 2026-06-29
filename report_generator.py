import json
import os
from datetime import datetime
from reports.pdf_generator import pdf_generator

OUTPUT_FOLDER = "output"
REPORT_FILE = os.path.join(
    OUTPUT_FOLDER,
    "report.json"
)
def generate_report(project_report: dict) -> None:
    """Generates the final JSON report
    and creates the PDF report."""
    print("REPORT GENERATOR")
    os.makedirs(
        OUTPUT_FOLDER,
        exist_ok=True
    )
    project_report["generated_at"] = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    )
    project_report["generator"] = "AI WorkOS"
    project_report["version"] = "1.0"
    try:
        print("Saving JSON Report...")
        with open(
            REPORT_FILE,
            "w",
            encoding="utf-8"
        )as report_file:

            json.dump(
                project_report,
                report_file,
                indent=4,
                ensure_ascii=False
            )

        print("JSON Report Saved Successfully")
        print("Generating PDF Report...")
        pdf_generator(project_report)
        print("PDF Report Generated Successfully")
        print("Report Generation Completed")

    except Exception as error:
        print("Report Generation Failed")
        print(error)