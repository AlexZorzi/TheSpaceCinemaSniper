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
        self.printandClean()
    def printandClean(self):
        for r_row, row in enumerate(self.json["seating_data"]["rows"]):
            print(row["row_label"], end=" ")
            row["columns"].reverse()
            for i, column in enumerate(row["columns"]):
                if column == None:
                    self.json["seating_data"]["rows"][r_row]["columns"].pop(i)
                    continue
                if column["status"] == 2 or column["status"] == 1 or column["status"] == 7:
                    print(Seating.FAIL, end=" ")
                elif column["area_id"] == "vip":
                    print(Seating.WARNING, end=" ")
                elif column["area_id"] == "special":
                    print(Seating.OKCYAN, end=" ")
                elif column["area_id"] == "standard":
                    print(Seating.OKBLUE, end=" ")
                print(column["name"], end=Seating.ENDC+" ")
        print()
    print()

    def selectBestSeatsByN(self, nposti):
        len_rows = len(self.json["seating_data"])
        if len_rows % 2 == 0:
            middle = floor(len_rows / 2)
        else:
            middle = floor(len_rows / 2 + 0.5)
        


