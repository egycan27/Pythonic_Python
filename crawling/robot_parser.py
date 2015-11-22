import robotparser
import crawling
print "Enter the site link"
link = raw_input()
link = "http://www."+link+".com"
print link
rp = robotparser.RobotFileParser()
rp.set_url(link+'/robots.txt')
rp.read()
url = link
user_agent = 'BadCrawler'
print (rp.can_fetch(user_agent,url))

