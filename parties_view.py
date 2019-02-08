
from flask import jsonify, make_response, request, Blueprint
from Forum.app.api.v1.models.parties.parties_models import PartiesModel

parties_bp = Blueprint('party_blueprint',__name__)

#creates a politicalparty
@parties_bp.route('/parties', methods = ['POST'])
def create_party():
   
    name = request.get_json['name']
    logoUrl = request.get_json['logoUrl']
    hqAddress = request.get_json['hqAddress'] 

    party = PartiesModel ()
    party.name=name
    party.logoUrl = logoUrl,
    party.hqAddress = hqAddress 
    party.save_party()

    return jsonify(party.save_party())

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