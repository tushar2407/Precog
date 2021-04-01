from pytorch_transformers import BertTokenizer 

tokenizer = BertTokenizer.from_pretrained('bert-base-multilingual-uncased')
print(tokenizer.tokenize('Can we see each other tomorrow for a drink?  '))