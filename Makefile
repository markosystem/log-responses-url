help:
	@echo "#### Help ###"
	@echo "setup => Install the dependencies;"
	@echo "docker-up => Up services docker like mongodb;"
	@echo "run => Starts the process of mapping the urls specified in the variable 'SITES_HEALTHCHECK';"
	@echo "all => Run all process, such as: help setup docker-up end run;"
	@echo "For database: visit the .env_default file."

setup:
	@echo "Instaling dependences"
	pip install -r requirements.txt
	@echo ""

docker-up:
	@echo "Run docker-compose up"
	docker-compose -f ./utils/docker-compose.yml up -d
	@echo ""

run:
	@echo "Run script python"
	python ./main.py
	@echo ""

all: help setup docker-up run