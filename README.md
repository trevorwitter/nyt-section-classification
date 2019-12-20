# New York Times Section Classification

- Classifies article section from headline + lead paragraph text

### Training Data
- Collects headline, lead paragraph, section name, and publication date for all articles published by New York Times in 2019 via [NYT API](https://developer.nytimes.com). 
- Data was obtained for 65,805 articles published in 49 sections.
![Section Count](/images/nyt_class_counts.png) 

### Model
- Word embedding
	- [GloVe](https://nlp.stanford.edu/projects/glove/) embedding transforms text to vector representations

- RNN layers
	- vector representations then used to train LSTM recurrent neural network

Model Summary:
- Model trained over 60 epochs with a batch size of 32

![Model Summary](/images/model_summary.png)

### Results
Model achieved 80.5% accuracy on test dataset
![loss](/images/loss.png)
![accuracy](/images/acc.png)

Confusion Matrix
![confusion matrix](/images/nyt_glove_lstm_cm.png)

