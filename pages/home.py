import streamlit as st 

def main():
    st.header("APPLICATION OVERVIEW")
    st.markdown("""
    Welcome to our comprehensive application designed to enhance your productivity and learning experience. 
    This app offers four key features:

    ### 1. Course Management & AI Assistance
    - **Add and Manage Courses**: Easily add new courses, ensuring no duplicates.
    - **Select and View Content**: Browse and view AI-generated content from selected courses, modules, and sub-modules.
    - **Keyword Extraction**: Automatically highlights relevant keywords from content.
    - **Chatbot Integration**: Provides an interactive chatbot for additional support based on selected content.
    - **Organized Layout**: Includes a sidebar for easy navigation and a main area for content display.

    ### 2. Notes Management System
    - **Create New Notes**: Enter a title and content for new notes, saved as files.
    - **Edit Existing Notes**: Modify titles and content of existing notes.
    - **Delete Notes**: Remove unwanted notes, deleting their respective files.
    - **Full-Size Editor**: Utilizes custom CSS for a full-size Quill editor.
    - **Note Management**: Manage all notes in expandable sections for easy viewing and editing.

    ### 3. Python Code Interpreter
    - **Dynamic Theme Selection**: Choose from themes like "monokai" and "dracula."
    - **Code Editor**: An interactive editor with syntax highlighting for Python code.
    - **Execute Code**: Run Python code within the app and see the output immediately.
    - **Output Display**: View results or errors of your code execution.
    - **AI Assistance**: Get help with errors or explanations.

    ### 4. Quiz Generation & Management
    - **Quiz Generation**: Create multiple-choice questions using the Groq API and the "llama-3.1-70b-versatile" model.
    - **JSON Extraction**: Extract and format quiz data from API responses using regular expressions.
    - **Automatic Navigation**: Move to the next question seamlessly after feedback.
    - **State Management**: Use Streamlit's session state to track questions, current index, and quiz completion.
    - **Performance Summary**: View a summary of correct answers versus total questions upon quiz completion.

    Use the navigation on the left to explore these features.
    """)
