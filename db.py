from typing import List


class Database:
    def __init__(self):
        self.data = {}  # timestamp: {"voltage": float, "current": float}

    def write(self, timestamp: int, metric: str, val: float) -> None:
        metric = metric.lower()
        if timestamp in self.data:
            self.data[timestamp][metric] = val
        else:
            self.data[timestamp] = {metric: val}

    def get(self, timestamp: int) -> dict:
        return self.data.get(timestamp, {})

    def query_range(self, start: int, end: int) -> List:
        out = []
        for key, val in sorted(self.data.items(), key=lambda x: x[0]):
            if key > end:
                break

            if key < start:
                continue

            out.append((key, val))

        return out




