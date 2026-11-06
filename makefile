install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt

check-types:
	./scripts/check_types.sh .

check-styles:
	./scripts/check.sh

fix:
	./scripts/fix.sh

clean:
	rm -rf __pycache__ *.pyc

run:
	make generate-actions
	./scripts/uv_run.sh main.py

test:
	pytest --disable-warnings $(ARGS) -vv -s

editor:
	python level_editor.py

uv-install:
	cd src/PyEng && ../../scripts/uv_install.sh

uv-update:
	cd src/PyEng && ../../scripts/uv_update.sh

generate-actions:
	python src/pyeng/components/system/input/generate_actions.py
	ruff format data/config/input_actions.py