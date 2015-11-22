import itertools
#Creating a max numbers of errors
# current number of concecutive dowload errors
num_errors = 0
for page in itertools.count(1):
	url = 'http:://example.webscraping.com/view/-%d' % page
	html = download(url)
	if html = None :
		num_errors +=1
		if num_errors == max_errors:

			breake
	else:
		# success - can scrap the site
		pass
		num_errors = 0
