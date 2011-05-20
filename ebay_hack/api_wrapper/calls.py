def get_url(operation_name):
    import ConfigParser
    config = ConfigParser.ConfigParser()
    config.read("config.ini")
    app_name = config.get("keys", "app_name")
    return "/services/search/FindingService/v1?OPERATION-NAME=" + operation_name + "&SERVICE-VERSION=1.9.0&SECURITY-APPNAME=" + app_name + "&RESPONSE-DATA-FORMAT=JSON"

def get_response(url, method="GET"):
    from httplib import HTTPConnection
    home = "svcs.sandbox.ebay.com"
    conn = HTTPConnection(home)
    conn.request(method, url)
    resp = conn.getresponse()
    response = resp.read()
    conn.close()
    return response

def getVersion():
    home = r"svcs.sandbox.ebay.com"
    url = get_url("getVersion")
    response = get_response(url)
    return response

def getSearchKeywordsRecommendation(keywords):
    if not keywords:
        print "enter a keyword"
    url = get_url("getSearchKeywordsRecommendation") + ("&keywords=%s" % keywords)
    response = get_response(url)
    return response

def getHistorgrams(categoryId):
    if not categoryId:
        print "enter a categoryId"
        return
    url = get_url("getHistograms") + ("&categoryId=%s" % categoryId)
    response = get_response(url)
    return response

def findItemsByKeywords(kw):
    if not kw:
        print "enter a keyword"
        return
    url = get_url("findItemsByKeywords") + ("&keywords=%s" % kw)
    response = get_response(url)
    return response

def findItemsByProduct(productId):
    if not productId:
        return
    url = get_url("findItemsByProduct") + ("&productId=%s" % productId)
    response = get_response(url)
    return response
