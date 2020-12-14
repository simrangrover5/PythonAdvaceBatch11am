"""This module conists of function which we can use to find the place from text """
import requests
def search_place_from_text(place):
    """
        It takes place as an argument and search the place 
        It prints the results it finds for the particular place
    """
    parameters = {
                "key" : "AIzaSyB6AhDcEux73PWbJaa1t6Oo7jBVGLrudfw",
                "input" : place,
                "inputtype" : "textquery",
                "fields" : "business_status,formatted_address,geometry,name,permanently_closed,photos,place_id,opening_hours,price_level,rating,user_ratings_total" 
                }
    url = "https://maps.googleapis.com/maps/api/place/findplacefromtext/json?"
    data = requests.get(url, params=parameters)
    if data.status_code == 200:
        data = data.json()
        address = data['candidates'][0].get('formatted_address')
        open_ = data['candidates'][0].get('opening_hours')
        rating = data['candidates'][0].get('rating')
        geo = data['candidates'][0].get('geometry')
        print(f"Address : {address}")
        print(f"Rating : {rating}")
        if geo:
            for key, value in geo['location'].items():
                print(key, ": ", value)
        if open_:
            for key, value in open_.items():
                print(key, ": ", value)
    else:
        print("Invalid Details")
PLACE = input("\n Enter any place : ")
search_place_from_text(PLACE)
