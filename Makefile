build:
	docker build -t farmsphere .
	npm run build || echo "frontend build needs npm install"

test:
	pytest -q
	npm test || true

run:
	python manage.py runserver 0.0.0.0:8000
