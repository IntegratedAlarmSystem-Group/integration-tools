# creates the json configuration for a Supervisor,
# the str method returns the json and must be saved
# in a corresponding file named id().json
class Supervisor:
  template = '''{
  "id": "%s",
  "dasusIDs": [
    %s
  ],
  "hostName": "almaias.eso.org",
  "logLevel": "INFO"
}'''

  def __init__(self, id):
    self.sid = id
    self.dasus = []

  # adds the dasu to this Supervisors list
  def add(self, dasuid):
    self.dasus.append(dasuid)

  def id(self):
    return self.sid

  def folder(self):
    return "Supervisor/"

  def __str__(self):
    list = '"'
    for dasu in self.dasus:
      list += dasu + '", "'

    return self.template % (self.sid, list[: -3])


if __name__ == '__main__':
  s = Supervisor("SupervisorID")
  s.add("DasuTemperature4")
  s.add("DasuTemperature5")
  print s
