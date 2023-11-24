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
        target_lang=input("Enter the target language(e.g, es for spanish):")
        translation=self.translator.translate(text, src=source_lang, dest=target_lang)
