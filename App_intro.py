import openai
import streamlit as st


# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

#with st.sidebar:
  # openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
  # "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    

st.title("💬Overview Of Your Personalized Assistant")
# Initial page config



#######################################
# 2 COLUMN View for quick overview
#######################################
col1, col2= st.columns(2)

    #######################################
    # COLUMN 1
    #######################################
    

col1.subheader('General setup & info ')
col1.markdown('''THE APP HERE IS FOR EDUCATIONAL PURPOSE, NO SERVICE GUARANTESS''')
col1.markdown('''ATTENTION: When chainging the a APP in the sidebar history and key is delete. 
              Some of the apps requrie a local storage of information. No intention to store history/input for long run, typically the app reboots frequently with full loss of history. 
              The source code is on [GITHUB](https://github.com/kienlef/streamlit-agents-frank), deployed on streamlit''')
col1.markdown('''[Get an OpenAI API key](https://platform.openai.com/account/api-keys)''')
col1.markdown('''[Always Check your OPENAI usage](https://platform.openai.com/account/usage)''')

col1.subheader('Credits go to:')
col1.markdown('''[BASE ORIGIN OF THIS APPS](https://github.com/langchain-ai/streamlit-agent)''')
col1.markdown('''[SteamLit the Cool Stuf for Analytics Deployment](https://streamlit.io)''')
col1.markdown('''[Langchain the framework behind](https://www.langchain.com)''')
col1.markdown('''[OPEN AI - CHAT GPT API](https://openai.com/chatgpt)''')          

    
    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets

col2.subheader('Why should you care')
col2.markdown('''The Analytics translators''')
col2.markdown('''We have the goal of integrating analytics capabilities in a company. 
              We should identify value cases for the business and help deploy data-driven applications 
              to support or automate intelligent decision-making.''')
col2.markdown('''The role is new and yet to be well defined. 
              It should be clear that this role or related roles will continuously evolve, 
              and the role name might change. ''')


col2.markdown('''In part one we defined the exisiting core capabilities:
              [Udemy - The Analytics Translator](https://www.udemy.com/course/the-analytics-translator/?referralCode=C7867E8B4A33A7DD211C)''')
col2.markdown(''' An overview Article can be found here: [The Analytics Translator](https://theanalyticstranslator.org)''')
              
col2.markdown(''' In this part two, we'll delve deep into what the future holds for our workplaces, 
              shining a light on the latest trends. We will weave in discussions about the fascinating world 
              of generative AI. As always, we break down complex topics into easy-to-understand concepts and applications. ''')


    # Connect to data sources
    



    