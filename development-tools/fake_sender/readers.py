import json
import os

IASIOS_FILE = 'CDB/IASIO/iasios.json'
TEMPLATES_FILE = 'CDB/TEMPLATE/templates.json'
DEFAULT_CDB_PATH = '../../cdb/fake/'
MOUNTED_CDB_PATH = 'cdb/'


class CdbReader:
    """ Defines a reader for the CDB """

    @classmethod
    def get_cdb_location(self):
        """
        Returns the location of the CDB

        Returns:
            string: the location of the CDB
        """
        if os.environ.get('MOUNTED_CDB', False):
            return MOUNTED_CDB_PATH
        else:
            return DEFAULT_CDB_PATH

    @classmethod
    def get_alarm_ids(self):
        """
        Return the list of all alarms ids from the CDB

        Returns:
            dict: A list alarm IDs
        """
        iasios = self.read_alarm_iasios()
        return [iasio['id'] for iasio in iasios]

    @classmethod
    def read_alarm_iasios(self):
        """
        Reads the IASIOs from the CDB that will become alarms

        Returns:
            dict: A list of IASIOs data
        """
        iasios = self.read_iasios_file()
        templates = self.read_templates()
        valid_iasios = []
        for iasio in iasios:
            if iasio["iasType"] != "ALARM":
                continue
            if "templateId" not in iasio:
                valid_iasios.append(iasio)
            else:
                template_range = CdbReader.find_template_range(
                    iasio['templateId'], templates
                )
                for i in template_range:
                    aux_iasio = iasio.copy()
                    aux_iasio['id'] = aux_iasio['id'] + '[!#' + str(i) + '!]'
                    valid_iasios.append(aux_iasio)

        return valid_iasios

    @classmethod
    def read_iasios_file(self):
        """
        Reads the iasios.json file with all the IASIOs

        Returns:
            dict: A list of IASIOs data
        """
        filepath = self.get_cdb_location() + IASIOS_FILE
        try:
            with open(filepath) as file:
                iasios = json.load(file)
        except IOError:
            print('%s not found. IASIOS not initialized', filepath)
            return []
        return iasios

    @classmethod
    def read_templates(self):
        """
        Reads the templates.json file from the CDB and returns its content

        Returns:
            dict: A list of templates data
        """
        filepath = self.get_cdb_location() + TEMPLATES_FILE
        try:
            with open(filepath) as file:
                templates = json.load(file)
        except IOError:
            print('%s not found. template not read', filepath)
            return []
        return templates

    @classmethod
    def find_template_range(self, template_id, templates):
        """
        Returns the range of the temaplate

        Args:
            template_id (string): the themplate of the ID
            templates (list): list of dictionaries with the templates

        Returns:
            dict: A range with the numbers of the template
            (including max and min)
        """
        for template in templates:
            if template['id'] == template_id:
                return range(int(template['min']), int(template['max']) + 1)
        return None
