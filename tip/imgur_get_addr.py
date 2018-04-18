import os
import sys
import argparse
import datetime

import pyimgur
import pyperclip

from dotenv import load_dotenv


DOTENV_DIR = '_______'
existDOTENV = os.path.exists(DOTENV_DIR)

# load dot-env file
if existDOTENV:
	load_dotenv(DOTENV_DIR)

def set_parser():
	parser = argparse.ArgumentParser(description="You get imgur url of image(s) with this script!")
	parser.add_argument('path', default=None, help='image path')
	return parser

def check_imgur_client():
	if existDOTENV:
		return os.environ['IMGUR_CLIENT_ID']
	else:
		raise ValueError('You must need imgur client id.')

def check_img_path(args):
	if args.path == None:
		raise ValueError('You must need image path')
	elif not os.path.exists(args.path):
		raise ValueError("\'%s\' not exists" % args.path)
	else:
		return args.path

def get_current_time():
	return '{0:%Y-%m-%dT%H:%M:%S}'.format(datetime.datetime.now())

# ========================
if __name__ == "__main__":
	
	# Check 
	parser = set_parser()
	args = parser.parse_args()

	# get img_path
	img_path = check_img_path(args)
	# get imgur client id
	IMGUR_CLIENT_ID = check_imgur_client()

	# Image Upload
	imgur = pyimgur.Imgur(IMGUR_CLIENT_ID)
	uploaded_img = imgur.upload_image(img_path, title='Uploaded %s' % get_current_time())
	addr = uploaded_img.link

	# Update clipboard
	pyperclip.copy(addr)
	print('Image Upload Success! URL is : %s' % addr)
	print('Press CTRL + V. Your clipboard is already updated!')