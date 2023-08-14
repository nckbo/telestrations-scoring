# Telestrations Scoring System
## Overview
This project aims to propose an objective scoring system for the popular drawing and guessing game, Telestrations. By using text embeddings, we can quantify the similarity between the original prompt and subsequent drawings/guesses. As the game progresses, players' drawings and guesses can deviate greatly from the original prompt, making it interesting to compute and visualize this deviation.

## Usage
Play a round of Telestrations and use the telestrations-template to record the results.
Feed the recorded data into the provided Jupyter notebook to compute the similarity scores.

## Key Features
Data Transformation: The recorded data is transformed to a melted format that provides a clear view of each round's drawings and guesses. The data is then cleaned by removing unnecessary columns and characters.

Embeddings: The system utilizes text embeddings to generate vectors representing the drawing prompts and guesses. The cosine similarity between these vectors provides a measure of how closely related the two texts are.

Scoring Mechanisms: The project provides three different scoring methods:

Linear Scoring
Logarithmic Scoring
Logistic Scoring
Each method processes the cosine similarity differently to produce a score.

Visualizations: The system showcases various visualizations such as:

Scatter plots that compare the cosine similarity to the computed score.
A scoreboard that shows each player's performance.
Line plots that trace the deviation of a drawing/guess from the original prompt over multiple rounds.
Box plots that highlight the distribution of similarities for each round.
## Requirements
Python libraries: pandas, numpy, seaborn, matplotlib, adjustText, openai, embeddings (custom module for text embeddings)
Excel template (telestrations-template.xlsx) to record game results.
## Steps to Run
Fill in the telestrations-data.xlsx with the results from your game (note that this project currently only supports 8 player games). Record rows in the order that the telestrations notebooks are passed. 
Execute the Jupyter notebook 'Telestration-scoring.ipynb.
Explore various visualizations and insights generated.
## Conclusion
With this scoring system, Telestrations games can now be more competitive and engaging, as players can track their performance over time. It provides a unique blend of fun and data analysis, offering a fresh take on a classic party game.

Happy drawing and guessing!
