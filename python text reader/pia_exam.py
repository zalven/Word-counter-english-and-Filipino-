import sys

# For string counting
class countText:
    def __init__(self, value, compare, vowels, consonant):
        self.compare = compare.split("\n")
        self.vowels = vowels
        self.consonant = consonant
        self.value = value
        self.comparedValues = set()
        self.countComparedValues = 0
        self.getWordsOnly = 0
        self.vowelsOnly = 0
        self.consonantOnly = 0
        self._changeValues()

    def _changeValues(self):
        for i in self.value.replace("\n", " ").split(" "):
            if i != "":
                if i.lower() in self.compare:
                    self.comparedValues.add(i.lower())
                    self.countComparedValues += 1
                self.getWordsOnly += 1
                for j in i.lower():
                    if j in self.vowels:
                        self.vowelsOnly += 1
                    elif j in self.consonant:
                        self.consonantOnly += 1

    def numberOfLines(self):
        return len([1 for i in self.value.split("\n") if i.replace(" ", "") != ""])

    def numberOfWords(self):
        return self.getWordsOnly

    def numberOfVowels(self):
        return self.vowelsOnly

    def numberOfConstants(self):
        return self.consonantOnly

    def numberOfComparedValues(self):
        return self.countComparedValues

    def allComparedWords(self):
        return self.comparedValues


# For reading files and writing files
class readAndWriteFiles:
    def __init__(self, readFilePath, writeFilePath, searchedPath):
        self.readFilePath = readFilePath
        self.writeFilePath = writeFilePath
        self.searchedPath = searchedPath

    def read(self):
        file = open(self.readFilePath, "r", encoding="utf-8")
        return file.read()

    def readSearchedPath(self):
        file = open(self.searchedPath, "r", encoding="utf-8")
        return file.read()

    def write(self, value):
        file = open(self.writeFilePath, "w", encoding="utf-8")
        file.write(value)
        file.close()


class MainClass:
    def __init__(self, values):
        self.values = values

    def main(self):
        # Check the folder if filipino or not
        
        searched = {
            "-e": {
                "searchedPath": "languageAndWords/englishWords.txt",
                "searchedVowel": "a e i o u".split(" "),
                "searchedConsonants": "b c d f g h j k l m n p q r s t v w x y z".split(" ")
            },
            "-f": {
                "searchedPath": "languageAndWords/tagalogWords.txt",
                "searchedVowel": "a e i o u".split(" "),
                "searchedConsonants": "b c d f g h j k l m n ñ ng p q r s t v x y z".split(" "),
            },
        }

        # get the read files and overwrite the files
        files = readAndWriteFiles(
            self.values[1], self.values[3], searched[self.values[0]]["searchedPath"]
        )

        # Count the text on the txt file
        text = countText(
            files.read(),
            files.readSearchedPath(),
            searched[self.values[0]]["searchedVowel"],
            searched[self.values[0]]["searchedConsonants"],
        )

        result = ""
        allWords = "\n".join(text.allComparedWords())
        if self.values[0] in "-e":
            result = "\n".join(
                [
                    f"number of lines: {text.numberOfLines()}",
                    f"number of words: {text.numberOfWords()} ",
                    f"number of vowels: {text.numberOfVowels()}",
                    f"number of consonant: {text.numberOfConstants()} ",
                    f"number of English Words: {text.numberOfComparedValues()} ",
                    f"\nEnglish Words used:\n{  allWords }",
                ]
            )

        if self.values[0] in "-f":
            result = "\n".join(
                [
                    f"Blg. ng hanay: {text.numberOfLines()}",
                    f"Blg ng Salita: {text.numberOfWords()} ",
                    f"Blg ng Patinig: {text.numberOfVowels()}",
                    f"Blg ng Katinig: {text.numberOfConstants()} ",
                    f"Ginamit na Salitang Pilipino:{text.numberOfComparedValues()} ",
                    f"\nEnglish Words used:\n{  allWords }",
                ]
            )

        print(result)
        files.write(result)


MainClass(sys.argv[1:]).main()
