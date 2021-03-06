

class Asce:
    """Creates the json configuration for an ASCE,
    the str method returns the json and must be saved
    in a corresponding file named id().json"""

    template = '''{
      "dasuID": "Dasu-%s",
      "id": "Asce-%s",
      "inputIDs": [
        "%s"
      ],
      "outputID": "%s",
      "transferFunctionID":"org.eso.ias.asce.transfer.impls.MinMaxThresholdTF",
       "props": [
        {
          "name": "org.eso.ias.tf.minmaxthreshold.highOn",
          "value": "%d"
        },
        {
          "name": "org.eso.ias.tf.minmaxthreshold.highOff",
          "value": "%d"
        },
        {
          "name": "org.eso.ias.tf.minmaxthreshold.lowOn",
          "value": "%d"
        },
        {
          "name": "org.eso.ias.tf.minmaxthreshold.lowOff",
          "value": "%d"
        }
      ]
    }'''

    def __init__(self, variable, id, min, max, delta=-1):
        self.outid = "WS-" + str(id) + "-" + variable
        self.varid = self.outid + "-Value"

        self.min = min
        self.max = max

        self.delta = delta
        if delta == -1:
            self.delta = 0.2 * (max - min)

    def id(self):
        return "Asce-" + self.outid

    def folder(self):
        return "ASCE/"

    def __str__(self):
        return self.template % \
            (self.outid, self.outid, self.varid, self.outid,
             self.max, self.max - self.delta,
             self.min, self.min + self.delta)


if __name__ == '__main__':
    a = Asce("Temperature", 2, -10, 30)
    print(a)
