# from langchain.agents import create_pandas_dataframe_agent
from langchain_experimental.agents.agent_toolkits.pandas.base import create_pandas_dataframe_agent
import pandas as pd
from langchain.llms import OpenAI

def init_llm(key):
    
    return OpenAI(openai_api_key=key)
  

def query_agent(data, query, llm):

    # Parse the CSV file and create a Pandas DataFrame from its contents.
    df = pd.read_csv(data)

    
    # Create a Pandas DataFrame agent.
    agent = create_pandas_dataframe_agent(llm, df, verbose=True)

    #Python REPL: A Python shell used to evaluating and executing Python commands. 
    #It takes python code as input and outputs the result. The input python code can be generated from another tool in the LangChain
    return agent.run(query)
