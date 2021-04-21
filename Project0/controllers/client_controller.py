from flask import jsonify, request
from exceptions.resource_not_found import ResourceNotFound
from exceptions.resource_unavailable import ResourceUnavailable
from models.account import Account
from models.client import Client
from services.client_service import ClientService


def route(app):
    @app.route("/clients", methods=['GET'])
    def get_all_clients():
        return jsonify(str(ClientService.all_clients())), 200

    @app.route("/clients/<client_id>", methods=['GET'])
    def get_client(client_id):
        try:
            client = ClientService.get_client_by_id(int(client_id))
            return jsonify(client.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients", methods=['POST'])
    def post_client():
        client = Client.json_parse(request.json)
        client = ClientService.create_client(client)
        return jsonify(client.json()), 201

    @app.route("/clients/<client_id>", methods=['PUT'])
    def put_client(client_id):
        try:
            client = Client.json_parse(request.json)
            client.client_id = int(client_id)
            update_client = ClientService.update_client(client)
            return jsonify(update_client.json()), 200
        except ResourceNotFound as r:
            return r.message, 404

    @app.route("/clients/<client_id>", methods=['DELETE'])
    def delete_client(client_id):
        try:
            ClientService.delete_client(int(client_id))
            return '', 205
        except ValueError as e:
            return f"No id:{client_id}", 404

    # FIX
    # @app.route("/clients/<client_id>/accounts", methods=['POST'])
    # def add_acc_to_client(client_id):
    #     account = ClientService.add_acc_to_client(client_id)
    #     return jsonify(account), 201

    @app.route("/clients/<client_id>/accounts", methods=['GET'])
    def get_client_accounts(client_id):

        account_list = ClientService.get_client_accounts(client_id)
        if len(account_list) != 0:
            return str(account_list), 200
        else:
            return f"Id:{client_id} NOT FOUND", 404