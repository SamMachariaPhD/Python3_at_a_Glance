"""
Unzip a .zip file
Regards, Sam Sirmaxford.
"""

from zipfile import ZipFile
with ZipFile(r'C:\Users\nitta\Downloads\test.zip','r') as zip_ref:
	zip_ref.extractall(r'C:\Users\nitta\Downloads')