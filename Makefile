start:
	~/anaconda3/bin/pip install -r requirements.txt \
	&& ~/anaconda3/bin/python3 app.py

test:
	~/anaconda3/bin/python3 -m unittest tests/*.py
