from seminar.seminar_06_08_912.domain.client import Client


class ClientService:
    def __init__(self, validator, repository):
        self._validator = validator
        self._repository = repository

    def create(self, client_id, client_cnp, client_name):
        client = Client(client_id, client_cnp, client_name)
        self._validator.validate(client)
        self._repository.store(client)
        return client

    def delete(self, client_id):
        return self._repository.delete(client_id)

    def update(self, client):
        self._repository.update(client)

    def get_client_count(self):
        return len(self._repository)
