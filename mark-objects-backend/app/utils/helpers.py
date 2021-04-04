import pymysql.cursors
from pymysql import MySQLError
from app.utils.config import Config


def query_database(query, parameter_values=None):
    connection = pymysql.connect(host=Config.MySql.DATABASE_SERVER, user=Config.MySql.DATABASE_USER,
                                 password=Config.MySql.DATABASE_PASS, db=Config.MySql.DATABASE_NAME,
                                 cursorclass=pymysql.cursors.DictCursor)
    try:
        cursor = connection.cursor()
        cursor.execute(query, parameter_values)
        result = []
        if cursor.rowcount == 1:
            result = cursor.fetchone()
        elif cursor.rowcount > 1:
            result = cursor.fetchall()
        return result
    except MySQLError as e:
        connection.rollback()
        # print("Error %d: %s" % (e.args[0], e.args[1]))
        raise e
    finally:
        connection.commit()
        connection.close()
