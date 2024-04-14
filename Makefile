# to activate the venv run: source venv/bin/activate

setup:
	@python3 -m venv venv 
	@pip3 install -r requirements.txt

freeze:
	@pip3 freeze > requirements.txt

docker:
	@docker-compose up -d

run:	
	@uvicorn main:app --reload	

alembic-revision:
	@alembic revision --autogenerate

alembic-upgrade:
	@alembic upgrade head