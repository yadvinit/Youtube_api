# Api for Youtube Video Fetech using Flask Web Framework

A Flask-based web app that fetches and displays the latest videos sorted in reverse chronological order of their publishing date-time from YouTube
videos for a given search query. 
Supports multiple API keys, pagination.

*******************************************************

## Features

- Search latest videos using YouTube Data API v3
- Pagination support (Next/Previous results)
- Multiple API key is key get exhausted 
- `.env` support to keep credentials secure

**********************************************************

## Technologies Used

- Python (Flask)
- YouTube Data API v3
- Jinja2 (for templating)
- HTML/CSS (basic frontend)
- dotenv (for environment variable management)

*********************************************************

## Project Structure

youtubeapi/
├── app.py                  
├── config.py               
├── .env                    
├── requirements.txt        
├── services/
│   └── youtube_service.py  
├── routes/
│   └── main_routes.py     
└── templates/
    └── home.html          

*********************************************************

## .env File structure 

YOUTUBE_API_KEY = your_key1,your_key2
