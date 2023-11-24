#!/usr/bin/python3
from googletrans import Translator
class LanguageTranslatorAPP:
    def __init__(self):
        self.translator= Translator()
        self.user_progress={'translations_completed': '0'}
    #add def for display menu
    def translate_text(self):
        text= input("Enter the text you wish to translate:")
        source_lang=input("Enter the source language(e.g, en for English):")
