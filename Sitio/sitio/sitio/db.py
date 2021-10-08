import os
BASE_DIR =  os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SQLITE ={
    'default':{
        'ENGINE':'django.db.backends.sqlite3',
        'NAME':os.path.join(BASE_DIR,'Oras.sqlite3')
        
    }
}
POSTGRESQL ={
    'default':{
        'ENGINE':'django.db.backends.postgresql_psycopg2',
        'NAME':'Oras',
        'USER':'postgres',
        'PASSWORD':'password',
        'HOTS':'localhost',
        'PORT':'5432'
    }
}
MYSQL ={
    'default':{
        'ENGINE':'django.db.backends.mysql',
        'NAME':'Oras',
        'USER':'root',
        'PASSWORD':'12345',
        'HOTS':'localhost',
        'PORT':'3306'
    }
}