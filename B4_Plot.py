import matplotlib.pyplot as plt
from IPython.display import Image, display

def Plot( data = None, category = '' ):
	if not data: return None

	for i in data:
		plt.grid( True )
		plt.ylabel( 'Count items' )

		plt.bar( list( i[ 0 ].keys() ), list( i[ 0 ].values() ), color ='maroon', width = 0.4 )
		plt.xlabel( f'Item { i[ 1 ] } / Max { i[ 1 ] } of { category }' )
		plt.title( f'Compare to max { i[ 1 ] } of Category { category } ( { i[ 2 ] } )' )
		plt.savefig( f'{ i[ 1 ] }_{ category }.png' )
		display( Image( filename = f'{ i[ 1 ] }_{ category }.png' ) )