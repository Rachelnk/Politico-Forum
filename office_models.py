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

    #fetching a list of all the offices
    @staticmethod
    def get_all_offices():
        return [vars(office) for office in politicaloffice]

    @staticmethod
    def get_specific_offices(id):
        return [vars(office) for office in politicaloffice if office.id == id ]
    
