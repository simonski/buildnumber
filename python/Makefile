default_target: build
.PHONY : default_target upload

# VERSION := $(shell $(PYTHON) setup.py --version)

clean:
	rm -rf dist
	rm -rf build
	rm -rf target
	rm -rf tests/.cache
	rm -rf .pytest_cache
	rm -rf buildnumber.db
	rm -rf buildnumber.egg-info
	rm -rf .eggs
	find . -name *.pyc -type f -delete
	find . -name *__pycache__ -delete
	python setup.py clean

test:
	python setup.py test

build: clean test
	python setup.py bdist_wheel --universal

upload: clean build
	twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
