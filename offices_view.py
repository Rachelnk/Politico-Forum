from flask import jsonify, make_response, request, Blueprint
from Forum.app.api.v1.models.offices.__init__ import OfficesModel

offices_bp = Blueprint('office_blueprint',__name__)
office_list= []
#OFFICE = OfficesModel()
@offices_bp.route("/offices", methods = ["POST"])
def create_office():  
    
    data = request.get_json()
   
    name = data['name']
    office_type = data['office_type']
    
  

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