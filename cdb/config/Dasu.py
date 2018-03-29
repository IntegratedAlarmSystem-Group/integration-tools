from Supervisor import Supervisor


class Dasu:
    """Creates the json configuration for a DASU,
    the str method returns the json and must be saved
    in a corresponding file named id().json"""

    template = '''{
        "id": "Dasu-%s",
        "asceIDs": [
            "Asce-%s"
        ],
        "outputId": "%s",
        "logLevel": "FATAL",
        "supervisorID": "%s"
    }'''

    def __init__(self, variable, id, supid):
        self.outid = "WS-" + str(id) + "-" + variable
        self.supid = supid

    def id(self):
        return "Dasu-" + self.outid

    def folder(self):
        return "DASU/"

    def __str__(self):
        return self.template % (self.outid, self.outid, self.outid,
                                self.supid)


if __name__ == '__main__':
    s = Supervisor("SupervisorID")
    d = Dasu("Temperature", 2, s.id())
    print(d)
