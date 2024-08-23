import streamlit as st
from dotenv import load_dotenv
import logging
from chatbot import chatbot  # Ensure chatbot is properly defined in chatbot.py
from api_service import get_course_syllabus_beginner, get_chat_completion  # Ensure these functions are defined in api_service.py

# Load environment variables
load_dotenv()

# Set up logging
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Set page configuration

# Initialize session state variables
def initialize_session_state():
    if "bot_response" not in st.session_state:
        st.session_state["bot_response"] = ""
    if 'modules' not in st.session_state:
        st.session_state.modules = {}
    if 'ai_content' not in st.session_state:
        st.session_state.ai_content = {}
    if 'courses' not in st.session_state:
        st.session_state.courses = ["Python", "Java", "C++"]
    if 'clicked_text' not in st.session_state:
        st.session_state.clicked_text = ""

# Ensure initialization happens before any access to session_state


def get_modules_and_sub_modules(course):
    if course not in st.session_state.modules:
        default_modules = get_course_syllabus_beginner(course)
        st.session_state.modules[course] = default_modules if default_modules else {}
    return st.session_state.modules[course]

def generate_ai_content(course, sub_module):
    if course not in st.session_state.ai_content:
        st.session_state.ai_content[course] = {}
    if sub_module not in st.session_state.ai_content[course]:
        content = get_chat_completion(f"{sub_module} in {course}")
        st.session_state.ai_content[course][sub_module] = content
    return st.session_state.ai_content[course][sub_module]

def add_course(course_name):
    if course_name and course_name not in st.session_state.courses:
        st.session_state.courses.append(course_name)
        st.success(f"Course '{course_name}' added successfully!")
    elif not course_name:
        st.error("Course name cannot be empty.")
    else:
        st.error(f"Course '{course_name}' already exists.")

def extract_keywords(content):
    import re

    pattern = r'\*\*(.*?)\*\*'
    all_keywords = re.findall(pattern, content)

    irrelevant_words = {"introduction", "conclusion", "explanation", "like", "kind", "words", "and", "the", "is", "a", "an", "of", "to", "in", "for", "on", "with", "by", "or", "as", "at", "that", "this", "are", "was", "were", "be", "has", "have", "had", "do", "does", "did", "will", "shall", "may", "might", "could", "should", "must", "would", "about", "below", "above", "before", "after", "during", "between", "among", "where", "when", "who", "whom", "whose", "which", "what", "how", "why", "then", "now", "there", "here", "such", "these", "those", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "books", "online coursers", "courses", "course", "tutorial", "tutorials", "tutor", "tutors", "tips and tricks", "tips", "tricks", "trick", "tip", "guide", "guides", "guidance", "guidances", "manual", "manuals", "conclusion"}

    specific_date_terms = {"today", "yesterday", "tomorrow", "this week", "last week", "next week", "this month", "last month", "next month", "this year", "last year", "next year"}

    def is_date_or_time(value):
        date_patterns = [
            r'\b\d{4}-\d{2}-\d{2}\b',
            r'\b\d{2}/\d{2}/\d{4}\b',
            r'\b\d{2}-\d{2}-\d{2}\b',
            r'\b\d{2} \w{3} \d{4}\b',
            r'\b\d{4}\b',
        ]
        time_patterns = [
            r'\b\d{2}:\d{2}\b',
            r'\b\d{2}:\d{2}:\d{2}\b',
        ]
        
        all_patterns = date_patterns + time_patterns

        for pattern in all_patterns:
            if re.fullmatch(pattern, value):
                return True
        return False

    def is_number(value):
        return re.fullmatch(r'\d+', value) is not None

    relevant_keywords = [
        kw for kw in all_keywords
        if kw.lower() not in irrelevant_words
        and kw.lower() not in specific_date_terms
        and not is_date_or_time(kw)
        and not is_number(kw)
    ]

    return relevant_keywords

def main():
    initialize_session_state()
    st.set_page_config(page_title="Python Tutor App", layout="wide")

    col1, col2 = st.columns([3, 2])

    with st.sidebar:
        st.title("Courses and Modules")
        st.subheader("Add a Course")
        new_course = st.text_input("Course Name")
        if st.button("Add Course", key="add_course_button"):
            add_course(new_course)

        selected_course = st.selectbox("Select a course", st.session_state.courses, key="course_selector")
        modules = get_modules_and_sub_modules(selected_course)

        if modules:
            selected_module = st.selectbox("Select a module", list(modules.keys()), key="module_selector")
            selected_sub_module = st.selectbox("Select a sub-module", modules.get(selected_module, []), key="sub_module_selector")
        else:
            selected_module = ""
            selected_sub_module = ""

    with col1:
        st.title(selected_course)
        if selected_sub_module:
            content = generate_ai_content(selected_course, selected_sub_module)
            keywords = extract_keywords(content)
            st.markdown(content, unsafe_allow_html=True)
        else:
            st.write("Please select a sub-module.")

    with col2:
        with st.expander("Chat Bot", expanded=True):
            if selected_sub_module:
                keywords = extract_keywords(generate_ai_content(selected_course, selected_sub_module))
                chatbot(selected_course, selected_module, selected_sub_module, keywords)
            else:
                st.write("Please select a sub-module.")

if __name__ == "__main__":
    main()
