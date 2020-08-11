build : 
	virtualenv venv -p python
	source ./venv/bin/activate; \
	pip3 install -r requirements.txt; \

