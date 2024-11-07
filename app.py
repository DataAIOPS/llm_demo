from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

genai.configure(api_key="AIzaSyDC-VVtwwTknm8vbXVHGdr8PaVnrYN3oIM")

def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    query = model.generate_content([prompt[0],question])
    return query.text

def read_sql_query(sql,db):
    conn = sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.commit()
    conn.close()
    return rows

# define prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name llm_demo and has the following columns - River_Name, Length_km, Origin, Mouth, 
    States_Flowing_Through \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM llm_demo ;
    \nExample 2 - Tell me all the River_Name having lenght greater than 1500Km?, 
    the SQL command will be something like this SELECT * FROM llm_demo where  Length_km > 1500; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """
]

## Streamlit App
st.set_page_config(page_title="Retrieve SQL queries")
st.header("Retrieve SQL Data Using Gemini App")

question = st.text_input("Input: ",key=input)

submit = st.button("Enter Your Question")

if submit:
    query = get_gemini_response(question,prompt)
    print(question)
    print(query)
    response=read_sql_query(query,'llm_demo.db')
    st.subheader("The response for your question is")
    for row in response:
        st.header(row)
