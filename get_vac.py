import json
import requests
import psycopg2

def get_data_employers_hh(name_campony: str):
    """
        Функция делает запрос на HH и берет данные работодателей.
        После записывает в файл employers_data.json.
        Если файл уже был создан, то он перезаписывается.
        :param only_with_vacancies: Если True - вывод работодателей с активными вакансиями и наоборот.
        :param count_employers: Кол-во получаемых работодателей. По умолчанию = 10
        :return: None
        """
    params = {
        "text": name_campony,
        "only_with_vacancies": True,
        "per_page": 10,
    }
    data_employers = requests.get("https://api.hh.ru/employers", params=params).json()

    with open('employers_data.json', 'w', encoding="UTF-8") as file:
        json.dump(data_employers, file, indent=4)

def get_data_vacancies_company(file_json: str = 'employers_data.json'):
    """
       Функция берет данные по работодателям из файла file_json и делает запрос по вакансиям на HH.
       После записывает в файл vacancies_data.json.
       Если файл уже был создан, то он перезаписывается.
       :param: file_json: Файл из которого будут браться данные для запроса
       :return: None
       """
    dict_data = {}

    with open(file_json, 'r') as json_file:
        data: list[dict] = json.loads(json_file.read())

    for row in data["items"]:
        data_vacancies = requests.get(row["vacancies_url"]).json()
        dict_data[row["id"]] = data_vacancies

    with open('vacancies_data.json', 'w', encoding="UTF-8") as file:
        json.dump(dict_data, file, indent=4, ensure_ascii=True)



