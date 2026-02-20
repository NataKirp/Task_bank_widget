import time
from typing import Any, Callable, Optional


def log(
    filename: Optional[str] = None,
) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """
    Декоратор для логирования выполнения функции.
    Если задан `filename`, лог записывается в файл, иначе выводится в консоль.
    """

    def wrapper(func: Callable[..., Any]) -> Callable[..., Any]:
        """
        Возвращает обёртку, которая логирует выполнение функции `func`.
        """

        def inner(*args: Any, **kwargs: Any):
            """
            Обёртка для выполнения функции `func` с логированием её результата и ошибок.
            """
            result = None
            text_error = ""
            start_time = time.time()
            formatted_start_time = time.strftime("%H:%M:%S", time.localtime(start_time))
            try:
                result = func(*args, **kwargs)
            except Exception as e:
                text_error = str(e)
            end_time = time.time()
            formatted_end_time = time.strftime("%H:%M:%S", time.localtime(end_time))
            log_text = (
                f"Начало выполнения функции {func.__name__}: {formatted_start_time}\n"
                f"Конец выполнения функции {func.__name__}: {formatted_end_time}\n"
                f"{func.__name__} ok. Результат: {result}"
                if text_error == ""
                else f"{func.__name__} error: {text_error}. Inputs: {args}, {kwargs}"
            )
            if filename is None:
                print(log_text)
            else:
                with open(filename, "w", encoding="utf-8") as file:
                    file.write(log_text)

        return inner

    return wrapper


@log()
def my_function(x, y):
    return x / y


my_function(2, 1)
