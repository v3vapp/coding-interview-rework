from fastapi import FastAPI, HTTPException
from typing import Optional
from pydantic import BaseModel
from python.main import PrimeNumberChecker

app = FastAPI()

class Params(BaseModel):
    minimum: int
    maximum: int
    sma_length: Optional[int] = None

@app.post("/v1/prime_number/")
async def create_item(params: Params):

    if params.maximum <= params.minimum:
        raise HTTPException(status_code=400, detail="maximum must be greater than minimum")

    elif params.sma_length is not None and params.sma_length <= 0:
        raise HTTPException(status_code=400, detail="sma_length must be greater than 0")

    else:
        try:
            datasets = PrimeNumberChecker(params.minimum, params.maximum, params.sma_length)

            prime_list = datasets.is_prime()
            twin_prime_list = datasets.is_twin_prime()
            img_path = datasets.primeNumber_pctChange()

        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Internal Server Error: {e}")

    return {"prime_list": prime_list, "twin_prime_list": twin_prime_list, "img_path": img_path}