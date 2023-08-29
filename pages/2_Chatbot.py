import openai
import streamlit as st

with st.sidebar:
    st.markdown('''The 💬 Chatbot has a history, clear it for starting new. 
                The prompting is simple chaining of the input passed to the selected model''')
    if ('OPENAIKEY' in st.secrets):
        st.success('OPEN AI Login credentials already provided!', icon='✅')
        openai_api_key = st.secrets['OPENAIKEY']
    else:
        openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
        "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"

   # selected_model = st.selectbox('Choose  OpenAI model', ['gpt-3.5-turbo', 'gpt-4'], key='selected_model')
    
    selected_model = st.radio("Choose OpenAI model 👇", ["gpt-3.5-turbo", "gpt-4"])
    


st.title("💬 Chatbot")

if "messages" not in st.session_state or st.sidebar.button("Clear conversation history"):
    st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    if not openai_api_key:
        st.info("Please add your OpenAI API key to continue.")
        st.stop()

    openai.api_key = openai_api_key
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = openai.ChatCompletion.create(model=selected_model, messages=st.session_state.messages)
    msg = response.choices[0].message
    st.session_state.messages.append(msg)
    st.chat_message("assistant").write(msg.content)
    st.chat_message("assistant").write('the current used model is: '+selected_model)
