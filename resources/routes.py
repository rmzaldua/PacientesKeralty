from .client import ClientsApi, ClientApi
from .paciente import PacientesApi, PacienteApi


def initialize_routes(api):
    api.add_resource(ClientsApi, '/api/clients')
    api.add_resource(ClientApi, '/api/client/<id>')
    api.add_resource(PacientesApi, '/api/pacientes')
    api.add_resource(PacienteApi, '/api/paciente/<id>')
