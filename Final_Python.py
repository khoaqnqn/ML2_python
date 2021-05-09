from B1_Crawl import Crawl
from B2_ListCategories import ListCategories
from B2_ReadLabel import ReadLabel
from B3_Standardization import Standardization
from B4_Plot import Plot
import sys

if __name__ == '__main__':
	if sys.argv and len( sys.argv ):
		Crawl()

	for category in ListCategories():
		if category.find( 'bai-tho' ) < 0: continue

		readLabel = ReadLabel( category )
		standardization = Standardization( readLabel[ 0 ] )
		Plot( standardization, readLabel[ 1 ] )
