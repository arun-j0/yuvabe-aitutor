import os
from dotenv import load_dotenv
import streamlit as st
from streamlit_ace import st_ace
import io
import contextlib
import requests

# Load environment variables from .env file
load_dotenv()

# Retrieve API keys from environment variables
groq_api_key = os.getenv("GROQ_API_KEY")

def get_chat_completion(message, context=""):
    api_url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    
    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {
                "role": "system",
                "content": (
                    "You are a programming assistant. Provide detailed explanations and solutions for code-related questions. "
                    "When provided with code, analyze it and offer debugging advice or improvements. For errors, explain the cause and suggest fixes. "
                    "Ensure responses are clear and include step-by-step instructions if necessary. Avoid unnecessary details and focus on resolving the issue."
                )
            },
            {"role": "user", "content": f"{context}\n\n{message}"}
        ],
        "max_tokens": 1000,
        "temperature": 0.7
    }
    
    response = requests.post(api_url, json=payload, headers=headers)
    
    if response.status_code == 200:
        chat_completion = response.json()
        return chat_completion["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code} - {response.json()}"

def run_code(code):
    output = io.StringIO()  # Create an in-memory file-like object to capture output
    try:
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            exec(code)  # Execute the code
        return output.getvalue(), ""  # Get the output as a string
    except Exception as e:
        return "", f"Error: {e}"  # Capture any exceptions as errors

def main():
    # Initialize session state with default values
    if 'code' not in st.session_state:
        st.session_state.code = "print('Hello, World!')"
    if 'code_output' not in st.session_state:
        st.session_state.code_output = ""
    if 'code_error' not in st.session_state:
        st.session_state.code_error = ""
    if 'chat_response' not in st.session_state:
        st.session_state.chat_response = ""
    if 'user_query' not in st.session_state:
        st.session_state.user_query = ""
    if 'hidden_answer' not in st.session_state:
        st.session_state.hidden_answer = ""

    # Define available themes
    THEMES = [
        "textmate", "monokai", "github", "solarized_light", "solarized_dark",
        "terminal", "eclipse", "xcode", "kuroir", "dracula"
    ]

    st.title("Python Code Interpreter with Dynamic Theme")

    # Dropdown for selecting the theme
    selected_theme = st.selectbox("Select Editor Theme:", THEMES, index=THEMES.index(st.session_state.get('selected_theme', 'textmate')))

    # Code editor with syntax highlighting and selected theme
    st.session_state.code = st_ace(
        value=st.session_state.code,
        language="python",
        theme=selected_theme,  # Use the selected theme
    )

    if st.button("Run Code"):
        st.session_state.code_output, st.session_state.code_error = run_code(st.session_state.code)

    st.subheader("Output")
    if st.session_state.code_output:
        st.code(st.session_state.code_output)  # Display the result
    if st.session_state.code_error:
        st.code(st.session_state.code_error, language="python")  # Display the error

    # Chatbot interface
    st.sidebar.header("Chatbot Help")
    
    # User's custom query input
    st.session_state.user_query = st.sidebar.text_input("Ask a specific question about your code or error:", value=st.session_state.user_query)
    
    if st.sidebar.button("Submit Query"):
        context = f"Code:\n{st.session_state.code}\n\nOutput/Error:\n{st.session_state.code_output}\n{st.session_state.code_error}"
        if st.session_state.user_query:
            if "code" in st.session_state.user_query.lower() or "error" in st.session_state.user_query.lower():
                st.session_state.chat_response = get_chat_completion(st.session_state.user_query, context)
            else:
                st.session_state.chat_response = get_chat_completion(st.session_state.user_query)

    # Chatbot predefined buttons
    if st.sidebar.button("Explain the Program"):
        context = f"Code:\n{st.session_state.code}\n\nOutput/Error:\n{st.session_state.code_output}\n{st.session_state.code_error}"
        st.session_state.chat_response = get_chat_completion("Explain the following code:", context)

    if st.sidebar.button("Help Me Fix the Error"):
        if st.session_state.code_error:
            context = f"Code:\n{st.session_state.code}\n\nError:\n{st.session_state.code_error}"
            st.session_state.chat_response = get_chat_completion("Help me fix this error:", context)
        else:
            st.session_state.chat_response = "No error to fix. Run some code first."

    if st.sidebar.button("Provide Me Some Simple Questions to Practice"):
        practice_question = get_chat_completion("Provide a simple programming question with input and output.")
        st.session_state.hidden_answer = get_chat_completion("Now provide the answer for the above question.")
        st.session_state.user_query = practice_question  # Set the practice question to user_query
        st.session_state.chat_response = practice_question  # Display the practice question

    # Display the chatbot response below the buttons
    st.sidebar.subheader("Response")
    if st.session_state.chat_response:
        st.sidebar.write(st.session_state.chat_response)

    # Button to clear the response
    if st.sidebar.button("Clear Response"):
        st.session_state.chat_response = ""
        st.session_state.user_query = ""
        st.session_state.hidden_answer = ""

if __name__ == "__main__":
    main()
