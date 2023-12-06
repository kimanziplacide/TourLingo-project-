#!/usr/bin/python3
from googletrans import Translator
import mysql.connector

class LanguageTranslatorAPP:
    def __init__(self):
        self.translator= Translator()
        self.db_connection= self.initialize_database()
        self.user_progress={'translations_completed': '0'}

    def initialize_database(self):
        return mysql.connector.connect(
            host="localhost",
            user="kabisa",
            password="Argentina@10",
            database="tourlingodbs"
        )

    def create_user(self, username, password):
        cursor = self.db_connection.cursor()
        query = "INSERT INTO data (username, password, translations_completed) VALUES (%s, %s, 0)"
        values = (username, password)
        cursor.execute(query, values)
        self.db_connection.commit()
        cursor.close()
    def authenticate_user(self, username, password):
        cursor = self.db_connection.cursor()
        query = "SELECT * FROM data WHERE username=%s AND password=%s"
        values = (username, password)
        cursor.execute(query, values)
        user_data = cursor.fetchone()
        cursor.close()
        return user_data
    def update_translations_completed(self, username):
        cursor = self.db_connection.cursor()
        query_select = "SELECT translations_completed FROM data WHERE username = %s"
        values_select = (username,)
    def display_menu(self):
        print("Welcome to TOURLINGO here is the MENU")
        print("1. Translate Text")
        print("2. Language Quiz")
        print("3. User Progress")
        print("4. Exit")
    def translate_text(self):
        text = input("Enter the text you wish to translate: ")

        while True:
            try:
                source_lang = input("Enter the source language (e.g., en for English): ")
                target_lang = input("Enter the target language (e.g., es for Spanish): ")
                translation = self.translator.translate(text, src=source_lang, dest=target_lang)
                break  # Break out of the loop if translation is successful
            except ValueError:
                print("Please, these language abreviation are not valid. Try again.")

        print(f"\nOriginal Text ({source_lang}): {text}")
        print(f"Translation ({target_lang}): {translation.text}\n")
    def run(self):
        while True:
            self.display_menu()
            name= input("Welcome again on TourLingo!!! We are here for you. what is your name:")

            choice = input(f"{name}!!Enter your choice (1 to 4): ")

            if choice == "1":
                self.translate_text()
            elif choice== "4":
                print("Thank you for using TourLingo,any time we are here to assist")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 4.")
if __name__ == "__main__":
    app = LanguageTranslatorAPP()
    app.run()
