ga:
	git add .

gp:
	git push

run: 
	uvicorn app.main:app --reload

cqch:
	black . && isort . && flake8 . && mypy .

celery:
	celery -A config worker -l INFO
