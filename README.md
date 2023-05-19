# ZomatoRestaurantandCuisine
<p>
  <img src="https://drive.google.com/uc?export=download&id=1Bd49vSfj1TPXnApPAm60ZOsJncv-rdSR" width="800">
</p>

## Introduction
 The Zomato project is a data-driven endeavor that utilizes web scraping and machine learning techniques to extract and analyze restaurant data from Zomato. By collecting information such as restaurant names, locations, ratings, cuisines, and prices, the project aims to provide personalized recommendations based on user preferences. With a user-friendly web interface, users can easily input their desired cuisine and price range to receive tailored restaurant suggestions. This project simplifies the process of choosing a restaurant by leveraging data and technology to enhance the dining experience.

## Problem aimed to solve:

- Simplifying Restaurant Selection.
- Saving Time and Effort in Searching for Restaurants.
- Providing Comprehensive Restaurant Information.
- Analyzing Restaurant Data for Insights.
## Data Description

- Table 1: Restaurant_info

| Attribute       | Description                                                       |
|-----------------|-------------------------------------------------------------------|
| restaurant_id   | Unique ID to identify the restaurant (Primary Key)                 |
| restaurant_link | Zomato URL for that restaurant                                    |
| name            | Name of the restaurant                                            |
| rating          | Rating of the restaurant on Zomato                                |
| price           | Price of one person                                               |
| cuisines        | Types of cuisine offered by the restaurant                        |

- Table 2: Restaurant_details

| Attribute                | Description                                                        |
|--------------------------|--------------------------------------------------------------------|
| restaurant_id            | Unique ID to identify the restaurant (Primary Key)                  |
| restaurant_name          | Name of the restaurant                                             |
| latitude                 | Latitude coordinates of the restaurant                             |
| longitude                | Longitude coordinates of the restaurant                            |
| location                 | Location of the restaurant                                         |
| delivery_review_number   | Number of people who have reviewed the delivery service of the restaurant  |

## Methodology

The following methodology was used to accomplish the project objectives:

- **Data Scraping:** Utilize Selenium and WebDriver to automate the web scraping process. Extract relevant information from the Zomato website, including restaurant names, locations, ratings, cuisines, and prices.

- **Data Cleaning:** Apply data cleaning techniques to ensure the accuracy and reliability of the extracted data. Handle missing values, remove duplicates, and standardize the data for further analysis.

- **Machine Learning Model:** Train a Random Forest model using the cleaned data. The model will learn from the features such as restaurant attributes, ratings, and prices to predict the cuisine and price range of restaurants.

- **Web Interface Development:** Create a user-friendly web page using Streamlit or a similar framework. Design an interface where users can input their cuisine and price preferences.

- **Prediction and Recommendation:** Utilize the trained machine learning model to predict the cuisine and price range based on user preferences. Provide personalized restaurant recommendations that align with the user's input.

- **Display Results:** Present the recommended restaurants to the user through the web interface. Display additional details such as restaurant names, locations, ratings, and cuisines to assist the user in making an informed decision.
## Results
### This is webpage that will take input from users and generate output according to user search.
<p>
  <img src="https://drive.google.com/uc?export=download&id=1qoVP3s4almI1duLkqwZGO0opWjcBz1iF" >
</p>

## Limitations and Challenges
- **Real-time Data Updates**: The project utilizes a specific dataset at a given point in time. However, restaurant information, ratings, and prices are subject to change over time. Therefore, the project may not reflect real-time updates and changes in the restaurant data.

- **Dependency on Zomato**: The project heavily relies on the Zomato platform and its data availability. Any changes in Zomato's policies, terms of service, or access to data may impact the project's functionality and data retrieval process.

- **Webscrapping**:The main challenge in the Zomato project was the limited knowledge of Selenium for web scraping. Extensive research and learning were required to overcome errors and obstacles encountered during the scraping process. With perseverance and continuous learning, the challenges were overcome, leading to successful data extraction from the Zomato website.
