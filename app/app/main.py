from flask import Flask
from flask import request
import pandas as pd
from flask_cors import CORS
from sqlalchemy import create_engine

engine = create_engine("postgresql://postgres:123@localhost:5432/helloworld")

app = Flask(__name__)
CORS(app)

conn = engine.connect()


@app.route("/upload_excel", methods=["POST"])
def UploadExcel():
    f = request.files["upload_excel"]
    data_xls = pd.read_excel(f)
    data_xls.to_sql("data", con=conn, if_exists="replace", index=False)
    return data_xls.to_json()


if __name__ == "__main__":
    app.run(debug=True)
