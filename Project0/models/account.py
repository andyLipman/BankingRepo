class Account:

    def __init__(self, account_id=0, account_number=0, client_id=0, account_type=0, account_balance=0):
        self.account_id = account_id
        self.account_number = account_number
        self.client_id = client_id
        self.account_type = account_type
        self.account_balance = account_balance

    def json(self):
        return {
            'accountid': self.account_id,
            'accountnumber': self.account_number,
            'clientid': self.client_id,
            'accounttype': self.account_type,
            'accountbalance': self.account_balance
        }

    @staticmethod
    def json_parse(json):
        account = Account()
        account.account_id = json["accountid"] if "accountid" in json else 0
        account.account_number = json["accountnumber"]
        account.client_id = json["clientid"]
        account.account_type = json["accounttype"]
        account.account_balance = json["accountbalance"]

        return account

    def __repr__(self):
        return str(self.json())
