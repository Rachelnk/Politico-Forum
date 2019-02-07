from flask import jsonify,make_response,request, Blueprint
from Forum.app.api.v1.models.parties.parties_models import PartiesModel

parties_bp = Blueprint('party_blueprint',__name__)

POLITICAL_PARTY = PartiesModel()
@parties_bp.route('/parties', methods=['GET'])
def get_parties():
    party_list = POLITICAL_PARTY.get_all_parties()
    if party_list:
        return  make_response(jsonify({
        "status":200,
        "data": party_list
    }),200)
    return  make_response(jsonify({
        "status":404,
        "error": "No office data found"
    }),404)

@parties_bp.route('/parties', methods = ['POST'])
def post_party():

    try:
        data = request.get_json()
        name = data['name'] ,
        founded = data['founded'],
        headquarter = data['headquarter'],
        leader =data['leader'],
        id = data['id']

    except:
        party = PartiesModel (
            name = name,
            founded = founded,
            headquarter = headquarter,
            leader = leader,
            id = id)
        party.post_party()

        return make_response(jsonify({"status": 201,
                                  "data": [{"name": name,
                                            "founded" : founded,
                                            "headquarter": headquarter,
                                            "leader": leader,
                                            "id": id,
                                                                                    "type": type,
                                            "name": name}]}), 201)

@parties_bp.route('/parties/<int:office_id>', methods =['GET'])
def get_specific_office(office_id):

    political_office = POLITICAL_PARTY.get_specific_office(office_id)

    if political_office:
        return make_response(jsonify({
            "status": 200,
            "data": political_office
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "Political office not found"
    }), 404)


@parties_bp.route('/offices', methods = ['DELETE'])
def delete_offices(office_id):
    political_office = POLITICAL_PARTY.delete_politicaloffice(office_id)
    if political_office:
        return make_response(jsonify({
            "status":200,
            "data": political_office
        }),200)
    return  make_response(jsonify({
        "status": 404,
        "error":"Political office not found"
    }), 404)
