from api import PetFriends
from settings import valid_email, valid_password
from settings import invalid_email, invalid_password
import os

pf = PetFriends()
# Test-1
"""Проверка ввода данных для входа на сайт с невалидным email. """
def test_get_api_key_for_invalid_user(email = invalid_email, password = valid_password):
    status, result = pf.get_api_key(email, password)
    if result == "email = valid_email, password = valid_password":
        # если данные валидные
        assert status == 200
        assert "key" in result
    else:
        assert status == 403

# Test-2
"""Проверка ввода данных для входа на сайт с невалидным password. """
def test_get_api_key_for_invalid_pass(email=valid_email, password=invalid_password):
    status, result = pf.get_api_key(email, password)
    if result == "email = valid_email, password = valid_password":
        # если данные валидные
        assert status == 200
        assert "key" in result
    else:
        assert status == 403

# Test-3
"""Проверка, что запрос моих питомцев возвращает не пустой список."""
def test_get_list_of_pets_with_valid_key(filter= 'my_pets'):
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
    print(result)





# Test-4
def test_add_new_pet_without_valid_data(name='', animal_type='', age='', pet_photo='images/Sonya.jpg'):
    """Проверяем дабавление нового питомца с пустыми полями"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и добавляем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_without_valid_data(auth_key, name, animal_type, age, pet_photo)


    assert status == 200
    assert result['name'] == name
    # Принимает пустые поля для ввода данных питамца


# Test-5
def test_add_new_pet(name='Рыжик', animal_type='колли', age='7'):

    # Запрашиваем ключ api и добавляем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name


# Test-6
def test_add_photo_of_pet(pet_photo='images/Юнона.jpg'):
    """Проверяем что можно добавить фото питомца """

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)
        _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')


        assert status == 200
        assert result['pet_photo'] == my_pets['pets'][0]['pet_photo']
        print(f'\n фото питомца {result}')
    else:
        raise Exception('There is no my pets')

# Test-7
def test_add_info_about_new_pet(name='Maximus', animal_type='Husky', age='7'):

       # запрашиваем ключ api и дабавляем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
     # добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name


# Test-7
def test_update_pet_info(name='Бублик', animal_type='двортерьер', age='5'):

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, 'my_pets')

    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        assert status == 200
        assert result['name'] == name
    else:
        raise Exception('There is no my pets')




# Test-8
def test_add_new_pet_with_novalid_data(name='Кеша', animal_type='попугай', age='-35'):
    """Проверяем дабавление нового питомца с отрицательным значением возраста"""


    # pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и добавляем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    age = '-35'

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert age
    print(f'\nотрицательный возраст {age}')


# Test-9
def test_add_new_pet_add_simvol(name='?*;№ВП%:75', animal_type=':*?%ПО%:Е', age='*()'):
    """Проверяем дабавление нового питомца с вводом символов"""


    # Запрашиваем ключ api и добавляем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    # Позволяет ввести невалидные значения


# Test-10
def test_add_new_pet_bigname(name='попкадуракпопкадуракпопкадуракпопкадурак', animal_type='попугай', age='125'):
    """Проверяем дабавление нового питомца с вводом символов"""


    # Запрашиваем ключ api и добавляем в переменную auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age)
    assert status == 200
    assert result['name'] == name
    # Позволяет ввести слишком длинное имя питомца



















    

