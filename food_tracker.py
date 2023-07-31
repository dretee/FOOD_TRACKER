def coustomers_food_perference(dictionary_for_all_the_food_served_in_the_area):
 
  food_preference = set()
  picked_numbers = []
 
  print(dictionary_for_all_the_food_served_in_the_area)
  number_input = (input('please pick your prefered food\
from the list above use the numbers to make your choice: ' ))
  
  for numb in number_input:
    if numb == '0':
      continue
    else:
      picked_numbers.append(int(numb))
  print(picked_numbers)

  for number, food in dictionary_for_all_the_food_served_in_the_area.items():
      if number in  picked_numbers:
        food_preference.add(food)
  print(food_preference)
  return food_preference

def main():
  restaurants = {
          "seafood_cove": {"🍤", "🍣", "🐟", "🦀", "🍞", "🥑", "🍔", "🍟"},
          "hungry_jacks": {"🍔", "🍟", "🍦", "🍕","🍤", "🍣","🥦", "🥕", "🍞"},
          "potting_shed": {"🥦", "🥕", "🍞", "🥑", "🍔", "🍟","🍤", "🍣"},
          }

  dictionary_for_all_the_food_served_in_the_area = {1 : "🍔", 2 : "🍕", 3 : "🍤", 4 : "🥕", 5 : "🍞", 6 : "🍣",
    7 : "🥑", 8 : "🐟", 9 : "🦀", 10 : "🍟", 11 : "🍦", 12 : "🥦"
    } 
  
  best_food = set()
  best_store = None

  prefered_foods = coustomers_food_perference(dictionary_for_all_the_food_served_in_the_area)
  
  for stores, menu in restaurants.items():
    crosser = prefered_foods.intersection(menu)

    if len(crosser) > len(best_food):
      best_food = crosser
      best_store = stores
  
  print(f'The suitable restaurant that will suit your preferance \
is {best_store} having majority of your preference {best_food}.')
  
if __name__ == '__main__':
  main()
