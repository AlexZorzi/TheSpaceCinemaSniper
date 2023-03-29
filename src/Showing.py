from Times import Times


class Showing:

    times = []
    def __init__(self, json):
        self.date_time = json["date_time"]
        self.date_day = json["date_day"]
        self.date_long = json["date_long"]
        for time_data in json["times"]:
            self.times.append(Times(time_data, self.date_time))


