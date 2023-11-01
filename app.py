import streamlit as st
from utils import query_agent
import asyncio


if 'OpenAI_API_Key' not in st.session_state:
    st.session_state['OpenAI_API_Key'] =''
    

st.title("Let's do some analysis on your CSV")

st.sidebar.title("😎🗝️")
st.session_state['OpenAI_API_Key']= st.sidebar.text_input("What's your OpenAI API key?", type="password")

done = st.sidebar.button("Add API key", key="load_button")

async def run_app( key=st.session_state['OpenAI_API_Key'] ):
    if done and key !="":
        #Proceed only if API keys are provided
    
    
        
        await st.header("Please upload your CSV file here:")
        
        # Capture the CSV file
        data = await st.file_uploader("Upload CSV file", type="csv")
        
        query = await st.text_area("Enter your query")
        button = await st.button("Generate Response")
        
        if button :
            # Get Response
            answer = await  query_agent(data=data, query=query, key= st.session_state['OpenAI_API_Key']  )
            await st.write(answer)


asyncio.run(run_app())
