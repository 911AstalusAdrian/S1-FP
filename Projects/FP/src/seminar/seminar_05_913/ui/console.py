from seminar.seminar_05_913.services.shelter import shelter


class ShelterUI:
    def __init__(self):
        self._shelter = shelter()

    def start(self):
        """
        ui -> shelter -> entities
        ui -> entities

        Handle main UI loop here
        @return:
        """
        # self._shelter.

        pass


cat_shelter = ShelterUI()
cat_shelter.start()
