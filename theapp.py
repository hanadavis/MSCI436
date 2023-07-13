# -*- coding: utf-8 -*-
"""theapp.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JisMBWwnKF94_ZPDBC73rZuEchTswBJv
"""

#install streamlist
!pip install -q streamlit

# Commented out IPython magic to ensure Python compatibility.
# %%writefile app.py
# 
# #import all necessary packages
# import streamlit as st
# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# 
# #import prediction function
# from model_house import predict
# 
# df_train = pd.read_csv('train.csv')
# 
# # Function for Price Prediction
# def page1():
#     st.title("Prediction of House Prices")
#     # Add content for Price Prediction
# 
#     #unique list of attributes for one hot encoded attributes (categorical variables)
#     house_styles = list(df_train['HouseStyle'].unique())
#     neighborhood_unique = list(df_train['Neighborhood'].unique())
#     centralair_unique = list(df_train['CentralAir'].unique())
# 
#     st.markdown('**Objective** : Given details about the house we will predict the house price. Please fill out all the fields then scroll down and click on the button to predict the price.')
# 
#     #take input from user for the features we have selected to make predictions on
#     LotArea = st.slider('Choose Lot Area', 1000, 500000, 1000)
#     HouseStyle = st.selectbox('Choose House Style', house_styles)
#     Neighborhood_input = st.selectbox('Choose Neighborhood', neighborhood_unique)
#     YearBuilt = st.slider('Choose Year Built', 1872, 2023,1872)
#     BedroomAbvGr = st.slider('Choose Number of Bedrooms', 1,100,1)
#     FullBath = st.slider('Choose Number of Full Bathrooms', 1,50,1)
#     CentralAir = st.radio('Central Air', centralair_unique, horizontal=True)
#     GarageCars = st.slider('Choose Number of Garage Cars', 0,100,0)
# 
#     #input_filled = LotArea and HouseStyle_num and Neighborhood_num and YearBuilt and Heating_num and CentralAir_num and GarageCars and SaleType_num
#     #if input_filled:
# 
#     #map input from users to list with unique attributes in order to use them in prediction function as numerical values
#     if st.button("Predict"):
# 
#         if HouseStyle == '2Story':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == '1Story':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == '1.5Fin':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == '1.5Unf':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == 'SFoyer':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == 'SLvl':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == '2.5Unf':
#           HouseStyle_num = house_styles.index(HouseStyle)
#         elif HouseStyle == '2.5Fin':
#           HouseStyle_num = house_styles.index(HouseStyle)
# 
#         if CentralAir == 'Y':
#           CentralAir_num = centralair_unique.index(CentralAir)
#         elif CentralAir == 'N':
#           CentralAir_num = centralair_unique.index(CentralAir)
# 
#             #if statements for select box of Neighborhood
#         if Neighborhood_input == 'CollgCr':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Veenker':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Crawfor':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'NoRidge':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Mitchel':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Somerst':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'NWAmes':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'OldTown':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'BrkSide':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Sawyer':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'NridgHt':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'NAmes':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'SawyerW':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'IDOTRR':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'MeadowV':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Edwards':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Timber':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Gilbert':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'StoneBr':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'ClearCr':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'NPkVill':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Blmngtn':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'BrDale':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'SWISU':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
#         elif Neighborhood_input == 'Blueste':
#           Neighborhood_num = neighborhood_unique.index(Neighborhood_input)
# 
#         # Create input array
#         arr = [float(LotArea), float(HouseStyle_num), float(Neighborhood_num), float(YearBuilt),
#               float(FullBath), float(BedroomAbvGr), float(CentralAir_num), float(GarageCars)]
# 
#         # Perform prediction
#         predicted_price = predict(arr)
# 
#         # Display the predicted price
#         predicted_price = max(predicted_price, 0)
#         st.write(f"<span style='font-size: 24px; color: green;'>The predicted price is $ {predicted_price:.2f}</span>", unsafe_allow_html=True)
# 
# # Data for correlation chart
# # Function for Visuals
# def page2():
#     st.title("Visuals")
#     # Add content for Visuals
#     st.title("Correlation Chart: Variables vs. Price")
#     st.markdown('**Objective**: Explore the correlation between variables and house prices.')
#     # Select variables for correlation
#     selected_vars = st.multiselect('Select variables', df_train.columns)
#     # Calculate correlation matrix
#     correlation_matrix = df_train[selected_vars + ['SalePrice']].corr()
#     # Plot correlation heatmap
#     fig, ax = plt.subplots(figsize=(10, 8))
#     sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5, ax=ax)
#     st.pyplot(fig)
# 
#     # Create a scatter plot
#     fig, ax = plt.subplots()
#     ax.scatter(df_train['BedroomAbvGr'], df_train['FullBath'])
# 
#     # Set labels and title
#     ax.set_xlabel('Bedrooms ')
#     ax.set_ylabel('Full Bathrooms')
#     ax.set_title('Scatter Plot of Lot Area vs. Sale Price')
# 
#     # Display the chart
#     st.pyplot(fig)
# 
#     #box plot
#     fig, ax = plt.subplots()
#     sns.boxplot(x='Neighborhood', y='SalePrice', data=df_train, ax=ax)
# 
#     # Set labels and title
#     ax.set_xlabel('Neighborhood')
#     ax.set_ylabel('Sale Price')
#     ax.set_title('Distribution of Sale Price by Neighborhood')
# 
#     # Rotate x-axis labels for better visibility
#     plt.xticks(rotation=45)
# 
#     # Display the chart
#     st.pyplot(fig)
# 
#     # Graph for bathrooms and bedrooms
#     # User input
#     num_bedrooms = st.slider('Number of Bedrooms', min_value=1, max_value=10, value=3, step=1)
#     num_bathrooms = st.slider('Number of Bathrooms', min_value=1, max_value=5, value=2, step=1)
# 
#     # Filter the dataset based on user input
#     filtered_df = df_train[(df_train['BedroomAbvGr'] == num_bedrooms) & (df_train['FullBath'] == num_bathrooms)]
# 
#     # Check if the filtered dataset is empty
#     if filtered_df.empty:
#         st.write("No data available for the selected number of bedrooms and bathrooms.")
#     else:
#         # Create the graph
#         plt.figure(figsize=(10, 6))
#         sns.boxplot(x=filtered_df['BedroomAbvGr'], y=filtered_df['SalePrice'])
#         plt.xlabel('Number of Bedrooms')
#         plt.ylabel('Sale Price')
#         plt.title('Effect of Number of Bedrooms and Bathrooms on Sale Price')
# 
#         # Show the graph
#         st.pyplot(plt)
# 
#     #lot area vs neighborhood
# 
# 
#     st.markdown('**Impact of Neighborhood on Lot Area**')
#     import altair as alt
# 
#     c = alt.Chart(df_train).mark_circle().encode(
#     x='Neighborhood', y='LotArea', tooltip=['Neighborhood', 'LotArea'])
# 
#     st.altair_chart(c, use_container_width=True)
# 
#     #neighborhood vs house style, scatter plot
#     # Create a scatter plot
#     fig, ax = plt.subplots()
#     ax.scatter(df_train['HouseStyle'], df_train['Neighborhood'])
# 
#     # Set labels and title
#     ax.set_xlabel('HouseStyle ')
#     ax.set_ylabel('Neighborhood')
#     ax.set_title('Scatter Plot of Neighborhood versus House Style') #fix
# 
#     # Display the chart
#     st.pyplot(fig)
# 
# # add all the charts in a different page
# 
# #make the predict button colored and the text in a different color
# 
# # Main function
# def main():
#     st.sidebar.title("Navigation")
#     # Create a sidebar with navigation links
#     page = st.sidebar.radio("Go to", ("Introduction","Price Prediction", "Visuals"))
# 
#     if page == "Introduction":
#       st.title("Welcome to the House Prices Prediction App")
#       st.write("This app allows you to predict the prices of houses based on various features.")
#       st.write("Please select a page from the sidebar to explore different functionalities.")
#     elif page == "Price Prediction":
#        page1()
#     elif page == "Visuals":
#        page2()
# 
# if __name__ == '__main__':
#     main()
#

#run streamlit

!streamlit run app.py & npx localtunnel --port 8501