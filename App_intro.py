import openai
import streamlit as st


# Use the full page instead of a narrow central column
st.set_page_config(layout="wide")

with st.sidebar:
   openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
   "[Get an OpenAI API key](https://platform.openai.com/account/api-keys)"
    #"[View the source code](https://github.com/streamlit/llm-examples/blob/main/Chatbot.py)"
    

st.title("💬Overview Of Your Personalized Assistant")
# Initial page config

st.text('The purpose of this app is to perpare and play with the future concepts of personalized assistens. It is part of the lecture series of THE ANALYTICS TRANSLATROR')


#######################################
# 2 COLUMN View for quick overview
#######################################
col1, col2= st.columns(2)

    #######################################
    # COLUMN 1
    #######################################
    

col1.subheader('General setup ')
col1.markdown("[Get an OpenAI API key](https://platform.openai.com/account/api-keys)")
col1.text('API looks like: \n sk-6PDrhh0j5zHe45MRAwK7T3BlbkFJG5KMzGhVX00eaHk45W')
col1.text('run locally: streamlit run app.py')
          


col1.subheader('Display text')
col1.code('''
st.text('Fixed width text')
st.markdown('_Markdown_') # see #*
st.caption('Balloons. Hundreds of them...')
st.latex(r\'\'\' e^{i\pi} + 1 = 0 \'\'\')
st.write('Most objects') # df, err, func, keras!
st.write(['st', 'is <', 3]) # see *
st.title('My title')
st.header('My header')
st.subheader('My sub')
st.code('for i in range(8): foo()')

# * optional kwarg unsafe_allow_html = True

''')

    
    #######################################
    # COLUMN 2
    #######################################

    # Display interactive widgets

col2.subheader('Display interactive widgets')
col2.code('''
st.button('Hit me')
st.data_editor('Edit data', data)
st.checkbox('Check me out')
st.radio('Pick one:', ['nose','ear'])
st.selectbox('Select', [1,2,3])
st.multiselect('Multiselect', [1,2,3])
st.slider('Slide me', min_value=0, max_value=10)
st.select_slider('Slide to select', options=[1,'2'])
st.text_input('Enter some text')
st.number_input('Enter a number')
st.text_area('Area for textual entry')
st.date_input('Date input')
st.time_input('Time entry')
st.file_uploader('File uploader')
st.download_button('On the dl', data)
st.camera_input("一二三,茄子!")
st.color_picker('Pick a color')
           ''')


    # Connect to data sources
    



    