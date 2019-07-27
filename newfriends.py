#!/usr/bin/python

import cgi
import sys
import os
import stat

form=cgi.FieldStorage()
user=form.getvalue("newusers")
id=form.getvalue('id')
print "Content-type:text/html\r\n\r\n"
print '<html>'
print '<body>\r\n'

print '<b>New Friends made!</b>\r\n<br>'
print '<br>'


def unique_list(l):
	ulist = []
	[ulist.append(x) for x in l if x not in ulist]
	return ulist
	

usera = []
for i in user:
	names = i.rstrip()
	usera.append(names)


friendtxt = open('./friends.txt','a+')
s = friendtxt.readlines()
flist = []
firstid = []
abc = None
for line in s:
	clean = line.rstrip()
	flist.append(clean)
	
counter = 0
for word in flist:
	firstid.append(word.split(' ',1)[0] )

check = 0
place = 0
for compare in firstid:
	if (compare == id):
		check = 1;
		break
	else:
		check = 2; 
	place = place +1

#print flist
#print firstid
#print id
#print place

add1 = []
add2 = []

#no previous documents
if (check == 2):
        print"here"
	add2 = [id] + usera
	str1 = " ".join(add2)
	str1 = str1 + '\n'
	friendtxt.write(str1)

###work from here
#print s[place]
#print "check"
if (check == 1):
	add1 = [flist[place]] + usera
	str2 = " ".join(add1)
	str2 = ' '.join(unique_list(str2.split()))
	flist[place] = str2
	
	#print flist[place]
	friendtxt.close()
	f2 = open('/home/2015/yoh7/public_html/friends.txt',"w")
	for parts in flist:
		parts = parts + '\n'		
		f2.write(parts)
		



	#friendtxt.close()
#	f = open('./friends.txt.',"w")
#	for parts in s:
#		if parts != "s[place]"+"\n":
#			f.write(line)
#			f.close
#
#add1 = flist[place] + 
#f2 = open('./friends.txt.',"a+")


print '</body>'
print '</html>'

