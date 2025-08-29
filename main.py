from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Union
import re

app = FastAPI()

FULL_NAME = "john_doe"    
DOB = "17091999"         
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"

class DataInput(BaseModel):
    data: List[str]

def process_array(arr: List[str]):
    evens, odds, alphabets, specials = [], [], [], []
    total_sum = 0

    for item in arr:
        if re.fullmatch(r"\d+", item): 
            num = int(item)
            if num % 2 == 0:
                evens.append(item)
            else:
                odds.append(item)
            total_sum += num
        elif item.isalpha(): 
            alphabets.append(item.upper())
        else:
            specials.append(item)

    concat_string = ""
    all_alpha = "".join([a for a in arr if a.isalpha()])
    all_alpha_reversed = all_alpha[::-1]

    for i, ch in enumerate(all_alpha_reversed):
        concat_string += ch.upper() if i % 2 == 0 else ch.lower()

    return evens, odds, alphabets, specials, str(total_sum), concat_string

@app.post("/bfhl")
async def bfhl(input_data: DataInput):
    try:
        evens, odds, alphabets, specials, total_sum, concat_string = process_array(input_data.data)

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odds,
            "even_numbers": evens,
            "alphabets": alphabets,
            "special_characters": specials,
            "sum": total_sum,
            "concat_string": concat_string
        }
        return response
    except Exception as e:
        return {"is_success": False, "error": str(e)}