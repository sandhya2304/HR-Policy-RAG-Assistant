


import streamlit as st
from hr_assistant.pipeline import ask,build_hr_assistant


st.set_page_config(page_title="HR policy assistant",page_icon=none)
st.title("HR policy assistant")
st.caption("Ask me any thins about the HR Policy")


@st.cache_resource(show_spinner="Setting up the assistat(only)")
def get_agent():
    return build_hr_assistant()


agent = get_agent()
if "messages" not in st.session_state:
    st.session_state.messages = []
    
#show the past conversation
for message in st.session_state.mesaages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
#get a new question from the user
question = st.chat_input("Ask a question about hr policy....")
if question:
    st.session_state.messages.apend({"role":"user","content":question})
    with st.chat_message("user"):
        st.markdown(question)
        
    with st.chat_message("assistant"):
        with st.spinner("Thinking...."):
            answer = ask(agent,question)
        st.markdown(answer)
    st.session_state.messages.append({"role":"assistant","content":answer})
        
