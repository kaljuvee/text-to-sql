import streamlit as st
from langchain.utilities import SQLDatabase
from langchain.chains import create_sql_query_chain
from langchain.llms import OpenAI
from sqlalchemy import create_engine, inspect
import pandas as pd
import os

# Streamlit app
st.title("Text to SQL Query Generator")

# Sidebar for database connection
st.sidebar.header("Database Connection")
db_uri = st.sidebar.text_input("PostgreSQL Alchemy URI", type="password")

# OpenAI API key input
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
os.environ["OPENAI_API_KEY"] = openai_api_key

# Main app logic
if db_uri and openai_api_key:
    try:
        # Create SQLAlchemy engine
        engine = create_engine(db_uri)
        
        # Create LangChain SQLDatabase object
        db = SQLDatabase.from_uri(db_uri)
        
        # Create OpenAI language model
        llm = OpenAI(temperature=0, verbose=True)
        
        # Create SQL query chain
        db_chain = create_sql_query_chain(llm, db)

        # Button to view schema
        if st.button("View Database Schema"):
            inspector = inspect(engine)
            schema_info = []
            for table_name in inspector.get_table_names():
                columns = [{"name": col["name"], "type": str(col["type"])} 
                           for col in inspector.get_columns(table_name)]
                schema_info.append({"table": table_name, "columns": columns})
            
            st.json(schema_info)

        # Text input for natural language query
        user_input = st.text_area("Enter your query in natural language:")

        # Button to generate SQL query
        if st.button("Generate SQL"):
            if user_input:
                try:
                    # Generate SQL query
                    result = db_chain.invoke({"question": user_input})
                    
                    # Display the generated SQL
                    st.subheader("Generated SQL Query:")
                    st.text_area("SQL Query", value=result, height=150)
                    
                    # Store the generated SQL in session state
                    st.session_state.generated_sql = result
                
                except Exception as e:
                    st.error(f"Error generating SQL: {str(e)}")
            else:
                st.warning("Please enter a query.")

        # Text area for SQL query (populated with generated SQL if available)
        sql_query = st.text_area("SQL Query", value=st.session_state.get('generated_sql', ''), height=150)

        # Button to execute SQL query
        if st.button("Execute SQL"):
            if sql_query:
                try:
                    # Execute the SQL query
                    df = pd.read_sql_query(sql_query, engine)
                    
                    # Display the result
                    st.subheader("Query Result:")
                    st.dataframe(df)
                
                except Exception as e:
                    st.error(f"Error executing SQL: {str(e)}")
            else:
                st.warning("Please enter an SQL query to execute.")

    except Exception as e:
        st.error(f"Error connecting to database: {str(e)}")
else:
    st.warning("Please enter both the PostgreSQL Alchemy URI and OpenAI API Key in the sidebar.")
