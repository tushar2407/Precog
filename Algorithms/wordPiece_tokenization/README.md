# Word Piece tokenization (BERT)

## Algo
Some tokenisation techniques are based on the characters instead of focusing on the words. Wordpiece tokenisation is such a method, instead of using the word units, it uses subword (wordpiece) units.

It is an iterative algorithm. First, we choose a large enough training corpus and we define either the maximum vocabulary size or the minimum change in the likelihood of the language model fitted on the data. Then the iterative algorithm is constructed in the following manner:

    1 - Initialise a vocabulary with the individual characters found in the corpus
    
    2 - Build a language model on the corpus by using the vocabulary from step 1.
    
    3- Generate one new word unit by combining two elements of the vocabulary. Choose the combined, new subword that increases the likelihood of the language model by the most when added to the model.
    
    4- Repeat step 2) and 3) until the maximum vocabulary size is achieved or when the increase in the likelihood falls below he predefined threshold.

If implemented in a naive fashion, finding the new token that increases the likelihood by the most can be computationally quite expensive **(O(|V|^2)** where |V| is the vocabulary size). Therefore, training can be speed up by only testing new subwords that actually exist in the corpus, or by choosing those that are likely in the corpus (have a high frequency).

## References:
    https://machinelearnit.com/2018/08/19/wordpiece-tokenisation/