import mysql.connector
import sys

def Connect():
    conn=None
    try:
        conn=mysql.connector.connect(
            host='localhost',
            username='root',
            password='@sql',
            database='taxi_booking_system'
        )


    except:
        print("Error", sys.exc_info())

    finally:

        return conn



