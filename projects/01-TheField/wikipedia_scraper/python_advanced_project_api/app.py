from fastapi import FastAPI, Cookie, Query
import os
import json
from fastapi.responses import JSONResponse
from uuid import uuid4
from typing import Optional
from datetime import datetime, timedelta


app = FastAPI()

# Create a dictionary to store the cookies
cookies = {}

""" Load the dataset from the json files and build a dictionary with the data """
data = {}
for f in os.listdir("./data/"):
    if f.endswith(".json"):
        with open(os.path.join("./data/", f)) as json_file:
            data[os.path.splitext(os.path.basename(f))[0]] = json.load(json_file)
            
def check_cookie_validity(cookie):
    """
    Check cookie validity

    Args:
        cookie_value (uuid): The cookie value to check

    Returns:
        _type_: _description_
    """
    cookie_value = cookie#cookie.get("user_cookie", None)
    if cookie_value == None or cookie_value not in cookies:
        return JSONResponse(content={"message": "The cookie is missing"}, status_code=403)
    if cookies[cookie_value] < datetime.now():
        if cookies[cookie_value] < datetime.now() - timedelta(days=2):
            del cookies[cookie_value]
        return JSONResponse(content={"message": "The cookie is expired"}, status_code=403)
    return "OK"
        
    
@app.get("/status/")
def get_api_status():
    """
    Returns the status of the API.

    Returns:
        A message confirming that the API is running.
    """
    return "Alive"

@app.get("/cookie/")
def generate_cookie():
    """
    Generates a cookie (valid for 30 seconds)

    Returns:
        A message confirming that the cookie has been created. The cookie is returned in the response itself and is valid for 30 seconds
    """
    content = {"message": "The cookie has been created"}
    response = JSONResponse(content=content)
    
    cookie = str(uuid4())
    cookies[cookie] = datetime.now() + timedelta(seconds=30)
    
    response.set_cookie(key="user_cookie", value=cookie)
    return response

@app.get("/check/")
def check_cookie(user_cookie: Optional[str] = Cookie(None)):
    """
    Checks if the cookie is valid or not.

    Returns:
        A message indicates whether the cookie is valid or not
    """
    cookie_validity = check_cookie_validity(user_cookie)
    if cookie_validity != "OK":
        return cookie_validity
    else:
        return JSONResponse(content={"message": "The cookie is valid"}, status_code=200)

@app.get("/countries")
def get_countries(user_cookie: Optional[str] = Cookie(None)):
    """
    Get the list of countries covered by the API

    Returns:
        The list of countries covered by the API
    """
    cookie_validity = check_cookie_validity(user_cookie)
    if cookie_validity != "OK":
        return cookie_validity
    else:
        return JSONResponse(content=list(data.keys()), status_code=200)

@app.get("/leaders")
def get_leaders_from_a_country(country: str = Query(None, description=f"Indicate here a country code among {list(data.keys())}"), user_cookie: Optional[str] = Cookie(None)):
    """
    Get the list of leaders of a country based on the country id

    Returns:
        The list of leaders of the country
    """
    cookie_validity = check_cookie_validity(user_cookie)
    if cookie_validity != "OK":
       return cookie_validity
    if country == None:
        return JSONResponse(content={"message": "Please specify a country"}, status_code=404)
    if country in list(data.keys()):
        return data[country]
    else:
        return JSONResponse(content={"message": f"This country is not covered by the API. Please pick one among {list(data.keys())}"}, status_code=404)
    
@app.get("/leader")
def get_leader_based_on_id(leader_id: str = Query(None, description=f"Indicate here a leader ID"), user_cookie: Optional[str] = Cookie(None)):
    """
    Get the details of a leader based on its id

    Returns:
        A dictionary containing the details about the leader
    """
    cookie_validity = check_cookie_validity(user_cookie)
    if cookie_validity != "OK":
        return cookie_validity
    if leader_id == None:
        return JSONResponse(content={"message": "Please specify a leader id"}, status_code=404)
    for country, leaders in data.items():
        for leader in leaders:
            if leader["id"] == leader_id:
                return leader
    
    return JSONResponse(content={"message": "Leader not found"}, status_code=404)


