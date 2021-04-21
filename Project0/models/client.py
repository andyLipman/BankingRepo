class Client:

    def __init__(self, clientid=0, firstname="", lastname=""):
        self.client_id = clientid
        self.first_name = firstname
        self.last_name = lastname

    def json(self):
        return {
            'clientid': self.client_id,
            'firstname': self.first_name,
            'lastname': self.last_name
        }

    @staticmethod
    def json_parse(json):
        client = Client()
        client.client_id = json["clientid"] if "clientid" in json else 0
        client.first_name = json["firstname"]
        client.last_name = json["lastname"]

        return client

    def __repr__(self):
        return str(self.json())
