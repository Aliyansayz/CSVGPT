import streamlit as st
from utils import query_agent


if 'OpenAI_API_Key' not in st.session_state:
    st.session_state['OpenAI_API_Key'] =''
    

st.title("Let's do some analysis on your CSV")

st.sidebar.title("😎🗝️")
st.session_state['OpenAI_API_Key']= st.sidebar.text_input("What's your OpenAI API key?", type="password")

done = st.sidebar.button("Add API key", key="load_button")

def run_app( key=st.session_state['OpenAI_API_Key'] ):
    if done and key !="":
        #Proceed only if API keys are provided
    
    
        
        st.header("Please upload your CSV file here:")
        
        # Capture the CSV file
        data =  st.file_uploader("Upload CSV file", type="csv")
        
        query =  st.text_area("Enter your query")
        button =  st.button("Generate Response")
        
        if button :
            # Get Response
            answer =   query_agent(data=data, query=query, key= st.session_state['OpenAI_API_Key']  )
            st.info(answer)


