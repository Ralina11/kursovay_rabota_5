from get_vac import *
from DBManager import create_table_employers_postgres, push_data_in_employers
from DBManager import create_table_vacancia_postgres,push_data_in_vacancies
def user_interaction():
    print("Привет, это парсер по поиску вакансий с  платформы HH, занимаюсь поиском поиском вакансий по компаниям ")
    name_campony = input("Введите интересующую вас компанию:  ")
    items = get_data_employers_hh(name_campony)
    items1 = get_data_vacancies_company()
    items2 = create_table_employers_postgres()
    items3 = push_data_in_employers()
    items4 = create_table_vacancia_postgres()
    items5 = push_data_in_vacancies()
if __name__ == "__main__":
    user_interaction()