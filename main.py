import os
from dotenv import load_dotenv
from agent import AgentSender
import argparse

def main():
    # Load environment variables
    load_dotenv()
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Set up argument parser
    parser = argparse.ArgumentParser(description="AgentSender - AI-powered cold email outreach")
    parser.add_argument("--goal", type=str, help="The goal for the agent to accomplish")
    args = parser.parse_args()
    
    # Create agent instance
    agent = AgentSender()
    
    # Get goal from command line or prompt
    goal = args.goal
    if not goal:
        goal = input("What should I do?\n> ")
    
    # Set and run the goal
    print(f"\nSetting goal: {goal}")
    agent.set_goal(goal)
    
    print("\nStarting execution...")
    results = agent.run()
    
    # Print final progress
    progress = agent.get_progress()
    print("\nExecution complete!")
    print(f"Progress: {progress['progress_percentage']:.1f}%")
    print(f"Completed steps: {progress['completed_steps']}/{progress['total_steps']}")
    
    if progress['failed_steps'] > 0:
        print(f"Failed steps: {progress['failed_steps']}")

if __name__ == "__main__":
    main()
