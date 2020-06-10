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
		--set image.tag=v0.3.1 \
		--set secrets.EXCEPTION_SECRET=swordfish \
		starlettelab \
		./charts/starlettelab/

bump-patch:
	bump2version patch
	git push --follow-tags

bump-minor:
	bump2version minor
	git push --follow-tags
