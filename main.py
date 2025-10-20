
from datetime import datetime, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

import hashlib

class StringInput(BaseModel): 
    value: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "String Analyzer API is running 🚀"}


# database
db = {}

# utility functions

def get_length(value: str) -> int:
    return len(value) 

def is_palindrome(value: str) -> bool: 
    cleaned_value = value.lower().replace(" ", "")
    return cleaned_value == cleaned_value[::-1]

def get_unique_characters(value: str) -> int:
    unique_characters = set(value) 
    return len(unique_characters)

def get_word_count(value: str)-> int: 
    words = value.split()
    return len(words)

def get_sha256_hash(value: str): 
    encoded_string = value.encode()
    hash_object = hashlib.sha256(encoded_string)
    hex_digest = hash_object.hexdigest()
    return hex_digest

def get_character_frequency(value: str)-> dict: 
    freq = {}
    for char in value: 
        freq[char] = freq.get(char, 0) + 1 
    return freq

def get_created_at() -> str: 
        return datetime.now(timezone.utc).isoformat()
        



@app.post("/strings")
def analyze_string(data: StringInput):
    value = data.value
    
    if value is None or not value.strip():
        raise HTTPException(status_code=400, detail="Missing or empty 'value' field")
    
    if not isinstance(value, str): 
        raise HTTPException(status_code=422, detail="Value must be a string")
    
    sha_hash = get_sha256_hash(value)
    
    if sha_hash in db: 
        raise HTTPException(status_code=409, detail="String already exists")
    
    properties = {
        "length": get_length(value), 
        "is_palindrome": is_palindrome(value), 
        "unique_characters": get_unique_characters(value),
        "word_count": get_word_count(value),
        "sha256_hash": get_sha256_hash(value),
        "character_frequency_map":get_character_frequency(value)
    }
    
    analyzed_data = {
        "id": sha_hash, 
        "value": value, 
        "properties": properties,
        "created_at": get_created_at(), 
        
    }
    
    db[sha_hash] = analyzed_data 
     
    return analyzed_data



@app.get("/strings/{string_id}")
def get_string(string_id: str): 
    if string_id not in db: 
        raise HTTPException(status_code = 404, detail="String not found" )
    return db[string_id]

@app.get("/strings")
def get_all_strings(
    is_palindrome: Optional[bool] = None, 
    min_length: Optional[int] = None, 
    max_length: Optional[int] = None,
    word_count: Optional[int] = None, 
    contains_character: Optional[str] = None  
):
    results = list(db.values())
    
    # filtering time
    if is_palindrome is not None: 
        results = [
            r for r in results
            if r["properties"]["is_palindrome"] == is_palindrome
        ]
        
    if min_length is not None: 
        results =[
            r for r in results
            if r["properties"]["length"] >= min_length
        ]
        
    if max_length is not None: 
        results =[
            r for r in results
            if r["properties"]["length"] <= max_length
        ]
        
    if word_count is not None: 
        results = [
            r for r in results
            if r["properties"]["word_count"] == word_count
        ]
        
    if contains_character is not None: 
        if len(contains_character) != 1: 
            raise HTTPException(status_code=400, detail="contains_character must be a single character")
        results = [
            r for r in results
            if contains_character in  r["value"]
        ]
    
    return{
        "data": results ,
        "count": len(results), 
        "filters_applied": {
            "is_palindrome": is_palindrome, 
            "min_length": min_length, 
            "max_length": max_length, 
            "word_count": word_count, 
            "contains_character": contains_character, 
        
        }
    }
    
    

    
@app.delete("/strings/{string_value}", status_code= 204)
def delete_string(string_value: str): 
    sha_hash = get_sha256_hash(string_value)
    if sha_hash not in db: 
        raise HTTPException(status_code=404, detail="String not found")
    db.pop(sha_hash)
    return None
    
    
@app.get("/strings/filter-by-natural-language")
def filter_by_natural_language(query: str):
    pass
    
    

    