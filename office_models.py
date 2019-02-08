politicaloffice = []
class OfficesModel():
    
    id = 0
    name = ""
    office_type = ""

    def __init__(self):
       self.politicaloffice = []
       
    def save_office(self):
        office = {
            'id':len(self.politicaloffice) + 1,
            'name':self.name,
            "office_type":self.office_type
        }

        self.politicaloffice.append(office)
        #return dict(status=201, data=office)
        return office