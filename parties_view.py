
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