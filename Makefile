prepare-venv: clean
	@echo "Creating new virtual environment..."
	virtualenv -p python3.6 --no-site-packages env
	env/bin/pip install -r requirements.txt

update-requirements:
	@echo "Updating environment requirements..."
	env/bin/pip freeze > requirements.txt

start:
	@echo "Not implemented..."

clean:
	@echo "Deleting old virtual environment..."
	rm -rf ./env
