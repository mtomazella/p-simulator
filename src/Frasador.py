import random

class Frasador:
    def __init__ ( self ):
        self.verbs = self.toList( './data/verbos.txt' )
        self.nouns = self.insertArticle( self.toList( './data/subs.txt' ) )

        # print(self.verbs)
        # print(self.nouns)

    def toList ( self, path ):
        file = open( path, 'r' )
        elements = file.readlines()
        for i in range(len( elements )-1):
            elements[i] = elements[i].lower().replace('\n','')
        file.close()
        return elements

    def insertArticle ( self, elements ):
        for i in range(len( elements )-1):
            try:
                elements[i] = ('a ' if elements[i][-1] == 'a' else 'o ') + elements[i]
            except:
                print(elements[i])
        return elements

    def genPhrase ( self ):
        verb = random.choice( self.verbs )
        noun = random.choice( self.nouns )

        verb = verb.capitalize()

        return verb + ' ' + noun