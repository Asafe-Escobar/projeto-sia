VENV=.venv
PYTHON=$(VENV)/bin/python3
PIP=$(VENV)/bin/pip

init:
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

run:
	$(VENV)/bin/streamlit run app.py

collect:
	$(PYTHON) -m src.cli

test:
	$(PYTHON) -m unittest discover -s src/tests

format:
	$(VENV)/bin/black .

clean:
	rm -rf __pycache__ .pytest_cache .mypy_cache
