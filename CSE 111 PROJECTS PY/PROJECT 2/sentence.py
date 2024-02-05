''' CSE 111 - Prove Activity - Week 3-4
Juanita P. Aguilera '''

'''Exceeded Requirements
Included: 
1. Program includes a get_adjective or get_adverb function 
2. Program builds sentences that include two prepositional phrases 
3. Program includes some other additional functionality: 
I also included a boucle while for the user if he wants another 
series of sentences and I added conditionals to avoid errors'''

import random


def main():
    print()
    print('Generator of sentences'.center(100, '*'))
    # Call the function 
    make_sentence(1, 'past', 'positive')
    make_sentence(1, 'present', 'negative')
    make_sentence(1, 'future', 'place')
    make_sentence(2, 'past', 'positive')
    make_sentence(2, 'present', 'negative')
    make_sentence(2, 'future', 'place')
    print()
    a = 0
    while a == 0:
        option = input('Do you want generate another sentences?\nType YES or NO: ')
        if option.lower() == 'yes':
            a = 1
            main()
        elif option.lower() == 'no':
            print('Thanks for using the program.')
            print('')
            a = 1
        else:
            print('Please enter the correct option')
            a = 0


def make_sentence(quantity, tense, adverb_type):
    ''' Function to build the sentences 
    Return a sentences'''

    sentences = print(f'{get_determiner(quantity).capitalize()} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity).lower()} {get_adverbs(adverb_type)} {get_verb(quantity, tense)} {get_determiner(quantity)} {get_adjective()} {get_noun(quantity)} {get_prepositional_phrase(quantity)}.')
    return sentences


def get_determiner(quantity):
    '''Return a randomly chosen determiner. A determiner is
    a word like 'the', 'a', 'one', 'some', 'many'.
    If quantity == 1, this function will return either 'a',
    'one', or 'the'. Otherwise this function will return
    either 'some', 'many', or 'the'.
    Parameter
    quantity: an integer.
    If quantity == 1, this function will return a
    determiner for a single noun. Otherwise this
    function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.'''

    if quantity == 1:
        words = ['a', 'one', 'the']
    else:
        words = ['either', 'some', 'many']
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word


def get_noun(quantity):
    '''Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
    'bird', 'boy', 'car', 'cat', 'child',
    'dog', 'girl', 'man', 'rabbit', 'woman'
    Otherwise, this function will return one of
    these ten plural nouns:
    'birds', 'boys', 'cars', 'cats', 'children',
    'dogs', 'girls', 'men', 'rabbits', 'women'
    Parameter
    quantity: an integer that determines if
    the returned noun is single or plural.
    Return: a randomly chosen noun.
    '''
    if quantity == 1:
        words = ['bird', 'boy', 'car', 'cat', 'child',
                 'dog', 'girl', 'man', 'rabbit', 'woman']
    else:
        words = ['birds', 'boys', 'cars', 'cats', 'children',
                 'dogs', 'girls', 'men', 'rabbits', 'women']
    word = random.choice(words)
    return word


def get_verb(quantity, tense):
    '''Return a randomly chosen verb. If tense is 'past',
    this function will return one of these ten verbs:
    'drank', 'ate', 'grew', 'laughed', 'thought',
    'ran', 'slept', 'talked', 'walked', 'wrote'
    If tense is 'present' and quantity is 1, this
    function will return one of these ten verbs:
    'drinks', 'eats', 'grows', 'laughs', 'thinks',
    'runs', 'sleeps', 'talks', 'walks', 'writes'
    If tense is 'present' and quantity is NOT 1,
    this function will return one of these ten verbs:
    'drink', 'eat', 'grow', 'laugh', 'think',
    'run', 'sleep', 'talk', 'walk', 'write'
    If tense is 'future', this function will return one of
    these ten verbs:
    'will drink', 'will eat', 'will grow', 'will laugh',
    'will think', 'will run', 'will sleep', 'will talk',
    'will walk', 'will write'
    Parameters
    quantity: an integer that determines if the
    returned verb is single or plural.
    tense: a string that determines the verb conjugation,
    either 'past', 'present' or 'future'.
    Return: a randomly chosen verb.'''
    if tense == 'past':
        words = ['drank', 'ate', 'grew', 'laughed', 'thought',
                 'ran', 'slept', 'talked', 'walked', 'wrote']
    elif quantity == 1 and tense == 'present':
        words = ['drinks', 'eats', 'grows', 'laughs', 'thinks',
                 'runs', 'sleeps', 'talks', 'walks', 'writes']
    elif quantity != 1 and tense == 'present':
        words = ['drink', 'eat', 'grow', 'laugh', 'think',
                 'run', 'sleep', 'talk', 'walk', 'write']
    elif tense == 'future':
        words = ['will drink', 'will eat', 'will grow', 'will laugh',
                 'will think', 'will run', 'will sleep', 'will talk',
                 'will walk', 'will write']
    word = random.choice(words)
    return word


def get_preposition():
    '''Return a randomly chosen preposition
    from this list of prepositions:
    'about', 'above', 'across', 'after', 'along',
    'around', 'at', 'before', 'behind', 'below',
    'beyond', 'by', 'despite', 'except', 'for',
    'from', 'in', 'into', 'near', 'of',
    'off', 'on', 'onto', 'out', 'over',
    'past', 'to', 'under', 'with', 'without'
    Return: a randomly chosen preposition.'''
    word = ['about', 'above', 'across', 'after', 'along',
            'around', 'at', 'before', 'behind', 'below',
            'beyond', 'by', 'despite', 'except', 'for',
            'from', 'in', 'into', 'near', 'of',
            'off', 'on', 'onto', 'out', 'over',
            'past', 'to', 'under', 'with', 'without']
    word = random.choice(word)
    return word


def get_prepositional_phrase(quantity):
    '''Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.
    Parameter
    quantity: an integer that determines if the determiner
    and noun in the prepositional phrase returned from
    this function are single or pluaral.
    Return: a prepositional phrase.'''
    prep = get_preposition()
    determ = get_determiner(quantity)
    noun = get_noun(quantity)
    adjectiv = get_adjective()
    if quantity == 1:
        determ = get_determiner(1)
        noun = get_noun(1)
    else:
        determ = get_determiner(2)
        noun = get_noun(2)

    prepositional_phrases = (f'{prep} {determ} {adjectiv} {noun} ')
    return prepositional_phrases


def get_adjective():
    '''Return a randomly chosen adjective
    from this list of adjective:
    'anxious', 'naughty', 'stubborn',
    'sensitive','intelligent','nice','emotional','nervous','mean','distracted',
    'dishone','rude','discreet','crazy','energetic'
    Return: a randomly chosen adjective.'''
    word = ['anxious', 'naughty', 'stubborn',
            'sensitive', 'intelligent', 'nice', 'emotional', 'nervous', 'mean', 'distracted', 'dishone',
            'rude', 'discreet', 'crazy', 'energetic']
    word = random.choice(word)
    return word


def get_adverbs(adverb_type):
    '''Return a randomly chosen adverb. If type is 'positive',
    this function will return one of these six adverbs:
    'beautifully', 'boldly', 'calmly','justly','gently', 'kindly'
    If type is 'negative', this function will return one of
    these six adverbs:
    'angrily', 'madly','poorly','tensely','lazily','greedily'
    If type is 'place', this function will return one of
    these six adverbs:
    'nearby','far away','miles apart','close by', 'outside','downtown'
    Parameters
    adverb_type: a string that determines the adverb conjugation,
    either 'positive', 'negative' or 'place'.
    Return: a randomly chosen adverb.'''
    if adverb_type == 'positive':
        adverb = ['beautifully', 'boldly',
                  'calmly', 'justly', 'gently', 'kindly']
    elif adverb_type == 'negative':
        adverb = ['angrily', 'madly', 'poorly',
                  'tensely', 'lazily', 'greedily']
    elif adverb_type == 'place':
        adverb = ['nearby', 'far away', 'miles apart',
                  'close by', 'outside', 'downtown']
        word = random.choice(adverb)
        return word


if __name__ == '__main__':
    main()
