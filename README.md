# **Machine-Learning-project-end-to-end**



![](https://github.com/BALAJIHARIDASAN/Machine-Learning-project-end-to-end/blob/main/ml.gif)


**About this file :**

**California Housing Prediction**

**Target variable** : Median House Value( Continious)

Model : 'Supervised Regression Model'

1. **longitude:** A measure of how far west a house is; a higher value is farther west
2. **latitude:** A measure of how far north a house is; a higher value is farther north
3. **housingMedianAge:** Median age of a house within a block; a lower number is a newer building
4. **totalRooms:** Total number of rooms within a block
5. **totalBedrooms:** Total number of bedrooms within a block
6. **population:** Total number of people residing within a block
7. **households:** Total number of households, a group of people residing within a home unit, for a block
8. **medianIncome:** Median income for households within a block of houses (measured in tens of thousands of US Dollars)
9. **medianHouseValue:** Median house value for households within a block (measured in US Dollars)
10. **oceanProximity:** Location of the house w.r.t ocean/sea

**About Dataset :**

**Context :**

This is the dataset used in the second chapter of Aurélien Géron's recent book 'Hands-On Machine learning with Scikit-Learn and TensorFlow'. It serves as an excellent introduction to implementing machine learning algorithms because it requires rudimentary data cleaning, has an easily understandable list of variables and sits at an optimal size between being to toyish and too cumbersome.

The data contains information from the 1990 California census. So although it may not help you with predicting current housing prices like the Zillow Zestimate dataset, it does provide an accessible introductory dataset for teaching people about the basics of machine learning.




# Requirements:

1. Github

2. Heroku or render

3. cloud(AWS, GCP, Azure)

4. pycharm or vs code


### create environment

conda create -p venv python==3.7 -y


### activate environment

conda activate venv/

#### create requirements.txt

pip install - r requriements.txt



### Docker file

FROM python:3.7    - os

COPY . /app        - app

WORKDIR /app       - working directory   

RUN pip install -r requirements.txt  - install requirements

EXPOSE $PORT  - port number sent from the environment

CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app  



### Render app 

- since heroku is not availabe iam using render app



# Housing folder :

- package for project

- __init__.py - converts the housing folder into packages

- required packages

- exception - to print the error details  in the project process

- logger - to keep the log or track the project

- pipeline - combination of every component

- config - the input to the every pipeline component

- entity - the output of the each pipeline component

- components - each stages of the pipeline

- Util  - helper function 

- constant  - the variable that need for housing folder

- every folder should contaion __init__ file.



### Pipline :

1. **Data Ingestion :**

    - Bring data into system from multiple resources

    - Split data into traina and test data

2. **Data validation :**
    
    - Data Range
    
    - Outliers check

    - Duplicate Values

    - NUll value check

    - Schema validation

    - Domain values

    - Data drift -  the statistics of old and new data is different

    - Imbalanced dataset

3. **Data Transformation :**

    - Perform EDA to understand the data

    - Perform Feature engineering (Pickle)


4. **Model Training :**

    - Model selection  (pickle)

    - Hyperparamter tuning

5. **Model Evaluation :**

    - Model comparsion  - Compare the performance of  old model to new model( set some threshold)


6. **Model pushing :**

    - Model deployement



