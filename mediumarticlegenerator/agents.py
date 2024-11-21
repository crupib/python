import os
from apikey import api_key 
from langchain import hub
from langchain_openai import OpenAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_community.agent_toolkits.load_tools import load_tools
os.environ["OPENAI_API_KEY_TEMP"]=api_key
llm = OpenAI(temperature=0.0)
tools = load_tools(['wikipedia','llm-math'],llm)
prompt = hub.pull("hwchase17/react")
agent = create_react_agent(llm,tools,prompt)
agent_executor=AgentExecutor(agent=agent,tools=tools,verbose=True)
answer = input('Input Wikipedia Research Task\n')
agent_executor.invoke({'input':answer})