#!coding:utf-8
'''
Created on 2010-9-1

@author: Zhoulin
'''

import re

#all Chinese paired characters
pairedSymbols = ((u'\u300A', u'\u300B'),(u'\u3008', u'\u3009'))
                #(u'\u300C', u'\u300D'), (u'\u300E', u'\u300F'), (u'\u2018', u'\u2019'), (u'\u201C', u'\u201D'),\
                #  (u'\uFF08', u'\uFF09'), (u'\u3014', u'\u3015'), (u'\u3010', u'\u3011'), )

#RegNonEnglishChars = re.compile(ur'[\u002B]')
#RegNonEnglishChars = re.compile('[^\u002B\u0020-\u002F\u003A-\u0040\u005B-\u0060\u007B-\u007E]')
#RegNonChineseChars = re.compile("""[^\u3002\uFF1F\uFF01\uFF0C\u3001\uFF1A\uFF1B\u300C-\u300F\u2018\u2019\u201C\u201D
#                                  \uFF08\uFF09\u3014\u3015\u3010\u3011\u2014\u2026\u2013\uFF0E\u300A\u300B\u3008\u3009]""")

RegNonEnglishChars = re.compile(r'\W')
RegNonChineseChars = re.compile(ur'[\u4e00-\u9fa5]')
RegNonSpacesChars = re.compile(r'[^\s]')
def RemoveAllChineseSigns(rawString = u''):
    return ''.join(RegNonChineseChars.findall(rawString))
    
def RemoveAllEnglishSigns(rawString = u''):
    return ''.join(RegNonEnglishChars.findall(rawString))

def RemoveAllSigns(rawString = u''):
    return RemoveAllEnglishSigns(RemoveAllChineseSigns(rawString))

def LCS(str1 = "", str2 = ""):
    """
    This methods receive two candidate strings and output their longest common substring length
    """
    if None == str1 or None == str2:
        return
    len1 = len(str1)
    len2 = len(str2)
    MinLen = min(len1, len2)
    
    Ret = [[0 for i in range(len2 + 1)] for j in range(len1 + 1)]
    
    Ret[0][0] = 0;
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            if str1[i - 1] == str2[j - 1]:
                Ret[i][j] = Ret[i - 1][j - 1] + 1;
            else:
                Ret[i][j] = max(Ret[i - 1][j], Ret[i][j - 1])
    
    if len1 == 0 or len2 == 0: return 0
    print len1, "---", len2
    return float(Ret[len1][len2]) / float(MinLen)

def ExtractNumber(rawString, fraction = True):
    """
    fraction == true --> real number
    fraction == false --> integer number
    """
    
    if fraction == True:
        regSyntax = r'[+-]?[0-9]+((,\d\d\d)+)?(\.[0-9]+)?'
    else:
        regSyntax = r'[+-]?[0-9]+'
    
    regSearch = re.compile(regSyntax)
    m = regSearch.search(rawString)
    if m:
        number = m.group()
        number = number.replace(',', "")
    else:
        number = ""
    
    return number

def ConcertTypeDescide(rawString1, rawString2, city):
    #concert type, need to strip following noises:
    #1.place
    #2.all numbers (mostly time)
    #3.type key words such as '演唱会'
    #our goal is intended to left the singer's name
    
    #delete type name
    rawString1 = rawString1.replace(u'演唱会'.decode('utf-8'), '')
    rawString2 = rawString2.replace(u'演唱会'.decode('utf-8'), '')
    
    #delete place name
    rawString1 = rawString1.replace(city, "")
    rawString2 = rawString2.replace(city, "")
    
    #delete digital numbers
    rawString1 = ''.join(re.findall(r'[^\d]+', rawString1))
    rawString2 = ''.join(re.findall(r'[^\d]+', rawString2))
    
    return LCS(rawString1, rawString2)
    
def IsWrappedBySymbols(rawString):
    #find symbols that are surrounded by some symbols
    print rawString
    regulerExpr = "(?<=%s).+?(?=%s)"
    for each in pairedSymbols:
        expr1 = regulerExpr % (each[0], each[1])
        keywordsReg = re.search(expr1, rawString)
        if keywordsReg:
            return True
    
    return False

def ExtractKeyWordsFromPairedSymbols(rawString):
    #find symbols that are surrounded by some symbols
    regulerExpr = ur"(?<=%s).+?(?=%s)"
    for each in pairedSymbols:
        keywordsReg = re.search(regulerExpr%(each[0], each[1]), rawString)
        if keywordsReg:
            return keywordsReg.group()
    
    return None

def KeyWordMatching(keyword, rawString):
    keyword = RemoveAllSigns(keyword)
    rawString = RemoveAllSigns(rawString)
    return LCS(keyword, rawString)  

def TypeDispatch(rawString1, rawString2, city):
    #different type of activity has different formats
    #these formats should be orthogonal
    rawString1 = RemoveAllSigns(rawString1)
    rawString2 = RemoveAllSigns(rawString2)
    if rawString1.find(u'演唱会'.decode('utf-8')) != -1 or rawString1.find(u'演唱会'.decode('utf-8'))!= -1:
        return ConcertTypeDescide(rawString1, rawString2, city)
    
    return -1    
