all:
	sudo pip install -r requirements.txt && \
  python main.py

start:
	python app.py
	
test:
	python -m tests.runner
