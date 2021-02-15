import cv2 as cv
import os

class Imagemzador:
    def __init__ ( self, inputPath = './data/inputImage.jpg', outputPath = './data' ):
        self.outputPath = outputPath
        self.inputPath  = inputPath

    def generateWithText ( self, text ):
        image = cv.imread( self.inputPath )
        if image is None:
            return False
        cv.putText( image, text, org=(37,68), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=0.45, color=(10,10,10), thickness=1, lineType=cv.LINE_AA )
        cv.imwrite( self.outputPath + '/out.jpg', image )

    def clearOutput ( self ):
        os.remove( self.outputPath + '/out.jpg' )