from Asce import Asce
from Dasu import Dasu
from Supervisor import Supervisor
from Iasios import Iasios
from TransferFunction import TransferFunction

import os


def main():
  vars = ["Temperature", "WindSpeed"]
  # "Pressure", "WindDirection", "Humidity", "Dewpoint"]
  ids = [2]
  config_weather(vars, ids)


# writes the configuration file for this object,
# the object can be Dasu, Asce, Supervisor or Iasio
def write_conf(config_obj):
  path = "CDB/" + config_obj.folder() + config_obj.id() + ".json"
  ensure_dir(os.path.dirname(path))

  file = open(path, 'w')
  file.write(str(config_obj))

  file.close()
  print "%s created" % path
  return


# ensures a directory exists, creating it if it doesn't
def ensure_dir(dir):
  if not os.path.exists(dir):
    os.makedirs(dir)
  return


# creates the json configuration for all the combination var-id
# for the weather station
def config_weather(vars, ids):

  # transfer function
  classname = "org.eso.ias.prototype.transfer.impls.MinMaxThresholdTF"
  write_conf(TransferFunction(classname, "SCALA"))

  iasios = Iasios()
  supervisor = Supervisor()

  for id in ids:
    for var in vars:
      dasu = Dasu(var, id)
      if var == "Temperature":
        asce = Asce(var, id, min=-20, max=1000, delta=5)
      elif var == "WindSpeed":
        asce = Asce(var, id, min=-1000, max=17, delta=3)
      # TODO: set the range for the Asce

      iasios.add(var, id)
      supervisor.add(dasu.id())

      write_conf(dasu)
      write_conf(asce)

  # add dummy configuration
  var = "dummy"
  id = ""

  dasu = Dasu(var, id)
  asce = Asce(var, id, min=0, max=50, delta=0)
  iasios.add(var, id)
  supervisor.add(dasu.id())
  write_conf(dasu)
  write_conf(asce)

  write_conf(iasios)
  write_conf(supervisor)
  return


if __name__ == '__main__':
  main()
