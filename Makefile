init:
	pip install -r requirements.txt

test:
	py.test tests

clean:
	find . -name '*.pyc' | xargs rm -rf
	find . -name '__pycache__' | xargs rm -rf
	rm  -rf checknml.egg-info
.PHONY: init test

