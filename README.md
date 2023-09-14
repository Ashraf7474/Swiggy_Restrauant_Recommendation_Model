# Swigg Restaurant Recommendation Model
![Capture37](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/08c5e11a-9c71-4d60-945b-49d7b9b68f3c)

# Tools & Technologies Used
![image](https://github.com/Sudhansu352010/1Mg-Homeopathic-Data-Analysis/assets/131376814/1d4cac22-bcd3-4990-b918-d739138c9396)

# OUR APPROACH FOR THE PROJECT
![image](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/6011d055-d1fd-409b-9c1f-1e71a08490fc)

# User's Manual
![Capture42](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/5b2e3e54-23d1-4eef-b94e-cd74c72b6737)

# --Introduction--

As it becomes crucial for customers at a new location to find the appropriate restaurant based on their preferences so a recommendation model can be a handful for the customers to get what they want and also for the companies to the betterment of services for their further future growth.

# --Problem Aimed to Solve--

To develop a Swiggy restaurant recommender model which can predict the suitable restaurant, price for two, and dish name based on a budget price, cuisine, and location

# --Data Description--

EXCEL FILES: This folder contains 3 Excel files where a. swiggy_table1 has the link of the restaurant, name of the restaurant, cuisine, price for 2 customers, and rating of the restaurants in .csv format. b. swiggy_table2 has the dish price, total rating numbers, dish name, dish category, and name of the restaurants. c. finalized_swiggy_dataset has the combined two tables mentioned above and the final dashboard based on this.

Jupiter notebook files: This folder has 3 files where a. web_scrapping has the Jupiter files which were used to scrap the data from Swiggy(Bangaluru) b. ml2 file was used to clean the dataset after extraction and to convert the HTML restaurant details into CSV files. c. swiggy_model file contains the code to create an algorithm to predict the restaurant name, the price for two, and the dish name based on the budget price, cuisine, and location.

restaurant_recommender folder has the source code file which we used to show our model on the HTML webpage.

# --Methodolgy--

The project involves extracting, collecting, and processing Swiggy restaurants' data and then utilizes data analysis techniques and machine learning modeling to predict the final output based on the preferences.

# --Phases--

Data Extraction: Gather comprehensive data from Swiggy, encompassing user interactions, orders, menus, and other relevant details.

Data Cleaning and Preprocessing: Process the extracted data to address inconsistencies, missing values, and outliers, ensuring high data quality and reliability.

Recommendation Model: Develop a sophisticated recommendation model that suggests personalized food choices based on user preferences, historical data, and menu offerings.

Prediction Model: Create a predictive model that anticipates future food demand, helping optimize inventory management and delivery operations.

Web Application (Streamlit): Integrate the prediction and recommendation models into a user-friendly web application using Streamlit. Users can explore food options, receive recommendations, and visualize predictive insights.

Power BI Dashboard: Design an interactive Power BI dashboard that visualizes key performance indicators, sales trends, and user preferences, aiding decision-makers in strategic planning.

# Web Scraping Code
![image](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/53d0c8e0-7f2f-4508-b03b-4d70e011a53f)
![image](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/05c6bc9b-f49b-4758-a20d-37906766e14c)
![image](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/592f5ba3-8291-41a5-8cea-497e32508f08)

The first CSV contains data on restaurants, including columns such as restaurant ID, restaurant name, restaurant link, price for two people, ratings, and the cuisines they serve. This table provides an overview of the restaurants available on the food delivery platform.

The second CSV contains information on dishes offered by the restaurants. It includes columns such as restaurant ID, restaurant name, dishes, cuisines, and the price of each dish. This table provides detailed information about the specific dishes offered by each restaurant.

# Data Snapshot
![Capture48](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/c2065031-6ced-4394-a626-670caec4c2c3)


# Preffered Price and Location Code
![Capture47](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/fd499c9a-b04d-4e36-adf2-64b081e761b7)

# Machine Learning Model Code(Snapshot)
![ml1](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/100ef6c4-3afa-421a-af17-6e53fa94ffeb)
![ml2](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/825868de-535c-4b31-801e-b724c62632f1)
![ml3](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/b6fff5cb-f998-44b8-a554-225d779bbf45)
![ml4](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/b1d34521-93c4-43f1-8edf-c3a672a49eb6)
![ml5](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/9e793c85-5e1d-4ef7-997f-c70009c9fd50)


# web page Code(snapshot)
![w1](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/3b176a49-75bd-40b7-a657-5ff4d11b1164)
![w2](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/1c6bffc2-a5f5-40ed-9b46-024038e972cd)
![w3](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/46d6c739-6809-4b95-ad17-924b6133e942)




# Web Page(Snapshot)

![Capture](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/7b8ca7a5-d6b3-4b7d-bb18-1d02a81e93de)

# DashBoard Creation
Here is the main dashboard which is dynamic in nature and the slicer added

![Dashboard_image](https://github.com/Ashraf7474/Swiggy_Restrauant_Recommendation_Model/assets/131772000/b56874be-738e-423e-b1c6-41cf572364eb)

# Insights

Beverages, Desserts, Indian & Biryani cuisine has the greatest number of restaurants

Clients can keep dishes related to this cuisine so that more consumers will get attracted to their restaurant

Most popular restaurant by ratings: Malabar Bay

Adugodi, Basavana Gudi, Basaveshwara Nagar - These areas have more number of restaurants, we can assume that more consumers are from these areas

Indira Nagar, Koramangala, Basaveshwara Nagar has a greater number of expensive restaurants based on average price.

# Challenges Faced

During the analysis, I may have faced challenges including data quality issues, website structure complexities, managing large data volumes, legal and ethical considerations, and interpreting the data for meaningful insights. Ensuring the accuracy and completeness of the scraped data while handling dynamic website elements can be demanding. Additionally, complying with legal and ethical boundaries, optimizing code, and addressing changing website structures require careful attention. Analyzing and interpreting the data, as well as maintaining technical expertise, are crucial for overcoming these challenges and deriving valuable insights from the project.






