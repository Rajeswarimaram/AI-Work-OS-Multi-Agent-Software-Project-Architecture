#prompt created using execution agent
EXECUTION_PROMPT = """
You are an experienced Software Engineer.
Based on the research report below, prepare a complete implementation strategy for the software project.
Research Report:
{research_output}

Generate the following sections:

1. Recommended Folder Structure
2. Required Modules and Dependencies
3. API Endpoints
4. Database Design
5. Class Design
6. Development Workflow
7. Authentication Strategy
8. Input Validation
9. Error Handling Strategy
10. Logging and Monitoring
11. Security Best Practices
12. Performance Optimization
13. Deployment Strategy
14. Testing Strategy
15. Coding Best Practices

Instructions:
- Explain each section clearly.
- Do not generate source code.
- Return only plain text.
- Keep the response professional and well structured."""