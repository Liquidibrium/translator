import goslate
from translate import Translator
from deep_translator import GoogleTranslator


def google_translate(text: str, lang: str = "de"):
    try:
        gs = goslate.Goslate()
        return gs.translate(text, target_language="en", source_language=lang)
    except Exception as e:
        print(e)
        return "Error"


def translator_translate(text: str, lang: str = "german"):
    try:
        translator = Translator(to_lang="en", from_lang=lang)
        return translator.translate(text)
    except Exception as e:
        print(e)
        return "Error"


def deep_translate(text: str, lang: str = "de"):
    try:
        translator = GoogleTranslator(source=lang, target='en')
        return translator.translate(text)
    except Exception as e:
        print(e)
        return "Error"
