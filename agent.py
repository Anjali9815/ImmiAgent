from tools import explain_visa_term, check_deadline, check_work_eligibility, track_document_status, get_timeline
from dotenv import load_dotenv
import os
import json
from groq import Groq
from tools_def import TOOL_DEFINITIONS

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

system_prompt = """You are IMMI, an Immigration AI Assistant for international students.
Before giving eligibility answers, ask the user about their status (visa type, enrollment duration, etc.)
Always clarify the user's situation before giving advice.
Add a disclaimer that this is informational, not legal advice.
After the user answers once, use the tools and give an answer. Don't keep asking.
If the user already provided their visa type and enrollment, that's enough - call the tool.
Limit clarifying questions to one round maximum."""

# Map function names to actual functions
tool_functions = {
    "explain_visa_term": explain_visa_term,
    "check_deadline": check_deadline,
    "check_work_eligibility": check_work_eligibility,
    "track_document_status": track_document_status,
    "get_timeline": get_timeline
}

# Conversation history for memory
messages = [{"role": "system", "content": system_prompt}]

print("IMMI: Hello! I'm IMMI, your Immigration AI Assistant. How can I help you today?")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Goodbye!")
        break

    messages.append({"role": "user", "content": user_input})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=messages,
            tools=TOOL_DEFINITIONS
        )

        message = response.choices[0].message

        print(message)
        print("***************************")

        if message.tool_calls:
            tool_call = message.tool_calls[0]
            function_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            # Call the actual function
            if function_name in tool_functions:
                result = tool_functions[function_name](**arguments)
            else:
                result = "Tool not found."

            # Send the tool result back to Groq for a final answer
            messages.append(message)
            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": json.dumps(result) if isinstance(result, dict) else str(result)
            })

            final_response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages
            )

            final_answer = final_response.choices[0].message.content
            print(f"IMMI: {final_answer}")
            messages.append({"role": "assistant", "content": final_answer})

        else:
            print(f"IMMI: {message.content}")
            messages.append({"role": "assistant", "content": message.content})

    except Exception as e:
        print(f"Error: {e}")

    print()