class HourTypeDto(object):

    def __init__(self, id=0, name="", estado=0):
        self.Id = id
        self.Name = name
        self.Estado = estado
    
    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.Name = json_data["Name"]
        self.Estado = json_data["Estado"]