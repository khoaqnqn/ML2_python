import os
import sys
from B1_Crawl import Crawl
from B2_ReadLabel import ReadLabel
from B3_Standardization import Standardization
from B4_Plot import Plot

HELP = '''
-mp             : for enable multi processing in some cases

-d:folder-name  : for new dataset with folder-name ( non-space separated )

-i:30           : for max items of each category

-c:5            : for max categories
'''

def main():
    dataset = 'dataset'
    enableMultiProcessing = False
    maxItems = 0
    maxCategories = 0

    # collect argv from cmd
    if sys.argv and len( sys.argv ) >= 2:
        for opt in sys.argv[ 1: ]:
            if opt[ :2 ] == '-h':
                print( HELP )

                return

            if opt[ :3 ] == '-mp':
                enableMultiProcessing = True

            if opt[ :3 ] == '-d:':
                dataset = opt[ 3: ]

            if opt[ :3 ] == '-i:':
                maxItems = opt[ 3: ]

            if opt[ :3 ] == '-c:':
                maxCategories = opt[ 3: ]

        # collect new dataset
        if dataset != 'dataset'\
            and not os.path.exists( os.path.join( os.getcwd(), dataset ) ):
            Crawl( dataset, maxCategories, maxItems )

    # loop over each category
    for category in os.listdir( os.path.join( os.getcwd(), dataset ) ):
        # ignore unused cases
        if category.find( 'bai-tho' ) < 0: continue

        readLabel = ReadLabel( category, dataset, enableMultiProcessing )

        standardization = Standardization( readLabel[ 0 ] )

        Plot( standardization, readLabel[ 1 ], dataset )

if __name__ == '__main__':
    main()
