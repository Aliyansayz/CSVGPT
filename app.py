import streamlit as st
from dotenv import load_dotenv

from langchain.llms import OpenAI
import pandas as pd
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent


st.title('Analyzer App')

# openai_api_key = st.sidebar.text_input('OpenAI API Key')
# OpenAI (openai_api_key=key)

def generate_response(input_text, data, key):

    load_dotenv()
    df = pd.read_csv(data) 
    llm = OpenAI( )
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)
    st.info(agent.run(input_text))


with st.form('my_form'):
    
  data =  st.file_uploader("Upload CSV file :", type="csv")
  text = st.text_area('')
  submitted = st.form_submit_button('Analyze CSV')
  
  if submitted :
    generate_response(text, data )
