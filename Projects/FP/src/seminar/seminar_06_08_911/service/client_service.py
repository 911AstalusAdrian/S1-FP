from ..domain.client import Client


class ClientServiceError(Exception):
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg


class ClientService:
    def __init__(self, client_repo, client_validator):
        self._repo = client_repo
        self._validator = client_validator

    @property
    def repo(self):
        return self._repo

    @property
    def validator(self):
        return self._validator

    @repo.setter
    def repo(self, _new_value):
        self._validator = _new_value

    def check_for_unique_id(self, driver_license):
        for _iterator in (0, len(self._repo)):
            if self._repo[_iterator].driver_license == driver_license:
                return True
        return False

    def create_client(self, driver_license, name, age):
        if self._validator == "":
            if self.check_for_unique_id(driver_license):
                _new_client = Client(driver_license, name, age)
                self._repo.append(_new_client)
            else:
                raise ClientServiceError("This driver license id already exists")
        else:
            raise ClientServiceError("Invalid format for client")

    def remove_client(self, client_id):
        for _iterator in (0, len(self._repo)):
            if self._repo[_iterator].id == client_id:
                self._repo.pop(_iterator)
                _iterator = _iterator - 1
