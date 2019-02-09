
from flask import jsonify, make_response, request, Blueprint
from Forum.app.api.v1.models.parties.parties_models import PartiesModel

parties_bp = Blueprint('party_blueprint',__name__)

#creates a politicalparty
@parties_bp.route('/parties', methods = ['POST'])
def create_party():
    data = request.get_json()
    
   
    name = data['name']
    logoUrl = data['logoUrl']
    hqAddress = data['hqAddress']
    

    party = PartiesModel ()
    party.name=name
    party.logoUrl = logoUrl
    party.hqAddress = hqAddress
    party.save_party()

    return jsonify(party.save_party())

#POLITICAL_PARTY = PartiesModel()
political_list = []
@parties_bp.route('/parties', methods=['GET'])
def get_parties():
    parties = PartiesModel.get_all_parties()
    #perform validation 
    if parties:
        return make_response(jsonify({
            "status" : 200,
            "data": parties
         }),200)
    return make_response(jsonify({
        "status": 404,
        "error": "No political party could be found"
    }), 404)




@parties_bp.route('/parties/<int:party_id>', methods =['GET'])
def get_specific_party(party_id):

    specific_patry = PartiesModel.get_specific_party(party_id)
    #= POLITICAL_PARTY.get_specific_office(office_id)

    if specific_patry:
        return make_response(jsonify({
            "status": 200,
            "data": specific_patry
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "Political office not found"
    }), 404)

@parties_bp.route("/parties", methods = ['DELETE'])

def delete_politicalparty(party_id):
    delete_party = PartiesModel.delete_politicalparty(party_id)
    if delete_party:
        return make_response(jsonify({
            "status":200,
            "data": delete_party
        }),200)
    return  make_response(jsonify({
        "status": 404,
        "error":"THe political office could not be deleted"
    }), 404)

@parties_bp.route("/parties/<int:party_id>", methods = ['PATCH'])
def edit_party(party_id):
    try:
        data = request.get_json()
        name = data["name"]
    except:
        return make_response(jsonify({
            "status": 400,
            "error": "Party name not found"
        }), 400)
    
    try:
        party = PartiesModel.get_party_attributes(party_id)[0]
    except IndexError:
        return make_response(jsonify({"status": 404, "data": "You cannot edit that party as it does not exist"}), 404)
    party.setname(name)
    return make_response(jsonify({"status": 200, "data": [{
        "id": party_id,
        "name": name
    }]}), 200)
