# missingWordsFinder.py
# This program checks train.txt entries for membership in CMUdict.
import sys
from string import punctuation
import pprint
import json
from nltk.corpus import cmudict

cmudict = cmudict.dict() # Carnegie Mellon University Pronouncing Dictionary

# C-style code in Python... :\

def main():
    haiku = load_haiku('train.txt')
    exceptions = cmudict_missing(haiku)
    build_dict = input("\nManually build an exceptions dictionary (y/n)? \n")
    if build_dict.lower() == 'n':
        sys.exit()
    else:
        missing_words_dict = make_exceptions_dict(exceptions)
        save_exceptions(missing_words_dict) # I originally forgot this line and had to diff with the source code from Github. :/

def load_haiku(filename):
    """Open and return training corpus of haiku as a set."""
    with open(filename) as in_file:
        haiku = set(in_file.read().replace('-', ' ').split()) # Load as a set to avoid repeats. Replace hyphens with spaces.
        return haiku

def cmudict_missing(word_set):
    """Find and return words in word set missing from cmudict."""
    exceptions = set() # Start an empty set to hold missing words.
    for word in word_set:
        word = word.lower().strip(punctuation)
        if word.endswith("'s") or word.endswith("’s"):
            word = word[:-2]
        if word not in cmudict:
            exceptions.add(word)
    print("\nexceptions:")
    print(*exceptions, sep='\n')
    print("\nNumber of unique words in haiku corpus = {}".format(len(word_set)))
    print("Number of words in corpus not in cmudict = {}".format(len(exceptions)))
    membership = (1 - (len(exceptions) / len(word_set))) * 100
    print("cmudict membership = {:.1f}{}".format(membership, '%'))
    return exceptions

def make_exceptions_dict(exceptions_set):
    """Return dictionary of words and syllable counts from a set of words."""
    missing_words = {} # Assign an empty dictionary to missing_words
    print("Input # syllables in word. Mistakes can be corrected at end. \n")
    for word in exceptions_set:
        while True:
            num_sylls = input("Enter number of syllables in {}: ".format(word))
            if num_sylls.isdigit():
                break
            else:
                print("                   Not a valid answer!", file=sys.stderr)
            missing_words[word] = int(num_sylls)
        print()
        pprint.pprint(missing_words, width=1)

        print("\nMake Changes to Dictionary Before Saving?")
        print("""
        0 - Exit & Save
        1 - Add a Word or Change a Syllable Count
        2 - Remove a Word
        """)

        while True:
            choice = input("\nEnter choice: ")
            if choice == '0':
                break
            elif choice == '1':
                word = input("\nWord to add or change: ")
                missing_words[word] = int(input("Enter number of syllables in {}: ".format(word)))
            elif choice == '2':
                word = input("\nEnter word to delete: ")
                missing_words.pop(word, None)
            
        print("\nNew words or syllable changes:")
        pprint.pprint(missing_words, width=1)

        return missing_words

def save_exceptions(missing_words):
    """Save exceptions dictionary as json file."""
    json_string = json.dumps(missing_words) # Serializes the missing_words dictionary into a string). Serializing is the process of converting data into a more transmittable string or storable format.
    f = open('missing_words.json', 'w')
    f.write(json_string)
    f.close()
    print("\nFile saved as missing_words.json")

if __name__ == '__main__':
    main()