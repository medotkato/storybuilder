init:
	python3 -m pip install -r requirements.txt

test:
	python3 -m pytest tests

.PHONY:
	init test
