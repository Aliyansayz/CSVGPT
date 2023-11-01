import streamlit as st
from utils import query_agent

if 'OpenAI_API_Key' not in st.session_state:
    st.session_state['OpenAI_API_Key'] =''
    

st.title("Let's do some analysis on your CSV")

st.session_state['OpenAI_API_Key']= st.sidebar.text_input("What's your OpenAI API key?",type="password")

done = st.sidebar.button("Add API key", key="done")

if done:
    #Proceed only if API keys are provided
    if st.session_state['OpenAI_API_Key'] !="" :


        st.header("Please upload your CSV file here:")
        
        # Capture the CSV file
        data = st.file_uploader("Upload CSV file",type="csv")
        
        query = st.text_area("Enter your query")
        button = st.button("Generate Response")
    
        if button and st.session_state['OpenAI_API_Key'] !="" :
            # Get Response
            answer =  query_agent(data, query, OpenAI_API_Key )
            st.write(answer)
