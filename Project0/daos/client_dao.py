from abc import abstractmethod, ABC


class clientDAO(ABC):

    @abstractmethod
    def create_client(self, client):
        pass

    @abstractmethod
    def get_client(self, client_id):
        pass

    @abstractmethod
    def all_clients(self):
        pass

    @abstractmethod
    def update_client(self, client_id):
        pass

    @abstractmethod
    def delete_client(self, client_id):
        pass

    @abstractmethod
    def add_acc_to_client(self, client_id):
        pass

    @abstractmethod
    def get_client_accounts(self, client_id):
        pass

    # @abstractmethod
    # def withdraw_from_account(self, change):
    #     pass

