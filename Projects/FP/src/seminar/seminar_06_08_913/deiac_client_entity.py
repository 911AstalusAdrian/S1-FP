class ClientException(Exception):
    def __init__(self, msg):
        self._msg = msg


class client:
    def __init__(self, ID, name, age):
        self.__ID = ID
        self.__name = name
        self.age = age

    @property
    def id(self):
        return self.__ID

    @property
    def Name(self):
        return self.__name

    @property
    def Age(self):
        return self.age

    @Age.setter
    def Age(self, value):
        self.age = value

    def __str__(self):
        return 'ID: ' + str(self.id) + ' ' + 'NAME: ' + str(self.Name) + ' ' + 'AGE: '+ str(self.Age)


def test_client():
    c = client('1387187890', 'Pop Maria', 25)
    assert c.id == '1387187890'
    assert c.Name == 'Pop Maria'
    assert c.Age == 25

    c.Age += 1
    assert c.Age == 26


test_client()

class ClientValidator:
    def validate(self, client):
        '''
        Validate a given client
        :param client:
        :return:
        '''
        if client.Age == '':
            raise ClientException('Age field should not be empty!')
        if client.Name == '':
            raise ClientException('Name field should not be empty!')
        if client.id == '':
            raise ClientException('Id field should not be empty!')
        if client.Age < 18:
            raise ClientException('The client should have at least 18 years old!')
        if len(client.id) < 10:
            raise ClientException('The client id should have 10 char str!')

def test_client_validator():

    try:
        c1 = client('712173991303', '', 18)
        cv = ClientValidator()
        cv.validate(c1)
        assert False
    except ClientException:
        assert True

    try:
        c1 = client('712173991303', 'Pop Ana', 15)
        cv = ClientValidator()
        cv.validate(c1)
        assert False
    except ClientException:
        assert True

    try:
        c1 = client('621874', 'Pop Ana', 34)
        cv = ClientValidator()
        cv.validate(c1)
        assert False
    except ClientException:
        assert True

    try:
        c1 = client('712173991303', 'Pop Ana', '')
        cv = ClientValidator()
        cv.validate(c1)
        assert False
    except ClientException:
        assert True


test_client_validator()
