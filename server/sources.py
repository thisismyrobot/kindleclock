import urllib


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