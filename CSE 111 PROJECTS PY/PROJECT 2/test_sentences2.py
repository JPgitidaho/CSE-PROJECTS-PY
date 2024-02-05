import random
import itertools
def main():
    # Generate and print six sentences with different characteristics
    quantity = [1, 1, 1, 2, 2, 2]
    tense = ["past", "present", "future", "past", "present", "future"]

    for (i, j) in itertools.zip_longest(quantity, tense):
        determiner = get_determiner(i)
        noun = get_noun(i)
        verb = get_verb(i, j)
        phrase = get_prepositional_phrase(i)
        print(f'{determiner.capitalize()} {noun} {verb} {phrase}.')
        
def get_determiner(quantity):
    """Return a randomly chosen determiner. A determiner is
    a word like "the", "a", "one", "two", "some", "many".
    If quantity == 1, this function will return
    either "the" or "one". Otherwise this function will
    return either "some" or "many".
    Parameter
    quantity: an integer.
    If quantity == 1, this function will return
    a determiner for a single noun. Otherwise this
    function will return a determiner for a plural noun.
    Return: a randomly chosen determiner.
    """
    if quantity == 1:
        words = ["a", "one", "the"]
    else:
        words = ["two", "some", "many", "the"]
    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word
def get_noun(quantity):
    """Return a randomly chosen noun.
    If quantity == 1, this function will
    return one of these ten single nouns:
    "bird", "boy", "car", "cat", "child",
    "dog", "girl", "man", "rabbit", "woman"
    Otherwise, this function will return one of these
    ten plural nouns:
    "birds", "boys", "cars", "cats", "children",
    "dogs", "girls", "men", "rabbits", "women"
    Parameter
    quantity: an integer that determines
    if the returned noun is single or plural.
    Return: a randomly chosen noun.
    """
    if quantity == 1:
        noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]
    else:

        noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]

 # Randomly choose and return a noun.
    noun = random.choice(noun)
    return noun

def get_verb(quantity, tense):
    """Return a randomly chosen verb. If tense is "past", this
    function will return one of these ten verbs:
    "drank", "ate", "grew", "laughed", "thought",
    "ran", "slept", "talked", "walked", "wrote"
    If tense is "present" and quantity is 1, this
    function will return one of these ten verbs:
    "drinks", "eats", "grows", "laughs", "thinks",
    "runs", "sleeps", "talks", "walks", "writes"
    If tense is "present" and quantity is NOT 1,
    this function will return one of these ten verbs:
    "drink", "eat", "grow", "laugh", "think",
    "run", "sleep", "talk", "walk", "write"
    If tense is "future", this function will return one of
    these ten verbs:
    "will drink", "will eat", "will grow", "will laugh",
    "will think", "will run", "will sleep", "will talk",
    "will walk", "will write"
    Parameters
    quantity: an integer that determines if the
    returned verb is single or plural.
    tense: a string that determines the verb conjugation,
    either "past", "present" or "future".
    Return: a randomly chosen verb.
    """
    if tense == "past":
        verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    elif tense == "present":
        if quantity == 1:
            verb = ["drinks", "eats", "grows", "laughs", "thinks",
            "runs", "sleeps", "talks", "walks", "writes"]
        else:
            verb = ["drink", "eat", "grow", "laugh", "think",
            "run", "sleep", "talk", "walk", "write"]
    elif tense == "future":
        verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
        
    # Randomly choose and return a determiner.
    verb = random.choice(verb)
    return verb
def get_preposition():
    """Return a randomly chosen preposition
    from this list of prepositions:
    "about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"
    Return: a randomly chosen preposition.
    """
    prepositions = ["about", "above", "across", "after", "along",
    "around", "at", "before", "behind", "below",
    "beyond", "by", "despite", "except", "for",
    "from", "in", "into", "near", "of",
    "off", "on", "onto", "out", "over",
    "past", "to", "under", "with", "without"]
    # Randomly choose and return a preposition.
    preposition = random.choice(prepositions)
    return preposition

def get_prepositional_phrase(quantity):
    """Build and return a prepositional phrase composed of three
    words: a preposition, a determiner, and a noun by calling the
    get_preposition, get_determiner, and get_noun functions.
    Parameter
    quantity: an integer that determines if the determiner
    and noun in the prepositional phrase returned from
    this function are singular or pluaral.
    Return: a prepositional phrase.
    """
    prep = get_preposition()
    determ = get_determiner(quantity)
    noun = get_noun(quantity)
    if quantity == 1:
        determ = get_determiner(1)
        noun = get_noun(1)
    else:
        determ = get_determiner(2)
        noun = get_noun(2)

    prepositional_phrases = (f'{prep} {determ} {noun}')
    return prepositional_phrases

if __name__ == "__main__":
 main()
