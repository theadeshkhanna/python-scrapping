from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from scapper import Scraper
from auth import verify_token
from database import Database

app = FastAPI()

class ScrapeRequest(BaseModel):
    pages: int = None
    proxy: str = None

@app.post("/scrape", dependencies=[Depends(verify_token)])
async def scrape_data(scrape_request: ScrapeRequest):
    scraper = Scraper(scrape_request.pages, scrape_request.proxy)
    scraped_data = scraper.scrape()
    Database.save(scraped_data)
    return {"message": f"{len(scraped_data)} products scraped and saved."}

