from googletrans import Translator
import mysql.connector
from mysql.connector import Error

class LanguageTranslatorAPP:
    def _init_(self):
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

            cursor.close()
            print("User created successfully!")
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
        # Method to update translations completed for a user
    def update_translations_completed(self, user_id):
        try:
            cursor = self.db_connection.cursor()
            query_update = "UPDATE user_progress SET translations_completed = translations_completed + 1 WHERE id = %s"
            values_update = (user_id,)
            cursor.execute(query_update, values_update)
            self.db_connection.commit()
            cursor.close()
            print("Translations completed!")
        except Error as e:
            print(f"Error updating translations completed: {e}")

            # Method to get user's progress
    def get_user_progress(self, user_id):
        try:
            cursor = self.db_connection.cursor()
            query_select = "SELECT translations_completed FROM user_progress WHERE id = %s"
            values_select = (user_id,)
            cursor.execute(query_select, values_select)
            progress_row = cursor.fetchone()
        if progress_row is not None:
                current_translations_completed = progress_row[0]
                cursor.close()
                return current_translations_completed
            else:
                print("No progress found.")
                cursor.close()
                return 0  # Default progress assumed to be 0 if no data found
        except Error as e:
            print(f"Error getting user progress: {e}")
            return None
    # Method to log in a user
    def login(self):
        username_to_authenticate = input("Enter your username for authentication: ")
        password_to_authenticate = input("Enter your password for authentication: ")
        authenticated_user_id = self.authenticate_user(username_to_authenticate, password_to_authenticate)    