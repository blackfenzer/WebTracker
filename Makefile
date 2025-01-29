BACKEND_DIR := ./backend
FRONTEND_DIR := ./frontend
m:
	python ${BACKEND_DIR}/manage.py migrate

db:
	python ${BACKEND_DIR}/manage.py makemigrations

r:
	python ${BACKEND_DIR}/manage.py runserver

dev:
	cd ${FRONTEND_DIR} && yarn run dev

start: r dev