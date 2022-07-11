# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from flask import Flask
from flask import request
import pandas as pd
from flask_cors import CORS
from sqlalchemy import create_engine
engine = create_engine('postgresql://postgres:123@localhost:5432/helloworld')

app = Flask(__name__)
CORS(app)

conn=engine.connect()

@app.route('/upload_excel',methods=["POST"])
def UploadExcel():
    f=request.files['upload_excel']
    data_xls=pd.read_excel(f)
    data_xls.to_sql('data',con=conn,if_exists='replace',index=False)
    return data_xls.to_json()


if __name__ == '__main__':
    app.run(debug=True)