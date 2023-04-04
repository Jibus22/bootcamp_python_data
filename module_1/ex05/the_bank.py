import random
import string

class Account(object):

    ID_COUNT = 1

    def __init__(self, name, **kwargs):
        self.__dict__.update(kwargs)

        self.id = self.ID_COUNT
        Account.ID_COUNT += 1
        self.name = name
        if not hasattr(self, "value"):
            self.value = 0

        if self.value < 0:
            raise AttributeError("Attribute value cannot be negative.")
        if not isinstance(self.name, str):
            raise AttributeError("Attribute name must be a str object.")

    def transfer(self, amount):
        self.value += amount


class Bank(object):
    """ The bank"""

    def __init__(self):
        self.accounts: Account = []

    def _check_validity(self, account):
        attrs = account.__dict__

        if len(attrs) % 2 == 0:
            return 1

        match = 0
        for key in attrs.keys():
            if key[0] == 'b':
                return 2
            if key.find("zip", 0, 3) != -1:
                match += 1
            if key.find("addr", 0, 4) != -1:
                match += 1

        if match == 0:
            return 3

        if "name" not in attrs:
            return 4
        elif "id" not in attrs:
            return 5
        elif "value" not in attrs:
            return 6

        if not isinstance(attrs["name"], str) or type(attrs["id"]) != int\
                 or (type(attrs["value"]) != int and\
                     type(attrs["value"]) != float):
            return -1
        return 0

    def _get_account_by_name(self, name):
        for acc in self.accounts:
            if acc.name == name:
                return acc
        return None

    def _insert_random_attr(self, account):
        while True:
            rdm_str = ''.join(random.choice(string.ascii_letters)\
                              for x in range(8))
            rdm_str = rdm_str.replace("b", "z", 1)
            if not hasattr(account, rdm_str):
                setattr(account, rdm_str, None)
                break

    def _fix_b_issue(self, account):
        b_attr = []
        for attr in account.__dict__.keys():
            if attr[0] == 'b':
                b_attr.append(attr)

        for attr in b_attr:
            if len(attr) > 1:
                new_key = attr[1:]
            else:
                new_key = ''.join(random.choice(string.ascii_letters)\
                                    for x in range(8))
            while True:
                if not hasattr(account, new_key):
                    break
                else:
                    new_key = ''.join(random.choice(string.ascii_letters)\
                                      for x in range(8))
            account.__dict__[new_key] = account.__dict__.pop(attr)

    def add(self, new_account):
        """ Add new_account in the Bank
            @new_account:  Account() new account to append
            @return   True if success, False if an error occured
        """

        if not isinstance(new_account, Account):
            return False
        if not "name" in new_account.__dict__:
            return False
        if self._get_account_by_name(new_account.name) is not None:
            return False

        self.accounts.append(new_account)
        return True

    def transfer(self, origin, dest, amount):
        """ Perform the fund transfer
            @origin:  str(name) of the first account
            @dest:    str(name) of the destination account
            @amount:  float(amount) amount to transfer
            @return   True if success, False if an error occured
        """

        if not isinstance(origin, str) or not isinstance(dest, str)\
                or (type(amount) is not int and type(amount) is not float):
            return False

        origin_acc = self._get_account_by_name(origin)
        dest_acc = self._get_account_by_name(dest)
        if origin_acc is None or dest_acc is None:
            return False

        if self._check_validity(origin_acc) or self._check_validity(dest_acc):
            return False

        if amount < 0 or origin_acc.value < amount:
            return False

        if origin_acc.name == dest_acc.name:
            return True

        dest_acc.transfer(amount)
        origin_acc.value -= amount

        return True

    def fix_account(self, name):
        """ fix account associated to name if corrupted
            @name:   str(name) of the account
            @return  True if success, False if an error occured
        """

        if not isinstance(name, str):
            return False
        acc = self._get_account_by_name(name)
        if acc is None:
            return False

        while True:
            ret = self._check_validity(acc)
            if ret:
                if ret == 1:
                    self._insert_random_attr(acc)
                elif ret == 2:
                    self._fix_b_issue(acc)
                elif ret == 3:
                    setattr(acc, "zip", None)
                elif ret == 5:
                    setattr(acc, "id", Account.ID_COUNT)
                    Account.ID_COUNT += 1
                elif ret == 6:
                    setattr(acc, "value", 0)
                elif ret == 4:
                    return False
                elif ret == -1:
                    return False
            else:
                return True
