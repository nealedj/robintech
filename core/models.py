from google.appengine.ext import db

class LinkedInKey(db.Model):
    email = db.TextProperty()
    client_key = db.TextProperty()
    client_secret = db.TextProperty()
    code = db.IntegerProperty()
    oauth_token = db.TextProperty()
    oauth_secret = db.TextProperty()

    def __init__(self, *args, **kwargs):
        kwargs['key_name'] = kwargs['email']
        super(LinkedInKey, self).__init__(*args, **kwargs)