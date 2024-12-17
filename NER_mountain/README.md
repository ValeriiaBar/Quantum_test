# NER Model for Mountain Name Recognition

## Project Overview
This project implements a Named Entity Recognition (NER) model to identify and tag mountain names in text data. The model uses the BERT transformer architecture for token classification, 
along with a dataset specifically curated for mountain names.

The key stages of this project include:
- Dataset Preparation: Creating a BIO-tagged dataset from a list of mountain names.
- Model Training: Fine-tuning a pre-trained BERT model for token classification.
- Evaluation: Assessing the model's performance on unseen data. (undone)
## Solution Explanation

### 1. Data Preparation
- from GeoNamas allCounries.zip was downloaded
- Python script to filter only Mountain, Mountains and Volcano by column Feature Code was written
- Python script to 'clean' data from excessive information was done
- due to ChatGPT 100 sentences about mountains were generated
- python script to create 1000 diffenert sentences was made
- i have LabelStudio used to label all of my 1000 sentences (B-mountain, I-mountain), but in process i had some doubt and generate the list of 100 the most famous and popular mountain,
  also generated sentences and labeled them, so i got 1097 sentences
- The input dataset consists of sentences containing mountain names.
- A BIO-tagging scheme (B-Begin, I-Inside, O-Outside) is applied to label tokens:
   - **B-MOUNTAIN**: Beginning of a mountain name (e.g., `Mount` in `Mount Everest`).
   - **I-MOUNTAIN**: Inside a multi-word mountain name (e.g., `Everest` in `Mount Everest`).
   - **O**: Tokens that do not belong to a mountain name.

#### Example BIO Tagging:
| Sentence                   | BIO Tags                        |
|----------------------------|---------------------------------|
| Mount Everest is majestic. | B-MOUNTAIN I-MOUNTAIN O O O     |
| Kilimanjaro is in Africa.  | B-MOUNTAIN O O O O              |

### 2. Model Configuration
- **Tokenizer**: `BertTokenizer` from Hugging Face.
- **Model**: `BertForTokenClassification`, fine-tuned for NER.
- **Framework**: PyTorch and Transformers library.
- **Dataset**: Prepared using `datasets.Dataset` for efficient processing.

The following are the necessary but uncompleted items

### 3. Training Process
- The dataset is split into training and validation sets.
- Trainer API from Hugging Face is used to fine-tune the model with custom arguments:
   - Learning rate
   - Batch size
   - Number of epochs
- Loss Function: Cross-entropy loss, as it is a standard for token classification tasks.

### 4. Model Evaluation
- Performance is evaluated using metrics such as precision, recall, and F1-score.
- Predictions on sample text confirm the model's ability to tag mountain names correctly.

---

