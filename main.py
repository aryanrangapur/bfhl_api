from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
import re

app = FastAPI()

# Your details
FULL_NAME = "aryan_rangapur"   
DOB = "09092004"              
EMAIL = "aryan.22bce7399@vitapstudent.ac.in"
ROLL_NUMBER = "22BCE7399"

class DataModel(BaseModel):
    data: List[str]

def alternating_caps(s: str) -> str:
    """Convert string to alternating caps (first char uppercase, next lowercase, etc.)."""
    result = []
    upper = True
    for ch in s:
        if ch.isalpha():
            result.append(ch.upper() if upper else ch.lower())
            upper = not upper
    return "".join(result)

@app.post("/bfhl")
async def process_data(payload: DataModel):
    try:
        even_numbers, odd_numbers, alphabets, special_characters = [], [], [], []
        total_sum = 0

        for item in payload.data:
            if item.isdigit():
                num = int(item)
                (even_numbers if num % 2 == 0 else odd_numbers).append(item)
                total_sum += num
            elif re.match("^[A-Za-z]+$", item):  # pure alphabets
                alphabets.append(item.upper())
            else:
                special_characters.append(item)

        # Concatenation of all alphabets (joined, reversed, alternating caps)
        concat_string = alternating_caps("".join(alphabets)[::-1])

        return {
            "is_success": True,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total_sum),
            "concat_string": concat_string
        }

    except Exception as e:
        return {
            "is_success": False,
            "user_id": f"{FULL_NAME}_{DOB}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": [],
            "even_numbers": [],
            "alphabets": [],
            "special_characters": [],
            "sum": "0",
            "concat_string": "",
            "error": str(e)
        }
