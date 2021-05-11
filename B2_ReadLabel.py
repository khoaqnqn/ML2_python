import os
import multiprocessing as mp
from tqdm import tqdm

def ReadItem( item = None, labelPath = None ):
    if not item\
        or not labelPath\
        or not os.path.exists( os.path.join( labelPath, item ) ): return None

    content = ''

    with open( os.path.join( labelPath, item ), 'r' ) as file:
        content = file.read()

    countLines = 0
    words = []
    
    for line in content.split( '\n' ):
        if line == '': continue

        countLines += 1

        for word in line.split( ' ' ):
            if word == '': continue

            words.append( word )

    return ( countLines, len( words ), len( words ) / countLines )

def ReadLabel( label = None, newFolder = 'dataset', multi = False ):
    labelPath = os.path.join( os.getcwd(), newFolder, label )

    if not label or not os.path.exists( labelPath ): return None

    if multi:
        # make colors
        pool = mp.Pool( mp.cpu_count() - 1 )
        results = pool.starmap( ReadItem, [ ( item, labelPath ) for item in tqdm( os.listdir( labelPath ), label ) ] )
        pool.close()
    else:
        results = [ ReadItem( item, labelPath ) for item in os.listdir( labelPath ) ]

    return [ results, label ]
