install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:
	black *.py

lint:
	pylint --disable=R,C mylib

test:
	python -m pytest -vv test_mathcode.py

all: install format lint test
