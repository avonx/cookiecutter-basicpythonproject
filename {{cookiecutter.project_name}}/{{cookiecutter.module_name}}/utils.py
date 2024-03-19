import os
import logging
from datetime import datetime

def setup_logging(log_level=logging.INFO, log_file=None):
    """
    ロギングの設定を行う関数。

    Args:
        log_level (int): ロギングレベル。デフォルトはINFO。
        log_file (str): ログ出力先のファイルパス。指定されない場合、コンソールに出力。

    Returns:
        None
    """
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    if log_file:
        logging.basicConfig(filename=log_file, level=log_level, format=log_format)
    else:
        logging.basicConfig(level=log_level, format=log_format)

def get_current_timestamp():
    """
    現在のタイムスタンプを取得する関数。

    Returns:
        str: 現在のタイムスタンプ（YYYY-MM-DD HH:MM:SS形式）。
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def create_directory(directory):
    """
    指定されたディレクトリを作成する関数。

    Args:
        directory (str): 作成するディレクトリのパス。

    Returns:
        None
    """
    os.makedirs(directory, exist_ok=True)

def read_file(file_path):
    """
    指定されたファイルを読み込む関数。

    Args:
        file_path (str): 読み込むファイルのパス。

    Returns:
        str: ファイルの内容。ファイルが存在しない場合は空の文字列。
    """
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except FileNotFoundError:
        return ''

def write_file(file_path, content):
    """
    指定されたファイルにコンテンツを書き込む関数。

    Args:
        file_path (str): 書き込むファイルのパス。
        content (str): 書き込むコンテンツ。

    Returns:
        None
    """
    with open(file_path, 'w') as file:
        file.write(content)