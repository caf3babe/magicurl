install:
	pip3 install -r requirements.txt
	python3 setup.py test
	python3 setup.py install

develop:
	pip3 install -r requirements.txt
	python3 setup.py test
	python3 setup.py develop
