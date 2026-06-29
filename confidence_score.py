def calculate_confidence(
    testing_report: dict,
    review_report: dict
) -> dict:
    """Calculates the final confidence score."""

    quality_score = testing_report.get("quality_score", 0)
    review_score = review_report.get("overall_score", 0)
    deployment_ready = review_report.get("deployment_ready", False)

    warnings = len(testing_report.get("warnings", []))
    improvements = len(review_report.get("improvements", []))

    confidence_score = int((quality_score * 0.45) + (review_score * 0.55))

    confidence_score -= warnings * 2
    confidence_score -= improvements

    if deployment_ready:
        confidence_score += 3

    confidence_score = max(0, min(100, confidence_score))

    if confidence_score >= 90:
        performance_rating = "Excellent ⭐⭐⭐⭐⭐"
    elif confidence_score >= 80:
        performance_rating = "Very Good ⭐⭐⭐⭐"
    elif confidence_score >= 70:
        performance_rating = "Good ⭐⭐⭐"
    elif confidence_score >= 60:
        performance_rating = "Average ⭐⭐"
    else:
        performance_rating = "Needs Improvement ⭐"

    return {
        "score": confidence_score,
        "rating": performance_rating,
        "deployment_ready": deployment_ready
    }