from googletrans import Translator
import mysql.connector
from mysql.connector import Error

class LanguageTranslatorAPP:
    def __init__(self):
        self.translator = Translator()
        self.db_connection = self.initialize_database()
        self.current_user = None  # Keep track of the current user
        self.current_user_id = None  # Keep track of the current user's ID

    # Initialization method to connect to the database
    def initialize_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="kabisa",
                password="Argentina@10",
                database="tourlingodbs"
            )
            return connection
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    # Function to print visual borders
    def print_visual_border(self):
        print("------------------------------")

    # Method to create a new user and insert into both tables
    def create_user(self, username, password):
        try:
            cursor = self.db_connection.cursor()

            # Insert into data table
            query_data = "INSERT INTO data (username, password) VALUES (%s, %s)"
            values_data = (username, password)
            cursor.execute(query_data, values_data)
            self.db_connection.commit()

            # Get the last inserted ID (auto-incremented primary key)
            user_id = cursor.lastrowid

            # Insert into user_progress table with the same ID
            query_progress = "INSERT INTO user_progress (id, translations_completed) VALUES (%s, 0)"
            values_progress = (user_id,)
            cursor.execute(query_progress, values_progress)
            self.db_connection.commit()

            # Consume any pending results
            cursor.fetchall()

            cursor.close()
            self.print_visual_border()
            print("User created successfully!")
            self.print_visual_border()
        except Error as e:
            print(f"Error creating user: {e}")

    # Method to authenticate a user
    def authenticate_user(self, username, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT id FROM data WHERE username=%s AND password=%s"
            values = (username, password)
            cursor.execute(query, values)
            user_data = cursor.fetchone()
            cursor.close()
            return user_data[0] if user_data else None
        except Error as e:
            print(f"Error authenticating user: {e}")
            return None

































































































    

           




 
























from googletrans import Translator
import mysql.connector
from mysql.connector import Error

class LanguageTranslatorAPP:
    def __init__(self):
        self.translator = Translator()
        self.db_connection = self.initialize_database()
        self.current_user = None  # Keep track of the current user
        self.current_user_id = None  # Keep track of the current user's ID

    # Initialization method to connect to the database
    def initialize_database(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="kabisa",
                password="Argentina@10",
                database="tourlingodbs"
            )
            return connection
        except Error as e:
            print(f"Error connecting to the database: {e}")
            raise

    # Function to print visual borders
    def print_visual_border(self):
        print("------------------------------")

    # Method to create a new user and insert into both tables
    def create_user(self, username, password):
        try:
            cursor = self.db_connection.cursor()

            # Insert into data table
            query_data = "INSERT INTO data (username, password) VALUES (%s, %s)"
            values_data = (username, password)
            cursor.execute(query_data, values_data)
            self.db_connection.commit()

            # Get the last inserted ID (auto-incremented primary key)
            user_id = cursor.lastrowid

            # Insert into user_progress table with the same ID
            query_progress = "INSERT INTO user_progress (id, translations_completed) VALUES (%s, 0)"
            values_progress = (user_id,)
            cursor.execute(query_progress, values_progress)
            self.db_connection.commit()

            # Consume any pending results
            cursor.fetchall()

            cursor.close()
            self.print_visual_border()
            print("User created successfully!")
            self.print_visual_border()
        except Error as e:
            print(f"Error creating user: {e}")

    # Method to authenticate a user
    def authenticate_user(self, username, password):
        try:
            cursor = self.db_connection.cursor()
            query = "SELECT id FROM data WHERE username=%s AND password=%s"
            values = (username, password)
            cursor.execute(query, values)
            user_data = cursor.fetchone()
            cursor.close()
            return user_data[0] if user_data else None
        except Error as e:
            print(f"Error authenticating user: {e}")
            return None

































































































    

           




 
























