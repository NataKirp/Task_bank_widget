import json
import os.path


def load_operations(file_path: str) -> list[dict]:
    """
    Функция загружает данные о финансовых транзакциях и возвращает их в виде словаря
    :param file_path: путь до JSON-файла с данными о транзакциях
    :return: словарь с данными о транзакциях
    """
    if not os.path.exists(file_path):
        print('Файл не найден')
        return []
    elif os.path.getsize(file_path) == 0:
        print('Файл пуст')
        return []
    else:
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)

            if not isinstance(data, list):
                print('Файл содержит не список')
                return []

    return data
#
# if __name__ == "__main__":
#     print(load_operations(os.path.join(os.path.dirname(__file__), '../data/operations.json')))
