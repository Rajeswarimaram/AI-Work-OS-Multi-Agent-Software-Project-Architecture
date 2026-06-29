from agents.orchestrator_agent import orchestrator_agent


def main():

    print("=" * 60)
    print("           AI WorkOS - Multi-Agent Task Automation")
    print("=" * 60)

    print("\nWelcome to AI WorkOS")
    print("Describe your software project below.\n")

    user_request = input("Enter Project Idea: ").strip()

    if not user_request:

        print("\n❌ Project description cannot be empty.")
        return

    print("\nGenerating AI Report...")
    print("Please wait...\n")

    try:

        final_report = orchestrator_agent(user_request)

        print("=" * 60)
        print("               FINAL PROJECT REPORT")
        print("=" * 60)

        print(f"\nProject Name : {final_report['project']}")
        print(f"Task Type    : {final_report['task_type']}")
        print(f"Status       : {final_report['status']}")

        print("\nConfidence Score")
        print("------------------------------")
        print(f"Score  : {final_report['confidence']['score']}%")
        print(f"Rating : {final_report['confidence']['rating']}")

        print("\nReport generated successfully.")
        print("Location : output/report.json")

        print("\nThank you for using AI WorkOS!")

    except Exception as error:

        print("\nAn unexpected error occurred.")
        print(error)


if __name__ == "__main__":
    main()