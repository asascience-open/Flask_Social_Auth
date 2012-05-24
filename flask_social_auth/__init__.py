from flask import Flask
from oauth import OAuth

# Create application object
app = Flask(__name__)
app.config.from_object('flask_social_auth.default')

oauth = OAuth()
facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=app.config.get('FACEBOOK_APP_ID'),
    consumer_secret=app.config.get('FACEBOOK_APP_SECRET'),
    request_token_params={'scope': 'email'}
)
twitter = oauth.remote_app('twitter',
    base_url='https://api.twitter.com/1/',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authenticate',
    consumer_key=app.config.get('TWITTER_CONSUMER_KEY'),
    consumer_secret=app.config.get('TWITTER_CONSUMER_SECRET')
)
google = oauth.remote_app('google',
    base_url=None,
    request_token_url=None, #this should only exist for OAuth1.0
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    consumer_key=app.config.get('GOOGLE_CLIENT_ID'),
    consumer_secret=app.config.get('GOOGLE_CLIENT_SECRET'),
    access_token_method='POST',
    request_token_params={'response_type':'code','scope':'https://www.googleapis.com/auth/userinfo.email','grant_type':'authorization_code'}
)

# Import everything
import flask_social_auth.views
