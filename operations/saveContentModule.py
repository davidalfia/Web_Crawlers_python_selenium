import json

"""
saving result into json
"""


class SaveContentModule(object):

    def __init__(self):
        pass

    @staticmethod
    def save(data_list, file_name):
        json_string = json.dumps([ob.__dict__ for ob in data_list], ensure_ascii=False, indent=2)
        with open(file_name+'.json', 'wb') as file:
            file.write(json_string.encode('utf-8'))
