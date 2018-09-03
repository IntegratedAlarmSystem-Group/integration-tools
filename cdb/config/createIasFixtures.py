import os
import json

BASE_PATH = os.path.dirname(os.path.realpath(__file__))

IAS_PATH = os.path.join(BASE_PATH, '../CDB/ias.json')
OUTPUT_FIXTURE__PATH = os.path.join(BASE_PATH, '../CDB/cdb.ias.json')


def create_ias_fixture(json_input):
    fixtures = []
    ias_id = 0
    prop_id = 0
    ias_dict = {}
    ias_dict['model'] = "cdb.ias"
    ias_dict['pk'] = ias_id
    ias_dict['fields'] = {
        'log_level': json_input['logLevel'],
        'refresh_rate': json_input['refreshRate'],
        'tolerance': json_input['tolerance'],
        'properties': []
    }

    for prop in json_input['props']:
        prop_dict = {}
        prop_dict['model'] = "cdb.property"
        prop_dict['pk'] = prop_id
        prop_dict['fields'] = {
            'value': prop['value'],
            'name': prop['name']
        }
        ias_dict['fields']['properties'].append(prop_id)
        prop_id += 1

        fixtures.append(prop_dict)
    fixtures.append(ias_dict)
    ias_id += 1

    return fixtures


def main():
    print(IAS_PATH)
    if os.path.isfile(IAS_PATH):

        with open(IAS_PATH) as f:
            ias_input = json.load(f)

        fixture = create_ias_fixture(ias_input)

        with open(OUTPUT_FIXTURE__PATH, 'w') as f:
            json.dump(fixture, f, indent=2)

    else:
        print("File 'ias.json' does not exist.")


if __name__ == '__main__':
    main()
