import streamlit as st
import time

# Sample dataset: Dictionary simulating a College MIS FAQ
chatbot_data = {
    "what is college name?": "CPSP College of Physicians and Surgeons Islamabad.",
    "what are the admission criteria?": "Admission criteria include entrance exam scores and previous academic records.",
    "how to apply for scholarships?": "You can apply for scholarships through the college portal or by contacting the scholarship office.",
    "what courses are offered?": "Our college offers courses in engineering, business, arts, and more.",
    "how can i access my grades?": "Grades can be accessed via the student portal using your login credentials.",
    "what is the fee structure?": "The fee structure is detailed on the college website under the 'Fee Structure' section."
}

def get_answer(user_question: str) -> str:
    """
    Attempts to match the user's question to one of the keys in the chatbot_data dictionary.
    Matching is done in a case-insensitive manner.
    """
    normalized_question = user_question.strip().lower()
    return chatbot_data.get(normalized_question, None)

def main():
    st.title("College MIS Chatbot")
    st.write("Welcome to the College MIS chatbot. Ask your questions about our college system below.")

    # Initialize conversation history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Chat input form inside a form container
    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Your message:")
        submit_button = st.form_submit_button(label="Send")

    if submit_button and user_input:
        # Append user's message to conversation history
        st.session_state.messages.append({"role": "user", "content": user_input})

        # Generate the bot's response
        answer = get_answer(user_input)
        if not answer:
            answer = "I'm sorry, I don't have an answer to that question."
        
        # Simulate a short delay (like the bot is thinking)
        time.sleep(0.5)
        
        st.session_state.messages.append({"role": "bot", "content": answer})

    # Display conversation history
    for msg in st.session_state.messages:
        role = msg["role"]
        content = msg["content"]
        if role == "user":
            st.markdown(
                f"<div style='text-align: right; background-color: #DCF8C6; padding: 8px; border-radius: 10px; display: inline-block; margin: 4px 0;'>"
                f"**You:** {content}</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"<div style='text-align: left; background-color: #F1F0F0; padding: 8px; border-radius: 10px; display: inline-block; margin: 4px 0;'>"
                f"**Bot:** {content}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
