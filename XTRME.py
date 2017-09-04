from bs4 import BeautifulSoup
import time
import requests
import urllib  
import os

url_list = {
	'9231':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Mathematics - Further (9231)/',
	'9608':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Computer Science (9608)/',
	'9691':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Computing (9691)/',
	'9698':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Psychology (9698)/',
	'9700':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Biology (9700)/',
	'9701':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Chemistry (9701)/',
	'9702':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Physics (9702)/',
	'9706':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Accounting (9706)/',
	'9707':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Business Studies (9707)/',
	'9708':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Economics (9708)/',
	'9709':'http://papers.xtremepapers.com/CIE/Cambridge International A and AS Level/Mathematics (9709)/'
}

def get_papers(url):

	'''download all the files at the url website'''

	# obatin url
	html = requests.get(url)
	soup = BeautifulSoup(html.text,'lxml')
	hrefs = soup.select('td.autoindex_td > a')

	if hrefs == []:
		print('wrong url provided')
		return -1
	hrefs.pop(0)
	print('Now starts to download, this may (defintely) take some times so you may want to go and grab yourself some drink and let this programe run alone.')
	
	#create folder
	folder_path = '.\\'+url.split('/')[-2]+'\\'
	if os.path.isdir(folder_path):
			print('folder {} already exists'.format(folder_path))
			pass
	else:
		print('creating new folder {}'.format(folder_path))
		os.mkdir(folder_path)

	# dowload file	
	for href in hrefs:
		time.sleep(0.5)  # please do not delete this
		href = 'http://papers.xtremepapers.com/'+href.get('href').strip('/.')
		filename = href.split('/')[-1]
		# print(href,filename,sep='-----') # test only

		# if the file already exists
		try:
			with open(folder_path+filename, 'r') as code:
				print('file already exists {}'.format(filename))
				pass
		# otherwise creating new file
		except FileNotFoundError:
			print('detected new file.',end=' ')
			try:
				# try to open new file
				with open(folder_path+filename, 'wb') as code:
					r = requests.get(href)
					code.write(r.content)
					print('successfully downloaded {}'.format(filename))
			# if cannot open/download
			except Exception:
				print('lost connections to the file {} or cannot i/o in the directory provided.'.format(filename))
				pass
	print('successfully downloaded all the files available at {}'.format(url))
	return 0


def main():

	# get code
	print('please provide the syllabus number of the papers you wants to download:', end ='')
	url_key = input()

	if url_key in url_list:
		print('detected syllabus code, processing...')
		get_papers(url_list[url_key])
		
	else:
		print('syllabus code did not detected')
		print('downloading form the website {}'.format(url_key))
		get_papers(url_key)

if __name__ == '__main__':
	main()
