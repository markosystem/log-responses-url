help:
	@echo "Help..."
	@echo "..."
	@echo ""

setup:
	@echo "Instaling dependences..."
	pip install -r requirements.txt
	@echo ""

run:
	@echo "Run script python..."
	python ./main.py
	@echo ""

all: help setup run