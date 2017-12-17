#-*- coding: gbk -*-
############
# 20121003 wcdj
# FindFilev0.1
# 遍历目录和搜索文件中的关键字
############

import os
import re
import os.path
rootdir = "/Users/vish23n/dev/code/qunarGit/cesar/cesar-web"                                   # 指明被遍历的文件夹
def getFrom(text):
    text = re.sub('\n', '', text)
    return text
def Tool():
    for parent,dirnames,filenames in os.walk(rootdir):
        # for dirname in  dirnames:
            # print "parent is:" + parent
            # print  "dirname is" + dirname
        outputFile = open("outputFilewrite.txt", "a")
        count = 0
        ddd = ""
        for filename in filenames:
            # print "parent is：" + parent
            # print "filename is:" + filename
            # print "the full name of the file is:" + os.path.join(parent,filename) #输出文件路径信息
            if ".orig" not in filename:
                if ".java" in filename:
                    # print "#########" + filename
                    curfile = open(os.path.join(parent,filename))
                    # print "finding %s..." %(curfile)
                    a = ""
                    b = ""
                    c = ""
                    e = ""
                    f = ""
                    g = ""

                    for line in curfile.readlines():
                        a = b
                        b = c
                        c = e
                        e = f
                        f = g
                        g = line
                        h = a +b +c + e + f + g
                        if "@Controller" not in h:
                            if "@RequestMapping" in g  :
                                if "@Read" not in h:
                                    if "@Write" in h:
                                        outputFile.write("the full name of the file is:" + os.path.join(parent,filename) + "\n")
                                        outputFile.write(h);
                                        count = count +1
                                        outputFile.write( "************************************************************************\n")
                        # print line
                        # print getFrom(line)
                        # outputFile.write(a);
                        # outputFile.write(b);
                        # outputFile.write(c);
                        # outputFile.write(e);
                        # outputFile.write(f);
                        # outputFile.write(h);
                        # outputFile.write(line);
                        # outputFile.write("#############\n");
                        # output = open('abc', 'w+')
                        # output.write(getFrom(line))
                        # output.close()
                        # bFind = "true"
                        # if bFind != "true":
                        #     print "find nothing !"

        # outputFile.write((count));
        # output.close()
        print count
        outputFile.close();



##########
# start
##########
if __name__ == '__main__':

    cdc = Tool()

  
print "End"
