from django.http import HttpResponse
from StringIO import StringIO
import json
import xlrd
import urllib
import zipfile

def index(request):
	option = request.GET.get('q', '')
	json_body = {'response': 'Invalid request'}

	def parse_params():
		if option == "add":  add_year(request.GET.get('year', ''))
		pass

	def add_year(year):

		def download_year():
			url = 'http://tennis-data.co.uk/'+year+'/'+year+'.zip'
			return StringIO(urllib.urlopen(url).read())
		
		def unzip():
			zip = zipfile.ZipFile(download_year())
			return zip.extract(year + ".xls")
		
		def process_XLS():
			file = unzip()
			print file

		process_XLS()
			

	def get_matches():
		pass

	parse_params()

	return HttpResponse(json.dumps(json_body), content_type="application/json")