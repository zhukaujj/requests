import requests
import os


class YaUploader:
    def __init__(self, token):
        self.token = token

    def _get_upload_disk(self, disk_path):
        get_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        headers = {'Content-Type': 'application/json',
                   'Authorization': 'OAuth {}'.format(self.token)
                   }
        params = {'path': disk_path,
                  'overwrite': 'true'
                  }
        response = requests.get(get_url, headers=headers, params=params)
        upload_url = response.json().get('href', '')
        return upload_url

    def upload(self, file_path):
        url_upload = self._get_upload_disk(os.path.basename(file_path))
        response = requests.put(url_upload, data=open(file_path, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print('Файл загружен')


if __name__ == '__main__':
    token = input('Введите токен: ')
    ya = YaUploader(token)
    path_to_file = input('Введите путь к файлу : ')
    ya.upload(path_to_file)