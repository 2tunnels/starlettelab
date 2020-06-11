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

lint-mypy:
	mypy .

lint-safety:
	safety check --full-report

lint: lint-isort lint-black lint-mypy lint-safety

docker-build:
	docker image build -t starlettelab .

docker-run:
	docker container run -it -p 8000:8000 starlettelab

helm-upgrade:
	helm upgrade \
		--atomic \
		--install \
		--namespace starlettelab \
		--set image.tag=v0.3.4 \
		--set secrets.EXCEPTION_SECRET=swordfish \
		--set secrets.BUGSNAG_API_KEY=secret \
		starlettelab \
		./charts/starlettelab/

patch:
	bump2version patch
	git push --follow-tags

minor:
	bump2version minor
	git push --follow-tags
