translations = {
    'computer': 'komputer',
    'mouse': 'myszka',
    'keyboard': 'klawiatura',
    'printer': 'drukarka'
}

word = input('Enter an English word to translate to Polish: ').lower()

if word in translations:
    print(f'The Polish translation of "{word}" is: {translations[word]}')
else:
    print(f'Translation for "{word}" is unavailable.')