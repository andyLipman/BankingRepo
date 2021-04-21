from daos.client_dao import clientDAO
from exceptions.resource_not_found import ResourceNotFound
from models.client import Client
from models.account import Account
from util.db_connection import connection


class ClientDAOImpl(clientDAO):

    def create_client(self, client):
        sql = "INSERT INTO clients VALUES(default, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (client.first_name, client.last_name))

        connection.commit()
        record = cursor.fetchone()

        new_client = Client(record[0], record[1], record[2])
        return new_client

    def get_client(self, client_id):
        sql = "SELECT * FROM clients WHERE clientid = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])

        record = cursor.fetchone()

        if record:
            return Client(record[0], record[1], record[2])
        else:
            raise ResourceNotFound(f"Client with id: {client_id} - Not Found")

    def all_clients(self):
        sql = "SELECT * FROM clients"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        client_list = []
        for record in records:
            client = Client(record[0], record[1], record[2])

            client_list.append(client)

        return client_list

    def update_client(self, change):
        sql = "UPDATE clients SET firstname = %s, lastname= %s WHERE clientid = %s RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (change.first_name, change.last_name, change.client_id))
        connection.commit()
        record = cursor.fetchone()

        if record:
            updated_client = Client(record[0], record[1], record[2])
            return updated_client
        else:
            raise ResourceNotFound(f"Client ID: {change.client_id}- NOT FOUND")

    def delete_client(self, client_id):
        sql = "DELETE FROM clients WHERE clientid = %s "

        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()

    def add_acc_to_client(self, client_id):
        sql = "INSERT INTO accounts Values(default, default, %s, accounttype = 1, accountbalance = 20) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()

        record = cursor.fetchone()

        new_account = Account(record[0], record[1], record[2], record[3], record[4])
        return new_account

    def get_client_accounts(self, client_id):
        sql = "select * from accounts where clientid=%s"
        cursor = connection.cursor()
        cursor.execute(sql, [client_id])
        connection.commit()

        records = cursor.fetchall()

        account_list = []

        for record in records:
            account = Account(record[0], record[1], record[2], record[3], record[4])
            account_list.append(account)

        return account_list

    # def withdraw_from_account(self, change):
    #     sql = "Update accounts set accountbalance = accountbalance-%s where accountnumber = %s"
    #     cursor = connection.cursor()
    #     cursor.execute(sql, change.)



def _test():
    client_dao = clientDAO()
    clients = client_dao.all_clients()
    print(clients)

    print(client_dao.get_client(1))


if __name__ == '__main__':
    _test()
