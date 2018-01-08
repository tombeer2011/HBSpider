import string
import json
item = 'This is a demo.\n'
item = item.strip("""\n\r""")

print(item)

jsonText = u'''{"cellInfoList":[{"area":14.88,"boundary":"1452,753,0;1452,1405,0;1017,1405,0;1017,753,0;","face":"&#x5357;","faceIds":"3","id":735661,"name":"&#x5367;&#x5BA4;","roomPics":[],"type":1,"windowTypeName":"&#x666E;&#x901A;&#x7A97;"},{"area":6.41,"boundary":"1017,753,0;1017,472,0;1183,472,0;1452,472,0;1452,753,0;","faceIds":"","id":735662,"name":"&#x5BA2;&#x5385;","roomPics":[],"type":3,"windowTypeName":"&#x666E;&#x901A;&#x7A97;"},{"area":4.48,"boundary":"1183,153,0;1452,153,0;1452,472,0;1183,472,0;","face":"&#x5317;","faceIds":"4","id":735663,"name":"&#x53A8;&#x623F;","roomPics":[],"type":5,"windowTypeName":"&#x666E;&#x901A;&#x7A97;"},{"area":2.78,"boundary":"1017,153,0;1183,153,0;1183,472,0;1017,472,0;","face":"&#x5317;","faceIds":"4","id":735664,"name":"&#x536B;&#x751F;&#x95F4;","roomPics":[],"type":6,"windowTypeName":"&#x666E;&#x901A;&#x7A97;"},{"area":3.08,"boundary":"1452,1405,0;1452,1540,0;1017,1540,0;1017,1405,0;","face":"&#x5357;","faceIds":"3","id":735665,"name":"&#x9633;&#x53F0;","roomPics":[],"type":13,"windowTypeName":"&#x666E;&#x901A;&#x7A97;"}],"isShowAlbum":false,"message":"","status":"ok"}'''
dict1 = dict()
dict1 = json.loads(jsonText)
print('json start')