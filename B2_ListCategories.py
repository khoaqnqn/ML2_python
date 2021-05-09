import os

def ListCategories( newFolder = 'dataset' ):
	return os.listdir( os.path.join( os.getcwd(), newFolder ) )
