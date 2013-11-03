'''
	Basic web crawler.

	Jordi Walter Hoock Castro.
'''
import re, urllib.request as url, random

class Crawler:
	"""
		Crawler class.
	"""
	
	page 			=	 ""
	sites 			= 	[]
	validUrls		= 	[]
	visitedSites 	= 	[]
	actualSite 		= 	0
	logLevel 		= 	0

	def __init__ ( self, page ):
		"""
			-Var page: In what page start to crawl.
		"""
		c 			= 0
		self.page 	= page

		while ( True ):
			self.parseSiteText()
			self.parseUrls()
			self.checkUrls()
			self.changeSite()
			print( "Iteration: %i, Site: %s" % (c, self.page) )
			c += 1

	def parseSiteText ( self ):
		""" 
			Convert site to plain text.
		"""

		# Here is a bug, FUCK!
		try:
			site = url.urlopen(self.page)
		except IOError as e:
			self.changeSite()
			self.__init__(self.page)

		self.page = str(site.read())

	def parseUrls ( self ):
		"""
			Find all urls in the site and add them into a array.
		"""
		# Thanks for the pattern stackoverflow, i adapted the pattern to my needs.
		self.sites = re.findall(r"<a.*?\s*href=\"(.*?)\".*?>(.*?)</a>", self.page)

	def checkUrls ( self ):
		"""
			Check sanity of the urls.
		"""
		# Thanks for the pattern stackoverflow, i adapted the pattern to my needs.
		checkPattern = '^(http|https|)://[a-zA-Z0-9\-\.]+\.(com|org|net|mil|edu|COM|ORG|NET|MIL|EDU|es)([/a-zA-Z0-9]+?.?(htm|php|asp|html)?)?$'
		for links in self.sites:
			if(re.search(checkPattern, links[0])):
				self.validUrls.append(links[0])

	def changeSite ( self ):
		"""
			Get random site from our array.
		"""

		# Have we already visited this site?.
		x = random.randint(0, len(self.validUrls)-1)
		while ( x in self.visitedSites ):
			x = random.randint(0, len(self.validUrls)-1)

		self.actualSite = x
		self.visitedSites.append(x)
		self.page = self.validUrls[x]
		
	def l ( self, level ):
		"""
			Get log of what is happening.

			-Var level:
				1: Print all.
				2: Print target site.
				3: Write sites to external file [APPEND].
		"""

		if 	 ( level == 1 ):
			pass
		elif ( level == 2 ):
			pass
		else:
			f = open('log', 'a')
			f.write("\n"+self.page)