from Showing import Showing


class Film:
    showings = []

    def __init__(self, json):
        self.id = json["id"]
        self.image_poster = json["image_poster"]
        self.synopsis_short = json["synopsis_short"]
        self.title = json["title"]
        self.video = json["video"]
        self.video = json["video"]
        self.virtual_reality = json["virtual_reality"]
        for showing_data in json["showings"]:
            self.showings.append(Showing(showing_data))
