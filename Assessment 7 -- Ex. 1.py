# Knowledge base as a dictionary
K_Base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings",
                        "No": "Check the power supply and motherboard"
                    }
                }
            }
        },
        "No": "Check the power supply and cables"
    }
}

# Function to navigate through the decision tree
def decision_tree(question, knowledge_base):
    # If the current knowledge base entry is a string (i.e., a solution), return it
    if isinstance(knowledge_base, str):
        return knowledge_base

    # Ask the question and get user's response
    print(question)
    user_input = input("Enter Yes or No: ")

    # Navigate the knowledge base based on user input
    if user_input in knowledge_base:
        next_step = knowledge_base[user_input]
        if isinstance(next_step, dict):  # If the next step is a dictionary, there's a follow-up question
            next_question = list(next_step.keys())[0]
            return decision_tree(next_question, next_step[next_question])
        else:  # Otherwise, it's the final answer
            return next_step
    else:
        return "Invalid input. Please answer with 'Yes' or 'No'."

# Start the decision tree diagnosis
def start_diagnosis():
    first_question = list(K_Base.keys())[0]
    solution = decision_tree(first_question, K_Base[first_question])
    print(f"Diagnosis: {solution}")

# Run the diagnosis
start_diagnosis()
