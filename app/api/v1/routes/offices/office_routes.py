from flask import jsonify, make_response, request, Blueprint
from Forum.app.api.v1.models.offices.office_models import OfficesModel

offices_bp = Blueprint('office_blueprint',__name__)
office_list= []
#OFFICE = OfficesModel()
@offices_bp.route("/offices", methods = ["POST"])
def create_office():  
    
    data = request.get_json()
   
    name = data['name']
    office_type = data['office_type']
    if not name:
        return "Office name is missing"
    elif not office_type: 
        return  "Office type has not been described"
    elif len(name) < 3:
        return "The number of characters in name should be greater than 3"

  

    new_office = OfficesModel ()
    new_office.name = name
    new_office.office_type= office_type
    new_office.save_office()

    return jsonify(new_office.save_office())
 

@offices_bp.route("/offices", methods= ['GET'])
def get_offices():
    office_list = OfficesModel.get_all_offices()
    if office_list:
     return  make_response(jsonify({
        "status":200,
        "data": office_list
    }),200)
    return  make_response(jsonify({
        "status":404,
        "error": "No office data found"
    }),404)


@offices_bp.route("/offices/<int:office_id>", methods =['GET'])
def get_specific_offices(office_id):

    political_office = OfficesModel.get_specific_offices(office_id)

    if political_office:
        return make_response(jsonify({
            "status": 200,
            "data": political_office
        }), 200)
    return make_response(jsonify({
        "status": 404,
        "error": "The political office does not exist"
    }), 404)


@offices_bp.route("/offices", methods = ['DELETE'])
def delete_politicaloffice(office_id):
    political_office = OfficesModel.delete_politicaloffice(office_id)
    if political_office:
        return make_response(jsonify({
            "status":200,
            "data": political_office
        }),200)
    return  make_response(jsonify({
        "status": 404,
        "error":"Political office not found"
    }), 404)
