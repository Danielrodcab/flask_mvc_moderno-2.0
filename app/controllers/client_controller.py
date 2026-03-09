from app.models.client import Client
from app import db

def get_clients():
    clients = Client.query.all()
    return [client.to_direct() for client in clients]

def get_client(client_id):
    client = Client.query.get_or_404(client_id)
    return client.to_direct()

def create_client(data):
    new_client = Client(name=data["name"])
    db.session.add(new_client)
    db.session.commit()
    return new_client.to_dict()

def update_client(client_id, data):
    client = Client.query.get_or_404(client_id)
    client.name = data.get("name", client.name)
    db.session.commit()
    return client.to_dict()

def delete_client(client_id):
    client = Client.query.get_or_404(client_id)
    db.session.delete(client)
    db.session.commit()
    return {"message": "El cliente fue eliminado"}