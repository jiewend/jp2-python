all:
	sudo pip install -r requirements.txt && \
  python main.py

start:
	python main.py

test:
	python -m tests.runner
