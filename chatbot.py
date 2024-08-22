import streamlit as st
from api_service import get_chat_completion
from helper import find_top_rated_videos
from config import youtube_api_key


# Ensure the session state is initialized
if 'bot_response' not in st.session_state:
    st.session_state.bot_response = ""

def chatbot(selected_course, selected_module, selected_sub_module,keywords):
    index = selected_sub_module.find(":")
    if index != -1:
        selected_sub_module = selected_sub_module[index + 1:].strip()
    
    st.subheader(f"Clear Your Doubts on {selected_sub_module} in {selected_course}")

    user_input = st.text_input("Ask your question:")

    if st.button("Send"):
        if user_input:
            st.session_state.bot_response = get_chat_completion(user_input)
        else:
            st.write("Please enter a question.")

    if st.button("Clear Response"):
        st.session_state.bot_response = ""

    if st.session_state.bot_response:
        st.write("**Bot Response:**")
        st.write(st.session_state.bot_response)

    if st.button("Facing difficulties? Watch a tutorial"):
        # Construct the topic based on submodule and course
        topic = f"{selected_sub_module} in {selected_course}"
        top_videos = find_top_rated_videos(youtube_api_key, [topic])
        
        if isinstance(top_videos, str):
            st.error(top_videos)
        else:
            for concept, videos in top_videos.items():
                st.write(f"**Tutorials for '{concept}':**")
                for video in videos:
                    st.write(f"**{video['title']}**")
                    st.write(f"Channel: {video['channel_name']}")
                    st.write(f"Uploaded on: {video['date_uploaded']}")
                    st.write(f"[Watch Video]({video['url']})")
                    st.video(video['url'])

    

    # Render keywords inside the expander
    if keywords:
        st.subheader("Keywords")
        long_keywords = [k for k in keywords if len(k) > 20]
        short_keywords = [k for k in keywords if len(k) <= 20]

        if long_keywords:
            for keyword in long_keywords:
                cleaned_keyword = keyword.replace(":", "")
                if st.button(f"{cleaned_keyword}", key=f"long_keyword_{cleaned_keyword}", help="Click to select"):
                    st.session_state.selected_keyword = cleaned_keyword
                    # No need to rerun; the input box value is directly updated

        if short_keywords:
            buttons_per_row = 2
            num_rows = (len(short_keywords) + buttons_per_row - 1) // buttons_per_row

            for row in range(num_rows):
                cols = st.columns(buttons_per_row)
                for col in range(buttons_per_row):
                    index = row * buttons_per_row + col
                    if index < len(short_keywords):
                        keyword = short_keywords[index]
                        cleaned_keyword = keyword.replace(":", "")
                        with cols[col]:
                            if st.button(f"{cleaned_keyword}", key=f"short_keyword_{cleaned_keyword}_{index}", help="Click to select"):
                                st.session_state.selected_keyword = cleaned_keyword
                                # No need to rerun; the input box value is directly updated

# Ensure this script is run directly
if __name__ == "__main__":
    st.title("Chatbot and Tutorial Finder")
