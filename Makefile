BACKEND_DIR := ./backend

m:
	python ${BACKEND_DIR}/manage.py migrate

db:
	python ${BACKEND_DIR}/manage.py makemigrations

r:
	python ${BACKEND_DIR}/manage.py runserver