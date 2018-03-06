import os
import sys
import json
import unittest

sys.path.insert(0, '..')

from createIasiosFixture import create_iasios_fixture

BASE_PATH = os.path.dirname(os.path.realpath(__file__))


class TestIasiosFixture(unittest.TestCase):

    def setUp(self):
        self.src_path = os.path.join(BASE_PATH, './iasios.json')

    def test_create_fixture_for_webserver(self):

        expected_json = """
            [
            {
              "model": "cdb.iasio",
              "pk": "AlarmTemperature2",
              "fields": {
                "short_desc": "Temperature reported by the weather station 2 out of range",
                "refresh_rate": 2000,
                "ias_type": "ALARM"
              }
            },
            {
              "model": "cdb.iasio",
              "pk": "Temperature2",
              "fields": {
                "short_desc": "Temperature reported by the weather station 2",
                "refresh_rate": 2000,
                "ias_type": "DOUBLE"
              }
            }
            ]
        """

        with open(self.src_path) as f:
            iasios_input = json.load(f)

        fixture_output = create_iasios_fixture(iasios_input)

        aux_json_output = fixture_output.sort(key=lambda x: x['pk'])
        aux_expected_json = json.loads(expected_json).sort(
            key=lambda x: x['pk']
        )

        self.assertEqual(aux_json_output, aux_expected_json)


if __name__ == '__main__':
    unittest.main()
