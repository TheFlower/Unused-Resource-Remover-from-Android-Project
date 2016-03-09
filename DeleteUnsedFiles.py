#!/usr/bin/env python


__author__      = "Jayant Gupta"


import os
import re
import sys
import csv
import os.path

""" delete unnecessary Image files, xml files , java class files from android project"""

#Global variables.
all_jp_files = set()     # set to store all jpg image file path
all_drawble_files = set()  #set to store all png file path
used_drawable_files = set()
files_deleted = 0
mega_bytes_deleted = 0
filestobedelated = []
javafiles = []                 #all java files
xmlfiles = []					# all xml files
xmlnewfiles = []
layoutpath=""
pathtojavaclass =""
javafileswithoutpath =[]

newusedclass = []
newusedxmlfile = []
newusedimagefile = []
newusedjpgfile = []
newusedpngfile = []
allfiles =[]

animxmlfile=[]     ##all anim
unsedanimfile =set()    ## all anim files

xmlfileindrawable = []

unsedjavafiles = set()
unsedxmlfiles = set()
unsedjpgfiles = set()
unsedpngfiles = set()


i=1
j=1

#Naive method to determine if a directory is an android /res folder.
def isResourceRoot(directory):
  return (
  (os.path.exists(directory+"/drawable"))        or
  (os.path.exists(directory+"/drawable-ldpi"))   or
  (os.path.exists(directory+"/drawable-mdpi"))   or
  (os.path.exists(directory+"/drawable-hdpi"))   or
  (os.path.exists(directory+"/drawable-xhdpi"))  or
  (os.path.exists(directory+"/drawable-xxhdpi")) or
  (os.path.exists(directory+"/drawable-xxxhdpi")))

#We only want to remove unused PICTURES (pngs)
def addFile(fileName):
  global j
  fileName = fileName.replace("R.drawable.", "").replace("@drawable/","")
  used_drawable_files.add(fileName)
  ufile=[]
  ufile.append(j)
  ufile.append(fileName)
  writernew.writerow(ufile)
  j=j+1
  

#Check to see what resources are referenced in this function.
def checkFileForResources(fileAsString):
  global newusedclass
  global newusedimagefile
  global newusedxmlfile
  global allfiles
  global xmlfiles
  global pathtojavaclass
  global javafiles
  global newusedjpgfile
  global newusedpngfile
  global all_jp_files
  global xmlfileindrawable
  global unsedanimfile
  #print "filepath to cheak"
  #print fileAsString
  if os.path.isfile(fileAsString):
	file = open(fileAsString, 'r')
	contents = file.read()
	file.close()
  else:
	return
	

  #Handle code files.
  pattern = re.compile('R\.drawable\.[a-zA-Z0-9_]*')
  results = pattern.findall(contents)
  for result in results:
	newusedimagefile.append(result)
	used_drawable_files.add(result)
	result =result.replace("R.drawable.","")
	#print "start png"
	for temp3 in all_drawble_files:
		#print temp3
		#print result
		#print temp3.find(result)
		if temp3.find(result) <> -1 :
			#print "found jpg file"
			if newusedpngfile.count(temp3) ==0:
				newusedpngfile.append(temp3)
	for temp3 in all_jp_files:
		#print temp3
		#print result
		#print temp3.find(result)
		if temp3.find(result) <> -1 :
			#print "found jpg file"
			if newusedjpgfile.count(temp3) == 0:
				newusedjpgfile.append(temp3)
				
	xmlfile1 = result + ".xml"
		#print xmlfile1
	for file2 in xmlfiles:
		if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
			if newusedxmlfile.count(file2)==0:
				newusedxmlfile.append(file2)
				allfiles.append(file2)
				
   #Handle code files.
  #pattern = re.compile('R\.id\.[a-zA-Z0-9_]*')
  pattern = re.compile('R\.idvvrgecececer\.[a-zA-Z0-9_]*')
  results = pattern.findall(contents)
  
  for result in results:
	newusedimagefile.append(result)
	used_drawable_files.add(result)
	
	result =result.replace("R.id.","")
	
	#print "start png"
	for temp3 in all_drawble_files:
		#print temp3
		#print result
		#print temp3.find(result)
		if temp3.find(result) <> -1 :
			#print "found jpg file"
			if newusedpngfile.count(temp3) ==0:
				newusedpngfile.append(temp3)
	for temp3 in all_jp_files:
		#print temp3
		#print result
		#print temp3.find(result)
		if temp3.find(result) <> -1 :
			#print "found jpg file"
			if newusedjpgfile.count(temp3) == 0:
				newusedjpgfile.append(temp3)
				
	xmlfile1 = result + ".xml"
		#print xmlfile1
	for file2 in xmlfiles:
		if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
			if newusedxmlfile.count(file2)==0:
				newusedxmlfile.append(file2)
				allfiles.append(file2)

				#code end here
  #Handle layout files.
  pattern = re.compile('@drawable/[a-zA-Z0-9_]*')
  results = pattern.findall(contents)
  for result in results:
	newusedimagefile.append(result)
	used_drawable_files.add(result)
	result =result.replace("@drawable/","")
	if result.find("wallet") <> -1:
		print result
	#print result
	#print "start jpg"
	for temp3 in all_drawble_files:
		#print temp3
		#print result
		#print temp3.find(result)
		if temp3.find(result) <> -1 :
			#print "found jpg file"
			if newusedpngfile.count(temp3) == 0:
				newusedpngfile.append(temp3)
	for temp3 in all_jp_files:
		#print temp3
		#print result
		#print temp3.find(result)
		if temp3.find(result) <> -1 :
			#print "found jpg file"
			if newusedjpgfile.count(temp3)==0:
				newusedjpgfile.append(temp3)
	
	xmlfile1 = result + ".xml"
		#print xmlfile1
	for file2 in xmlfiles:
		if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
			if newusedxmlfile.count(file2)==0:
				newusedxmlfile.append(file2)
				allfiles.append(file2)
				#allfiles.append(temp3)

#Handle class files.
  pattern = re.compile('[a-zA-Z0-9_]*\.class')
  results = pattern.findall(contents)
  for result in results:
	#print "plase see" 
	#print result
	result = result.replace(".class",".java")
	#search class file in java class list
	#print result
	#print "12345"
	filetoadd=""
	for temp in javafiles:
		#print temp
		#print result
		if temp.endswith(result):
			#print "found"
			#print temp
			filetoadd=temp
			#print filetoadd
			break
	#iletoadd = pathtojavaclass + '/' + result
	#print "##file##"
	#print filetoadd
	#newusedclass.append(filetoadd)
	#filetoadd = filetoadd.replace(".class" , ".java")
	#check if file is already processed , if not then only add to allfiles
	#print "process"
	#print filetoadd
	#print allfiles
	#print newusedclass
	if newusedclass.count(filetoadd) == 0:
		#print "inside to add file"
		newusedclass.append(filetoadd)
		allfiles.append(filetoadd)

	#handle other java files whose object are created check individual files in existing class file
  	
#Handle xml file files.
  pattern = re.compile('R\.layout\.[a-zA-Z0-9_]*')
  #print "xml file found"
  results = pattern.findall(contents)
  #print results
  for result in results:
		#newusedxmlfile.append(result)
		#print result
		result = result.replace("R.layout.","")
		xmlfile1 = result + ".xml"
		#print xmlfile1
		for file2 in xmlfiles:
			if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
				if newusedxmlfile.count(file2)==0:
					newusedxmlfile.append(file2)
					allfiles.append(file2)
				#break
	

#Handle xml file files.
  pattern = re.compile('R\.anim\.[a-zA-Z0-9_]*')
  #print "xml file found"
  results = pattern.findall(contents)
  #print results
  for result in results:
		#newusedxmlfile.append(result)
		#print result
		result = result.replace("R.anim.","")
		xmlfile1 = result + ".xml"
		#print xmlfile1
		for file2 in xmlfiles:
			if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
				if newusedxmlfile.count(file2)==0:
					newusedxmlfile.append(file2)
					allfiles.append(file2)
				#break	
  #Handle xml file files.
  pattern = re.compile('@layout/[a-zA-Z0-9_]*')
  #print "xml file found"
  results = pattern.findall(contents)
  #print results
  for result in results:
		#newusedxmlfile.append(result)
		#print result
		result = result.replace("@layout/","")
		xmlfile1 = result + ".xml"
		print xmlfile1
		for file2 in xmlfiles:
			if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
				if newusedxmlfile.count(file2)==0:
					newusedxmlfile.append(file2)
					allfiles.append(file2)
				#break
  #handle other java files whose object are created check individual files in existing class file
  for javaall in javafileswithoutpath:
	pattern = re.compile(javaall)
	results = pattern.findall(contents)
	if len(results) > 0:
		r=results[0]
		for ar in javafiles:
			rq=r+".java"
			#print rq
			if ar.endswith(rq):
				if newusedclass.count(ar)==0:
					allfiles.append(ar)
					newusedclass.append(ar)
					#print "98765432"
					#print ar
					#print "java class is added to newusedclass"
		
	#print "another java class files"
	#print results
	
	#Handle xml file  drawble.
  pattern = re.compile('R\.drawable\.[a-zA-Z0-9_]*')
  #print "xml file found"
  results = pattern.findall(contents)
  #print results
  for result in results:
		#newusedxmlfile.append(result)
		#print result
		result = result.replace("R\.drawable.","")
		xmlfile1 = result + ".xml"
		#print xmlfile1
		for file2 in xmlfiles:
			if file2.endswith(xmlfile1):
				#print "found"
				# first cheack its exist in newusedxmlfile
				if newusedxmlfile.count(file2)==0:
					newusedxmlfile.append(file2)
					allfiles.append(file2)
				#break
  
	#print results
		

#We only want to if it's an unreferenced PNG.
def deleteIfUnusedPNG(directory, fileName):
    if fileName.endswith(".png"):
      fileNameWithoutExt = os.path.splitext(fileName)[0]
      if fileName.endswith(".9.png"):
        fileNameWithoutExt = os.path.splitext(fileNameWithoutExt)[0]
      if fileNameWithoutExt not in used_drawable_files:
		global files_deleted
		global mega_bytes_deleted
		global i
        #Do stats tracking.
		files_deleted += 1
		current_file_size = os.path.getsize(directory+"/"+fileName) / 1024.0 / 1024.0
		mega_bytes_deleted += current_file_size

        #Actually delete the file.
        ##os.unlink(directory+"/"+fileName)
		#print ("Deleted (%.2f Mbs): " + directory+"/"+fileName) % current_file_size
		#print "file detected " + directory+"/"+fileName
		fileppath = directory+"/"+fileName
		a=[]
		a.append(i)
		i=i+1
		a.append(fileppath)
		writer.writerow(a)

##########
## MAIN ##
##########

#Make sure they passed in a project source directory.
if not len(sys.argv) == 2:
  print 'Usage: "python DeleteUnsed.py project_src__main_directory"'
  print "Enter the class files name correspond to mainactivity xml file, "
  print "java files name which is set main launcher file in Manifest file"
  print "example:  MainActivity.java"
  quit()

print "enter the  Main Activity Class name, from where search has to start"
print "example :   MainActivity.java"
str = raw_input("enter class name\n");
str="MainActivity.java"                       # starting class file name
str ="SplashActivity.java"

rootDirectory = sys.argv[1]
resDirectory = rootDirectory
fo = open("abc.csv","wb")
fi = open ("used.csv","wb")
writer = csv.writer(fo)
writernew = csv.writer(fi)
i=1
j=1

drawable_mdpi_path =""
drawable_hdpi_path =""
drawable_xdpi_path =""
drawable_xxdpi_path =""
drawable_path =""
drawable_ldpi_path =""
drawable_sw600dp_path=""
drawable_path_list=[]
animpath =""

#Figure out which resources are actually used.
for root, dirs, files in os.walk(rootDirectory):
	#global javafiles
	#sglobal xmlfiles
	#print root
	#print root
	#print dirs
	if root.endswith("res\layout"):
		#print root
		layoutpath=root
		
	if root.endswith("res\drawable"):
		#print root
		drawable_path=root
		drawable_path_list.append(root)
	if root.endswith("res\\anim"):
		animpath=root
		print "**************"
		print root
		print animpath
		
	if root.endswith("res\drawable-hdpi"):
		#print root
		drawable_hdpi_path=root
		drawable_path_list.append(root)
	if root.endswith("res\drawable-ldpi"):
		#print root
		drawable_ldpi_path=root
		drawable_path_list.append(root)
	if root.endswith("res\drawable-sw600dp"):
		#print root
		drawable_sw600dp_path=root
		drawable_path_list.append(root)
	if root.endswith("res\drawable-xhdpi"):
		#print root
		drawable_xdpi_path=root
		drawable_path_list.append(root)
	if root.endswith("res\drawable-xxhdpi"):
		#print root
		drawable_xxdpi_path=root
		drawable_path_list.append(root)
	if root.endswith("res\drawable-mdpi"):
		#print root
		drawable_mdpi_path=root
		drawable_path_list.append(root)
	
	
	
	for file in files:
		if file.endswith(".java"):
			javafiles.append(root+"/" +file)
			jfile = file.replace(".java","")
			javafileswithoutpath.append(jfile)
			pathtojavaclass=root+""
			#print "path find isto****************8888"
			#print root
		if file.endswith(".xml"):
			xmlfiles.append(root+"/" +file)
		if file.endswith(".png"):
			all_drawble_files.add(root+"/"+file)
		if file.endswith(".jpg"):
			all_jp_files.add(root+"/"+file)         #all  .jpg files are added to set all_jp_files
	if isResourceRoot(root):
		resDirectory = root
	#for file in files:
		#checkFileForResources(root+"/"+file)    ##calling method
		#print "sorryy"
	
#print "start123"	
#print 
#print javafiles
#print xmlfiles

for root, dirs, files in os.walk(layoutpath):
	#global xmlnewfiles
	for file in files:
		if file.endswith(".xml"):
			xmlnewfiles.append(root+"/" +file)   ## all xml files have to searched


			
for root, dirs, files in os.walk(animpath):   # for anim folder
	#global xmlnewfiles
	for file in files:
		if file.endswith(".xml"):
			animxmlfile.append(root+"/" +file)   ## all xml files have to searched
			xmlnewfiles.append(root+"/" +file) 
			
for pathnew in drawable_path_list:			
	for root, dirs, files in os.walk(pathnew):
		#global xmlnewfiles
		for file in files:
			if file.endswith(".xml"):
				xmlnewfiles.append(root+"/" +file)
				xmlfileindrawable.append(root+"/" +file)


#Delete the unused pngs.
#for root, dirs, files in os.walk(resDirectory):
#    for file in files:
#      deleteIfUnusedPNG(root, file)

#hardcoding for android manifest file and image used in manifest files
manifestfile = "AndroidManifest.xml"
stylefile ="styles.xml"
stylepath = []
manipath = ""
for file in xmlfiles:
	if file.endswith(manifestfile):
		manipath=file
	if file.endswith(stylefile):
		stylepath.append(file)

print "test222"
print stylepath
#quit()
newusedxmlfile.append(manipath)
for sfile in stylepath:
		allfiles.append(sfile)
		newusedxmlfile.append(sfile)
classpath = ""
for file in javafiles:
	if file.endswith(str):
		classpath=file
	
	
#print "class path"	
#print classpath
allfiles.append(classpath)
#print allfiles
#print "start allfile"

while len(allfiles)>0:
	afile = allfiles.pop()
	#print "files poped out"
	#print afile
	newusedclass.append(afile)
	checkFileForResources(afile)
	
#for afile in allfiles:
#	print "3333333333333333333"
#	checkFileForResources(afile)
#	index=allfiles.find(afile)
#	allfiles.remove(index)

#print "used class file"
#print newusedclass
#print "java class path"
#print pathtojavaclass
#Print out how many files were actually deleted.
#print "saving path for java files"
filejava = open("javafiles.csv","wb")
filewriter = csv.writer(filejava)
p=1
for tempfile in newusedclass:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1
	
filejava2 = open("alljavafiles.csv","wb")
filewriter = csv.writer(filejava2)
p=1
for tempfile in javafiles:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1
	
filexml = open("xmlfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in newusedxmlfile:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1	

filexml = open("allxmlfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in xmlnewfiles:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1	
	
filexml = open("usedimage.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in used_drawable_files:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1
	
filexml = open("allimage.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in all_drawble_files:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1
	
	
filexml = open("usedpngfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in newusedpngfile:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	p=p+1

for temp5 in all_jp_files:
		if newusedjpgfile.count(temp5)==0:
			#print "unsed file"
			unsedjpgfiles.add(temp5)
#print unsedjavafiles
for temp5 in all_drawble_files:
		if newusedpngfile.count(temp5)==0:
			#print "unsed jpg file"
			unsedpngfiles.add(temp5)
for temp5 in javafiles:
		if newusedclass.count(temp5)==0:
			#print "unsed jpg file"
			unsedjavafiles.add(temp5)
for temp5 in xmlnewfiles:
		if newusedxmlfile.count(temp5)==0:
			#print "unsed jpg file"
			unsedxmlfiles.add(temp5)
			
for temp5 in animxmlfile:
	if newusedxmlfile.count(temp5)==0:
		#print "unsed jpg file"
		unsedanimfile.add(temp5)
#print unsedjpgfiles
#print unsedpngfiles
#print unsedjavafiles
#print unsedxmlfiles

filexml = open("usedanimfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in animxmlfile:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	#os.unlink(tempfile)
	p=p+1

filexml = open("unusedanimfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in unsedanimfile:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	os.unlink(tempfile)
	p=p+1

filexml = open("unusedjavafiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in unsedjavafiles:
	q=[]
	q.append(p)
	q.append(tempfile)
	filewriter.writerow(q)
	os.unlink(tempfile)
	p=p+1
filexml = open("unusedpngfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in unsedpngfiles:
	q=[]
	q.append(p)
	q.append(tempfile)
	os.unlink(tempfile)
	filewriter.writerow(q)
	p=p+1
filexml = open("unusedxmlfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in unsedxmlfiles:
	q=[]
	q.append(p)
	q.append(tempfile)
	os.unlink(tempfile)
	filewriter.writerow(q)
	p=p+1
filexml = open("unusedjpgfiles.csv","wb")
filewriter = csv.writer(filexml)
p=1
for tempfile in unsedjpgfiles:
	q=[]
	q.append(p)
	q.append(tempfile)
	os.unlink(tempfile)
	filewriter.writerow(q)
	p=p+1
print ""
print "end of execution"
