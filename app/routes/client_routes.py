from flask import Blueprint, request, jsonify
from app.controllers.client_controller import (
    get_clients,
    get_client,
    create_client,
    update_client,
    delete_client
)

client_bp = Blueprint("client", __name__)

@client_bp.route("/", methods=["GET"])
def list_clients():
    clients = get_clients()
    return jsonify(clients), 200

@client_bp.route("</int:client_id>", methods=["GET"])
def get_single_client(client_id):
    client = get_client(client_id)
    return jsonify(client), 200

@client_bp.route("/", methods=["POST"])
def add_client():
    data = request.get_json()
    if not data or "name" not in data:
        return jsonify({"error": "Nombre es obligatorio"}), 400
    new_client = create_client(data)
    return jsonify(new_client), 201

@client_bp.route("/<int:client_id>", methods=["PUT"])
def edit_client(client_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "Dtaos invalidos"}), 400
    updated_client = update_client(client_id, data)
    return jsonify(updated_client), 200

@client_bp.route("</int:client_id>", metods=["DELETE"])
def remove_client(client_id):
    delete_client(client_id)
    return "", 204