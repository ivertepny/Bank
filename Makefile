build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d --remove-orphans

down:
	docker compose -f local.yml down

down-v:
	docker compose -f local.yml down -v

banker-config:
	doccker compose -f local.yml config

makemigrations:
	docker compose -f local.yml --rm run api python manage.py makemigrations

migrate:
	docker compose -f local.yml --rm run api python manage.py migrate

collectstatic:
	docker compose -f local.yml --rm run api python manage.py collectstatic --noinput --clear

superuser:
	docker compose -f local.yml --rm run api python manage.py createsuperuser

flush:
	docker compose -f local.yml --rm run api python manage.py flush --noinput

network-inspect:
	docker network inspect banker_local_nw

banker-db:
	docker compose -f local.yml exec postgres psql --username=postgres --dbname=postgres

