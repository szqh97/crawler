#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib2
import BeautifulSoup
import random

#curl command is:
#curl 'http://tu.duowan.com/m/bxgif?offset=60&order=created&math=0.8618605642657563' -H 'Host: tu.duowan.com' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0' -H 'Accept: application/json, text/javascript, */*; q=0.01' -H 'Accept-Language: en-US,en;q=0.5' -H 'Accept-Encoding: gzip, deflate' -H 'X-Requested-With: XMLHttpRequest' -H 'Referer: http://tu.duowan.com/m/bxgif' -H 'Cookie: hdo_ui=0.9203390055920907; 20150823statistics=2kforotam6; Hm_lvt_4941f2298273634934f789da00bbabe0=1440303312,1440303442,1440303466,1440336345; BA=l=313&le=166.06&ip=; Hm_lpvt_4941f2298273634934f789da00bbabe0=1440336345' -H 'Connection: keep-alive'

headers = {'Host': 'tu.duowan.com',
'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0',
'Accept': 'application/json, text/javascript, */*; q=0.01',
'Accept-Language': 'en-US,en;q=0.5',
'Accept-Encoding': 'gzip, deflate',
'X-Requested-With': 'XMLHttpRequest',
'Referer': 'http://tu.duowan.com/m/bxgif',
'Cookie': 'hdo_ui=0.9203390055920907; 20150823statistics=2kforotam6; Hm_lvt_4941f2298273634934f789da00bbabe0=1440303312,1440303442,1440303466,1440336345; BA=l=313&le=166.06&ip=; Hm_lpvt_4941f2298273634934f789da00bbabe0=1440336345',
'Connection': 'keep-alive'}


duowan_url = 'http://tu.duowan.com/m/bxgif?offset=%d&order=created&math=%s'




