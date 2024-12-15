dependencies:
	- pip install -r requirements.txt

radon: 
	- radon cc .\startup.py

lint:
	- black .

unittest:
	- python -m unittest discover -s tests/units -p 'test_*.py'

