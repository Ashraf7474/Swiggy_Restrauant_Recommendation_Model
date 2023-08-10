import streamlit as st
import pandas as pd
import joblib
import numpy as np
# Load the dataset
loaded_model = joblib.load('E:\\OneDrive\Desktop\model\Model\dishprice.joblib')


df = pd.read_csv("E:\OneDrive\Desktop\model\Model\\restaurant_data.csv")

def recommendation(location, cuisine,Price_for_1):
    # for the area selected, display the popular cuisine
    popular_cuis = ''
    popular_cuisine = df[df['Location'] == location].groupby('Cuisine')['Cuisine'].count().sort_values(ascending=False)
    popular_cuisine = popular_cuisine[popular_cuisine == popular_cuisine.max()].index.tolist()
    if len(popular_cuisine) == 1:
        popular_cuis = popular_cuisine[0]
    else:
        for i in popular_cuisine:
            if i not in popular_cuisine[-1]:
                popular_cuis += i
                popular_cuis += ', '
            else:
                popular_cuis += i

    # average price for 1
    avg_price_for_1 = round(df[df['Location'] == location]['Price_for_1'].mean(),0)

    # Display the most popular Restaurant and Cuisine they are serving
    most_popular_restaurant = df[(df['Location'] == location)].sort_values('Rating', ascending=False).iloc[0][0]

    serves = ''
    most_popular_restaurant_serve = df[df['Restaurant_Name'] == most_popular_restaurant]['Cuisine'].tolist()
    if len(most_popular_restaurant_serve) == 1:
        serves = most_popular_restaurant_serve[0]
    else:
        for i in most_popular_restaurant_serve:
            if i not in most_popular_restaurant_serve[-1]:
                serves += i
                serves += ', '
            else:
                serves += i
    # Display the most popular restaurant that is serving the same cuisine as user provided cuisine
    result = df[(df['Location'] == location) & (df['Cuisine'] == cuisine)].sort_values('Rating', ascending=False)
    if not result.empty:
        most_popular_restaurant_that_serves_your_cuisine = result.iloc[0][0]
        output = result.iloc[0][0]
    else:
        most_popular_restaurant_that_serves_your_cuisine = "No results found."
        output = "No results found."

    return [avg_price_for_1, popular_cuis, most_popular_restaurant, serves,
            most_popular_restaurant_that_serves_your_cuisine]






def app():

    st.title("RESTURANT RECOMMANDATION SYSTEM")

    # Dropdown for cuisine
    cuisine_options = ['afghani', 'american', 'andhra', 'arabian', 'asian', 'biryani', 'breakfast', 'british', 'burgers', 'burmese', 'cafe', 'chettinad', 'chinese', 'coastal', 'continental', 'desserts', 'european', 'fast food', 'french', 'healthy food', 'hyderabadi', 'ice cream', 'indian', 'italian', 'jain', 'japanese', 'kebabs', 'kerala', 'mangalorean', 'mediterranean', 'mexican', 'mughlai', 'north indian', 'pan asian', 'pastas', 'pizzas', 'rajasthani', 'rolls', 'salads', 'seafood', 'south indian', 'spanish', 'street food', 'sushi', 'thai', 'tibetan']
    user_input1 = st.selectbox("Cuisine:", cuisine_options)

    # Dropdown for location
    location_options = ['adugodi', 'ashok-nagar', 'banashankari', 'banaswadi', 'basavanagudi', 'basaveshwara-nagar', 'bel-road', 'bima-nagar', 'bommanahalli', 'brigade-road', 'central', 'chikpete', 'course-road', 'cunningham-road', 'domlur', 'ejipura', 'ganganagar', 'halasuru', 'hebbal', 'hennur', 'indiranagar', 'jayanagar', 'jp-nagar', 'kalyan-nagar', 'kammanahalli', 'koramangala', 'lavelle-road', 'layout', 'magrth-road', 'majestic', 'malleshwaram', 'marathahalli', 'mathikere', 'mg-road', 'muneswara-nagar', 'nagarathpete', 'nagawara', 'rajajinagar', 'richmond-road', 'rt-nagar', 'sadashiv-nagar', 'sanjay-nagar', 'seshadripuram', 'shanti-nagar', 'shivaji-nagar', 'st-marks-road', 'stage-btm', 'street', 'tavarekere', 'temple-road', 'tengumal-nagar', 'town', 'ulsoor', 'vasanth-nagar', 'vijay-nagar', 'wilson-garden', 'yeshwantpur']
    user_input2 = st.selectbox("Location:", location_options)

    user_input3 = st.number_input("Price for 1:")

    prediction_price = ''

    if st.button('Submit'):
        st.title("Based on Prefered Location")
        output = recommendation(user_input2, user_input1, user_input3)
        st.write("Popular Cuisine:", output[1])
        st.write("Average Price for 1:", output[0])
        st.write("Most Popular Restaurant:", output[2], )
        st.write("Serves:", output[3])
        st.write("Popular Restaurant that serves your cuisine:", output[4])
        st.title("Recommandation")
        st.write("prediction Price:" ,output[0]*1.1)
        st.write("Prediction:", "koramangala")


if __name__ == '__main__':
    app()




