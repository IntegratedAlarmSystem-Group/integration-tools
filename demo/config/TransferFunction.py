

class TransferFunction:
    """Creates the json configuration for a TransferFunction,
    the str method returns the json and must be saved
    in a corresponding file named id().json"""

    template = '''{
      "className" : "%s",
      "implLang" : "%s"
    }'''

    def __init__(self, classname, lang):
        self.classnmame = classname
        self.lang = lang

    def id(self):
        return self.classnmame

    def folder(self):
        return "TF/"

    def __str__(self):
        return self.template % (self.classnmame, self.lang)


if __name__ == '__main__':
    tf_name = "org.eso.ias.asce.transfer.impls.MinMaxThresholdTF"
    tf = TransferFunction(tf_name, "SCALA")
    print(tf)
