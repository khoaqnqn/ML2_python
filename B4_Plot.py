import os
import matplotlib.pyplot as plt
from IPython.display import Image, display
from pathlib import Path

def Plot( data = None, category = '', dataset = 'dataset' ):
    if not data: return None

    figs = os.path.join( dataset, 'figs' )

    Path( figs ).mkdir( parents = True, exist_ok=True )

    plt.figure( figsize = ( 18, 3 ) )
    plt.subplots_adjust( wspace= 0.5 )
    plt.grid( True )
    plt.ylabel( 'Count items' )

    row = len( data )

    plotIndex = f'1{ row }'

    for index, item in enumerate( data ):
        y = list( item[ 0 ].values() )

        plt.subplot( int( f'{ plotIndex }{ index + 1 }' ) )
        plt.bar( list( item[ 0 ].keys() ), y, color = item[ 3 ] )
        plt.xlabel( f'Item { item[ 1 ] } / Max { item[ 1 ] } of { category }' )
        plt.title( f'{ item[ 1 ] } of { category } ( Max: { item[ 2 ] } )' )

        for index, data in enumerate( y ): plt.text( x = index , y = data , s = str( data ) )

    plt.savefig( f'{ figs }/{ item[ 1 ] }_{ category }.png' )
    plt.clf()
    display( Image( filename = f'{ figs }/{ item[ 1 ] }_{ category }.png' ) )
