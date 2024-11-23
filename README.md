# Expenses test project

#### Setup
* `cp .env.local .env`
* `chown u+x expenses/scripts/run.sh` in case if permission changed
* `docker compose up -d --build`

#### API Documentation
Available here [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)

#### Codestyle check
`ruff check --fix` if you setup local poetry shell, otherwise `docker compose exec -it app ruff check --fix`

#### Notes
* pagination can be nice for retrieving data
* expenses api enpoints should be each in separate folder with own views and serializers, if project going to grow. 
Made it simple for this test app
* date input types use only YYYY-MM-DD format, can be changed in validators
* expenses/models.py:8 CATEGORY_CHOICES should be moved to model and saved in db,
instead on every change there will be new migration
* logging is absent
* docker-compose mount all folder and files, for production should be chnaged