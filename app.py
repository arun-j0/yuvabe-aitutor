import streamlit as st

# Import page functions
from pages.course import main as COURSES_WITH_AI_ASSISTANCE
from pages.Interpreter import main as PYTHON_CODE_INTERPRETER
from pages.notes import main as NOTES_MANAGEMENT

def main():
    pages = {
        "Home": st.Page(COURSES_WITH_AI_ASSISTANCE, title="Course Management & AI Assistance"),
        "PyCode": st.Page(PYTHON_CODE_INTERPRETER, title="Python Code Interpreter"),
        "Note": st.Page(NOTES_MANAGEMENT, title="Notes Management System"),
    }
    st.header("APPLICATION OVERVIEW")
    st.markdown("""
    Welcome to our comprehensive application designed to enhance your productivity and learning experience. 
    This app offers three key features:

    ### 1. Course Management & AI Assistance
    - **Add and Manage Courses**: Easily add new courses, ensuring no duplicates.
    - **Select and View Content**: Browse and view AI-generated content from selected courses, modules, and sub-modules.
    - **Keyword Extraction**: Automatically highlights relevant keywords from content.
    - **Chatbot Integration**: Provides an interactive chatbot for additional support based on selected content.
    - **Organized Layout**: Includes a sidebar for easy navigation and a main area for content display.

    ### 2. Notes Management System
    - **Create New Notes**: Users can enter a title and content for new notes, saved as files.
    - **Edit Existing Notes**: Modify titles and content of existing notes.
    - **Delete Notes**: Remove unwanted notes, deleting their respective files.
    - **Full-Size Editor**: Utilizes custom CSS for a full-size Quill editor.
    - **Note Management**: Manage all notes in expandable sections for easy viewing and editing.

    ### 3. Python Code Interpreter
    - **Dynamic Theme Selection**: Choose from a variety of themes, including popular ones like "monokai" and "dracula."
    - **Code Editor**: An interactive editor with syntax highlighting for writing Python code.
    - **Execute Code**: Run Python code directly within the app and see the output immediately.
    - **Output Display**: View the results or errors of your executed code in a clean format.
    - **AI- Assistant**: Erros can be rectfied or explanations can be asked.

    Use the navigation on the left to explore these features.
    
    
    ### WORKS YET TO BE DONE
    -Auto response for a keyword when cliked\n
    -Keywords retrival method need to be changed\n
    -Need to work on Naviagtion Menu
    
    """)

    # Access pages using keys
    for page_name in pages:  # Iterate over page names (keys)
        current_page = pages[page_name]  # Get the corresponding StreamlitPage
        # (Optional) Perform actions with current_page if needed

if __name__ == "__main__":
    main()