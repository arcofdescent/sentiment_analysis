# Sentiment Analysis

## Objective
Leran how to deploy models and serve them for inference using FastAPI.

## Model
We start with using the [TextBlob](https://textblob.readthedocs.io/en/dev/) model defined in *backend/app/model.py*. Soon I hope to use more advanced transformer models like BERT from HuggingFace. Requires more compute on your local machine or VM though.

## Setup
1. Clone this repo
2. `cd backend`
3. `uv sync` - you need to have `uv` installed first. This will install the Python deps.
4. Run the tests. `pytest -sv`
5. Hack on `app/model.py`

## Next steps
1. Explore more models
1. Implement a FastAPI endpoint server
1. Write a simple front-end using React
1. Dockerize the app for easy deployment



