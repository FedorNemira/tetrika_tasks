import re
import wikipediaapi 


wiki_wiki = wikipediaapi.Wikipedia('en')

wiki_wiki = wikipediaapi.Wikipedia(
        language='ru',
        extract_format=wikipediaapi.ExtractFormat.WIKI
)

def count_animals(categorymembers, level=0, max_level=0):
        animals_list = []
        for c in categorymembers.values():    
            animals_list.append(c.title)

        letters_list = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯABCDEFGHIJKLMNOPQRSTUVWXYZ'
        
        for letter in letters_list:
                result = [animal for animal in animals_list if animal.startswith(letter)]
                print(f'{letter}: {len(result)}')
        

cat = wiki_wiki.page("Категория:Животные по алфавиту")

count_animals(cat.categorymembers)


