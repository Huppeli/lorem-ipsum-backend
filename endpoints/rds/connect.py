import psycopg2
from common import helpers

HOST = 'junction2018.cd3wkyqepubp.eu-west-1.rds.amazonaws.com'


def handler(event, context):
    db = psycopg2.connect(host=HOST, user='toni', password='loremipsum', dbname='loremipsum')
    cursor = db.cursor()
    cursor.close()
    return helpers.gen_response('successful connection')
