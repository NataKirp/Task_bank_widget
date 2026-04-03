import sys

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.user_input import display_menu, process_file_choice, select_status, sort_params, rub_params, description_param
from src.utils import process_bank_search, process_bank_operations
from src.widget import get_date, mask_account_card


def main():
    """Главная функция: управление выполнением программы."""
    try:
        print('Привет! Добро пожаловать в программу работы с банковскими транзакциями.')
        menu_choice = display_menu()  # запрос типа файла
        data = process_file_choice(menu_choice)  # создание списка словарей из выбранного типа файла
        status = select_status()  # выбор статуса для фильтрации
        filtered_by_state = filter_by_state(data, status)  # создание списка словарей, отфильтрованного по статусу
        order = sort_params()
        rub_only = rub_params()
        search_word = description_param()
        if order is None:
            transactions = filtered_by_state
        else:
            transactions = sort_by_date(filtered_by_state, order)  # сортировка по дате
        if rub_only:
            transactions = list(filter_by_currency(transactions, 'RUB'))  # фильтрация по RUB, если 'да'
        else:
            pass
        if search_word:
            transactions = process_bank_search(transactions, search_word)  # фильтрация по слову в описании
        else:
            pass
        if not transactions:
            print('\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации')
        else:
            print('\nРаспечатываю итоговый список транзакций...\n')
            if search_word:
                grouped_by_description = process_bank_operations(transactions, search_word)
            else:
                categories = list(set([item['description'] for item in transactions if 'description' in item]))
                grouped_by_description = process_bank_operations(transactions, categories)

            print(f'Всего банковских операций в выборке:')
            for item, count in grouped_by_description.items():
                print(f'Категория {item}: {count} операций')

        for item in transactions:
            for key, value in item.items():
                if value != value:  # замена nan на пустую строку
                    item[key] = ''

            item['date'] = get_date(item.get('date'))
            item['from'] = mask_account_card(item.get('from', ''))
            item['to'] = mask_account_card(item.get('to', ''))

            print(f"\n{item.get('date')} {item.get('description')}")
            print(f"{item.get('from', 'нет данных')} -> {item.get('to', 'нет данных')}")
            if menu_choice == '1':
                print(
                    f"Сумма: {item.get('operationAmount').get('amount')} {item.get('operationAmount').get('currency').get('code')}\n")
            else:
                print(f"Сумма: {item.get('amount')} {item.get('currency_code')}\n")

        print("Программа успешно завершена.")

    except KeyboardInterrupt:
        print("\nПрограмма принудительно остановлена пользователем.")
        sys.exit(0)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
