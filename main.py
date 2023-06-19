import json

from flask import Flask, request
from request_handler import RequestHandler

app = Flask(__name__)

request_handler = RequestHandler()


def validate_input(data: str) -> bool:
    try:
        for reading in data.split("\r\n") if "\r\n" in data else data.split("\n"):
            fragments = reading.split(" ")
            if len(fragments) != 3:
                return False

            if not fragments[0].isnumeric() or fragments[1].lower() not in ("current", "voltage") or \
                    not fragments[2].replace(".", "").isnumeric():
                return False
    except Exception as e:
        print(e.args[0])
        return False

    return True


@app.route("/data", methods=["GET", "POST"])
def handle_request():
    if request.method == "POST":
        # data is of the form:
        #  {timestamp} {name} {value}
        data = request.data.decode("utf-8")

        if not validate_input(data):
            return {"success": False}
        else:
            request_handler.store_data(data)
            return {"success": True}

    else:
        args = request.args
        out = request_handler.get_data(args.get("from"), args.get("to"))
        return json.dumps(out)


if __name__ == "__main__":
    app.run()
