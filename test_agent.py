import os
from dotenv import load_dotenv
from agent import AgentSender
import json

def test_agent():
    # Load environment variables
    load_dotenv()
    
    # Check for OpenAI API key
    if not os.getenv("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY not found in environment variables.")
        print("Please create a .env file with your OpenAI API key.")
        return
    
    # Create agent instance
    agent = AgentSender()
    
    # Test goal
    test_goal = "Find 3 AI startup founders and prepare personalized outreach"
    
    print(f"\nSetting test goal: {test_goal}")
    agent.set_goal(test_goal)
    
    # Print the steps that were created
    print("\nCreated steps:")
    for step in agent.current_steps:
        print(f"\nStep {step['step_id']}:")
        print(f"Description: {step['description']}")
        print(f"Tool: {step['tool']}")
        print(f"Status: {step['status']}")
    
    # Run the agent
    print("\nStarting execution...")
    results = agent.run()
    
    # Print results
    print("\nExecution results:")
    for i, result in enumerate(results, 1):
        print(f"\nResult {i}:")
        if "error" in result:
            print(f"Error: {result['error']}")
        elif "leads" in result:
            print(f"Found {len(result['leads'])} leads:")
            for lead in result['leads']:
                print(f"\n- {lead['name']} ({lead['role']})")
                print(f"  Company: {lead['company']}")
                print(f"  Email: {lead['email']}")
    
    # Print final progress
    progress = agent.get_progress()
    print("\nFinal progress:")
    print(f"Progress: {progress['progress_percentage']:.1f}%")
    print(f"Completed steps: {progress['completed_steps']}/{progress['total_steps']}")
    if progress['failed_steps'] > 0:
        print(f"Failed steps: {progress['failed_steps']}")
    
    # Check logs
    print("\nChecking logs...")
    leads = agent.memory.get_all_leads()
    print(f"Total leads found: {len(leads)}")
    
    steps = agent.memory.get_all_steps()
    print(f"Total steps logged: {len(steps)}")

if __name__ == "__main__":
    test_agent() 