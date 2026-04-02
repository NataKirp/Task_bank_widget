from src.file_readers import read_csv_file, read_excel_file
from src.utils import load_operations


def display_menu() -> str:
    """
    Функция отображает приветствие, меню и запрашивает выбранный пользователем тип файла с транзакциями
    :return: номер пункта меню, выбранный пользователем
    """
    while True:
        print('Выберите необходимый пункт меню: ')
        print('1. Получить информацию о транзакциях из JSON-файла.')
        print('2. Получить информацию о транзакциях из CSV-файла.')
        print('3. Получить информацию о транзакциях из XLSX - файла.')
        menu_choice = input('> ')
        if menu_choice in ['1', '2', '3']:
            return menu_choice
        else:
            print('Неправильное значение. Введите значение 1, 2 или 3.')


def process_file_choice(choice: str) -> list[dict]:
    """
    Функция выводит в консоль выбранный пользователем пункт меню с типом файла
    и создает список словарей из указанного типа файла
    :param choice: число, соответсвующее номеру пункта в меню выбора типа файла с транзакциями
    :return: список словарей, загруженный из файла выбранного типа
    """
    file_types = {
        '1': 'JSON-файл',
        '2': 'CSV-файл',
        '3': 'XLSX-файл'
    }
    print(f'Для обработки выбран {file_types[choice]}.')

    if file_types[choice] == 'JSON-файл':
        data = load_operations('data/operations.json')
    elif file_types[choice] == 'CSV-файл':
        data = read_csv_file('data/transactions.csv')
    elif file_types[choice] == 'XLSX-файл':
        data = read_excel_file('data/transactions_excel.xlsx')

    return data


def select_status() -> str | None:
    """
    Функция запрашивает один из вариантов статуса банковской операции для фильтрации
    :return: сообщение с указанием выбранного статуса
    """
    while True:
        print('Введите статус, по которому необходимо выполнить фильтрацию.\n'
              'Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING.')
        status_choice = input('> ').upper()
        if status_choice in ['EXECUTED', 'CANCELED', 'PENDING']:
            print(f'Операции отфильтрованы по статусу {status_choice}')
            return status_choice
        else:
            print(f'Статус операции {status_choice} недоступен.')


def sort_params() -> bool | None:
    """
    Функция запрашивает необходимость сортировки по дате и порядок сортировки
    :return: булево для указания порядка сортировки или None, если сортировка не нужна
    """
    while True:
        print('Отсортировать операции по дате? Да/Нет')
        sort_date_choice = input('> ').lower()
        if sort_date_choice == 'да':
            while True:
                print('Отсортировать по возрастанию или по убыванию?')
                order_sort_choice = input('> ').lower()
                if order_sort_choice == 'по возрастанию':
                    order = False
                    break
                elif order_sort_choice == 'по убыванию':
                    order = True
                    break
                else:
                    print('Неправильное значение. Введите: По возрастанию или: По убыванию')
            break
        elif sort_date_choice == 'нет':
            order = None
            break
        else:
            print('Неправильное значение. Введите: Да или: Нет')
    return order


def rub_params() -> bool:
    """
    Функция запрашивает необходимость отбора только рублевых транзакций
    :return: булево, обозначающее нужен отбор или нет
    """
    while True:
        print('Выводить только рублевые транзакции? Да/Нет')
        sort_rub_choice = input('> ').lower()
        if sort_rub_choice == 'да':
            rub_only = True
            break
        elif sort_rub_choice == 'нет':
            rub_only = False
            break
        else:
            print('Неправильное значение. Введите: Да или: Нет')
    return rub_only


def get_user_input(prompt: str) -> str:
    """
    Функция запрашивает у пользователя текстовый ввод в консоли
    :param prompt: результат ввода пользователя
    :return: отформатированный текст ввода пользователя
    """
    return input(prompt).lower().strip()


def description_param(get_input=get_user_input) -> str | None:
    """
    Функция запрашивает необходимость фильтрации транзакций по заданному слову в описании
    :param get_input: отформатированный ответ пользователя
    :return: слово для фильтрации или None
    """
    while True:
        filter_descr_choice = get_input(
            'Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n> '
        )
        if filter_descr_choice == 'да':
            search_word = get_input('Введите слово для фильтрации транзакций\n> ')
            break
        elif filter_descr_choice == 'нет':
            search_word = None
            break
        else:
            print('Неправильное значение. Введите: Да или: Нет')
    return search_word
