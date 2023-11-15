django-insecure-ut0v9((fjv_1rz1pe)2%m0!wngf0%zx%lsdc=y!hgc!rt2sv4o

### Initial
1. `PROJECT_ID=pongtogether`
2. `gcloud config set project $PROJECT_ID`
3. More: [GitHub](https://github.com/GoogleCloudPlatform/serverless-expeditions/tree/main/cloud-run-django-terraform)

### Auflistung von Commands die Services in Google Cloud neu aufzubauen:
1. Im env.tpl die Variable auf `USE_CLOUD_SQL_AUTH_PROXY=true`
2. run dienst löschen
3. `gcloud builds submit`
4. `terraform apply -var project=pongtogether`
5. `gcloud builds submit --config cloudbuild-migrate.yaml`

### Wenn Lokal gearbeitet wird:
1. Google Proxy Starten: `cloud-sql-proxy.exe --address 0.0.0.0 --port 1234 pongtogether:europe-west4:pongt`  
2. Im env.tpl die Variable auf `USE_CLOUD_SQL_AUTH_PROXY=true`
3. `python manage.py makemigrations`
4. `python manage.py makemigrations polls`
5. `python manage.py makemigrations polls`
6. `python manage.py migrate`
7. `python manage.py collectstatic`
8. `python manage.py runserver`