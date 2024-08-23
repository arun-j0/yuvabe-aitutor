import streamlit as st

# Import page functions
from pages.course import  main as COURSES_WITH_AI_ASSISTANCE
from pages.Interpreter import main as PYTHON_CODE_INTERPRETER
from pages.notes import main as NOTES_MANAGEMENT
from pages.home import main as HOME_PAGE
from pages.quiz import main as QUIZ_PAGE

def main():
    pages = [
        st.Page(HOME_PAGE, title="HOME"), 
        st.Page(COURSES_WITH_AI_ASSISTANCE, url_path="/courses",title="COURSES"),
        st.Page(NOTES_MANAGEMENT,url_path="/notes",title="NOTES"),
        st.Page(PYTHON_CODE_INTERPRETER,url_path="/interpreter",title="PYTHON INTERPRETER"),
        st.Page(QUIZ_PAGE,url_path="/quiz",title="QUIZ")
    ]

    pg = st.navigation(pages)
    pg.run()
    
    

if __name__ == "__main__":
    main()