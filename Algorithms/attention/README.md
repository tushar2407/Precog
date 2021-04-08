# Attention model
> Here are the best references to understand the working behind attention models right from RNN to LSTM to GRU to Seq2Seq to Attention and finally self-attention.
---
## Disadvantages of Attention:
>  One disadvantage is that the context vector is calucated through hidden state between source and target sentence, leaving the attention inside source sentence and target sentence itself ignored 
>
> Another is that RNN is hard to parallelize, leading the calculation time-consuming 
---
> ## Key, Query, Value

--> Through the calculation of similarity between **Query** and each **Key**, we can get the attention score of the **Value**, corresponding to the **Key**. 
>
--> **Attention score** is the **importance** of a **input word**.
>
--> We then multiply each value vector by the attention score and sum up the weighted value vector, which is Attention/context vector.
>
--> the key and value are usually came to the same thing, therefore **key=value**.

---
> ## Three kinds of attention
    Transformer consists of 3 kinds of attention:
    - Self Attention in encoder
    - Self Attention in decoder
    - Encoder-Decoder Attention, which is similar to the concept of attention model

![Fig 1](https://miro.medium.com/max/3000/1*6gWbzqnAQjpg1n35rrExZQ.png)

# Self-Attention formal algorithm
## How to calculate attention
    We will take a look from the microcosmic perspective by vectors Attention(q_{t}, K, V), then proceed to look at how it’s actually implemented with matrices.

    The "first" step in calculating self-attention is to create three vectors from each of the encoder’s input vectors (in this case, the embedding of each word in “Are you very big?”). Then we multiply the embeddings by three different matrices to create a Query vector, a Key vector, and a Value vector for each word. In this paper, outputs of dimension d_{model}=512.

    The "second" step in calculating self-attention is to calculate a score <q_{t}, k_{s}> by taking the dot product of the query vector with the key vector of the respective word we’re scoring, which is similar to e_{ij} in attention model. Say we’re calculating the self-attention for the first word in this example, “Are”. We need to score each word of the input sentence such as “you”, ‘very’, ‘big?’ against this word. The score determines how much focus to place on other parts of the input sentence as we encode a word at a certain position. So if we’re processing the self-attention for the word in position #1, the first score would be the dot product of q1 and k1 (“Are vs Are”). The second score would be the dot product of q1 and k2(“Are vs you”).


    The "third" step is to divide the scores by \sqrt_{d_{k}} (the paper assumes d_{k} = 64.), then pass the result into exponential with division 1/Z. The result is attention/softmax score. Interestingly, we can turn this structure into softmax description where Z equals the sum of exponential — Figure(9). This attention score determines how much each word will be expressed at this position, just like how attention model did. Clearly the word at this position will have the highest softmax score, but sometimes it’s useful to attend to another word that is relevant to the current word.

    The "final" step is to multiply each value vector by the attention score, then sum up the weighted value vectors (z_{i}). This produces the output of the self-attention layer at this position (for the first word), similar to context vector in attention model

![Calculation of attention](https://miro.medium.com/max/3000/1*qSpa4BLAwa3pOgZ3lyxgBg.png)

![Calculation of Attention in matrix form](https://miro.medium.com/max/875/1*_PaA3wgyz1I0zRZtZNmu_w.png)
## Multi-head attention

    If we only computed a single attention weighted sum of the values, it would be hard to capture diverse representations of the input. To improve the performance of the model, instead of doing a single attention function with d_{model}-dimensional keys, values and queries, authors found it beneficial to linearly project the queries, keys and values h times with different linear projections to d_{q}, d_{k} and d_{v} dimensions, respectively. In the paper, d_{k}=d_{v}=d_{model}/h=64.

    Also, the Transformer uses eight attention heads, so we end up with eight sets for each encoder/decoder. Each set is used to project the input embeddings into a different representation subspace. If we do the same self-attention calculation we described before, we end up with eight different Z matrices. However, the feed-forward layer is not expecting eight matrices. We need to concatenate them and condense these eight down into a single matrix by multiply them with an additional weights matrix WO — figure(12).

![Mutli head attention](https://miro.medium.com/max/875/1*bROJ3Utxf_zIhz-SkATYzw.png)

> ## References
>
    [ ] https://medium.com/@bgg/seq2seq-pay-attention-to-self-attention-part-1-d332e85e9aad
    [ ] https://medium.com/@bgg/seq2seq-pay-attention-to-self-attention-part-2-cf81bf32c73d
    [ ] Coursera course of Andrew Ng - Sequence models
    [ ] Idea of Key-Value -> [paper](https://arxiv.org/pdf/1606.03126.pdf)
    [ ] [Recommendation System](https://arxiv.org/pdf/1711.06632.pdf) 
