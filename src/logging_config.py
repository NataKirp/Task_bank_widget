import logging
import os

os.chdir('C:/Users/Vasilyev/Documents/Python/Homework/task_bank_widget')


def setup_logging(module_name: str):
    logger = logging.getLogger(module_name)
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(f'logs/{module_name}.log', mode='w', encoding='utf-8')
    file_formatter = logging.Formatter('%(asctime)s : %(filename)s : %(levelname)s : %(message)s')
    file_handler.setFormatter(file_formatter)
    logger.addHandler(file_handler)
    return logger
