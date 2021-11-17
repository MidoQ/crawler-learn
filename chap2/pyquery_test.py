"""
使用PyQuery
"""

from pyquery import PyQuery as pq

HTML = '''
<!DOCTYPE html>
<html>
<head></head>
<div>
    <h1>
    This is a header1.
    </h1>
    <ul>
        <li class="item-0">first item</li>
        <li class="item-1"><a href="link2.html">second item</a></li>
        <li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
        <li class="item-1 active"><a href="link4.html">fourth item</a></li>
        <li class="item-0"><a href="link5.html">fifth item</a></li>
    </ul>
    <h2>
    This is a header2.
    </h2>
</div>
</html>
'''

doc = pq(HTML)
print(doc('li'))

# doc = pq(url='https://cuiqingcai.com/')
# print(doc('title'))
