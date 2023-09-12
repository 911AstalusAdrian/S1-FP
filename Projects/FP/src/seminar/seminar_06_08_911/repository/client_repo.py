from seminar.seminar_06_08_911.domain.client import Client


class ClientRepo:
    def __init__(self, clients=None):
        self._clients = []
        if clients is not None:
            self.add_all(clients)

    @property
    def clients(self):
        return self._clients

    def add_all(self, clients):
        self._clients = clients

    def add_client(self, client):
        self._clients.append(client)

    def remove_client(self, client_id):
        self._clients = list(filter(client_id, self._clients))


def test_init_client():
    clients = [Client('123', 'Popescu', '18'), Client('124', 'X', '19'), Client('125', 'Y', '99')]
    repo = ClientRepo(clients)
    assert len(repo.clients) == 3
    return repo


def test_add_client():
    repo = test_init_client()
    repo.add_client(Client('122', 'Ana', '16'))
    assert len(repo.clients) == 4


def test_remove_client():
    repo = test_init_client()
    repo.remove_client(lambda client: not client.license_series == '123')
    assert len(repo.clients) == 2

    test_init_client()
    test_add_client()
    test_remove_client()
