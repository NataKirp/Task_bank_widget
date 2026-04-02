import json
import os.path
import re
from collections import Counter

# from data.transactions_input import transactions
# from src.file_readers import read_excel_file, read_csv_file
# # from data.transactions_input import transactions
from src.logging_config import setup_logging

utils_logger = setup_logging("utils")


def load_operations(file_path: str) -> list[dict]:
    """
    Функция загружает данные о финансовых транзакциях и возвращает их в виде словаря
    :param file_path: путь до JSON-файла с данными о транзакциях
    :return: словарь с данными о транзакциях
    """
    utils_logger.info("Начало работы функции load_operations")
    if not os.path.exists(file_path):
        utils_logger.error(f"Файл {file_path} не найден")
        print("Файл не найден")
        return []
    elif os.path.getsize(file_path) == 0:
        utils_logger.warning(f"Файл {file_path} пуст")
        print("Файл пуст")
        return []
    else:
        with open(file_path, encoding="utf-8") as f:
            data = json.load(f)
            if not isinstance(data, list):
                utils_logger.warning(f"Файл {file_path} содержит не список")
                print("Файл содержит не список")
                return []
    utils_logger.info(f"Файл {file_path} успешно прочитан")
    utils_logger.info("Вывод словаря с данными о транзакциях")
    utils_logger.info("Завершение работы функции load_operations")
    return data


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция отбирает банковские операции по заданному описанию
    :param data: список словарей с данными о банковских операциях
    :param search: строка поиска
    :return: список словарей, у которых в описании есть данная строка
    """
    pattern = re.compile(search, re.IGNORECASE)
    filtered_list = []
    found = False  # Флаг для проверки хотя бы одной операции
    for d in data:
        # Проверяем, есть ли поле описание и содержит ли оно искомую строку
        description = d.get("description", "")
        if isinstance(description, str) and re.search(pattern, description):
            filtered_list.append(d)
            found = True
    if not found:
        print("Нет операций, соответствующих описанию")
    return filtered_list


def process_bank_operations(data: list[dict], categories: list | str) -> dict:
    """
    Функция подсчитывает количество банковских операций по заданным категориям
    :param data: список словарей с данными о банковских операциях
    :param categories: список категорий операций
    :return: словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории
    """
    descriptions = [
        key["description"]
        for key in data
        if isinstance(key, dict) and "description" in key
    ]

    # Проверка, список категорий - строка или список
    if isinstance(categories, str):
        # Если строка, фильтрация описания по вхождению категории в строку
        grouped_by_category = [
            item
            for item in descriptions
            if isinstance(item, str) and categories.lower() in item.lower()
        ]
    elif isinstance(categories, list):
        # Если список, фильтрация описания по вхождению категории в список
        grouped_by_category = [
            item
            for item in descriptions
            if isinstance(item, str)
            and item.lower() in [cat.lower() for cat in categories]
        ]
    else:
        raise TypeError("Перечень операций должен быть списком либо строкой")
    return dict(Counter(grouped_by_category))


# if __name__ == "__main__":
# print(load_operations(os.path.join(os.path.dirname(__file__), '../data/operations.json')))
# print(process_bank_search(transactions, 'перевод'))
# print(process_bank_search(transactions, 'Организации'))
# categories_list = ["Перевод со счета на счет", "Перевод с карты на карту", "Перевод организации"]
# print(process_bank_operations(transactions, categories_list))
#     trans_json = load_operations(os.path.join(os.path.dirname(__file__), '../data/operations.json'))
#     print(process_bank_operations(trans_json, "Организации"))
#     trans_xlsx = read_excel_file(os.path.join(os.path.dirname(__file__), '../data/transactions_excel.xlsx'))
#     print(process_bank_search(trans_xlsx, 'организации'))
#     print(process_bank_operations(trans_xlsx, "Организации"))
#     trans_csv = read_csv_file(os.path.join(os.path.dirname(__file__), '../data/transactions.csv'))
#     print(process_bank_search(trans_csv, 'организации'))
#     print(process_bank_operations(trans_csv, "Организации"))
