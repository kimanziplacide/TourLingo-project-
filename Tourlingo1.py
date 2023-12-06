#!/usr/bin/python3
from googletrans import Translator
import mysql.connector

class LanguageTranslatorAPP:
    def __init__(self):
        self.translator= Translator()
        self.db_connection= self.initialize_database()
        self.user_progress={'translations_completed': '0'}

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
