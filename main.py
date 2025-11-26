from API_server import app, upload_csv
import uvicorn
from create_db_and_tables.create_tables import create_db_and_tables
from create_db_and_tables.add_to_tables import add_soldier, get_status_soldier



if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
    create_db_and_tables()

    print(upload_csv())
    for i in upload_csv():
        add_soldier(upload_csv['list_of_soldiers'][5], upload_csv['list_of_soldiers'][4],
                    upload_csv['list_of_soldiers'][3], upload_csv['list_of_soldiers'][2],
                    upload_csv['list_of_soldiers'][1], upload_csv['list_of_soldiers'][0])
