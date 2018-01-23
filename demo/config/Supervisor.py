# creates the json configuration for a Supervisor,
# the str method returns the json and must be saved
# in a corresponding file named id().json
class Supervisor:
  template = '''{
  "id": "SupervisorID",
  "dasusIDs": [
    %s
  ],
  "hostName": "almaias.eso.org",
  "logLevel": "INFO"
}'''

  def __init__(self, dasulist=[]):
    self.dasus = dasulist

  # adds the dasu to this Supervisors list
  def add(self, dasuid):
    self.dasus.append(dasuid)

  def id(self):
    return "SupervisorID"

  def folder(self):
    return "Supervisor/"

  def __str__(self):
    list = '"'
    for dasu in self.dasus:
      list += dasu + '", "'

    return self.template % list[: -3]


if __name__ == '__main__':
  s = Supervisor(["DasuTemperature2", "DasuTemperature3"])
  s.add("DasuTemperature4")
  print s
