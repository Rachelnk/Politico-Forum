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