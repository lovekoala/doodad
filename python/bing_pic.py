import urllib
html_url = 'http://www.bing.com'
html_content = urllib.urlopen(html_url).read()
prefix = "g_img={url:'"
picurl_start = html_content.find(prefix)+len(prefix)
postfix = "jpg"
picurl_end = html_content.find(postfix,picurl_start) + len(postfix)
picurl = html_content[picurl_start:picurl_end]
urllib.urlretrieve(picurl, picurl[picurl.rfind("/")+1:])

