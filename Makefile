test:
	pytest -vv --cov=starlettelab --junitxml=.junit/test-results.xml

isort:
	isort --recursive .

black:
	black .

format: isort black

lint-isort:
	isort --recursive --check-only .

lint-black:
	black --check .

lint-safety:
	safety check --full-report

lint: lint-isort lint-black lint-safety
