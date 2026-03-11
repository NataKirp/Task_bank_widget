import json
import os.path

from src.logging_config import setup_logging

utils_logger = setup_logging('utils')


def load_operations(file_path: str) -> list[dict]:
    """
    Функция загружает данные о финансовых транзакциях и возвращает их в виде словаря
    :param file_path: путь до JSON-файла с данными о транзакциях
    :return: словарь с данными о транзакциях
    """
    utils_logger.info('Начало работы функции load_operations')
    if not os.path.exists(file_path):
        utils_logger.error(f'Файл {file_path} не найден')
        print('Файл не найден')
        return []
    elif os.path.getsize(file_path) == 0:
        utils_logger.warning(f'Файл {file_path} пуст')
        print('Файл пуст')
        return []
    else:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
            if not isinstance(data, list):
                utils_logger.warning(f'Файл {file_path} содержит не список')
                print('Файл содержит не список')
                return []
    utils_logger.info(f'Файл {file_path} успешно прочитан')
    utils_logger.info('Вывод словаря с данными о транзакциях')
    utils_logger.info('Завершение работы функции load_operations')
    return data


# if __name__ == "__main__":
#     print(load_operations(os.path.join(os.path.dirname(__file__), '../data/operations.json')))
