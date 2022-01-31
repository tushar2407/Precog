#!/usr/bin/env python
# coding: utf-8

# In[1]:


from google.colab import drive
drive.mount('/content/drive')


# In[2]:


get_ipython().run_line_magic('cd', '/content/drive/MyDrive/')


# In[3]:


filename = "Advocacy/train_ready/train_farmer.csv"


# In[4]:


get_ipython().system('pip install transformers')


# In[5]:


import os
import time
import datetime

import pandas as pd
import numpy as np
import random

import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

import torch
from torch.utils.data import Dataset, DataLoader, random_split, RandomSampler, SequentialSampler
torch.manual_seed(42)

from transformers import GPT2LMHeadModel,  GPT2Tokenizer, GPT2Config, GPT2LMHeadModel, BertTokenizerFast
from transformers import AdamW, get_linear_schedule_with_warmup

import nltk
nltk.download('punkt')

from tqdm import tqdm


# In[6]:


df = pd.read_csv(filename)
df = df.iloc[:5]
df.head()


# In[7]:


data = df.tweet_emoji_cleaned
data


# In[8]:


class GPT2Dataset(Dataset):  
    def __init__(self, control_code, truncate=False, gpt2_type="gpt2-large", max_length=2048):

        self.tokenizer = GPT2Tokenizer.from_pretrained(gpt2_type)
        self.data = []

        for row in df['tweet_emoji_cleaned']:
          self.data.append(torch.tensor(
                self.tokenizer.encode(f"<|{control_code}|>{row[:max_length]}<|endoftext|>")
            ))               
        if truncate:
            self.data = self.data[:20000]
        self.data_count = len(self.data)
        
    def __len__(self):
        return self.data_count

    def __getitem__(self, item):
        return self.data[item]
    
dataset = GPT2Dataset(data, truncate=True)      


# In[9]:


#Get the tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained('gpt2-large')
# configuration = GPT2Config.from_pretrained('gpt2-large', output_hidden_states=False)
model = GPT2LMHeadModel.from_pretrained('gpt2-large')

#Accumulated batch size (since GPT2 is so big)
def pack_tensor(new_tensor, packed_tensor, max_seq_len):
    if packed_tensor is None:
        return new_tensor, True, None
    if new_tensor.size()[1] + packed_tensor.size()[1] > max_seq_len:
        return packed_tensor, False, new_tensor
    else:
        packed_tensor = torch.cat([new_tensor, packed_tensor[:, 1:]], dim=1)
        return packed_tensor, True, None


# In[10]:


def train(
    dataset, model, tokenizer,
    batch_size=4, epochs=5, lr=2e-5,
    max_seq_len=400, warmup_steps=200,
    gpt2_type="gpt2-large", output_dir=".", output_prefix="wreckgar",
    test_mode=False,save_model_on_epoch=False,
):
    acc_steps = 100
    device=torch.device("cuda")
    model = model.cuda()
    model.train()

    optimizer = AdamW(model.parameters(), lr=lr)
    scheduler = get_linear_schedule_with_warmup(
        optimizer, num_warmup_steps=warmup_steps, num_training_steps=-1
    )

    train_dataloader = DataLoader(dataset, batch_size=1, shuffle=True)
    loss=0
    accumulating_batch_count = 0
    input_tensor = None

    for epoch in range(epochs):

        print(f"Training epoch {epoch}")
        print(loss)
        for idx, entry in tqdm(enumerate(train_dataloader)):
            (input_tensor, carry_on, remainder) = pack_tensor(entry, input_tensor, 1280)

            if carry_on and idx != len(train_dataloader) - 1:
                continue

            input_tensor = input_tensor.to(device)
            outputs = model(input_tensor, labels=input_tensor)
            loss = outputs[0]
            loss.backward()

            if (accumulating_batch_count % batch_size) == 0:
                optimizer.step()
                scheduler.step()
                optimizer.zero_grad()
                model.zero_grad()

            accumulating_batch_count += 1
            input_tensor = None
        if save_model_on_epoch:
            torch.save(
                model.state_dict(),
                os.path.join(output_dir, f"{output_prefix}-{epoch}.pt"),
            )
    return model


# In[11]:


model = train(dataset, model, tokenizer)


# In[12]:


get_ipython().system('nvidia-smi')


# In[ ]:




