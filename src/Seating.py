import math
from math import floor


class Seating:
    OKCYAN = '\033[96m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    OKBLUE = '\033[94m'
    UNDERLINE = '\033[4m'
    OKGREEN = '\033[92m'

    def __init__(self, json):
        self.json = json
        self.y = self.json["seating_data"]['total_rows']
        self.x = self.json["seating_data"]['total_columns']  # off by one
        row_i = 0
        rows = self.json["seating_data"]["rows"]
        while row_i < len(self.json["seating_data"]["rows"]):
            if all(v is None for v in rows[row_i]["columns"]):
                self.json["seating_data"]["rows"].pop(row_i)
                continue

            print(rows[row_i]["row_label"], end=" ")
            rows[row_i]["columns"].reverse()
            seat_i = 0
            seats = rows[row_i]["columns"]
            while seat_i < len(rows[row_i]["columns"]):
                if seats[seat_i] is None:
                    self.json["seating_data"]["rows"][row_i]["columns"].pop(seat_i)
                    continue
                if seats[seat_i]["status"] != 0:
                    print(Seating.FAIL, end=" ")
                elif seats[seat_i]["area_id"] == "vip":
                    print(Seating.WARNING, end=" ")
                elif seats[seat_i]["area_id"] == "special":
                    print(Seating.OKCYAN, end=" ")
                elif seats[seat_i]["area_id"] == "standard":
                    print(Seating.OKBLUE, end=" ")
                print(seats[seat_i]["name"], end=Seating.ENDC + " ")
                seat_i += 1
            print()
            row_i += 1

    def selectBestSeatsByN(self, nposti):
        half_y = floor(self.y / 2) + (self.y % 2)
        half_x = floor(self.x / 2) + (self.x % 2)
        bestSeats = {"distance": 999, "seats": []}
        for row_index, row in enumerate(self.json["seating_data"]["rows"]):
            for seat_index, seat in enumerate(row["columns"]):
                # if seat_index + nposti <= len(row["columns"]) -1:

                center_seat_index = ((seat_index * 2) + (nposti -1)) / 2
                # sqrt( (x1 - x2)^2 + (y1 - y2)^2 )
                distance = math.sqrt(((center_seat_index - half_x) ** 2) + ((row_index + 1 - half_y) ** 2))
                if bestSeats["distance"] <= distance:
                    continue

                selected = 0
                selected_data = []
                while selected < nposti:
                    if selected + seat_index <= len(row["columns"]) - 1 and row["columns"][selected + seat_index]["status"] == 0:
                        selected_data += [row["columns"][selected + seat_index]]
                    else:
                        break
                    selected += 1
                if selected == nposti:
                    bestSeats["seats"] = selected_data
                    bestSeats["distance"] = distance

        for seat in bestSeats["seats"]:
            print(seat["name"])
