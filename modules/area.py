import json 

class Area:
    def __init__(self):
        f = open("area.json","r",encoding="utf-8")
        self.data = json.load(f)
    def search(self,area):
        self.dataArea = self.data["offices"]
        for region in self.dataArea.keys():
            detailRegion = self.dataArea[region]
            if(area in detailRegion["name"]):
                return(region[0:2]+"0000")
        self.dataArea = self.data["centers"]
        for region in self.dataArea.keys():
            detailRegion = self.dataArea[region]
            if(area in detailRegion["name"]):
                return(region[0:2]+"0000")
