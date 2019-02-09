politicalparty = []
class PartiesModel():
    
    id = 0
    name = ""
    logoUrl = ""
    hqAddress =""
   
    def __init__(self):
        self.politicalparty =[]
       
    def save_party(self):
        #party_details is a diciotnary
        party = {
            'id':len(self.politicalparty) + 1,
            'name':self.name,
            'logoUrl':self.logoUrl,
            'hqAddress':self.hqAddress
        }

        self.politicalparty.append(party)
        return dict(status=201, data=self.politicalparty)



    def delete_politicalparty(self, party_id):
        try:
            for party in self.politicalparty:
                if party.id == party_id:
                    self.politicalparty.pop(party_id)
                    return True
        except:
            return False
    #fetching a list of all the offices
    @staticmethod
    def get_all_parties():
        return [vars(party) for party in politicalparty]
    
    #fetching a specific office
    @staticmethod
    def get_specific_party(id):
        return [vars(party) for party in politicalparty if id == id]
    
    #fetch a parties details
    def get_party_attributes(id):
        return[party for party in politicalparty if party.id == id]

    def patch_party(self,newpartyname):
        self.name =newpartyname
      
    def delete_party(party_id):
        for party in politicalparty:
            if party.id == party_id:
                politicalparty.remove(party)
            else:
                return False




