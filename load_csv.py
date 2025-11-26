# from config import cursor, conn


def import_data(rows):
    with open("soldiers.csv", "w") as f:
        f.write(f'{rows}')
    return 'add '

# import_data('fjdksl00000000')

# def load_data():
#     filepath = "C:\\Users\\משתמש זה\\The_Seven_Harvests"
#     with open(filepath, encoding="utf-8") as f:  # פתיחה של הקובץ
#         reader = conn.reader(f)  # קריאה של הקובץ
#         next(reader)  # דילוג על שורה ראשונה
#
#         for row in reader:
#             cursor.execute("""INSERT INTO courses (
#             institution, city, address, course,
#             district, telephone, email)
#             VALUES (%s, %s, %s, %s, %s, %s, %s);""", row)
#         return 'data load.'
#
#
# load_data()
