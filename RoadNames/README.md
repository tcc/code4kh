Preparations
==================================
1. 準備 [Python](http://python.org/), [virtualenv](http://pypi.python.org/pypi/virtualenv)。
2. 準備資料。

    - 建立一個 out/ 目錄。
    - 請參考 [道路地名英譯](http://www.kcg.gov.tw/CP.aspx?n=56973F3DBA0F5999&s=9932698DDE87221B), `道路地名英譯` 連結。
    - 目前資料 5086 筆。
    - 使用瀏覽器逐頁存到 out/*.html。
    - 每頁設為 600 筆, 存成 rnis[1..9].html 9 個檔案。


Files
==================================
1. dump_json.py 把 html 內的資料取出, 轉為 json。
2. dump_xls.py 把 JSON 資料全部整合成為一個 xls。
3. README.md 這個說明檔案。
4. requirements.txt 執行時需要 Python Libs。


Libraries
==================================
請參考 requirements.txt

    Scrapy==0.16.4
    Twisted==12.3.0
    lxml==3.1beta1
    pyOpenSSL==0.13
    simplejson==3.0.7
    tabledown==0.1
    w3lib==1.2
    wsgiref==0.1.2
    xlrd==0.8.0
    xlwt==0.7.4
    zope.interface==4.0.3


Executions
==================================
1. 設置環境 (大約 2~5 分鐘)

    	$ cd RoadNames
	    $ virtualenv --no-site-packages rt
	    $ source rt/bin/activate
	    $ pip install -r requirements.txt

2. 從 HTML 產生 JSON

	    $ cd out
	    $ python ../dump_json.py *html

3. 從 JSON 產生 xls

    	$ python ../dump_xls.py *json
	    (以第一個 json 檔案為 xls 主檔名)

***