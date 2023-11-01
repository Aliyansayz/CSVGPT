import streamlit as st
from utils import query_agent
from utils import init_llm


if 'OpenAI_API_Key' not in st.session_state:
    st.session_state['OpenAI_API_Key'] =''
    

st.title("Let's do some analysis on your CSV")

st.sidebar.title("😎🗝️")
st.session_state['OpenAI_API_Key']= st.sidebar.text_input("What's your OpenAI API key?", type="password")

done = st.sidebar.button("Add API key", key="load_button")


if done and st.session_state['OpenAI_API_Key'] !="":
    #Proceed only if API keys are provided

        llm = init_llm(key= st.session_state['OpenAI_API_Key'] )


if llm :
    
    st.header("Please upload your CSV file here:")
    
    # Capture the CSV file
    data = st.file_uploader("Upload CSV file",type="csv")
    
    query = st.text_area("Enter your query")
    button = st.button("Generate Response")

    if button :
        # Get Response
        answer =  query_agent(data=data, query=query, llm=llm )
        st.write(answer)
