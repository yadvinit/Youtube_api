from flask import Blueprint, render_template, request, current_app
from services.youtube_service import get_recent_videos

# flask bluprint
main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def home():
    query = request.args.get('q', current_app.config['DEFAULT_SEARCH_QUERY'])
    page_token = request.args.get('pageToken', '')
    
    
    result = get_recent_videos(query, page_token)
    
    
    if 'error' in result:
        return render_template('home.html', 
                              query=query,
                              error=result['error'])
    
   

    
   
    return render_template('home.html',
                          query=query,
                          videos=result['videos'],
                          next_token=result['next_token'],
                          prev_token=result['prev_token'])

#/api route for api calls

@main_bp.route('/api')
def getapi():
    query = request.args.get('q', current_app.config['DEFAULT_SEARCH_QUERY'])
    page_token = request.args.get('pageToken', '')
    result = get_recent_videos(query, page_token)
    if 'error' in result:
        return result
    
    return result