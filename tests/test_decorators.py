import pathlib

from src.decorators import log


# Тестирование обработки исключений
def test_log_errors(capsys):
    @log()
    def my_function(x, y):
        return x / y

    my_function(2, 0)
    captured = capsys.readouterr()
    assert "Результат выполнения функции my_function: division by zero. Inputs: (2, 0), {}" in captured.out


# Тестирование вывода в консоль
def test_log_to_console(capsys):
    @log()
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert "Начало выполнения функции my_function:" in captured.out
    assert "Конец выполнения функции my_function:" in captured.out
    assert "Результат выполнения функции my_function: ok. Inputs: (1, 2), {}" in captured.out


# Тестирование записи в файл
def test_log_to_file(tmp_path: pathlib.Path):
    filename = tmp_path / 'log.txt'

    @log(str(filename))
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    with open(filename, 'r', encoding='utf-8') as file:
        log_txt = file.read()
        assert "Начало выполнения функции my_function:" in log_txt
        assert "Конец выполнения функции my_function:" in log_txt
        assert "Результат выполнения функции my_function: ok. Inputs: (1, 2), {}" in log_txt
