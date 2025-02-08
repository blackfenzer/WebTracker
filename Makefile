BACKEND_DIR := ./backend
FRONTEND_DIR := ./frontend

m:
	python ${BACKEND_DIR}/manage.py migrate

db:
	python ${BACKEND_DIR}/manage.py makemigrations

server:
	python ${BACKEND_DIR}/manage.py runserver

client:
	cd ${FRONTEND_DIR} && yarn run dev

docker:
	docker compose up -d

beat:
	cd ${BACKEND_DIR} && celery -A tracker beat --loglevel=info

worker:
	cd ${BACKEND_DIR} && celery -A tracker worker --loglevel=info -P eventlet


pip:
	cd ${BACKEND_DIR} && pip install -r requirements.txt

node:
	cd ${FRONTEND_DIR} && pnpm install


irFrontend: node client

irBackend: pip db m server

