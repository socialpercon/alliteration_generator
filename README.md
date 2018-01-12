# alliteration_generator
A simple prototype for a program which finds alliterative phrases synonymous with a user’s input (for example, ‘large man’ returns ‘sizable sir’ and 'bulky beau').


HOW IT WORKS

- The user inputs a phrase of any length. (The program ignores stopwords like 'the', 'of', etc.)
- The program visits www.thesaurus.com and gathers data in the form of html.
- The program asks the user to disambiguate their input using disambiguations pulled from the html.
- The program offers the user a list of alliterative phrases synonymous with the input.


FUTURE FEATURES

- Currently the program can't handle inflections like tense and plurality.
- Currently the program doesn't have a GUI.
- Currently the program uses www.thesaurus.com for its data, but a better source would be something like WordNet.

I am working on a more robust version of this program with a tkinter GUI which uses WordNet and allows users to select whether or not they want to allow hyponyms in their results. 





