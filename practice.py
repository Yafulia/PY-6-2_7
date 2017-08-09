import os
import requests

def translate_it(fromlang, tolang, current_dir, target_dir, f_name):
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
    key = 'trnsl.1.1.20161025T233221Z.47834a66fd7895d0.a95fd4bfde5c1794fa433453956bd261eae80152'
    
    defis = '-'
    
    if fromlang not in {'ru', 'en', 'fr', 'de', 'es'}:
        fromlang = ''
        defis = ''
    
    if tolang not in {'ru', 'en', 'fr', 'de', 'es'}:
        tolang = 'ru'
    
    with open(os.path.join(current_dir, f_name)) as f:
        text = f.read()

    params = {
        'key': key,
        'lang': fromlang + defis + tolang,
        'text': text
    }
    response = requests.get(url, params=params).json()
    content = ' '.join(response.get('text', []))

    with open(os.path.join(target_dir, f_name), 'w') as f:
        f.write(content)

def main():
    files = ['DE.txt', 'FR.txt', 'ES.txt']
    for file in files:
        print(file)
        fromlang = input('Введите язык с которого переводить (ru, en, fr, de, es): ')
        tolang = input('Введите язык на который переводить (ru, en, fr, de, es): ')
        current_dir = input('Введите путь к файлу с текстом: ')
        target_dir = input('Введите путь к файлу с результатом: ')

        translate_it(fromlang, tolang, current_dir, target_dir, file)

main()