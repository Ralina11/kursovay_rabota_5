import psycopg2
import json


def create_con():
    """Функция для подключения к БД Postgres"""
    con = psycopg2.connect(
        database='KUR5',
        user='postgres',
        password='Ralina:11',
        host='localhost'
    )

    return con


def create_table_employers_postgres() -> None:
    """
    Функция подключается к БД course_project_5 и создаёт таблицу employers
    """
    con = create_con()
    cur = con.cursor()
    cur.execute('''CREATE TABLE employers
            (id int PRIMARY KEY NOT NULL,
            name TEXT NOT NULL,
            url TEXT);'''
                )
    con.commit()
    con.close()


def push_data_in_employers(file_json: str = 'employers_data.json'):
    """Функция открывает файл, берёт данные и загружает их в таблицу employers"""
    result_companies: list[tuple] = []

    with open(file_json) as json_file:
        data = json.load(json_file)
    for row in data["items"]:
        items = tuple([row["id"], row["name"], row["url"]])
        result_companies.append(items)


    con = create_con()
    cur = con.cursor()
    for row in result_companies:
        cur.execute("INSERT INTO employers VALUES (%s, %s, %s)", row)
    con.commit()
    con.close()

def create_table_vacancia_postgres() -> None:
    """
    Функция подключается к БД course_project_5 и создаёт таблицу employers
    """
    con = create_con()
    cur = con.cursor()
    cur.execute('''CREATE TABLE vacancies
            (id serial PRIMARY KEY NOT NULL,
             employers_id INT REFERENCES employers(id) NOT NULL,
             name TEXT NOT NULL,
             url TEXT,
             salary_from int DEFAULT NUll,
             salary_to int DEFAULT NULL);
             '''
                )
    con.commit()
    con.close()

def push_data_in_vacancies(file_json: str = 'vacancies_data.json'):
    """Функция открывает файл, берёт данные и загружает их в таблицу employers"""
    result_vacancies: list[tuple] = []

    with open(file_json) as json_file:
        data = json.load(json_file)
    for key, value in data.items():
            row = value["items"]
            for r in row:
                id = r["id"],
                employers_id = r["employer"]["id"],
                name  = r["name"],
                url = r["url"],
                if r["salary"] is not None:
                    salary_from = r["salary"]["from"]
                    salary_to = r["salary"]["to"]
                else:
                    salary_from = 0
                    salary_to = 0
                items = tuple([id, employers_id, name, url, salary_from, salary_to])
                result_vacancies.append(items)


    con = create_con()
    cur = con.cursor()
    for row in result_vacancies:
        cur.execute("INSERT INTO vacancies VALUES (%s, %s, %s, %s, %s, %s)", row)
    con.commit()
    con.close()