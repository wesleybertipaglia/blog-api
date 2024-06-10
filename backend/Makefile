setup:	
	@pip3 install -r requirements.txt

requirements:
	@pip3 freeze > requirements.txt
run:	
	@uvicorn main:app --reload	

venv-init: 
	@python3 -m venv venv

venv-activate:
	@source venv/bin/activate

venv-deactivate:
	@source deactivate

docker-up:
	@docker compose up -d

docker-down:
	@docker compose down

alembic-init:
	@alembic init alembic

alembic-migration:
	@alembic revision --autogenerate -m "autogenerate migration"

alembic-upgrade:
	@alembic upgrade head