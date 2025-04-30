menu = {
   'soup': 'lentil',
   'oyster': 'kumamoto',
   'special': 'schitzel',
}
template = ('Today\'s soup is %(soup)s, '
            'buy one get two %(oyster)s oysters, '
            'and our special entrée is %(special)s.')
formatted = template % menu
print(formatted)
