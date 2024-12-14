dependencies:
	- pip install -r requirements.txt

radon: 
	- radon cc .\startup.py

lint:
	- black .
