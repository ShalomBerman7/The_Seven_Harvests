from csv import reader
from io import StringIO
from fastapi import UploadFile, FastAPI
import uvicorn

app = FastAPI()


@app.post('/assignWithCsv')
def upload_csv(file: UploadFile):
    if file.content_type != 'text/csv':
        return {'error': 'File must be a CSV'}

    content = file.file.read().decode('utf-8')

    read = reader(StringIO(content))
    header = next(read)
    rows = list(read)

    list_of_soldiers = []

    for line in rows:
        list_of_soldiers.append(line)
    print(list_of_soldiers)

    return {'message': f'Successfully processed CSV with {len(rows)} rows',
            'list_of_soldiers': list_of_soldiers}
