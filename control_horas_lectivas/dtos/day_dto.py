class DayDto(object):

    def __init__(self, id=0, name="", order=0, capital="", estado=0):
        self.Id = id
        self.Name = name
        self.Order = order
        self.Capital = capital
        self.Estado = estado
    
    def from_json(self, json_data):
        self.Id = json_data["Id"]
        self.Name = json_data["Name"]
        self.Order = json_data["Order"]
        self.Estado = json_data["Estado"]
    
    def from_json_delete(self, json_data):
        self.Id = json_data["Id"]