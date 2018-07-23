from pprint import pprint

class Contact(object):
    def __init__(self, end='`'):
        self._end = end
        self.tries = {'count': 0}

    def make_trie(self, word):
        trie = self.tries

        for letter in word:
            next_trie = trie.setdefault(letter, {'count': 0})
            trie['count'] += 1
            trie = next_trie
        trie[self._end] = self._end
        return self.tries

    def count_word(self, word):
        trie = prev_trie = self.tries
        if word[0] not in trie:
            return 0

        for letter in word:
            if letter in trie:
                prev_trie = trie
                trie = trie[letter]
            else:
                return 0

        if self._end in trie:
            return trie['count'] + 1

        return trie['count']

contact = Contact()
# contact.make_trie('hack')
# contact.make_trie('hackerrank')


contact = Contact()
contact.make_trie('s')
contact.make_trie('ss')
contact.make_trie('sss')
contact.make_trie('ssss')
contact.make_trie('sssss')
contact.count_word('s')

# contact = Contact()
# contact.make_trie('eouecvksgllpvfxfvndu')
# contact.count_word('zivh')


print(contact.count_word('s'))