# to activate the venv run: source venv/bin/activate

setup:
	@python3 -m venv venv 
	@pip3 install -r requirements.txt

freeze:
	@pip3 freeze > requirements.txt

run:
	@uvicorn main:app --reload
