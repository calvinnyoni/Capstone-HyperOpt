import mysql.connector
from mysql.connector.errors import OperationalError, Error

from helper import inform, warn, raise_exception


class CarlSATDB(object):
    def __init__(self):
        self.connection = mysql.connector.connect(user='carlsat', password='12345678', host='localhost', database='CarlSAT_DB')
        self.config = {'user': 'carlsat', 'password': '12345678', 'host':'localhost', 'database': 'CarlSAT_DB'}

    def connect(self):
        self.connection = mysql.connector.connect(**self.config)

    def send_query(self, query, *args):
        """
        send query to be executed and deal with attribute and database errors from connection not
        being open. Reopen connection on exception and retry command
        :param query: query/transaction to be executed in our DB
        :param args: additional arguments passed to us
        :return: status of query (SUCCESS or FAIL)
        """
        try:
            inform('Attempting execution of query: `%s`' % query)
            self.execute_query(query, *args)
        except (AttributeError, OperationalError):
            warn('Connection to database lost. Reestablishing connection')
            self.connect()
            inform('Reconnected to database')
            self.execute_query(query, *args)
            inform('Retrying execution of query: `%s`' % query)

    def execute_query(self, query, *args):
        try:
            db_cursor = self.connection.cursor()
            db_cursor.execute(query, *args)
            self.connection.commit()
        except Error as err:
            err_msg = "Error code: %s\nSQLSTATE value: %s\nError message: %s\nError: %s\nError: %s\n" \
                      % (err.errno, err.sqlstate, err.msg, err, str(err))
            raise_exception(err_msg)
            inform('Rolling back transaction')
            self.connection.rollback()

    def disconnect(self):
        self.connection.close()


def create_database():
    # set up connection to MySQL service
    inform('Connecting to CarlSAT_DB')
    carlsat_db = CarlSATDB()
    carlsat_db.send_query('CREATE DATABASE IF NOT EXISTS CarlSAT_DB')
    carlsat_db.send_query('USE CarlSAT_DB')
    inform('Database connection established')

    # create table
    table = """
            CREATE TABLE IF NOT EXISTS Ancestry (
                RunID INT NOT NULL,
                Random NVARCHAR(15),
                CONSTRAINT PK_Ancestry PRIMARY_KEY (RunID) ORDER BY RunID,
            );
            """
    carlsat_db.send_query(table)


def read_database():
    pass


def write_to_database():
    pass


if '__name__' != '__main__':
    pass
#create_database()