PYTHON = python
MANAGE = $(PYTHON) manage.py

install:        ## Install project dependencies
	pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

migrations:     ## Create new database migrations
	$(MANAGE) makemigrations

migrate:        ## Apply database migrations
	$(MANAGE) migrate

run:      ## Run the Django development server
	$(MANAGE) runserver