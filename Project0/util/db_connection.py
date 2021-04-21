import psycopg2
from psycopg2._psycopg import OperationalError


def create_connection():
    try:
	# CREDENTIALS DELETED FOR GITHUB
        conn = psycopg2.connect(
            database=,
            user=,
            password=,
            host='project0db.cx6o2okagtle.us-east-1.rds.amazonaws.com',
            port='5432'
        )
        return conn
    except OperationalError as e:
        print(f"{e}")
    # return conn


connection = create_connection()
