import os
import matplotlib.pyplot as plt
from IPython.display import Image, display
from pathlib import Path

def Plot( data = None, category = '', dataset = 'dataset' ):
    if not data: return None

    figs = os.path.join( dataset, 'figs' )

    Path( figs ).mkdir( parents = True, exist_ok=True )

    plt.figure()

    plt.grid( True )
    plt.ylabel( 'Count items' )

    row = len( data )

    plotIndex = f'1{ row }'

    for index, i in enumerate( data ):
        plt.subplot( int( f'{ plotIndex }{ index + 1 }' ) )
        plt.bar( list( i[ 0 ].keys() ), list( i[ 0 ].values() ), color ='maroon' )
        plt.xlabel( f'Item { i[ 1 ] } / Max { i[ 1 ] } of { category }' )
        plt.title( f'Compare to max { i[ 1 ] } of Category { category } ( { i[ 2 ] } )' )

    plt.savefig( f'{ figs }/{ i[ 1 ] }_{ category }.png' )
    display( Image( filename = f'{ figs }/{ i[ 1 ] }_{ category }.png' ) )
