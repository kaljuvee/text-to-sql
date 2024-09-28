# Streamlit LangChain SQL Generator

This application uses Streamlit and LangChain to generate SQL queries from natural language input and execute them against a PostgreSQL database.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- A PostgreSQL database
- An OpenAI API key

## Installation

1. Clone this repository or download the source code.

2. Navigate to the project directory:
   ```
   cd path/to/project
   ```

3. (Optional but recommended) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Configuration

1. Ensure you have a PostgreSQL database set up and accessible.

2. Have your OpenAI API key ready. If you don't have one, you can obtain it from the [OpenAI website](https://beta.openai.com/account/api-keys).

## Running the Application

1. Make sure you're in the project directory and your virtual environment is activated (if you're using one).

2. Run the Streamlit app:
   ```
   streamlit run sql_generator_app.py
   ```

3. Your default web browser should open automatically with the app. If it doesn't, you can manually open the URL displayed in the terminal (usually `http://localhost:8501`).

## Using the Application

1. In the sidebar, enter your PostgreSQL database URI. It should be in the format:
   ```
   postgresql://username:password@host:port/database
   ```

2. Enter your OpenAI API key in the sidebar.

3. (Optional) Click "View Database Schema" to see the structure of your database.

4. Enter your query in natural language in the text area provided.

5. Click "Generate SQL" to create an SQL query based on your input.

6. Review and optionally modify the generated SQL query.

7. Click "Execute SQL" to run the query and view the results.

## Notes

- Keep your database URI and OpenAI API key confidential.
- This application is for demonstration purposes and may need additional security measures for production use.
- Ensure you have the necessary permissions to read from (and potentially write to) your database.

## Troubleshooting

If you encounter any issues:
- Ensure all prerequisites are installed correctly.
- Check that your database URI and OpenAI API key are entered correctly.
- Verify that your database is accessible from your current network.
- Check the console output for any error messages.

For further assistance, please open an issue in the project repository.
