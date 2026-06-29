import os

import streamlit as st

from agents.memory_agent import load_history
from agents.orchestrator_agent import orchestrator_agent


# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI WorkOS",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ==========================================
# LOAD CUSTOM CSS
# ==========================================

def load_styles() -> None:
    """
    Loads the custom CSS stylesheet.
    """

    try:

        with open(
            "assets/style.css",
            "r",
            encoding="utf-8"
        ) as style_file:

            st.markdown(
                f"<style>{style_file.read()}</style>",
                unsafe_allow_html=True
            )

    except FileNotFoundError:

        st.warning(
            "Custom stylesheet not found."
        )


load_styles()


# ==========================================
# SESSION STATE
# ==========================================

if "result" not in st.session_state:

    st.session_state.result = None


# ==========================================
# LOAD PROJECT HISTORY
# ==========================================

project_history = load_history()


# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("🤖 AI WorkOS")

    st.success("🟢 Multi-Agent System Online")

    st.markdown("---")

    st.subheader("Active AI Agents")

    st.write("🧠 Research Agent")

    st.write("⚙️ Execution Agent")

    st.write("🧪 Testing Agent")

    st.write("🔍 Critic Agent")

    st.write("💾 Memory Agent")

    st.write("📋 Synthesizer Agent")

    st.write("🎯 Orchestrator Agent")

    st.markdown("---")

    st.subheader("Project Statistics")

    st.metric(
        "Completed Projects",
        len(project_history)
    )

    st.metric(
        "AI Agents",
        "7"
    )

    st.metric(
        "System",
        "Ready"
    )

    st.markdown("---")

    st.subheader("Recent Projects")

    if project_history:

        for project in reversed(project_history[-5:]):

            st.caption(
                project.get(
                    "project_name",
                    "Unknown Project"
                )
            )

    else:

        st.caption(
            "No project history available."
        )

    st.markdown("---")

    st.caption("AI WorkOS v1.0")


# ==========================================
# APPLICATION HEADER
# ==========================================

st.markdown(
    """
# 🤖 AI WorkOS

### Adaptive Multi-Agent Task Automation Platform

Transform software ideas into professional engineering plans using specialized AI agents.
"""
)

st.markdown("---")


# ==========================================
# DASHBOARD
# ==========================================

dashboard_col1, dashboard_col2, dashboard_col3, dashboard_col4 = st.columns(4)

with dashboard_col1:

    st.metric(
        "AI Agents",
        "7"
    )

with dashboard_col2:

    st.metric(
        "Projects",
        len(project_history)
    )

with dashboard_col3:

    st.metric(
        "Architecture",
        "Multi-Agent"
    )

with dashboard_col4:

    st.metric(
        "System Status",
        "🟢 Online"
    )

st.markdown("---")
# ==========================================
# USER INPUT
# ==========================================

st.subheader("💡 Describe Your Software Project")

user_request = st.text_area(

    label="",

    height=220,

    placeholder="""
Example:

Build an AI-powered Hospital Management System.

Include:

• Authentication
• User Roles
• AI Features
• Dashboard
• Database
• APIs
• Deployment Strategy
"""
)

start_analysis = st.button(
    "🚀 Start AI Analysis",
    use_container_width=True
)


# ==========================================
# AI WORKFLOW
# ==========================================

if start_analysis:

    if not user_request.strip():

        st.warning(
            "⚠ Please enter your software project description."
        )

        st.stop()

    with st.spinner(
        " AI WorkOS is analyzing your project..."
    ):

        progress_bar = st.progress(0)

        status_box = st.empty()

        workflow_steps = [

            ("Research Agent is analyzing project requirements...", 10),

            ("Execution Agent is preparing the implementation strategy...", 25),

            ("Testing Agent is validating the implementation...", 45),

            (" Critic Agent is reviewing software quality...", 65),

            ("Memory Agent is storing project history...", 80),

            (" Synthesizer Agent is preparing the final report...", 90)

        ]

        for message, percentage in workflow_steps:

            status_box.info(message)

            progress_bar.progress(
                percentage
            )

        final_result = orchestrator_agent(
            user_request
        )

        st.session_state.result = final_result

        progress_bar.progress(100)

        status_box.success(
            " AI WorkOS completed successfully."
        )

    st.success(
        " Project analysis completed successfully."
    )

    


# ==========================================
# LOAD GENERATED RESULT
# ==========================================

project_result = st.session_state.result

if project_result is None:

    st.info(
        " Enter your software project idea above and click 'Start AI Analysis'."
    )

    st.stop()
    # ==========================================
# ENGINEERING DASHBOARD
# ==========================================

st.markdown("---")

st.header(" AI WorkOS Engineering Dashboard")

confidence_report = project_result.get(
    "confidence",
    {}
)

confidence_score = confidence_report.get(
    "score",
    0
)

confidence_rating = confidence_report.get(
    "rating",
    "Unknown"
)

progress_column, score_column = st.columns([4, 1])

with progress_column:

    st.progress(
        confidence_score / 100
    )

with score_column:

    st.metric(
        "Confidence",
        f"{confidence_score}%"
    )

st.success(
    f"Overall Rating: {confidence_rating}"
)

st.markdown("---")


# ==========================================
# PROJECT SUMMARY
# ==========================================

summary_col1, summary_col2, summary_col3 = st.columns(3)

review_report = project_result.get(
    "review_report",
    {}
)

with summary_col1:

    st.metric(
        "Task Type",
        project_result.get(
            "task_type",
            "Unknown"
        )
    )

with summary_col2:

    st.metric(
        "Project Status",
        project_result.get(
            "status",
            "Unknown"
        )
    )

with summary_col3:

    deployment_ready = review_report.get(
        "deployment_ready",
        False
    )

    st.metric(
        "Deployment",
        "Ready " if deployment_ready else "Not Ready ⚠"
    )

st.markdown("---")


# ==========================================
# RESEARCH REPORT
# ==========================================

with st.expander(
    "Research Agent Report",
    expanded=True
):

    st.write(

        project_result.get(
            "research_report",
            "No research report available."
        )

    )


# ==========================================
# IMPLEMENTATION REPORT
# ==========================================

with st.expander(
    " Execution Agent Report"
):

    st.write(

        project_result.get(
            "implementation_report",
            "No implementation report available."
        )

    )
    # ==========================================
# TESTING REPORT
# ==========================================

with st.expander(
    " Testing Agent Report"
):

    testing_report = project_result.get(
        "testing_report",
        {}
    )

    st.metric(
        "Quality Score",
        testing_report.get(
            "quality_score",
            0
        )
    )

    st.markdown("###  Validation Checks")

    for check in testing_report.get(
        "checks",
        []
    ):

        st.success(check)

    warning_list = testing_report.get(
        "warnings",
        []
    )

    if warning_list:

        st.markdown("###  Warnings")

        for warning in warning_list:

            st.warning(warning)

    st.markdown("###  Recommendations")

    for recommendation in testing_report.get(
        "recommendations",
        []
    ):

        st.info(recommendation)


# ==========================================
# CRITIC REPORT
# ==========================================

with st.expander(
    " Critic Agent Review"
):

    project_review = project_result.get(
        "review_report",
        {}
    )

    st.metric(
        "Industry Score",
        project_review.get(
            "overall_score",
            0
        )
    )

    st.metric(
        "Industry Rating",
        project_review.get(
            "industry_rating",
            "Unknown"
        )
    )

    st.metric(
        "Deployment Ready",
        "Yes "
        if project_review.get(
            "deployment_ready",
            False
        )
        else "No "
    )

    st.markdown(
        "###  Architecture Review"
    )

    st.info(
        project_review.get(
            "architecture_review",
            "Not Available"
        )
    )

    st.markdown(
        "###  Security Review"
    )

    st.info(
        project_review.get(
            "security_review",
            "Not Available"
        )
    )

    st.markdown(
        "###  Performance Review"
    )

    st.info(
        project_review.get(
            "performance_review",
            "Not Available"
        )
    )

    st.markdown(
        "###  Maintainability Review"
    )

    st.info(
        project_review.get(
            "maintainability_review",
            "Not Available"
        )
    )

    st.markdown(
        "###  Strengths"
    )

    for strength in project_review.get(
        "strengths",
        []
    ):

        st.success(strength)

    st.markdown(
        "###  Suggested Improvements"
    )

    for improvement in project_review.get(
        "improvements",
        []
    ):

        st.warning(improvement)

    st.markdown(
        "### Final Verdict"
    )

    st.success(
        project_review.get(
            "final_verdict",
            "Not Available"
        )
    )


# ==========================================
# FUTURE ENHANCEMENTS
# ==========================================

with st.expander(
    " Future Enhancements"
):

    for feature in project_result.get(
        "future_scope",
        []
    ):

        st.write(
            f"• {feature}"
        )


# ==========================================
# DOWNLOAD REPORT
# ==========================================

st.markdown("---")

st.subheader(
    " Download Report"
)

pdf_file = "output/AI_WorkOS_Report.pdf"

if os.path.exists(pdf_file):

    with open(
        pdf_file,
        "rb"
    ) as pdf_document:

        st.download_button(

            label="Download PDF Report",

            data=pdf_document,

            file_name="AI_WorkOS_Report.pdf",

            mime="application/pdf",

            use_container_width=True
        )

else:

    st.warning(
        "PDF report is not available."
    )


# ==========================================
# FOOTER
# ==========================================

st.markdown("---")

st.caption(
    "© 2026 AI WorkOS • Adaptive Multi-Agent Task Automation Platform"
)