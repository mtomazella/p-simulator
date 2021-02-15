import os
from dotenv import load_dotenv
load_dotenv()
from src.Twitter import Twitter
from src.Frasador import Frasador
from src.set_interval import setInterval
from src.Imagemzador import Imagemzador

tt = Twitter( { 
    'consumer_key': os.getenv( 'CONSUMER_KEY' ), 
    'consumer_secret': os.getenv( 'CONSUMER_SECRET' ),
    'access_token': os.getenv( 'access_token' ),
    'token_secret': os.getenv( 'token_secret' ),
} )

frasador = Frasador()
imagemzador = Imagemzador()

def post ():
    phrase = frasador.genPhrase()
    print( phrase )
    imagemzador.generateWithText( phrase )
    tt.postImage( './data/out.jpg' )
    imagemzador.clearOutput()

post()
loop = setInterval( post, 3600 )

print( 'Bot Running' )