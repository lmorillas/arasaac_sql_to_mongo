# arasaac sql to mongo
Build mongo collections for araaac images &amp; translations 

* python2
* docker-compose para mongo y mysql (legado)
* configuración de idiomas en `idiomas.json`
* configuración de entorno en src/.env


```bash
git clone https://github.com/lmorillas/arasaac_sql_to_mongo.git
docker-compose up -d
virtualenv env
source env/bin/activate
pip install -r requirements.txt
cd src 
python procesar_sql_a_mongo_pymongo.py
```

## Ejemplo .env

``` bash
MYSQL_DATABASE = 'arasaac'
MONGO_DATABASE = 'arasaac'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'example'
HOST_MONGO = 'host_name'
HOST_MYSQL = 'host_name'
FOLDER_LOCUTIONS = '<ruta a carpeta raíz de locuciones>'  
FOLDER_SVGS = '<ruta a carpeta de svgs>'
```
