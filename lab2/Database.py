import mysql.connector

class Database:
    def __init__(self, config):
        self.host = config['host'] 
        self.user = config['user']
        self.password = config['password']
        self.database = config['database']
        self.conn = None
        self.cursor = None


    def connect(self):
        self.conn = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.conn.cursor()

    def create_employee_table(self):
        if self.conn is not None:
            self.cursor = self.conn.cursor()  # Initialize the cursor object
            self.cursor.execute('''CREATE TABLE IF NOT EXISTS employee (
                first_name VARCHAR(255),
                last_name VARCHAR(255),
                age INT,
                department VARCHAR(255),
                salary DECIMAL(10, 2)
            )''')
            self.conn.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()