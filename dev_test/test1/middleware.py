from datetime import datetime
#import requests
from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
import time

class usermiddleware(object):
	def __init__(self):
		self.temp = datetime.now()
		

	def process_request(self,request):
		request.start_time = time.time()
		
	def process_response(self, request,response):
		duration = time.time() - request.start_time
		print "*"*30
		print int (duration * 1000)
		print "*"*30
		return response
		