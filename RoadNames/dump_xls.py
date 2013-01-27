# -*- coding: utf-8 -*- 
#
# test raw/foo.raw
from tabledown.tdxls import TDXls
import codecs, os, re, simplejson, sys

mcc = {
     '_':['roads'],
     'roads':{
         '*':{
             'zh':['A1',u'中文'],
             'en':['B1',u'英文'],
             'type':['C1',u'類型'],
             'unit':['D1',u'單位'],
         },
     },
 }

def valid_raw_file(filename):
    if not os.path.exists(filename):
        print "! ({0}) didn't exised, stop!".format(filename)
        return False
    return True

def consolidate_json(lst, filename):
    inf = codecs.open(filename, 'r', 'utf-8')
    in_lst = simplejson.load(inf)
    inf.close()
    lst = lst + in_lst
    return lst

if __name__ == "__main__":
    c_lst=[]

    for arg in sys.argv[1:]:
        if (valid_raw_file(arg)):

            outn=basen=os.path.basename(sys.argv[1])
            dirn=os.path.dirname(sys.argv[1])
            if outn.find(".")>0:
                outn=outn.split(".")[0]+".xls"
            else:
                outn=outn+".xls"
            if len(dirn)==0: outfn=outn
            else: outfn=dirn+"/"+outn

            c_lst = consolidate_json(c_lst, arg)

    print "out xls: "+outfn
    tdx = TDXls(mcc)
    tdx.dict2xls({'roads':c_lst}, outfn)


#html2json('/Users/tcchou/w/t/code4ks/RoadNames/raw/test_raw.html')

