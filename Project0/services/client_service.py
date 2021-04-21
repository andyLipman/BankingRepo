from daos.client_dao_impl import ClientDAOImpl
# from exceptions.resource_unavailable import ResourceUnavailable


class ClientService:
    client_dao = ClientDAOImpl()

    @classmethod
    def create_client(cls, client):
        return cls.client_dao.create_client(client)

    @classmethod
    def all_clients(cls):
        return cls.client_dao.all_clients()

    @classmethod
    def get_client_by_id(cls, client_id):
        return cls.client_dao.get_client(client_id)

    @classmethod
    def update_client(cls, change):
        return cls.client_dao.update_client(change)

    @classmethod
    def delete_client(cls, client_id):
        return cls.client_dao.delete_client(client_id)

    @classmethod
    def add_acc_to_client(cls, client_id):
        return cls.client_dao.add_acc_to_client(client_id)

    @classmethod
    def get_client_accounts(cls, client_id):
        return cls.client_dao.get_client_accounts(client_id)

    # @classmethod
    # def withdraw_from_account(cls, change):
    #     return cls.client_dao.withdraw_from_account(change)
