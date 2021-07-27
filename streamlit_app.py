import streamlit as st
import spoonacular as sp

def toStr(arr):
  arr_str =''
  for n in arr:
    arr_str += n + ','

  listver = list(arr_str)
  listver2 = ''
  listver2 = listver2.join(listver[:-1])

  return listver2

api = sp.API("bd80779ab3ae4516846129806a4a211e")

st.image("/content/drive/MyDrive/Logo.png")
st.header("Get Personalized Food Recommendations With Recipes!")

search_q = st.text_input("Enter dish name", value ="Type Here", help = "Leave empty for random results")
cuisine_options = st.multiselect("Choose your cuisine", ['african','american','british','cajun','caribbean','chinese','eastern european','european','french','german','greek','indian','irish','italian','japanese','jewish','korean','latin american','mediterranean','mexican','middle eastern','nordic','southern','spanish','thai','vietnamese'])
meal_type = st.multiselect("Choose meal type", ['main course','side dish','dessert','appetizer','salad','bread','breakfast','soup','beverage','sauce','marinade','fingerfood','snack','drink'])
max_cals = st.slider("Select maximum calories", 0, 5000,200, 50, help = "0 for no limit")
max_time = st.slider("Select maximum time required (mins)", 0, 600,30, 5, help = "0 for no limit")
#st.text(max_time)

cuisine_options_str = toStr(cuisine_options)
#cuisine_options_str

meal_type_str = toStr(meal_type)
#meal_type_str
if st.button('Find Food!'):
  if search_q == 'Type Here' or search_q == '':
    search_q = '';
  if max_cals == 0 and max_time == 0:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, instructionsRequired = True, number = 1, fillIngredients = True)
  elif max_cals == 0:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, maxReadyTime = max_time, instructionsRequired = True, number = 1, fillIngredients = True)
  elif max_time == 0:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, maxCalories = max_cals, instructionsRequired = True, number = 1, fillIngredients = True)
  else:
    response = api.search_recipes_complex(query = search_q, cuisine = cuisine_options_str, type = meal_type_str, maxReadyTime = max_time, maxCalories = max_cals, instructionsRequired = True, number = 1, fillIngredients = True)
  
  data = response.json()
  data

