from typing import TextIO, Any
import json

# TODO: config system
DATA_FILENAME = "lang.json"

def decodeLanguageFile(file: TextIO):
    try:
        data = json.load(file)
        return data

    except json.decoder.JSONDecodeError as err:
        print(f"Error loading language file: {err}")

def encodeLanguageFile(data: Any, file: TextIO):
    data = json.dump(data, file)
    return

from enum import Enum
class SyntaxCategory(Enum):
    ADJECTIVE = "ADJECTIVE"
    ADPOSITION = "ADPOSITION"
    ADVERB = "ABVERB"
    CONJUNCTION = "CONJUNCTION"
    DETERMINER = "DETERMINER"
    INTERJECTION = "INTERJECTION"
    NOUN = "NOUN"
    PARTICLE = "PARTICLE"
    PRONOUN = "PRONOUN"
    VERB = "VERB"

class Entry:
    def __init__( self, word: str, category: SyntaxCategory, meaning: str = "", translation: str = ""):
        self.word = word
        self.category = category
        self.meaning = meaning
        self.translation = translation

    def data(self) -> Any:
        return {
            'word': self.word,
            'category': self.category,
            'meaning': self.meaning,
            'translation': self.translation
        }

class Language:
    def __init__(self, name: str):
        self.name = name
        self.entries: dict[str, list[Entry]] = {}

    def data(self) -> Any:
        return {
            'name': self.name,
            'entries': [e.data() for e in self.entries]
        }

class LanguageSystem:
    def __init__(self):
        self.languages: list[Language] = []
        self.filename: str = DATA_FILENAME # TODO: config system
        self.activeLanguageIndex: int | None = None
        self.activeLanguage: Language | None = None

    def newLanguage(self, name):
        self.languages.append(Language(name))
        self.activeLanguageIndex = len(self.languages) - 1
        self.activeLanguage = self.languages[self.activeLanguageIndex]

    def data(self) -> Any:
        return { 'langs': [l.data() for l in self.languages] }

    def save(self):
        with open(self.filename, 'w') as file:
            encodeLanguageFile(self.data(), file)

def displayLanguages(system, *args):
    if len(system.languages) < 1:
        print("There are no loaded languages")
        return

    _langs = ' '.join((l.name for l in system.languages))
    if system.activeLanguage is None:
        _active = "None"
    else:
        _active = f"{system.activeLanguage.name} ({system.activeLanguageIndex})"

    print("Loaded languages:")
    print(_langs)
    print(f"Active language: {_active}")
    return

def newLanguage(system, *args):
    if len(args) < 2:
        print("No language name specified")
        return

    system.newLanguage(args[1])
    print(f"Language created: {args[1]}")
    return

def clearActiveLanguage(system, *args):
    system.activeLanguage = None
    system.activeLanguageIndex = None
    return

def debugPrintData(system, *args):
    print(self.data())
    return

# mapping for interface commands specific to language system
languageSystemCommands =  {
    'clear' : clearActiveLanguage,
    'list'  : displayLanguages,
    'new'   : newLanguage,

    'debug' : debugPrintData
}

def runLanguageSystem():
    global languageSystemCommands

    print("Language System")
    print("===============")

    system = LanguageSystem()

    isRunning = True
    while isRunning:
        cmdArgs = input("> ").split(' ')
        if len(cmdArgs) < 1:
            continue

        if cmdArgs[0] == "exit":
            isRunning = False
            continue

        cmd = languageSystemCommands.get(cmdArgs[0])
        if cmd is None:
            print("Invalid command", end = "\n\n")
            continue

        cmd(system, *cmdArgs)
        print("")

def test_program():
    import ui
    ui.runGUI()

def main():
    # TODO: config system
    # TODO: parse command line args
    #runLanguageSystem()
    test_program()
    print("Program terminated")

if __name__ == "__main__":
    main()
