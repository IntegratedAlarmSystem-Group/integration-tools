from Supervisor import Supervisor

# creates the json configuration for a DASU,
# the str method returns the json and must be saved
# in a corresponding file named id().json
class Dasu:
  template = '''{
  "id": "Dasu%s",
  "asceIDs": [
    "Asce%s"
  ],
  "outputId": "Alarm%s",
  "logLevel": "FATAL",
  "supervisorID": "%s"
}'''

  def __init__(self, variable, id, supid):
    self.varid = variable + str(id)
    self.supid = supid

  def id(self):
    return "Dasu" + self.varid

  def folder(self):
    return "DASU/"

  def __str__(self):
    return self.template % (self.varid, self.varid, self.varid, self.supid)


if __name__ == '__main__':
  s = Supervisor("SupervisorID")
  d = Dasu("Temperature", 2, s.id())
  print d
