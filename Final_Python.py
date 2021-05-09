from B1_Crawl import Crawl
from B2_ListCategories import ListCategories
from B2_ReadLabel import ReadLabel
from B3_Standardization import Standardization
from B4_Plot import Plot
import sys

if __name__ == '__main__':
	newFolder = 'dataset'
	mp = False

	if sys.argv and len( sys.argv ) >= 2:
		newFolder = sys.argv[ 1 ]

		if sys.argv[ 2 ] == 'True': mp = True

		if newFolder != 'dataset': Crawl( newFolder )

	for category in ListCategories( newFolder ):
		if category.find( 'bai-tho' ) < 0: continue

		readLabel = ReadLabel( category, newFolder, mp )
		standardization = Standardization( readLabel[ 0 ] )
		Plot( standardization, readLabel[ 1 ] )
