import pandas as pd


def read_csv_file(file_path: str) -> list[dict]:
    """
    Функция для считывания финансовых операций из CSV файла
    :param file_path: Путь к файлу CSV
    :return: Список словарей с транзакциями
    """
    df = pd.read_csv(file_path, delimiter=';')
    result = df.to_dict(orient='records')
    return result


def read_excel_file(file_path: str) -> list[dict]:
    """
    Функция для считывания финансовых операций из Excel файла
    :param file_path: Путь к файлу Excel
    :return: Список словарей с транзакциями
    """
    df = pd.read_excel(file_path)
    result = df.to_dict(orient='records')
    return result

#
# if __name__ == '__main__':
#     print(read_csv_file('../data/transactions.csv'))
#     print(read_excel_file('../data/transactions_excel.xlsx'))
