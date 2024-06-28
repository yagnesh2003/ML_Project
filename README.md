## End to end Machine Learning project

Hi there, We are going to implement an end to end Machine learning project with flask api. The title of the project is Student Performance Indicator.
The Student Performance Indicator is an end-to-end machine learning project designed to predict students' math scores based on various features related to their backgrounds and academic achievements. By leveraging the student performance dataset, the project aims to identify key factors that influence a student's performance in mathematics.

# Dataset Features:

Gender: The gender of the student.
Race/Ethnicity: The racial and ethnic background of the student.
Parental Level of Education: The highest level of education attained by the student's parents.
Educational Course Done or Not: Whether the student has completed a preparatory course.
Reading Score: The reading score of the student.
Writing Score: The writing score of the student.
Target Feature - Math Score: The math score of the student, which is the primary variable we aim to predict.
By analyzing these features, the project develops a predictive model to estimate a student's math score, providing insights into the educational and personal factors that most significantly impact mathematical performance.

# Dataset Source - https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977
The data consists of 8 column and 1000 rows.

# Motivation:
The motivation for building this project is to make people understand how machine learning (ML) is applied in real-world problems and to highlight the importance of ML in real-world applications. Through this project, I aim to demonstrate the practical value of ML in educational settings and its potential to drive data-driven insights and improvements.


Languages used = Python, HTML, CSS

Framework Used = Flask

Libraries Used = numpy, pandas, sklearn

Additional features : Logging and error handling with custom exception

I have created a virtual environment in my vs code which has many folders and files in stuctured manner , so that it's easy for users to understand. I will explain what each folder and each file does , what is its function so that it's easy for you to connect.

Artifacts : This folder contains the files or inputs used in the project. FOr eg : Train.csv is used for training model, test.csv is used for evaluation of model. Model.pkl, preprocessor.pkl will be uploaded to flask api to show the results on a web app.
Src: We will write all our code of machine modelling inisde the src folder.
Components : Any machine learning project has three phases : Data ingestion , Data Transformation, Model Training . ALl these functions will be done inside components folder.
We will also have logger.py file for logging (printing messages at every stages), exception.py for error handling , and utils.py for storing all the function which will be commonly used in whole environment.

Templates : Inside templates, I will have codes to build basic webpages to show the results .
app.py : We will use flask framework to build a basic web app in order to show the resluts.
requirements.txt : This file stores all the libraries used in building this project .
setup.py : It is a module used to build and distribute Python packages. It typically contains information about the package, such as its name, version, and dependencies, as well as instructions for building and installing the package

# Instructions #
You need to have anaconda set up on your system . 
Launch vs code using your anaconda navigator . 
Create a virtual environment inside vs code using conda create and activate it using conda activate (env_name)
Note : You need to be inside the activated environment all the time you are working on the project.
Once you are done with setting up environment, you can install the required libraries using eigther pip command or requirement.txt file.
First run the setup.py file and then run the requirements.txt file. In case any library is not in the requirements.txt , you can install using pip command or add the library name inside requirements.txt and run it.
NOTE : The latest numoy versions (>= 2.0.0) are not compatible  with the catboost version. So, you need to install the lesser version of numpy (preferably 1.26.4 or lower) in order to make it work. 
Now you are good to go on with the coding part.
