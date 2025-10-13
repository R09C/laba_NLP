import nltk
from nltk.tokenize import word_tokenize
import pymorphy3


with open("text.txt", "r", encoding="utf-8") as file:
    text = file.read()


nltk.download("punkt_tab")
m_analyzer = pymorphy3.MorphAnalyzer()

word_mass_with_punctuation = word_tokenize(text)
word_mass = []
punctuation = {
    ".",
    ",",
    "!",
    "?",
    ";",
    ":",
    "-",
    "(",
    ")",
    "[",
    "]",
    "{",
    "}",
    "'",
    '"',
    "...",
    "—",
}
for word in word_mass_with_punctuation:
    if word not in punctuation:
        word_mass.append(word.lower())


# print(word_mass_with_punctuation,"\n", word_mass)

return_pairs = []

for i in range(len(word_mass) - 1):
    word_1 = m_analyzer.parse(word_mass[i])[0]
    word_1_tag = word_1.tag
    word_2 = m_analyzer.parse(word_mass[i + 1])[0]
    word_2_tag = word_2.tag

    if (
        (word_1_tag.POS in ["ADJF", "NOUN"])
        and (word_2_tag.POS in ["ADJF", "NOUN"])
        and (word_1_tag.case == word_2_tag.case)
        and (word_1_tag.gender == word_2_tag.gender)
        and (word_1_tag.number == word_2_tag.number)
    ):
        return_pairs.append((word_1.normal_form, word_2.normal_form))

print(return_pairs)
