from daos.account_dao_impl import AccountDAOImpl
from exceptions.resource_unavailable import ResourceUnavailable


class AccountService:
    account_dao = AccountDAOImpl()

    @classmethod
    def create_account(cls, account):
        return cls.account_dao.create_account(account)

    @classmethod
    def all_accounts(cls):
        return cls.account_dao.all_accounts()

    @classmethod
    def get_account_by_id(cls, account_id):
        if account_id:
            return cls.account_dao.get_account(account_id)
        else:
            raise ResourceUnavailable(f"There is no account by id: {account_id} - Not Found")

    @classmethod
    def update_account(cls, account):
        return cls.account_dao.update_account(account)

    @classmethod
    def delete_account(cls, account_id):
        return cls.account_dao.delete_account(account_id)
