from flask_restful import Resource
from flask import jsonify


clientes = [
    {
        "id":1,
        "nombre": "Elkin",
        "apellido": "Rodriguez",
    },
    {
        "id":2,
        "nombre": "Paola",
        "apellido": "Arevalo"
    }
]


class Clientes(Resource):
    def get(self):

        return jsonify(
            {
                "clientes": clientes
            }
        )

