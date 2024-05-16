init: 
	@python3 -m venv venv

setup:	
	@pip3 install -r requirements.txt
	@alembic init alembic

freeze:
	@pip3 freeze > requirements.txt

docker:
	@docker compose up -d

run:	
	@uvicorn main:app --reload	

alembic-revision:
	@alembic revision --autogenerate

alembic-upgrade:
	@alembic upgrade head