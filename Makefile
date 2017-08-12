default: dev

clean:
	make -C app/static clean

dev:
	make -C app/static dev

prod:
	make -C app/static prod

check:
	python -m unittest discover app/

run: prod
	gunicorn --chdir app api:app --log-level debug
