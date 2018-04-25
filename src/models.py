# coding: utf-8

'''
[  
  {
      "_id" : ObjectId("5aabb680d5a3febb7f3487fc"),
      "idPictogram" : 1234,
      "keywords" : [ 
          {
	      "idKeyword": 1825
              "keyword" : "comida",
              "locution" : 34567,
              "meaning" : "Acto de alimentarse a mediodía",
              "lse" : 17589,
              "type" : "noun",
              "downloads" : 0,
              "sinonyms" : [ 
                  "manjar", 
                  "alimento"
              ]
          }, 
          {
	      "idKeyword": 1826 	
              "keyword" : "cena",
              "locution" : 23657,
              "meaning" : "Acto de alimentarse por la noche",
              "lse" : 17629,
              "type" : "noun",
              "downloads" : 0
          }
      ],
      "status" : "publish",
      "created": {
            "$date": "2015-03-23T09:08:31Z"
        }, 
      "lastUpdate": {
            "$date": "2015-03-23T09:08:31Z"
        }, 
      "license" : "MIT",
      "downloads" : 0,
      "authors" : [ ----------------------------------------> Referencia a colección users
          {
              "name" : "Pepito",
              "email" : "prueba@prueba.com",
              "url" : "http://www.marca.es",
              "company" : "DGA"
          }
      ],
      "tags" : [ 
          "alimentación", 
          "plato"
      ],
      "legacyTags": [legacyTags]
  },
]

'''

from pymongo import MongoClient
client = MongoClient()

class Word(EmbeddedDocument):
    id_palabra = IntField()
    palabra = StringField()
    definicion = StringField()
    tipo_palabra = StringField()
    id_colaborador = IntField()
    fecha_creacion = DateTimeField()
    ultima_modificacion = DateTimeField()
    estado = IntField()

class Author(EmbeddedDocument):
    id_author = IntField()
    email = StringField(required=False)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)

class AraImage(Document):
    title = StringField(max_length=120)
    author = EmbeddedDocumentField(Author)
    #image = fs_ImageField(fs=fs_images, thumbnails=[60, 60], required=False)
    image = StringField(required=True)
    labels = ListField(EmbeddedDocumentField(Word))
    tags = ListField(StringField())
    created = DateTimeField()
    modificated = DateTimeField()
    id_image = IntField()
    image_type = StringField()
    licencia = StringField()

    meta = {
         'abstract': True
    }

class AraImage_es(AraImage):
    meta = {
        'collection': 'araimage_es'
    }

class AraImage_en(AraImage):
    meta = {
        'collection': 'araimage_en'
    }

class AraImage_ru(AraImage):
    meta = {
        'collection': 'araimage_ru'
    }

class AraImage_ro(AraImage):
    meta = {
        'collection': 'araimage_ro'
    }

class AraImage_ar(AraImage):
    meta = {
        'collection': 'araimage_ar'
    }

class AraImage_zh(AraImage):
    meta = {
        'collection': 'araimage_zh'
    }


class AraImage_bg(AraImage):
    meta = {
        'collection': 'araimage_bg'
    }


class AraImage_pl(AraImage):
    meta = {
        'collection': 'araimage_pl'
    }


class AraImage_fr(AraImage):
    meta = {
        'collection': 'araimage_fr'
    }


class AraImage_ca(AraImage):
    meta = {
        'collection': 'araimage_ca'
    }


class AraImage_eu(AraImage):
    meta = {
        'collection': 'araimage_eu'
    }


class AraImage_de(AraImage):
    meta = {
        'collection': 'araimage_de'
    }


class AraImage_it(AraImage):
    meta = {
        'collection': 'araimage_it'
    }


class AraImage_pt(AraImage):
    meta = {
        'collection': 'araimage_pt'
    }


class AraImage_ga(AraImage):
    meta = {
        'collection': 'araimage_ga'
    }


class AraImage_br(AraImage):
    meta = {
        'collection': 'araimage_br'
    }
