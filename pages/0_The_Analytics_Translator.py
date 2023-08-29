import streamlit as st
import streamlit.components.v1 as components

 # Render a Markdown File
with open(f'content/Analytics_Translator_Intro.md', 'r') as f:
     st.markdown(f.read())

# embed html file
with open(f'content/Analytics_Translator_Wheel.html', 'r') as f:
     components.html(f.read(),width=1200,height=1000,scrolling=True)


st.markdown(' ### The the full article and webpage')
# embed homepage
components.iframe('https://theanalyticstranslator.org',height=800,scrolling=True)


    
