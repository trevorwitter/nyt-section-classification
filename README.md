# New York Times Section Classification

- Classifies article section from headline + lead paragraph text

#### Training Data
- Collects headline, lead paragraph, section name, and publication date for all articles published by New York Times in 2019


#### Model
Word embedding
- [GloVe](https://nlp.stanford.edu/projects/glove/) embedding transforms text to vector representations
RNN layers
- vector representations then used to train LSTM recurrent neural network

Model Summary:
![Model Summary](/images/model_summary.png)
