#!/usr/bin/python3
from googletrans import Translator
class LanguageTranslatorAPP:
    def __init__(self):
        self.translator= Translator()
        self.user_progress={'translations_completed': '0'}
