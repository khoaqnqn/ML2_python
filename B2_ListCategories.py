import os

def ListCategories():
	return os.listdir( os.path.join( os.getcwd(), 'dataset' ) )
