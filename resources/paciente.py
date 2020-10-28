from flask import Response, request
from database.models import Paciente
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class PacientesApi(Resource):
    def get(self):
        pacientes = Paciente.objects().to_json()
        return Response(pacientes, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        paciente = Paciente(**body).save()
        id = paciente.id
        return {'id': str(id)}, 200


class ClientApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Paciente.objects.get(id=id).update(**body)
        return '', 200

    @jwt_required
    def delete(self, id):
        paciente = Paciente.objects.get(id=id).delete()
        return '', 200

    def get(self, id):
        try:
            paciente = Paciente.objects.get(id=id).to_json()
            return Response(paciente, mimetype="application/json", status=200)
        except Exception as error:
            return Response(error, status=400, mimetype='application/json')
