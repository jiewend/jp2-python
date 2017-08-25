all:
	sudo pip install -r requirements.txt && \
  python app.py

start:
	python app.py
	
test:
	python -m tests.runner
