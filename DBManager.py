import psycopg2


class DBManager:
    """Класс для подключения и работы с DB postgres"""

    def __init__(self, database: str = 'KUR5', user: str = 'postgres',
                 password: str = 'Ralina:11', host: str = 'localhost'):
        self.__database = database
        self.__user = user
        self.__password = password
        self.__host = host

    def get_companies_and_vacancies_count(self):
        """Получает список всех компаний и количество вакансий у каждой компании."""
        con = psycopg2.connect(database=self.__database, user=self.__user, password=self.__password, host=self.__host)

        cur = con.cursor()
        cur.execute(
            '''SELECT company_name, COUNT(*) from employers
            INNER JOIN vacancies USING (employers_id)
            GROUP BY company_name
            ORDER BY company_name;'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_all_vacancies(self):
        '''Получает список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию'''

        con = psycopg2.connect(database=self.__database, user=self.__user, password=self.__password, host=self.__host)

        cur = con.cursor()
        cur.execute(
            '''SELECT company_name, vacancies.vacancies_name, vacancies.salary_from, vacancies.salary_to, vacancies.url 
            FROM employers
            INNER JOIN vacancies USING (employers_id)
            ORDER BY company_name;'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_avg_salary(self):
        '''Получает среднюю зарплату по вакансиям'''

        con = psycopg2.connect(database=self.__database, user=self.__user, password=self.__password, host=self.__host)

        cur = con.cursor()
        cur.execute(
            '''SELECT AVG(salary_from) from vacancies;'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_vacancies_with_higher_salary(self):
        '''Получает список всех вакансий, у которых зарплата выше средней по всем вакансиям'''

        con = psycopg2.connect(database=self.__database, user=self.__user, password=self.__password, host=self.__host)

        cur = con.cursor()
        cur.execute(
            '''SELECT  vacancies_name
            FROM vacancies
            WHERE salary_from > ( select AVG(salary_from) from vacancies);'''
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data

    def get_vacancies_with_keyword(self, word):
        '''Получает список всех вакансий, в названии которых содержатся переданные в метод слова, например “python”.'''

        con = psycopg2.connect(database=self.__database, user=self.__user, password=self.__password, host=self.__host)

        cur = con.cursor()
        cur.execute(
            f"SELECT * FROM vacancies WHERE vacancies_name LIKE'%{word}%'"
        )
        data = cur.fetchall()
        cur.close()
        con.close()
        return data
