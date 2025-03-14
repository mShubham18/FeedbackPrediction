# Feedback Prediction System

A machine learning-based system that analyzes customer feedback and predicts sentiment (positive, negative, or neutral) using Natural Language Processing (NLP) techniques.

## Features

- Web-based interface for easy interaction
- CSV file upload support
- Real-time sentiment analysis
- Downloadable predictions
- Built with Streamlit and TensorFlow

## Prerequisites

- Python 3.12+
- Required packages (install using `pip install -r requirements.txt`)

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd FeedbackPrediction
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```

## Usage

1. Launch the application using the command above
2. Upload a CSV file containing customer reviews
   - The CSV should have a single column with review text
   - Column name doesn't matter as it will be automatically renamed
3. Wait for the processing to complete
4. Download the results as a CSV file containing:
   - Original message
   - Predicted sentiment (positive/negative/neutral)

## Project Structure

- `app.py`: Main web application
- `models/`: Contains trained model and vectorizer
- `data/`: Data storage
- `pipelines/`: Data processing pipelines
- `*.ipynb`: Jupyter notebooks for development and analysis

## Model Details

The system uses:
- Neural Network model for sentiment classification
- NLTK for text preprocessing
- TF-IDF vectorization for feature extraction

## Contributing

Feel free to submit issues and enhancement requests! 