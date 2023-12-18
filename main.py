import streamlit as st
import json
import requests
import time

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
    st.title("The product finder :)")
    data["product_name"]= st.text_input("Please type your product name")
    data["API_KEY"] = st.text_input("Please enter your HuggingFace API key", type="password")
    st.write("If you don't know how to get your HuggingFace API key, please watch this [1 minute video below](https://www.youtube.com/watch?v=jo_fTD2H4xA&ab_channel=RunThat)")
    return data
def match_the_product(product_name,API_KEY):
    product_names=extract_product_names_from_json("Black Friday.json")
def main():  
    user_data=streamlit_look()
    match_the_product(user_data["product_name"],user_data["API_KEY"])
    
    
    #for i in extract_product_names_from_json("Black Friday.json"):
    #    st.write(i)
    

if __name__ == "__main__":
    main()