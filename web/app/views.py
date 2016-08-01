from flask import Response
from app import app
import mmap
import urllib
import logging

file_handler = logging.FileHandler('app.log')
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


@app.route('/')
def index():
	def generate():
		with open("/Users/aayush.rk/Desktop/test.log") as f:
			for row in f.readlines():
				yield row
return Response(generate(), mimetype='text/plain')

