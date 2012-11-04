import datetime
import re
import rfc3339
import urllib
import xml.dom.minidom


def agenda():
    try:
        results = ""
        URL = open("calxmlurl.txt").read()
        start = datetime.datetime.now()
        start = start.replace(hour=0, minute=0, second=0)
        end = datetime.datetime.now()
        end = end.replace(hour=23, minute=59, second=59)
        URL += "&" + urllib.urlencode({"start-min":
                                       rfc3339.rfc3339(start,
                                                       use_system_timezone=False)});
        URL += "&" + urllib.urlencode({"start-max":
                                       rfc3339.rfc3339(end,
                                                       use_system_timezone=False)});
        dom = xml.dom.minidom.parse(urllib.urlopen(URL))
        added = 0
        for e in dom.getElementsByTagName("entry"):
            added += 1
            if added > 5:
                results += "..."
                break
            event = e.getElementsByTagName("title")[0].lastChild.toxml().encode('ascii','ignore')
            times = e.getElementsByTagName("summary")[0].lastChild.toxml().encode('ascii','ignore').split("\n")[0]
            times = re.findall(r'.*?([0-9]{2}:[0-9]{2}).*?', times)
            time = "All day"
            if len(times) == 1:
                time = times[0]
            elif len(times) == 2:
                time = times[0] + "-" + times[1]
            results += event + " - <em>" + time + "</em> " + "<br />"
        return results
    except:
        pass
    return "???"


def forecast():
    try:
        URL = "ftp://ftp2.bom.gov.au/anon/gen/fwo/IDA00007.dat"
        data = urllib.urlopen(URL).read()
        temp = ""
        for line in data.split("\n"):
            if line.startswith("094029"):
                if (line.split("#")[6] != ""):
                    temp = "Min: " + line.split("#")[6] + ", "
                temp += "Max: " + line.split("#")[7]
        for line in data.split("\n"):
            if line.startswith("094029"):
                return temp + "<br />" + line.split("#")[22]
    except:
        pass
    return "???"


def temperature():
    try:
        URL = "http://www.bom.gov.au/fwo/IDT60901/IDT60901.94970.axf"
        data = urllib.urlopen(URL).read()
        for line in data.split("\n"):
            if line.startswith("0,94970"):
                return line.split(",")[7]
    except:
        pass
    return "???"