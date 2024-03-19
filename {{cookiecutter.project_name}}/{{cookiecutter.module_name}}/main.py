import logging
from {{cookiecutter.module_name}} import utils

def main():
    # setup_logging関数の呼び出し
    utils.setup_logging(log_level=logging.DEBUG, log_file='app.log')

if __name__ == "__main__":
    main()