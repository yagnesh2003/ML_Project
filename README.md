# Student Performance Indicator
## Overview
The Student Performance Indicator is an end-to-end machine learning project aimed at predicting students' math scores based on various features related to their backgrounds and academic achievements. By leveraging the student performance dataset, the project seeks to identify key factors that influence a student's performance in mathematics.

## Dataset Features
The dataset includes the following features:

* Gender: The gender of the student.
* Race/Ethnicity: The racial and ethnic background of the student.
Parental Level of Education: The highest level of education attained by the student's parents.
Educational Course Done or Not: Whether the student has completed a preparatory course.
Reading Score: The reading score of the student.
Writing Score: The writing score of the student.
Target Feature - Math Score: The math score of the student, which is the primary variable we aim to predict.
By analyzing these features, the project develops a predictive model to estimate a student's math score, providing insights into the educational and personal factors that most significantly impact mathematical performance.

## Dataset Source: Kaggle - Student Performance in Exams

The dataset consists of 8 columns and 1000 rows.
## Motivation
The motivation for building this project is to make people understand how machine learning (ML) is applied to real-world problems and to highlight the importance of ML in real-world applications. Through this project, we aim to demonstrate the practical value of ML in educational settings and its potential to drive data-driven insights and improvements.

## Technologies and Tools
Languages Used: Python, HTML, CSS
Framework Used: Flask
Libraries Used: numpy, pandas, sklearn
Additional Features: Logging and error handling with custom exception handling
## Project Structure
I have created a virtual environment in VS Code with a structured folder system to ensure easy navigation and understanding. Here is a brief overview of each folder and file:

Artifacts: This folder contains the files or inputs used in the project. For example, train.csv is used for training the model, test.csv is used for evaluation, and model.pkl and preprocessor.pkl will be uploaded to the Flask API to show the results on a web app.

Src: This folder contains all the code related to machine learning modeling.

Components: This folder includes the main phases of any machine learning project:
Data Ingestion: Functions for loading and preprocessing data.
Data Transformation: Functions for transforming data into a suitable format for modeling.
Model Training: Functions for training the machine learning model.
Logger.py: For logging messages at various stages.
Exception.py: For error handling.
Utils.py: For storing commonly used functions.
Templates: Contains HTML files for building basic web pages to display results.

app.py: The main Flask application to build a basic web app for displaying results.

requirements.txt: Lists all the libraries used in the project.

setup.py: Used to build and distribute Python packages, containing information about the package such as its name, version, and dependencies.

## Instructions
### Setup Environment:

Install Anaconda on your system.
Launch VS Code using Anaconda Navigator.
Create a virtual environment in VS Code using conda create and activate it using conda activate (env_name).
Ensure you are inside the activated environment whenever working on the project.
### Install Dependencies:

Install the required libraries using pip install -r requirements.txt.
First, run setup.py and then requirements.txt.
If any library is not in requirements.txt, you can install it using pip install <library_name> or add the library name inside requirements.txt and run it again.
Note: The latest numpy versions (>= 2.0.0) are not compatible with the catboost version. Install a lower version of numpy (preferably 1.26.4 or lower).
### Run the Application:

Once all dependencies are installed, you can proceed with coding and running the project.
By following these instructions, you will be able to set up and run the Student Performance Indicator project smoothly. This project not only demonstrates the application of machine learning in a real-world context but also provides a valuable tool for educational analysis and improvement.









