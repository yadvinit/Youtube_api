import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    #spliting the api key for using different 
    YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY", "").split(",")
    
    
    # api key setting for showing the result
    YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'
    DEFAULT_SEARCH_QUERY = 'basketball'
    RESULTS_PER_PAGE = 10