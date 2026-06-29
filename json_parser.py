import json
def parse_json(ai_response: str) -> dict:
    """Converts the AI response into
    a valid Python dictionary.
    Supports:
    - Plain JSON
    - Markdown wrapped JSON
    - Empty or invalid responses"""
    if not ai_response:
        return {

            "success": False,

            "error": "Empty response received from AI."
        }
    try:
        cleaned_response = (
        ai_response
        .replace("```json", "")
        .replace("```", "")
        .strip()
        )
        parsed_response = json.loads(
            cleaned_response
        )
        return parsed_response
    except json.JSONDecodeError:
        print("JSON Parsing Error")
        print(ai_response)
        return {
        "success": False,
        "error": "Invalid JSON received from AI.",
        "raw_output": ai_response,
        "status": "FAILED",
        "quality_score": 0,
         "checks": [],
        "warnings": [
           "Unable to parse the AI response."
        ],
        "recommendations": [
             "Please generate the report again."
            ],
        "overall_score": 0,
        "deployment_ready": False,
        "industry_rating": "Unknown",
        "architecture_review": "",
        "security_review": "",
        "performance_review": "",
        "maintainability_review": "",
        "strengths": [],
        "improvements": [],
        "final_verdict": "The AI response could not be processed."
        }
    except Exception as error:
        print(error)
        return {
        "success": False,
        "error": str(error),
        "raw_output": ai_response
        }