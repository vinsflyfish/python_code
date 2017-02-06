#!/usr/bin/python2.6
# -*- coding: utf-8 -*-

# This code is created for crontab to start dead thread
# Author: 		lufyzhang
# Date:	  		20170206
# LastModify:	20170206

import os
import subprocess

def pidof(program_name):
	strResult = os.popen("pidof " + str(program_name)).read()
	strResult = strResult.rstrip('\n')
	print "pidof command:",strResult
	if len(strResult) == 0:
		return 0
	arr = strResult.split(" ")
	print "current thread pid list:",arr
	threadNum = len(arr)
	return threadNum

def checkAlive(program_name,exe_absolute_dir):
	threadNum = pidof(program_name)
	print "thread num:",threadNum
	if threadNum > 0:
		print "thread is alive!"
	else:
		print "thread is not exist, now to start!"
		subprocess.call([exe_absolute_dir])
		threadNum = pidof(program_name)
		print "current thread num is:",threadNum
	return 0

# main function
def run():
	# program_name should not a shell which canot check by pidof 
	program_name = "run"
	# the script to run your program and should not block
	exe_absolute_dir = "./start.sh"
	# start to check
	checkAlive(program_name,exe_absolute_dir)

run()
