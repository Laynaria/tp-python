from quote import quote
from pprint import pprint

# 1. Concevoir un inventaire des titres de livres classés par fréquence d'apparition dans le résultat en ordre
# décroissant de Edgar Allan Poe.
search1 = "Edgar Allan Poe"
result1 = quote(search1)

def sortFunc(e):
    return e.get("book")

result1.sort(key=sortFunc, reverse=True)

pprint(result1)

# 2. Dresser un inventaire des mots classés par ordre décroissant de présence dans les citations de Edgar
# Allan Poe. Ne pas afficher les mots présents moins de 5 fois.
inventory = []
valueArray = []

for citation in result1:
    citation_split = citation["quote"].replace("?", " ").replace("—", " ").replace("'", " ").replace('"', " ").replace("\\", " ").replace(".", " ").replace(",", " ").lower().split(" ")
    for word in citation_split:
            if word != "":
                inventory.append(word)

uniqueWord = list(set(inventory))

for word in uniqueWord:
     valueArray.append(0)

inventoryDictionnary = dict(zip(uniqueWord, valueArray))

for word in inventory:
     inventoryDictionnary[word] +=1

inventoryDictionnary = {k:v for k,v in inventoryDictionnary.items() if v > 5}

sorted_items = sorted(inventoryDictionnary.items(), key=lambda kv: (kv[1], kv[0]))

print("\n")
print("Inventory question 2:")
pprint(sorted_items)

# 3. À partir de la liste des auteurs, générer 30 citations pour chacun de ces auteurs et générer un set des
# mots en commun à tous ces auteurs. (10 citations si le pc est lent)

author_list = ["Edgar Allan Poe", "Arthur Schopenhauer", "Georges Orwell", "Victor Hugo", "Simone De Beauvoir", "Frank Herbert", "Gustave Flaubert", 
               "Guy De Maupassant", "Isaac Asimov", "Ernest Hemingway", "Voltaire", "Tolkien", "Agatha Christie", "Emile Zola", "William Shakespear", "William Shakespear"]

all_author_words = []

for author in author_list:
     search_result = quote(author, limit=10)

     this_author_words = []
     for citation in search_result:
        citation_split = citation["quote"].replace("?", " ").replace("—", " ").replace("'", " ").replace('"', " ").replace("\\", " ").replace(".", " ").replace(",", " ").lower().split(" ")
        for word in citation_split:
            if word != "":
                this_author_words.append(word)

     all_author_words.append(set(this_author_words))

common_words = set

for word_set in all_author_words:
     common_words = common_words.intersection(word_set)


print(common_words) # result : {'that', 'a', 'the', 'of', 'to', 'is', 'and'}


# Exemple : si le mot "concombre" est utilisé dans une des citations de Victor Hugo, alors si "concombre"
# est présent dans une des citations de TOUS les auteurs, il doit être présent dans ce set.

# Optionnal
# 4. Faire un classement décroissant des auteurs par le nombre de fois qu'ils utilisent le mot "the" en
# affichant l'auteur et le nombre de fois que "the" est présent dans ses 30 citations.

# Optionnal
# 5. Écrire ce classement dans un fichier csv avec pour noms de colonne "auteur" et "nombre d'occurrences
# du mot 'the'".