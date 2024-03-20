# 4. Makefileの活用:
#     - `Makefile`を使用して、よく使用するコマンドを簡単に実行できるようにします。
#     - 仮想環境の作成と有効化: `make venv`コマンドを実行すると、仮想環境が作成され、必要な依存関係がインストールされます。
#     - テストの実行: `make test`コマンドを実行すると、テストが実行されます。
#     - コードのフォーマット: `make format`コマンドを実行すると、blackとisortを使用してコードがフォーマットされます。
#     - リンティング: `make lint`コマンドを実行すると、flake8を使用してコードのリンティングが行われます。
#     - クリーンアップ: `make clean`コマンドを実行すると、不要なファイルや一時ファイルが削除されます。

.PHONY: venv
venv:
	python{{ cookiecutter.python_version }} -m venv .venv
	git init
	.venv/bin/pip install --upgrade pip
	.venv/bin/pip install poetry
	.venv/bin/poetry config virtualenvs.in-project true
	.venv/bin/poetry install
	.venv/bin/pre-commit install

.PHONY: test
test:
	.venv/bin/pytest tests/

.PHONY: format
format:
	.venv/bin/black .
	.venv/bin/isort .

.PHONY: lint
lint:
	.venv/bin/flake8 .

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -rf *.egg-info
	rm -rf dist
	rm -rf build