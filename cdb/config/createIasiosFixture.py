import os
import json

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

IASIOS_PATH = os.path.join(BASE_PATH, '../CDB/IASIO/iasios.json')
OUTPUT_FIXTURE__PATH = os.path.join(BASE_PATH, '../CDB/cdb.iasios.json')


def create_iasios_fixture(json_input):

    fixtures = []

    for c in json_input:

        aux_dict = {}
        aux_dict['model'] = "cdb.iasio"
        aux_dict['pk'] = c['id']
        aux_dict['fields'] = {
            'short_desc': c['shortDesc'],
            'ias_type': c['iasType'],
        }

        fixtures.append(aux_dict)

    return fixtures


def main():

    if os.path.isfile(IASIOS_PATH):

        with open(IASIOS_PATH) as f:
            iasios_input = json.load(f)

        fixture = create_iasios_fixture(iasios_input)

        with open(OUTPUT_FIXTURE__PATH, 'w') as f:
            json.dump(fixture, f, indent=2)

    else:
        print("File 'iasios.json' does not exist.")


if __name__ == '__main__':
    main()
