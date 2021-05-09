import os
import time
import requests
import json
from slugify import slugify
from bs4 import BeautifulSoup
from pathlib import Path

total = {}
roundedItemsPerCategory = 500
pwd = ''

def getPoemAndCrawl( thumbDOM, parentDir ):
	aTag = thumbDOM.find( 'a' )
	parsedTitle = aTag.text.split( '–' )

	if len( parsedTitle ) != 2:
		total[ parentDir ][ 'ignoredItems' ].append({
			'name': aTag.text,
			'originalURL': aTag[ 'href' ],
		})

		return 0

	start = time.time()
	reqPoem = requests.get( aTag[ 'href' ] );
	domPoem = BeautifulSoup( reqPoem.text, 'html.parser' )
	entry = domPoem.find( 'div', { 'class': 'entry' } )
	# remove share-post
	entry.find( 'div', { 'class': 'share-post' } ).decompose()

	encodedName = '{}-{:04d}.txt'.format( parentDir, total[ parentDir ][ 'i' ] )
	encodedPath = os.path.join(
		pwd,
		parentDir,
		'{}-{:04d}.txt'.format( parentDir, total[ parentDir ][ 'i' ] )
	)

	total[ parentDir ][ 'i' ] += 1
	total[ parentDir ][ 'items' ].append({
		'content'       : entry.text,
		'title'         : parsedTitle[ 0 ],
		'author'        : parsedTitle[ 1 ],
		'encodedName'   : encodedName,
		'encodedPath'   : encodedPath,
		'originalURL'   : aTag[ 'href' ],
	})

	with open( encodedPath, 'w+' ) as file: file.write( entry.text )

	end = time.time()
	print( '{:2.2f} (ms) - {} - {}'.format( end - start, aTag.text, aTag[ 'href' ] ) )

	return 1

def loopPage( url, page, folderName ):
	URL = f'{ url }/page/{ page }'
	reqPage = requests.get( URL )
	domPage = BeautifulSoup( reqPage.text, 'html.parser' )
	poemsInPage = domPage.findAll( 'h2', { 'class': 'post-box-title' } );

	for thumbDOM in poemsInPage:
		getPoemAndCrawl( thumbDOM, folderName )

	nextPage = domPage.find( 'span', { 'id': 'tie-next-page' } )
	try: return nextPage.find( 'a' ).text
	except: return 0

def loopCat( eachCategory ):
	aTag = eachCategory.find( 'a' )

	if aTag == -1: return 0

	folderName = slugify( aTag.text )

	Path( os.path.join( pwd, folderName ) ).mkdir( parents = True, exist_ok=True )
	total[ folderName ] = { 'i': 0, 'items': [], 'ignoredItems': [] }

	hasLoop = True
	curPage = 1

	while hasLoop and total[ folderName ][ 'i' ] < roundedItemsPerCategory:
		hasLoop = loopPage( aTag[ 'href' ], curPage, folderName )
		curPage += 1

	return 1

def Crawl( newFolder = None ):
	global pwd
	pwd = os.path.join( os.getcwd(), newFolder )
	Path( pwd ).mkdir( parents = True, exist_ok=True )

	r = requests.get( 'https://thuvientho.com/' )
	dom = BeautifulSoup( r.text, 'html.parser' )
	rootCategory = dom.find( 'ul', { 'class': 'menu-sub-content' } )

	# loop over mainpage to get category
	for eachCategory in rootCategory.children:
		loopCat( eachCategory )

	with open( os.path.join( pwd, f'total.txt' ), 'w+' ) as file:
		file.write( json.dumps( total ) )
