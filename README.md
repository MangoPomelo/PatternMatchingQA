# Pattern Matching QA

This project is a pattern matching question answering script demo, which is simple enough to consider as a baseline approach or a tutorial.

## How does it work

1. Take the sentence from command line
1. Every word in the sentence will be scanned by a list of _EntityKeywordDictionaries_ and _RelationshipKeywordDictionaries_, which then triggers the classification strategy to transform it into labels
    - For example, sentence like "What is Amantadine used to treat?" would trigger the _Cure_ keyword (as Relationship) and _Drug_ keyword (as Entity)
    - According to the classification strategy, this sentence will be transformed into a `drug_disease` relationship label and `Amantadine` entity label
1. Since the entity and relationship have been determined, the query will be constructed and send to a database or even a file to get the answer
1. Prompt the answer back to the command line

## How to run it

Run `python3 .\Chatbot.py` in command line only to start the integration test. To start a conversation, you have to add a while loop into the main function of `Chatbot.py`

## Configuration

### The way to adapt a specific database

There is no configuration file, any adaption must be done by modifying the `Parser.py`

### The way to add more classification strategy

Add keyword dictionaries manually, then change the process in `Classifier.py`
