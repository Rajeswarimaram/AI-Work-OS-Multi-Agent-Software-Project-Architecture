def classify_task(user_request):
    """
    Classifies the user's request into an appropriate project category.
    """

    request = user_request.lower().strip()

    software_keywords = [
        "software",
        "application",
        "system",
        "project",
        "management",
        "platform",
        "dashboard",
        "website",
        "web",
        "mobile"
    ]

    ai_keywords = [
        "ai",
        "artificial intelligence",
        "machine learning",
        "deep learning",
        "chatbot",
        "llm",
        "agent",
        "automation",
        "gemini",
        "openai"
    ]

    coding_keywords = [
        "python",
        "java",
        "c++",
        "javascript",
        "code",
        "algorithm",
        "program"
    ]

    resume_keywords = [
        "resume",
        "cv",
        "job",
        "career",
        "linkedin"
    ]

    document_keywords = [
        "pdf",
        "document",
        "report",
        "notes",
        "file"
    ]

    # ----------------------------
    # AI Projects
    # ----------------------------

    for word in ai_keywords:
        if word in request:
            return "AI Project"

    # ----------------------------
    # Software Engineering
    # ----------------------------

    for word in software_keywords:
        if word in request:
            return "Software Engineering"

    # ----------------------------
    # Coding
    # ----------------------------

    for word in coding_keywords:
        if word in request:
            return "Programming"

    # ----------------------------
    # Resume
    # ----------------------------

    for word in resume_keywords:
        if word in request:
            return "Resume Analysis"

    # ----------------------------
    # Documents
    # ----------------------------

    for word in document_keywords:
        if word in request:
            return "Document Analysis"

    return "General Task"