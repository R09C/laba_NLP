import nltk
from nltk.tokenize import word_tokenize
import pymorphy3

text = """— Ну что, князь, Генуя и Лукка стали теперь поместьями фамилии Буонапарте. Нет, я вас предупреждаю, если вы мне не скажете, что у нас война, если вы еще позволите себе защищать все гадости этого Антихриста (я убеждена, что он Антихрист) — я вас больше не знаю, вы уж не мой верный раб, как вы говорите. Ну, здравствуйте, здравствуйте, моя дорогая, mon bon. Je vois que je vous fais peur, [Вижу, что я вас пугаю,] садитесь и рассказывайте.
Так говорила в июле 1805 года известная Анна Павловна Шерер, фрейлина и приближенная императрицы Марии Феодоровны, встречая важного и чиновного князя Василия, первого приехавшего на ее вечер. Анна Павловна кашляла, страдая mode de la grippe, [род гриппа] как она говорила, грипп был тогда новое слово, которого почти никто еще не употреблял. В числе бесчисленных лиц в золе Анны Павловны была principesse Hélène Kourakine, [княгиня Элен Куракина] красавица, которую привел с собою князь Василий, известная своим обществом, и молодая, маленькая княгиня Болконская, беременная, жена уже нашумевшего в то время князя Андрея Болконского, сына известного князя Николая Андреевича Болконского, прозванного King of Prussia, [Прусский король] и единственный сын богатого Николая Петровича Болконского, у которого была дочь, княжна Марья, и которая вследствие расстроенного здоровья мужа, не выезжала в свет и теперь приехала с своей m-lle Bourienne, [мадемуазель Бурьенн] компаньонкой.
— С вами теперь остается моя дочь, — сказал князь Василий тихонько входящей княгине, гладя ее по голове. — Пожалуйста, Анна Павловна, будьте снисходительны к ней, она очень молода, и я очень на нее надеюсь.
"""
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