import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables from .env file
load_dotenv()

# Get database credentials from environment variables
db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASSWORD')
db_host = os.environ.get('DB_HOST')
db_port = os.environ.get('DB_PORT')
db_name = os.environ.get('DB_NAME')

# Construct the PostgreSQL connection string
db_connection_str = f'postgresql+psycopg2://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

# Create the SQLAlchemy engine
try:
    db_connection = create_engine(db_connection_str)
    print("Database connection established successfully (using .env).")
except Exception as e:
    print(f"Error: Could not connect to the database.  Check environment variables and database settings. Error: {e}")
    # It's good practice to stop if the database connection fails.
    exit()

# You can add a function to get the engine, if needed.
def get_db_connection():
    return db_connection

if __name__ == '__main__':
    #test the connection
    connection = get_db_connection()
    try:
        connection.connect()
        print("connection is working")
    except Exception as e:
        print(e)
    finally:
        connection.dispose()