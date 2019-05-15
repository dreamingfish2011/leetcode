#coding:utf-8
import os
import re
movie_name = os.listdir('./')
for temp in movie_name:
    if "No" in temp:
        no = re.match('(.*?)No(.*?)\.py',temp)
        digits = no.group(2)
        name = no.group(1)
        if digits.isdigit():
            new_name = "_"+str(digits)+"_"+name +".py"
            print(new_name)
            os.rename('./'+temp,'./'+new_name)