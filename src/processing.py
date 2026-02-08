def filter_by_state(list_of_dicts: list[dict], state: str = "EXECUTED") -> list[dict]:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    :param list_of_dicts: Список словарей
    :param state: Ключ, по значению которого фильтруется список (по умолчанию 'EXECUTED')
    :return: Список с заданным значением ключа
    """
    target_state = []
    for item in list_of_dicts:
        if item["state"] == state:
            target_state.append(item)
    return target_state


def sort_by_date(list_of_dicts: list[dict], descending: bool = True) -> list[dict]:
    """
    Функция принимает список словарей и необязательный параметр,
    задающий порядок сортировки (по умолчанию — убывание).
    Функция должна возвращать новый список, отсортированный по дате (date).
    :param list_of_dicts: Список словарей
    :param descending: Порядок сортировки (False - возрастание, True - убывание)
    :return: Отсортированный список
    """
    return sorted(list_of_dicts, key=lambda item: item["date"], reverse=descending)


if __name__ == "__main__":
    transactions = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    print(filter_by_state(transactions, "EXECUTED"))
    print(sort_by_date(transactions))
