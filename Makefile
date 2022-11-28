install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv *.py

format:	
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=test_.*?py *.py

refactor: format lint

build:
	docker build -t fastapi_cd .

deploy:
	#pushes container to ECR (your info will be different!)
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 309324599654.dkr.ecr.us-east-1.amazonaws.com
	docker build -t fastapi_cd .
	docker tag fastapi_cd:latest 309324599654.dkr.ecr.us-east-1.amazonaws.com/fastapi_cd:latest
	docker push 309324599654.dkr.ecr.us-east-1.amazonaws.com/fastapi_cd:latest

all: install format lint build deploy test
