from API_server import app, upload_csv
import uvicorn
from create_db_and_tables.create_tables import create_db_and_tables




if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
    create_db_and_tables()