#!/usr/bin/python
# -*- coding: utf-8 -*-
# file:missingEpisodes.py

# Copyright (C) 2008 Damjan Dimitrioski <damjandimitrioski@gmail.com>
# missingEpisodes.py is part of missingEpisodes.

#    missingEpisodes is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    missingEpisodes is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with missingEpisodes.  If not, see <http://www.gnu.org/licenses/>.

from glob import glob
from re import split
from os.path import splitext
from os.path import join
from os.path import basename
from os.path import exists
from sys import argv

import locale
import gettext



#lokal = locale.getlocale()[0]

#locale.setlocale(locale.LC_ALL, 'en_US.utf8')

#lokal = locale.getlocale()
#print (lokal)
#"""
localedir = '/usr/share/locale'
APP_NAME="missingEpisodes"

gettext.bindtextdomain(APP_NAME, localedir)
gettext.textdomain(APP_NAME)

_ = gettext.gettext

#msg1 = _("Постојат: %s.")
msg1 = _("Existing: %s.")

#msg2 = _("Недостигаат: %s.")
msg2 = _("Missing: %s.")

msg3 = _("They're: \n")
#msg3 = _("Тие се: \n")


help = _("""
	Usage:	%s path startPattern min max extension debug ...
		The program is used to find missing "episodes" in a folder.

		path		- put the folder path, else put .
		startPattern	- the pattern sequence of the files, 
				  e.g: fooEdition2:Section5
		min		- starting point.
		max		- ending point.
		extension	- the file extension e.g ogm, "*" for all types
		debug		- writes extended (eat my ass) data.
		-h, --help      - display this help and exit
""")
help = help % basename (argv[0])
#-?, --help                      Покажи ги сите опции за помош
path		= None
key		= None
videoTypes	= None
episodesNMin	= None
episodesNMax	= None


debug = False

try:
	if argv[6] == "-d":
		debug = True
except:	""


numbers		= []
episodes	= []
missing		= []
found		= []


_path = None

def dummyList():
	# Generating numbers from 1 to episodesN and formating them with 0 as prefix if < 10

	for i in range (episodesNMin, episodesNMax+1):
		if i < 10:
			numbers.append("0"+str(i))
		else:
			numbers.append(str(i))
	#print files
	#print len(files)

def cleanEpisodes():
	for ep in files:
		nobase	= basename (ep)
		noext	= splitext(nobase) [0]
		#print 2 * "-"
		#print "noext=%s" % noext
		#print "key=%s" % key
		_split = split(key, noext)[1]
		#print "split=%s" % _split
		episodes.append(_split)

def compareEpisodes():
	for num in numbers:
		#print num
		if num in episodes:
			if (debug):	print ("Епизода %s постои" % (num))
			found.append(num)

		else:
			if (debug):print ("Епизода %s не постои" % (num))
			missing.append(num)

def printData():
	global videoTypes
	totalM = len(missing)
	print (20*"=")
	print (msg1 % len(found))
	print (msg2 % totalM)
	print ("\t" + msg3)
	print ("\t" + 20*"=")
	id = 1
	if videoTypes == "*":	videoTypes=""
	#"""
	for miss in missing:
		print ("\t%d: %s%s%s.%s%s" % (id, path, key, miss, videoTypes, ""))
		id+=1
	#"""

def main():
	global path, key, episodesNMin, episodesNMax, videoTypes, _path, files
	try:
		path		= argv[1]
		if path =="":
			raise NameError ('Wrong path for argument 1')

	except NameError:
		raise
		print (help)

	finally:
		key		= argv[2]
		episodesNMin	= int(argv[3])
		episodesNMax	= int(argv[4])
		videoTypes	= argv[5]
		_path = join(path, "*."+videoTypes)
		files = glob(_path)
		dummyList()
		cleanEpisodes()
		compareEpisodes()
		printData()		

if __name__ == "__main__":
	if argv[1] == "--help" or argv[1] == "-h":
		print (help)
	else:
		main()

