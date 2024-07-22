import os
from apikey import api_key 
import streamlit as st
from langchain_openai import OpenAI
from langchain.chains import LLMChain, SimpleSequentialChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

os.environ["OPENAI_API_KEY_TEMP"]=api_key
st.title('Medium Article Generator')
topic = st.text_input('Input your topic of interest')
title_template = PromptTemplate(
    input_variables=['topic'],
    template='Give me medium article title on {topic}'
)
article_template = PromptTemplate(
    input_variables=['title'],
    template='Give me medium article for {title} including title'
)
llm = OpenAI(temperature=0.9)
llm2 = ChatOpenAI(model_name='gpt-4',temperature=0.9)
title_chain = LLMChain(llm=llm,prompt=title_template, verbose = True)
article_chain = LLMChain(llm=llm2,prompt=article_template,verbose=True)
overall_chain = SimpleSequentialChain(chains=[title_chain,article_chain],verbose = True)
if topic:
    response = overall_chain.invoke(topic)
    st.write(response['output'])

