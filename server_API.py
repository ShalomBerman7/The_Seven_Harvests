from csv import reader
from io import StringIO
from fastapi import UploadFile, FastAPI
import uvicorn
# from sorting import selection_sort
from load_csv import import_data


app = FastAPI()



@app.post('/assignWithCsv')
def upload_csv(file: UploadFile):
    if file.content_type != 'text/csv':
        return {'error': 'File must be a CSV'}

    content = file.file.read().decode('utf-8')

    read = reader(StringIO(content))
    header = next(read)
    rows = list(read)

    for line in rows:
        import_data(str(line))
    #     print(line)

    return {
        'filename': file.filename,
        'content_type': file.content_type,
        'total_rows': len(rows),
        'columns': header,
        'data': rows,
        'message': f'Successfully processed CSV with {len(rows)} rows'
    }


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8000)
