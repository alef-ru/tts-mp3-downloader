import urllib
import time
import fileinput

url = r'http://code.responsivevoice.org/getvoice.php?t={line}&tl=en-US'

urllib.URLopener.version = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36 SE 2.X MetaSr 1.0'

print("Type words or phrases each on a new line")
for line in fileinput.input():
	line = line.strip()
	if not line:
		continue
 	filePath = url.format(line = line)
	print("\"{line}\" is being downloaded".format(line=line))	
	urllib.urlretrieve(filePath, line+".mp3") 
	time.sleep(10) # just in case that service may ban me for to many requests