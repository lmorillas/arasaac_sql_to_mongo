# arasaac sql to mongo
Build mongo collections for araaac images &amp; translations 

* python2
* docker-compose para mongo y mysql (legado)
* configuración de idiomas en `idiomas.json`
* configurar bases de datos en src/procesar_sql_a_mongo_pymongo.py

```bash
git clone https://github.com/lmorillas/arasaac_sql_to_mongo.git
docker-compose up -d
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd src 
python procesar_sql_a_mongo_pymongo.py
```
