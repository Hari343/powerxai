from datetime import datetime
import time
from typing import List

from db import Database


class RequestHandler:
    def __init__(self):
        self.db = Database()

    def store_data(self, data: str) -> bool:
        for reading in data.split("\r\n"):
            fragments = reading.split(" ")
            self.db.write(int(fragments[0]), fragments[1], float(fragments[2]))

        return True  # this db op will always succeed as we are using in-memory db.

    def get_data(self, start: str, end: str) -> List:
        start = time.mktime(datetime.strptime(start, "%Y-%m-%d").timetuple())
        end = time.mktime(datetime.strptime(end, "%Y-%m-%d").timetuple())

        return self.process_data(self.db.query_range(int(start), int(end)))

    @staticmethod
    def process_data(data: List) -> List:
        if not data:
            return []

        out = []
        current_date, average_readings = None, {"current": [], "voltage": []}

        for reading in data:
            timestamp, curr_and_volt = reading
            datetime_string = datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S.%f')[:-3]
            date = datetime_string.split(" ")[0]
            for key in curr_and_volt:
                out.append({"time": datetime_string, "name": key, "value": curr_and_volt[key]})

            if date == current_date or current_date is None:
                average_readings["current"].append(curr_and_volt.get("current", 0))
                average_readings["voltage"].append(curr_and_volt.get("voltage", 0))
            else:
                out.append({"time": current_date, "name": "power",
                            "value": (sum(average_readings["current"]) / len(average_readings["current"])) * (
                                    sum(average_readings["voltage"]) / len(average_readings["voltage"]))})
                average_readings["current"].clear()
                average_readings["voltage"].clear()

            current_date = date

        if average_readings["current"] and average_readings["voltage"]:
            out.append({"time": current_date, "name": "power",
                        "value": (sum(average_readings["current"]) / len(average_readings["current"])) * (
                                    sum(average_readings["voltage"]) / len(average_readings["voltage"]))})

        return out









