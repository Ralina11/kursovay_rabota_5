from get_vac import *
from write_bd import create_table_employers_postgres, push_data_in_employers
from write_bd import create_table_vacancia_postgres, push_data_in_vacancies
from DBManager import DBManager


def user_interaction():
    print("Привет, это парсер по поиску вакансий с  платформы HH, занимаюсь поиском поиском вакансий по компаниям ")
    name_campony = input("Введите интересующие вас компании (до 10 штук, через запятую):  ")

    companies_list = name_campony.split(",")

    for company in companies_list:
        get_data_employers_hh(company)

    get_data_vacancies_company()

    create_table_employers_postgres()
    push_data_in_employers()

    create_table_vacancia_postgres()
    push_data_in_vacancies()

    """Создаем экземпляры класса DBManager """
    DB = DBManager()
    print("Операция выполнена, вакансии добавлены\nХотели бы вы выполнить операции? ДА или НЕТ")
    answer = input("введите свой ответ: ")
    if answer.lower() == "да":
        y = 0
        while y < 6:
            print("1.Получить список всех компаний и количество вакансий у каждой компании.\n2.Получить список всех вакансий с информацией о них.\n3.Получить среднюю зарплату по вакансиям.\n4.Получить список всех вакансий, у которых зарплата выше средней.\n5.Получить список всех вакансий, в названии которых содержатся переданные слова.\n6.Завершить обработку .")
            answer2 = input("введите свой ответ: ")
            if answer2 == "1":
                item1 = DB.get_companies_and_vacancies_count()
                print("список всех компаний и количество вакансий у каждой компании")
                print(item1)
                y+=1
            elif answer2 == "2":
                item2 = DB.get_all_vacancies()
                print(
                    "список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию.")
                print(item2)
                y += 1
            elif answer2 == "3":
                item3 = DB.get_avg_salary()
                print("средняя зарплата по вакансиям.")
                print(item3)
                y += 1
            elif answer2 == "4":
                item4 = DB.get_vacancies_with_higher_salary()
                print("список всех вакансий, у которых зарплата выше средней по всем вакансиям.")
                print(item4)
                y += 1
            elif answer2 == "5":
                word = str(input('введи ключ слово: '))
                item5 = DB.get_vacancies_with_keyword(word)
                if item5 == []:
                    print("Совпадений не найдено")
                else:
                    print("список всех вакансий, в названии которых содержатся переданные в метод слова")
                    print(item5)
                    y += 1
            elif answer2 == "6":
                print("Обработка завершина")
                y += 6
            else:
                print("Ввод не верный введите от 1 - 6")
    else:
        print("ввод не верный")


if __name__ == "__main__":
    user_interaction()