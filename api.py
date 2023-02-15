import requests
import json
# import requests_toolbelt
from requests_toolbelt.multipart.encoder import MultipartEncoder


class PetFriends:
    def __init__(self):
        self.base_url = "https://petfriends.skillfactory.ru/"

    def get_api_key(self, email, password):

        headers = {
            "email": email,
            "password": password,
        }

        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def get_api_key_pass(self, email, password):

        headers = {
            "email": email,
            "password": password,
        }
        res = requests.get(self.base_url+'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result



    def get_list_of_pets(self, auth_key, filter):
        headers = {"auth_key": auth_key['key']}
        filter = {'filter': filter}
        res = requests.get(self.base_url + 'api/pets?filter=my_pets', headers=headers, params=filter)

        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result




    def add_new_pet_without_valid_data(self, auth_key, name, animal_type, age, pet_photo):
        data = MultipartEncoder(
            fields={'name': name,
                    'animal_type': animal_type,
                    'age': age,
                    'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')

                    })
        headers = {'auth_key': auth_key['key'], 'Content-type': data.content_type}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result


    def add_new_pet(self, auth_key, name, animal_type, age):

        data = {'name': name,
                'animal_type': animal_type,
                'age': age,
        }
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/create_pet_simple', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result



    def add_photo_of_pet(self, auth_key, pet_id, pet_photo):

        data = MultipartEncoder(
            fields={'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpg')
        })

        headers = {'auth_key': auth_key['key'], 'Content-type': data.content_type}
        res = requests.post(self.base_url + 'api/pets/set_photo/' + pet_id, headers=headers, data=data)
        status = res.status_code

        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result


    def add_info_about_new_pet(self, auth_key, name, animal_type, age):
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        headers = {'auth_key': auth_key['key']}
        res = requests.post(self.base_url + api/create_pet_simple, headers=headers, data=data)
        status = res.status_code

        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result


    def update_pet_info(self, auth_key, pet_id, name, animal_type, age):
        """Метод отправляет запрос на сервер об обновлении данных питомуа по указанному ID и
                        возвращает статус запроса и result в формате JSON с обновлённыи данными питомца"""
        headers = {'auth_key': auth_key['key']}
        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age
        }
        res = requests.put(self.base_url + 'api/pets/ + pet_id', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        return status, result




    def add_new_pet_with_novalid_data(self, auth_key, name, animal_type, age):

        data = {
                'name': name,
                'animal_type': animal_type,
                'age': age,

        }
        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result



    def add_new_pet_add_simvol(self, auth_key, name, animal_type, age):

        data = {
               'name': name,
                'animal_type': animal_type,
                'age': age
        }

        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result



    def add_new_pet_bigname(self, auth_key, name, animal_type, age):

        data = {
               'name': name,
                'animal_type': animal_type,
                'age': age
        }

        headers = {'auth_key': auth_key['key']}

        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except:
            result = res.text
        print(result)
        return status, result

















