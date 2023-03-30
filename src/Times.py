

class Times:

    def __init__(self, json, date_time):
        self.date_time = date_time
        self.date = json["date"]
        self.time = json["time"]
        self.screen_number = json["screen_number"]
        self.screen_type = json["screen_type"]
        self.link = json["link"]

    def getLink(self):
        adapted_time = self.time.replace(":","-")
        screenid_link = self.link.replace("{screenId}", self.screen_number)
        link_sessionDate = screenid_link.replace("{sessionDate}", self.date_time)
        link_final = link_sessionDate.replace("{sessionTime}", adapted_time)
        return link_final

