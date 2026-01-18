.PHONY: run test export clean

run:
	python3 -m src.main

test:
	pytest

export:
	python3 -m src.main

clean:
	rm -rf __pycache__ .pytest_cache
