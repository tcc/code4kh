# -*- coding: utf-8 -*- 
#
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
import codecs, os, re, simplejson, sys

def valid_raw_file(filename):
    if not os.path.exists(filename):
        print "! ({0}) didn't exised, stop!".format(filename)
        return False
    return True

def uniform_str(str):
    str = str.replace(u'\u3000','')
    str = re.sub(r'"','', str)
    str = re.sub(r'(^\s+|\s+$)','', str)
    str = re.sub(r'\s{2,}',' ', str)
    return str

def html2json(filename):
    outn=basen=os.path.basename(filename)
    dirn=os.path.dirname(filename)
    if outn.find(".")>0:
        outn=outn.split(".")[0]+".json"
    else:
        outn=outn+".json"
    if len(dirn)==0: outfn=outn
    else: outfn=dirn+"/"+outn

    body = codecs.open(filename,'r','utf-8').read()
    hxs = HtmlXPathSelector(text=body)

    roads_lst=[]

    roads = hxs.select('//table[contains(@id,"ctl00_ContentPlaceHolder1_gvIndex")]/tr')
    # road_html=HtmlXPathSelector(text=roads[1].extract())

    for road in roads:
        road_html=HtmlXPathSelector(text=road.extract())
        road_data = road_html.select("//tr/td")

        try:
            if len(road_data)>0 and road_data[0].extract().find('valign')>0:
                road_tmp = []
                for road_cell in road_data:
                    span_html=HtmlXPathSelector(text=road_cell.extract())
                    span_data = span_html.select("//td/span/text()")

                    for span_cell in span_data:
                        road_str=span_cell.extract()
                        road_tmp.append(uniform_str(road_str))
                if len(road_tmp)==4:
                    #print road_tmp
                    road_map={'zh':road_tmp[0], 'en':road_tmp[1], 'type':road_tmp[2], 'unit':road_tmp[3]}
                    roads_lst.append(road_map)

                del road_tmp
        except:
            #print "Unexpected error:", sys.exc_info()[0]
            pass

    if len(roads_lst)>0:
        outf = open(outfn, 'w')
        outf.write(simplejson.dumps(roads_lst,ensure_ascii=False,indent=4 * ' ').encode('utf-8'))
        outf.close()
        #print roads_lst
        print "out json: "+outfn


if __name__ == "__main__":
    for arg in sys.argv[1:]:
        if (valid_raw_file(arg)):
            html2json(arg)


#html2json('/Users/tcchou/w/t/code4ks/RoadNames/raw/test_raw.html')

