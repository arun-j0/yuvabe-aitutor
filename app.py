import streamlit as st

# Import page functions
from pages.course import main as COURSES_WITH_AI_ASSISTANCE
from pages.Interpreter import main as PYTHON_CODE_INTERPRETER
from pages.notes import main as NOTES_MANAGEMENT
from pages.home import main as HOME_PAGE
from pages.quiz import app as QUIZ_PAGE

def main():
    pages = [
        st.Page(HOME_PAGE, title="HOME"), 
        st.Page(COURSES_WITH_AI_ASSISTANCE, url_path="/courses",title="COURSES"),
        st.Page(NOTES_MANAGEMENT,url_path="/notes",title="NOTES"),
        st.Page(PYTHON_CODE_INTERPRETER,url_path="/interpretr",title="PYTHON INTERPRETER"),
        st.Page(QUIZ_PAGE,url_path="/quiz",title="QUIZ")
    ]
    
    pg = st.navigation(pages)
    pg.run()
    
   
    
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
    """)
    
if __name__ == "__main__":
    main()