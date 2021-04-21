from daos.account_dao import accountDAO
from exceptions.resource_not_found import ResourceNotFound
from models.account import Account
from util.db_connection import connection


class AccountDAOImpl(accountDAO):

    def get_account(self, account_id):
        sql = "SELECT * FROM accounts WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [account_id])

        record = cursor.fetchone()

        if record:
            return Account(record[0], record[1], record[2], record[3], record[4])
        else:
            raise ResourceNotFound(f"Account with id:{account_id} - Not Found")

    def all_accounts(self):
        sql = "SELECT * FROM accounts"
        cursor = connection.cursor()
        cursor.execute(sql)
        records = cursor.fetchall()

        account_list = []

        if records:
            for record in records:
                account = Account(record[0], record[1], record[2], record[3], record[4])

                account_list.append(account.json())
        else:
            raise ResourceNotFound(f"Currently there are no accounts- Not Found")

    def update_account(self, change):
        sql = "UPDATE accounts Set clientId=%s, accounttype=%s, accountbalance=%s where accountid = %s"

        cursor = connection.cursor()
        cursor.execute(sql, (change.clientId, change.accounttype, change.accountbalance))
        connection.commit()

        record = cursor.fetchone()

        if record:
            updated_account = Account(record[0], record[1], record[2], record[3], record[4])
            return updated_account
        else:
            raise ResourceNotFound(f"there is no account with that ID.")

    def delete_account(self, account_id):
        sql = "DELETE FROM accounts WHERE id = %s"

        cursor = connection.cursor()
        cursor.execute(sql, [account_id])
        connection.commit()

    def create_account(self, account):
        sql = "INSERT INTO accounts VALUES(default, default, %s, %s, %s) RETURNING *"

        cursor = connection.cursor()
        cursor.execute(sql, (account.client_id, account.account_type, account.account_balance))

        connection.commit()
        record = cursor.fetchone()

        new_account = Account(record[0], record[1], record[2], record[3], record[4])
        return new_account


def _test():
    a_dao = AccountDAOImpl()
    accounts = accountDAO.all_accounts()
    print(accounts)

    print(AccountDAOImpl.get_account(1))


if __name__ == '__main__':
    _test()
