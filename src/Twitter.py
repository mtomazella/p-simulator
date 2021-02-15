import tweepy

class Twitter:
    def __init__ ( self, auth = { 'consumer_key': '', 'consumer_secret': '', 'access_token': '', 'token_secret': '' } ):
        # print( auth['consumer_key'] )
        # print( auth['consumer_secret'] )
        self.auth = tweepy.OAuthHandler( auth['consumer_key'], auth['consumer_secret'] )
        self.auth.set_access_token( auth['access_token'], auth['token_secret'] )
        self.api  = tweepy.API( self.auth )

    def get_screenName ( self, user = None ):
        if user == None:
            return self.api.me().screen_name
        else:
            return self.api.get_user( user ).screen_name

    def postText ( self, text ):
        self.api.update_status( text )

    def postImage ( self, imagePath, subtitle = '' ):
        print( imagePath, subtitle )
        self.api.update_with_media( imagePath, status = subtitle )