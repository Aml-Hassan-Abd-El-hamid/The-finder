import streamlit as st
import json
import requests
import time
import pandas as pd
import cohere
import numpy as np
def extract_product_names_from_json(file_name):
    product_names=[]
    file = open(file_name)
    data = json.load(file) 
    for d in data:
        product_names.append(d['name'])
    return product_names
def streamlit_look():
    """
    Modest front-end code:)
    """
    data={}
    st.title("Welcome to the product finder :)")
    data["product_name"]= st.text_input("Please type your product name")
    data["api_key"] = st.text_input("Please enter your cohere API key", type="password")
    st.write("""If you don't know how to get your cohere API key, please do the following:
                \n1- sign up for a free [cohere account](https://cohere.com/)
                \n2- log in to your cohere account and from the dashboard you can find your api key, 
             there are free and paid options, the free one works just fine here""")
    
    return data
def match_the_product(product_name,api_key):
    st.write("Please wait")
    d={"products":extract_product_names_from_json("Black Friday.json")}
    df = pd.DataFrame(d)
    co = cohere.Client(api_key)
    embeddings = co.embed(list(df["products"]), model="multilingual-22-12").embeddings
    embeddings_np = np.array(embeddings)  # Convert the list to numpy array 
    
    query_embedding = co.embed([product_name], model='multilingual-22-12').embeddings
    results = np.array(query_embedding) @ embeddings_np.T # Shape [1, 768] @ [768, 6] = [1, 6]
    
    sorted_index =np.argsort(results)[0][::-1] # Sort in Descending Order
    df['products'][sorted_index].reset_index(drop=True)
    df["sorted_index"]=sorted_index

    #show the most 3 closest items
    st.write(df.iloc[[df["sorted_index"].iloc[0]]]["products"].to_string(index=False))
    st.write(df.iloc[[df["sorted_index"].iloc[1]]]["products"].to_string(index=False))
    st.write(df.iloc[[df["sorted_index"].iloc[2]]]["products"].to_string(index=False))
    
def main():  
    user_data=streamlit_look()
    search = st.button("search")
    if search:
        try:
            match_the_product(user_data["product_name"],user_data["api_key"])
            st.write("done")
        except:
            st.write("""An exception occurred
                  You probably didn't enter a prober API key or a product name for the search""")

if __name__ == "__main__":
    main()