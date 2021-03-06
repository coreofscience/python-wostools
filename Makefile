.PHONY: clean clean-test clean-pyc clean-build docs help, test-watch
.DEFAULT_GOAL := help

NOTIFY_FILE := /tmp/pytest-$$(pwd | md5sum | cut -d " " -f 1)

define BROWSER_PYSCRIPT
import os, webbrowser, sys

try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 wostools tests

test: ## run tests quickly with the default Python
	python -m pytest

test-watch:
	@ptw \
		--ext "py,feature" \
		--onpass "coverage report --skip-empty --skip-covered -m" \
		--onfail "notify-send.sh -R $(NOTIFY_FILE) -i face-worried --hint int:transient:1 'Test failed' 'Ooops we have a problem, not all tests passed'" \
		--onexit "notify-send.sh -R $(NOTIFY_FILE) -i media-playback-stop --hint int:transient:1 'Test runner stopped' 'Just so you know, the test runner stopped'" \
		--runner "coverage run --source wostools -m pytest" \

coverage: ## check code coverage quickly with the default Python
	coverage run --source wostools -m pytest
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python setup.py sdist
	python setup.py bdist_wheel
	ls -l dist

install: clean ## install the package to the active Python's site-packages
	python setup.py install
