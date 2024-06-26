import streamlit as st
from bot.chatbot import ChatBot


def welcome_sidebar():
    with st.sidebar:
            # st.image("assets/ai_bot.jpg")
            st.markdown(
                "🧙‍♂️✨ Introducing CarsNodi.ai 🚗, your personal AI assistant for navigating the vast world of automobiles in India. Seamlessly integrating LLMs, CarsNodi.ai empowers users to explore and select from an extensive range of cars offered by leading manufacturers across the country. Whether you're seeking performance, comfort, or eco-friendliness, CarsNodi.ai is your trusted companion, providing expert guidance to help you find the perfect vehicle tailored to your preferences and needs.🌟"
            )
            st.markdown("---")
            # st.image("assets/tw-logo.png")
            
def display_chat(user):
    if "bot" not in st.session_state.keys():
        st.session_state["bot"] = ChatBot(user)
        response = st.session_state["bot"].get_response("start the conversation", context_needed=False)
        st.session_state.messages = [{"role": "assistant", "content": response}]
    
    # if "messages" not in st.session_state.keys():
    #     response = st.session_state["bot"].get_response("start the conversation")
    #     st.session_state.messages = [{"role": "assistant", "content": response}]
        
    # Display or clear chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    # User-provided prompt
    if prompt := st.chat_input():
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            print(prompt)

    # Generate a new response if last message is not from assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state["bot"].get_response(prompt, context_needed=True)
                placeholder = st.empty()
                full_response = ''
                for item in response:
                    full_response += item
                    placeholder.markdown(full_response)
                placeholder.markdown(full_response)
        message = {"role": "assistant", "content": full_response}
        st.session_state.messages.append(message)
# welcome_sidebar()
# display_chat()