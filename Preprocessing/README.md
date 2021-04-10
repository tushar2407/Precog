# NLPretext
## Installation
    - python -m spacy download en_core_web_sm
    - pip install nlpretext

## Documentation
    - Replacing EMAIL
        from nlpretext.basic.preprocess import replace_emails
        example = "I have forwarded this email to obama@whitehouse.gov"
        example = replace_emails(example, replace_with="*EMAIL*")
        # "I have forwarded this email to *EMAIL*"
    - Replacing Emoji
        from nlpretext.social.preprocess import extract_emojis
        example = "I take care of my skin 😀"
        example = extract_emojis(example)
        print(example)
        # [':grinning_face:']
    - Text Augmentation
        from nlpretext.augmentation.text_augmentation import augment_text
        example = "I want to buy a small black handbag please."
        entities = [{'entity': 'Color', 'word': 'black', 'startCharIndex': 22, 'endCharIndex': 27}]
        example = augment_text(example, method=”wordnet_synonym”, entities=entities)
        print(example)
        # "I need to buy a small black pocketbook please."
    
## Text Augmentation
    The augmentation module helps you to generate new texts based on your given examples by modifying some words in the initial ones and to keep associated entities unchanged, if any, in the case of NER tasks. If you want words other than entities to remain unchanged, you can specify it within the stopwords argument. Modifications depend on the chosen method, the ones currently supported by the module are substitutions with synonyms using Wordnet or BERT from the nlpaug library.
## Usage
    - python preprocess.py
## Referenecs
    https://nlpretext.readthedocs.io/en/latest/