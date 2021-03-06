

class Iasios:
    """Creates the json configuration for the IASIOs,
    the str method returns the json and must be saved
    in a corresponding file named id().json"""

    template = ''' {
        "id": "%s-Value",
        "shortDesc": "%s reported by the weather station %s",
        "iasType": "DOUBLE"
    }'''

    alarmtemplate = ''' {
        "id": "%s",
        "shortDesc": "%s reported by the weather station %s out of range",
        "iasType": "ALARM"
    }'''

    def __init__(self):
        self.iasios = []

    # adds the variable to this IASIOs list
    def add(self, var, id):
        varid = 'WS-' + str(id) + '-' + var

        iasval = Iasios.template % (varid, var, str(id))
        iasalarm = Iasios.alarmtemplate % (varid, var, str(id))

        self.iasios.append(iasval)
        self.iasios.append(iasalarm)

    def id(self):
        return "iasios"

    def folder(self):
        return "IASIO/"

    def __str__(self):
        out = "[\n"

        for iasio in self.iasios:
            out += iasio + ",\n"

        out = out[:-2] + "\n]"
        return out


if __name__ == '__main__':
    i = Iasios()
    i.add("Temperature", 2)
    i.add("Pressure", 2)
    print(i)
