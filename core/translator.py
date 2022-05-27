import goslate


def translate(text, lang):
    gs = goslate.Goslate()
    return gs.translate(text, lang)


res = translate("Selbstbindung der Bundesagentur für Arbeit", "en")

print(res)