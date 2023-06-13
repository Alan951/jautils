from datetime import datetime
import json
import csv
import os
import pkgutil
import xmltodict

class IOUtils:

    @staticmethod
    def load_conf():
        try:
            data = pkgutil.get_data(__name__, 'conf.json')
            data = json.loads(data)
            return data
        except Exception as err:
            print('[!] Error al cargar el archivo de configuración: ', err )
            return None

    @staticmethod
    def generate_filename(ext=''):
        basename = "output - "
        dynamicname = '{}'.format(datetime.now().strftime('%d-%m-%YT%H-%M-%S'))
        if ext != '':
            ext = '.' + ext

        return f'{basename}{dynamicname}{ext}'

    @staticmethod
    def load(path):
        if(not os.path.isfile(path)):
            print(f'[!] El archivo {path} no existe')
            raise FileNotFoundError('path: {}'.format(path))
        #check file type by extension
        if(path.endswith('.json')):
            return IOUtils.load_json(path)
        elif(path.endswith('.csv')):
            return IOUtils.load_csv(path)
        elif(path.endswith('.txt')):
            return IOUtils.load_txt(path)
        else:
            raise Exception('El archivo {} no es un archivo valido'.format(path))

    @staticmethod
    def load_txt(path):
        try:
            with open(path, 'r') as f:
                # remove 'new line' character and assign to content
                content = [x.strip() for x in f.readlines()]
        except FileNotFoundError:
            print(f'[!] El archivo {path} no existe...')
            return None

        return content

    @staticmethod
    def load_json(path):
        try:
            with open(path, 'r', encoding='utf8') as f:
                content = json.load(f)
        except FileNotFoundError:
            print(f'[!] El archivo {path} no existe...')
            return None

        return content

    @staticmethod
    def load_csv(path, mode='dict', delimiter=','):
        csv.field_size_limit(100000000)
        try:
            with open(path, 'r', encoding="utf8") as f:
                if(mode == 'dict'):
                    return list(csv.DictReader(f, delimiter=delimiter))
                elif(mode == 'list'):
                    return list(csv.reader(f, delimiter=delimiter))

        except FileNotFoundError as err:
            print(f"[!] El archivo {path} no existe...")
            print(err)
            return None

    @staticmethod
    def load_xml(path, node = None):
        with open(path, 'r', encoding='utf8') as f:
            dict = xmltodict.parse(f.read())

        return dict

    @staticmethod
    def export_json(path, data):
        with open(path, 'w', encoding='utf8') as f:
            json.dump(data, f, indent=2)

    @staticmethod
    def export_csv(path, data):
        with open(path, 'w', encoding='utf8', newline='') as f:
            if(type(data) is dict):
                writer = csv.DictWriter(f, fieldnames=data[0].keys())
                writer.writeheader()
                for r in data:
                    writer.writerow(r)
            elif(type(data) is list):
                writer = csv.writer(f)
                for r in data:
                    writer.writerow(r)
            else:
                print('data type not supported yet')
if __name__ == '__main__':
    #print(IOUtils.load_json('cmdb_mapping.json'))

    print(IOUtils.load_csv('test.csv', mode='list'))