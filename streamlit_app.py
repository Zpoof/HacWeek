import streamlit as st
import spoonacular as sp
import json
from PIL import Image
import requests
from IPython.display import display
import textwrap

def toStr(arr):
  arr_str =''
  for n in arr:
    arr_str += n + ','

  listver = list(arr_str)
  listver2 = ''
  listver2 = listver2.join(listver[:-1])

  return listver2

api = sp.API("bd80779ab3ae4516846129806a4a211e")

st.image("Logo.png")
st.header("Get Personalized Food Recommendations With Recipes!")
st.text(" ")

max_cals = st.slider("Select maximum calories", 0, 5000,0, 50, help = "0 for no limit")
max_time = st.slider("Select maximum time required (mins)", 0, 600,0, 5, help = "0 for no limit")

cuisine_options = st.multiselect("Choose your cuisine", ['African','American','British','Cajun','Caribbean','Chinese','Eastern european','European','French','German','Greek','Indian','Irish','Italian','Japanese','Jewish','Korean','Latin American','Mediterranean','Mexican','Middle Eastern','Nordic','Southern','Spanish','Thai','Vietnamese'])
cuisine_options = [x.lower() for x in cuisine_options]

meal_type = st.multiselect("Choose meal type", ['Main Course','Side Dish','Dessert','Appetizer','Salad','Bread','Breakfast','Soup','Beverage','Sauce','Marinade','Fingerfood','Snack','Drink'])
meal_type = [x.lower() for x in meal_type]

diets = st.selectbox('Select a diet: ', ('Any', 'Vegan', 'Vegetarian'))
if diets == 'Any':
  diets = ''
else:
  diets = diets.lower()


search_q = st.text_input("Enter dish name", value ="Type Here(Optional)", help = "Leave empty for random results")
#st.text(max_time)

cuisine_options_str = toStr(cuisine_options)
#cuisine_options_str

meal_type_str = toStr(meal_type)
#meal_type_str
st.text(" ")
if st.button('Find Food!'):
  if search_q == 'Type Here(Optional)' or search_q == '':
    search_q = '';
  if max_cals == 0 and max_time == 0:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, instructionsRequired = True, number = 1, fillIngredients = True, diet = diets)
  elif max_cals == 0:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, maxReadyTime = max_time, instructionsRequired = True, number = 1, fillIngredients = True, diet = diets)
  elif max_time == 0:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, maxCalories = max_cals, instructionsRequired = True, number = 1, fillIngredients = True, diet = diets)
  else:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, maxReadyTime = max_time, maxCalories = max_cals, instructionsRequired = True, number = 1, fillIngredients = True, diet = diets)
    

  data = response.json()
  var = data
  if len(var.get("results")) == 0:
    st.warning("Sorry! No results found.")
    st.stop()
  
  
  x = var.get("results")[0]
  
  
  st.title(x.get('title'))
  st.image(x.get("image"), width = 600)
  st.header("Ingredients: ")

  y = x.get("missedIngredients")
  for n in y:
    st.text(n.get('original'))
    #im = Image.open(requests.get(n.get('image'), stream=True).raw)
    #st.image(im)

  st.text(" ")
  st.header("Instructions: ")
  res = api.get_analyzed_recipe_instructions(id=x.get('id'), stepBreakdown=False)
  rec = res.json()
  u = rec[0].get('steps')
  if len(u) > 1:
    for n in u:
      if n.get('step')[0] == " ":
        p = '-' + n.get('step')
      else:
        p = '- ' + n.get('step')  
        
      p = textwrap.fill(p, 90)
      st.text(p)
  else:
    p = u[0].get('step')
    p = p.split('.')
    for n in p:
      if n[0] == " ":
        q = '-' + n;
      else:
        q = '- ' + n;
      
      q = textwrap.fill(q, 90)
      st.text(q)
