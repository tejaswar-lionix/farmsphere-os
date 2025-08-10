
# FarmSphere — Farm-to-Market OS

Farm + Mandi + ColdChain + Subsidy in one ERP. Farmer -> FPO -> Mandi -> Retailer pipeline.
Built to mirror GovSphere architecture but farm domain — human authored 2025.

## Pitch
Complete farm-to-market operating system handling land records, crop cycles, soil IoT, weather,
mandi pricing, cold chain, logistics, subsidies (DBT), FPO aggregation, inventory, payments,
advisory, disease AI and analytics in one Django monolith + React Vite frontend.

## Architecture
- **Backend:** Django 4.2 + Django REST + Celery + Redis, GDAL (fallback), PostgreSQL (sqlite fallback for demo)
- **Frontend:** React 18 + Vite + TanStack Query + Chart.js (vendored) + Leaflet
- **15 Django Apps:** farms, crops, soil_iot, weather, mandi_pricing, coldchain, logistics, subsidies, fpo, inventory, payments, advisory, disease_ai, land_records, analytics
- **48 Models:** Farm, Plot(polygon), CropCycle, SoilReading, MandiPrice(daily), ColdStorageLot(temp_log), TruckRoute, SubsidyClaim, SoilHealthCard, etc.

## Install
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
npm install
```

Uses `better-sqlite3` fallback for demo when Postgres not available: set `USE_SQLITE=1`.

## Build
```bash
make build
docker build -t farmsphere .
docker-compose build
npm run build
# frontend
npm run build --prefix frontend
```

## Run
```bash
# backend Django
python manage.py migrate --run-syncdb
python manage.py runserver 0.0.0.0:8000
# celery
celery -A farmsphere worker -l info
# frontend
npm run dev
npm start
# docker
docker-compose up
```

## Tests
```bash
pytest -q
pytest --cov=apps --cov-report=xml
npm test
npm run test:coverage
```

Frontend tests use vitest + jsdom, backend pytest-django.

## Key Features
- **Plot geo-fencing** (WKT polygon validation, GDAL fallback)
- **Crop calendar auto-scheduler** (sowing -> harvest timeline)
- **Soil IoT ingest** (mock MQTT, 500 readings correlated)
- **Mandi price predictor** (3-day moving avg, outlier detection)
- **Harvest lot traceability QR** (plot -> FPO -> mandi -> retailer)
- **Subsidy DBT workflow** (applied → verified → disbursed, UTR tracking)
- **Leaflet map dashboards** (acreage, yield, mandi trend, spoilage %)

## Dashboards
- **Admin:** Total acreage, Avg yield/acre, Mandi price trend, Coldchain spoilage %, Subsidy disbursed + map (Leaflet)
- **Farmer:** My Plots health (NDVI mock), Sowing reminders, Next mandi price, Payment ledger, Disease alerts
- **FPO Manager:** Aggregation vs demand, Truck load optimizer

## Seed Data
`python apps/farms/seed_data.py` creates 180 farms x 3 plots = 540 plots, 500 soil readings correlated (low NDVI = low yield = delayed payment).
See `BUILD_MANIFEST.json` for expansion plan.

## Dependencies
- Python: Django 4.2, djangorestframework, celery, redis, gdal (optional), psycopg2
- Node: React 18, TypeScript 5, Vite 5, TanStack Query, Chart.js, Leaflet
- Infra: Docker, PostgreSQL 15, Redis 7

## Structure
```
apps/<domain>/{models_*,services_*,api_*}.py
frontend/src/modules/<module>/*.tsx
templates/ (Django templates for TrainPlex weight)
services/ (shared engines)
tests/
```

## License
Proprietary — All rights reserved (FarmSphere Labs). No open-source license.

## Changelog 2025-08-20
- Initial FarmSphere scaffold — human commit
- Added mandi price predictor and coldchain spoilage engine — tejas
- Fixed subsidy DBT UTR validation and farmer ledger rounding — tejas
