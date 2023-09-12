class ClientException(Exception):
    def __init__(self, msg=''):
        self._msg = msg

    def __str__(self):
        return self._msg


class ClientValidationException(ClientException):
    def __init__(self, error_list):
        self._errors = error_list

    @property
    def errors(self):
        # Gives access to the list of errors
        return self._errors

    def __str__(self):
        # str representation
        result = ''
        for e in self.errors:
            result += e
            result += '\n'
        return result


class Client:
    def __init__(self, c_id, name, age):
        self._cid = c_id
        self._name = name
        self._age = age

    @property
    def license_series(self):
        return self._cid

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value

    @name.setter
    def name(self, value):
        self._name = value

    @license_series.setter
    def license_series(self, value):
        self._cid = value


class ClientValidator:
    def validate(self, client):
        """
        Validate a given client
        """
        errors = []
        if len(client.license_series) == 0:
            errors.append('Invalid license series, empty value provided.')
        if len(client.name) == 0:
            errors.append('Invalid name, empty value provided.')
        if not isinstance(client.age, int):
            errors.append('Invalid age input.')
        if client.age == 0:
            errors.append('Invalid age, empty value provided.')


def test_client():
    try:
        c1 = Client('123', '', 25)
        cv = ClientValidator()
        cv.validate(c1)
    except ClientValidationException as e:
        print(e.errors)
