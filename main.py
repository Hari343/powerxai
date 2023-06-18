from flask import Flask

from db import get_reading, add_reading

app = Flask(__name__)


@app.post("/data")
def post_data():
    # TODO: parse incoming data, and save it to the database
    # data is of the form:
    #  {timestamp} {name} {value}

    return {"success": False}


@app.get("/data")
def get_data():
    # TODO: check what dates have been requested, and retrieve all data within the given range

    return {"success": False}


if __name__ == "__main__":
    app.run()
