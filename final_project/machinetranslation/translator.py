from deep_translator import MyMemoryTranslator


def englishToFrench(englishText):
    dict = {
        'Hello': 'Bonjour',
        'Let\'s go': 'Allons-y'
    }
    frenchText = dict[englishText]
    return frenchText


def frenchToEnglish(frenchText):
    dict = {
        'Bonjour': 'Hello',
        'Allons-y': 'Let\'s go'
    }
    englishText = dict[frenchText]
    return englishText
