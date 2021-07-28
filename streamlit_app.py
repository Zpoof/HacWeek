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

max_cals = st.slider("Select maximum calories", 0, 5000,200, 50, help = "0 for no limit")
max_time = st.slider("Select maximum time required (mins)", 0, 600,30, 5, help = "0 for no limit")

cuisine_options = st.multiselect("Choose your cuisine", ['african','american','british','cajun','caribbean','chinese','eastern european','european','french','german','greek','indian','irish','italian','japanese','jewish','korean','latin american','mediterranean','mexican','middle eastern','nordic','southern','spanish','thai','vietnamese'])
meal_type = st.multiselect("Choose meal type", ['main course','side dish','dessert','appetizer','salad','bread','breakfast','soup','beverage','sauce','marinade','fingerfood','snack','drink'])
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
  
  data = """
{
  "results": [
    {
      "id": 649280,
      "usedIngredientCount": 0,
      "missedIngredientCount": 10,
      "missedIngredients": [
        {
          "id": 11294,
          "amount": 1,
          "unit": "medium",
          "unitLong": "medium",
          "unitShort": "medium",
          "aisle": "Produce",
          "name": "sweet onion",
          "original": "1 medium sweet onion finely chopped",
          "originalString": "1 medium sweet onion finely chopped",
          "originalName": "sweet onion finely chopped",
          "metaInformation": [
            "sweet",
            "finely chopped"
          ],
          "meta": [
            "sweet",
            "finely chopped"
          ],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/sweet-onion.png"
        },
        {
          "id": 11265,
          "amount": 8,
          "unit": "ounces",
          "unitLong": "ounces",
          "unitShort": "oz",
          "aisle": "Produce",
          "name": "portabella mushroom cap",
          "original": "8 ounces portabella mushroom sliced",
          "originalString": "8 ounces portabella mushroom sliced",
          "originalName": "portabella mushroom sliced",
          "metaInformation": [
            "sliced"
          ],
          "meta": [
            "sliced"
          ],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/portabello-mushrooms.jpg"
        },
        {
          "id": 1001,
          "amount": 2,
          "unit": "tablespoons",
          "unitLong": "tablespoons",
          "unitShort": "Tbsp",
          "aisle": "Milk, Eggs, Other Dairy",
          "name": "butter",
          "original": "2 tablespoons butter",
          "originalString": "2 tablespoons butter",
          "originalName": "butter",
          "metaInformation": [],
          "meta": [],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/butter-sliced.jpg"
        },
        {
          "id": 11463,
          "amount": 16,
          "unit": "ounces",
          "unitLong": "ounces",
          "unitShort": "oz",
          "aisle": "Frozen",
          "name": "frozen spinach",
          "original": "16 ounces frozen spinach thawed and drained well",
          "originalString": "16 ounces frozen spinach thawed and drained well",
          "originalName": "frozen spinach thawed and drained well",
          "metaInformation": [
            "frozen",
            "thawed",
            "drained",
            "well"
          ],
          "meta": [
            "frozen",
            "thawed",
            "drained",
            "well"
          ],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/spinach-frozen.jpg"
        },
        {
          "id": 11477,
          "amount": 3,
          "unit": "",
          "unitLong": "",
          "unitShort": "",
          "aisle": "Produce",
          "name": "zucchini",
          "original": "3 zucchini",
          "originalString": "3 zucchini",
          "originalName": "zucchini",
          "metaInformation": [],
          "meta": [],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/zucchini.jpg"
        },
        {
          "id": 1036,
          "amount": 30,
          "unit": "ounces",
          "unitLong": "ounces",
          "unitShort": "oz",
          "aisle": "Cheese",
          "name": "ricotta cheese",
          "original": "30 ounces ricotta cheese",
          "originalString": "30 ounces ricotta cheese",
          "originalName": "ricotta cheese",
          "metaInformation": [],
          "meta": [],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/ricotta.png"
        },
        {
          "id": 1123,
          "amount": 2,
          "unit": "",
          "unitLong": "",
          "unitShort": "",
          "aisle": "Milk, Eggs, Other Dairy",
          "name": "eggs",
          "original": "2 eggs",
          "originalString": "2 eggs",
          "originalName": "eggs",
          "metaInformation": [],
          "meta": [],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/egg.png"
        },
        {
          "id": 1026,
          "amount": 2,
          "unit": "cups",
          "unitLong": "cups",
          "unitShort": "cup",
          "aisle": "Cheese",
          "name": "mozzarella cheese",
          "original": "2 cups mozzarella cheese",
          "originalString": "2 cups mozzarella cheese",
          "originalName": "mozzarella cheese",
          "metaInformation": [],
          "meta": [],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/mozzarella.png"
        },
        {
          "id": 1033,
          "amount": 0.5,
          "unit": "cup",
          "unitLong": "cups",
          "unitShort": "cup",
          "aisle": "Cheese",
          "name": "parmesan",
          "original": "1/2 cup grated parmesan",
          "originalString": "1/2 cup grated parmesan",
          "originalName": "grated parmesan",
          "metaInformation": [
            "grated"
          ],
          "meta": [
            "grated"
          ],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/parmesan.jpg"
        },
        {
          "id": 6159,
          "amount": 1,
          "unit": "quart",
          "unitLong": "quart",
          "unitShort": "qt",
          "aisle": "Canned and Jarred",
          "name": "tomato soup",
          "original": "1 quart Pacific Natural Foods Organic Creamy Tomato Soup",
          "originalString": "1 quart Pacific Natural Foods Organic Creamy Tomato Soup",
          "originalName": "Pacific Natural Foods Organic Creamy Tomato Soup",
          "metaInformation": [
            "organic"
          ],
          "meta": [
            "organic"
          ],
          "image": "https://spoonacular.com/cdn/ingredients_100x100/tomato-soup.png"
        }
      ],
      "likes": 0,
      "usedIngredients": [],
      "unusedIngredients": [],
      "title": "Lasagna Silvia",
      "image": "https://spoonacular.com/recipeImages/649280-312x231.jpg",
      "imageType": "jpg"
    }
  ],
  "offset": 0,
  "number": 1,
  "totalResults": 8
}
"""

  data = response.json()
  var = data
  x = var.get("results")[0]
  st.title(x.get('title'))
  st.image(x.get("image"))
  st.header("Ingredients: ")

  y = x.get("missedIngredients")
  for n in y:
    st.text(n.get('original'))
    #im = Image.open(requests.get(n.get('image'), stream=True).raw)
    #st.image(im)

  st.text(" ")
  st.header("Instructions: ")
  res = api.get_analyzed_recipe_instructions(id=x.get('id'), stepBreakdown=False)
  rese = '''[
  {
    "name": "",
    "steps": [
      {
        "number": 1,
        "step": "Pre heat oven to 350 degrees",
        "ingredients": [],
        "equipment": [
          {
            "id": 404784,
            "name": "oven",
            "localizedName": "oven",
            "image": "oven.jpg"
          }
        ]
      },
      {
        "number": 2,
        "step": "Coat a 9X12 Lasagna pan with non stick spray",
        "ingredients": [],
        "equipment": [
          {
            "id": 404645,
            "name": "frying pan",
            "localizedName": "frying pan",
            "image": "pan.png"
          }
        ]
      },
      {
        "number": 3,
        "step": "Drain ricotta cheese in a sieve while preparing onions and mushrooms.",
        "ingredients": [
          {
            "id": 1036,
            "name": "ricotta cheese",
            "localizedName": "ricotta cheese",
            "image": "ricotta.png"
          },
          {
            "id": 11260,
            "name": "mushrooms",
            "localizedName": "mushrooms",
            "image": "mushrooms.png"
          },
          {
            "id": 11282,
            "name": "onion",
            "localizedName": "onion",
            "image": "brown-onion.png"
          }
        ],
        "equipment": [
          {
            "id": 405600,
            "name": "sieve",
            "localizedName": "sieve",
            "image": "strainer.png"
          }
        ]
      },
      {
        "number": 4,
        "step": "On medium heat, saut onion on  in 2 tablespoons virgin olive oil until translucent; about 10 minutes. Transfer to large mixing bowl.",
        "ingredients": [
          {
            "id": 1064053,
            "name": "virgin olive oil",
            "localizedName": "virgin olive oil",
            "image": "olive-oil.jpg"
          },
          {
            "id": 11282,
            "name": "onion",
            "localizedName": "onion",
            "image": "brown-onion.png"
          }
        ],
        "equipment": [
          {
            "id": 405907,
            "name": "mixing bowl",
            "localizedName": "mixing bowl",
            "image": "mixing-bowl.jpg"
          }
        ],
        "length": {
          "number": 10,
          "unit": "minutes"
        }
      },
      {
        "number": 5,
        "step": "In a large frying pan over medium/high heat saut portabella mushrooms in 2 tablespoons butter and 2 tablespoons olive oil until softened; about 5 minutes.  Add to the onions.",
        "ingredients": [
          {
            "id": 11265,
            "name": "portobello mushrooms",
            "localizedName": "portobello mushrooms",
            "image": "portabello-mushrooms.jpg"
          },
          {
            "id": 4053,
            "name": "olive oil",
            "localizedName": "olive oil",
            "image": "olive-oil.jpg"
          },
          {
            "id": 1001,
            "name": "butter",
            "localizedName": "butter",
            "image": "butter-sliced.jpg"
          },
          {
            "id": 11282,
            "name": "onion",
            "localizedName": "onion",
            "image": "brown-onion.png"
          }
        ],
        "equipment": [
          {
            "id": 404645,
            "name": "frying pan",
            "localizedName": "frying pan",
            "image": "pan.png"
          }
        ],
        "length": {
          "number": 5,
          "unit": "minutes"
        }
      },
      {
        "number": 6,
        "step": "Beat the two eggs and mix with the ricotta cheese.",
        "ingredients": [
          {
            "id": 1036,
            "name": "ricotta cheese",
            "localizedName": "ricotta cheese",
            "image": "ricotta.png"
          },
          {
            "id": 1123,
            "name": "egg",
            "localizedName": "egg",
            "image": "egg.png"
          }
        ],
        "equipment": []
      },
      {
        "number": 7,
        "step": "Mix the ricotta egg mixture into, onions and mushrooms and then the well drained spinach.",
        "ingredients": [
          {
            "id": 11260,
            "name": "mushrooms",
            "localizedName": "mushrooms",
            "image": "mushrooms.png"
          },
          {
            "id": 1036,
            "name": "ricotta cheese",
            "localizedName": "ricotta cheese",
            "image": "ricotta.png"
          },
          {
            "id": 10011457,
            "name": "spinach",
            "localizedName": "spinach",
            "image": "spinach.jpg"
          },
          {
            "id": 11282,
            "name": "onion",
            "localizedName": "onion",
            "image": "brown-onion.png"
          },
          {
            "id": 1123,
            "name": "egg",
            "localizedName": "egg",
            "image": "egg.png"
          }
        ],
        "equipment": []
      },
      {
        "number": 8,
        "step": "Thinly slice 3 zucchini lengthwise to create noodles.",
        "ingredients": [
          {
            "id": 11477,
            "name": "zucchini",
            "localizedName": "zucchini",
            "image": "zucchini.jpg"
          },
          {
            "id": 20420,
            "name": "pasta",
            "localizedName": "pasta",
            "image": "fusilli.jpg"
          }
        ],
        "equipment": []
      },
      {
        "number": 9,
        "step": "Cover the bottom of the lasagna pan with 1/4th of the Pacific Natural Foods Organic Creamy Tomato Soup.",
        "ingredients": [
          {
            "id": 6159,
            "name": "tomato soup",
            "localizedName": "tomato soup",
            "image": "tomato-soup.png"
          }
        ],
        "equipment": [
          {
            "id": 404645,
            "name": "frying pan",
            "localizedName": "frying pan",
            "image": "pan.png"
          }
        ]
      },
      {
        "number": 10,
        "step": "Place a layer of zucchini noodles in the lasagna pan, slightly overlapping them.",
        "ingredients": [
          {
            "id": 10111477,
            "name": "zucchini noodles",
            "localizedName": "zucchini noodles",
            "image": "zoodles.jpg"
          }
        ],
        "equipment": [
          {
            "id": 404645,
            "name": "frying pan",
            "localizedName": "frying pan",
            "image": "pan.png"
          }
        ]
      },
      {
        "number": 11,
        "step": "Spread 1/3 of the ricotta, mushroom, spinach mixture across the zucchini.",
        "ingredients": [
          {
            "id": 11260,
            "name": "mushrooms",
            "localizedName": "mushrooms",
            "image": "mushrooms.png"
          },
          {
            "id": 11477,
            "name": "zucchini",
            "localizedName": "zucchini",
            "image": "zucchini.jpg"
          },
          {
            "id": 1036,
            "name": "ricotta cheese",
            "localizedName": "ricotta cheese",
            "image": "ricotta.png"
          },
          {
            "id": 10011457,
            "name": "spinach",
            "localizedName": "spinach",
            "image": "spinach.jpg"
          },
          {
            "id": 0,
            "name": "spread",
            "localizedName": "spread",
            "image": ""
          }
        ],
        "equipment": []
      },
      {
        "number": 12,
        "step": "Sprinkle with 1/4 of the mozzarella cheese.",
        "ingredients": [
          {
            "id": 1026,
            "name": "mozzarella",
            "localizedName": "mozzarella",
            "image": "mozzarella.png"
          }
        ],
        "equipment": []
      },
      {
        "number": 13,
        "step": "Repeat the layers two more times.",
        "ingredients": [],
        "equipment": []
      },
      {
        "number": 14,
        "step": "Top with the tomato soup and sprinkle the last of the mozzarella across the lasagna.",
        "ingredients": [
          {
            "id": 6159,
            "name": "tomato soup",
            "localizedName": "tomato soup",
            "image": "tomato-soup.png"
          },
          {
            "id": 1026,
            "name": "mozzarella",
            "localizedName": "mozzarella",
            "image": "mozzarella.png"
          }
        ],
        "equipment": []
      },
      {
        "number": 15,
        "step": "Finish by topping the lasagna with the parmesan cheese; you will have a 2 cheese top.",
        "ingredients": [
          {
            "id": 1033,
            "name": "parmesan",
            "localizedName": "parmesan",
            "image": "parmesan.jpg"
          },
          {
            "id": 1041009,
            "name": "cheese",
            "localizedName": "cheese",
            "image": "cheddar-cheese.png"
          }
        ],
        "equipment": []
      },
      {
        "number": 16,
        "step": "Coat aluminum foil with non stick spray and cover the lasagna to keep the cheese from getting too dark.",
        "ingredients": [
          {
            "id": 1041009,
            "name": "cheese",
            "localizedName": "cheese",
            "image": "cheddar-cheese.png"
          }
        ],
        "equipment": [
          {
            "id": 404765,
            "name": "aluminum foil",
            "localizedName": "aluminum foil",
            "image": "aluminum-foil.png"
          }
        ]
      },
      {
        "number": 17,
        "step": "Bake for 1 hour, then uncover and bake for 15 minutes more.",
        "ingredients": [],
        "equipment": [
          {
            "id": 404784,
            "name": "oven",
            "localizedName": "oven",
            "image": "oven.jpg"
          }
        ],
        "length": {
          "number": 75,
          "unit": "minutes"
        }
      },
      {
        "number": 18,
        "step": "Let lasagna rest for 15 to 20 minutes prior to serving.",
        "ingredients": [],
        "equipment": [],
        "length": {
          "number": 15,
          "unit": "minutes"
        }
      }
    ]
  }
]'''
  rec = res.json()
  u = rec[0].get('steps')
  if len(u) > 1:
    for n in u:
      p = '- ' + n.get('step')
      p = textwrap.fill(p, 90)
      st.text(p)
  else:
    st.text(u[0].get('step'))









