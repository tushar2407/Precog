# Transformer

## Algorithm
    Define the model
        In this tutorial, we train nn.TransformerEncoder model on a language modeling task. The language modeling task is to assign a  probability for the likelihood of a given word (or a sequence of words) to follow a sequence of words. A sequence of tokens are passed to the embedding layer first, followed by a positional encoding layer to account for the order of the word (see the next paragraph for more details). The nn.TransformerEncoder consists of multiple layers of nn.TransformerEncoderLayer. Along with the input sequence, a square attention mask is required because the self-attention layers in nn.TransformerEncoder are only allowed to attend the earlier positions in the sequence. For the language modeling task, any tokens on the future positions should be masked. To have the actual words, the output of nn.TransformerEncoder model is sent to the final Linear layer, which is followed by a log-Softmax function.

    PositionalEncoding module injects some information about the relative or absolute position of the tokens in the sequence. The positional encodings have the same dimension as the embeddings so that the two can be summed. Here, we use sine and cosine functions of different frequencies.

    Load and batch data
        This tutorial uses torchtext to generate Wikitext-2     dataset.    The vocab object is built based on the train    dataset and is    used to numericalize tokens into     tensors. Starting from    sequential data, the batchify () function arranges the  dataset into columns, trimming     off any tokens remaining  after the data has been   divided into batches of size     batch_size. For  instance, with the alphabet as the sequence     (total   length of 26) and a batch size of 4, we would divide      the alphabet into 4 sequences of length 6:

        These columns are treated as independent by the model,  which    means that the dependence of G and F can not be     learned, but   allows more efficient batch processing.

    Functions to generate input and target sequence
        get_batch() function generates the input and target sequence for the transformer model. It subdivides the source data into chunks of length bptt. For the language modeling task, the model needs the following words as Target. For example, with a bptt value of 2, we’d get the following two Variables for i = 0:

        It should be noted that the chunks are along dimension 0, consistent with the S dimension in the Transformer model. The batch dimension N is along dimension 1.
    
    Initiate an instance
        The model is set up with the hyperparameter below. The vocab size is equal to the length of the vocab object.

    Run the model
        CrossEntropyLoss is applied to track the loss and SGD implements stochastic gradient descent method as the optimizer. The initial learning rate is set to 5.0. StepLR is applied to adjust the learn rate through epochs. During the training, we use nn.utils.clip_grad_norm_ function to scale all the gradient together to prevent exploding.

        Loop over epochs. Save the model if the validation loss is the best we’ve seen so far. Adjust the learning rate after each epoch.



## References
    https://pytorch.org/tutorials/beginner/transformer_tutorial.html