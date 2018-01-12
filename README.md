# alliteration_generator
A simple prototype for a program which finds alliterative phrases synonymous with a user’s input (for example, ‘large man’ returns ‘sizable sir’ and 'bulky beau').


**HOW IT WORKS**

- The user inputs a phrase of any length. (The program ignores stopwords like 'the', 'of', etc.)
- The program visits www.thesaurus.com and gathers data in the form of html.
- The program asks the user to disambiguate their input using synonyms pulled from the html.
- The program offers the user a list of alliterative phrases synonymous with the input.


**IN-PROGRESS FEATURES**

- GUI
- Handle inflections like tense and plurality
- Use WordNet as the source of synonyms rather than www.thesaurus.com
- Allow users to select whether they want to include hyponyms in their results (for example, 'tree' could output 'elm') 





