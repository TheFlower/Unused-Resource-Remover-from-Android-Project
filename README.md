# Unused-Resource-Remover-from-Android-Project
It helps to reduce size of Android project(.apk files) by removing unnecessary resources (.jpg, .png, .xml, .java) from the android project. 

This python script help to reduce size of android project (.apk file). It removes unused .xml, .java, .jpg and .png files from the Android project. There is two variant of script –

1.	DeleteUnusedFiles.py - It search and delete all unused files in android project.
2.	GetUnsedFiles.py – If search all unused files and create list of files containing paths and names of all unused files.
Caution- Before using DeleteUnsedFiles.py first test with GetUnsedFiles.py to test. Sometimes the script may delete some files which are in used.

Requirements - Python 2.7

Uses – In command line run
C:/ Python DeleteUnusedFiles.py  [path to your Android project directory]
Later it asked the first java files from where your app starts like (splashactivity.java). Enter the class name example -   MainActivity.java.
These scripts automatically search all files in project directory and make a list of all unused files.

If there is any suggestions or error just inform me. 
