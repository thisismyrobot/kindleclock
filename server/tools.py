import htmlentitydefs
import mimetypes
import re

def unescape(text):
    """ Great little function from http://effbot.org/zone/re-sub.htm#unescape-html
    """
    def fixup(m):
        text = m.group(0)
        if text[:2] == "&#":
            # character reference
            try:
                if text[:3] == "&#x":
                    return unichr(int(text[3:-1], 16))
                else:
                    return unichr(int(text[2:-1]))
            except ValueError:
                pass
        else:
            # named entity
            try:
                text = unichr(htmlentitydefs.name2codepoint[text[1:-1]])
            except KeyError:
                pass
        return text # leave as is
    return re.sub("&#?\w+;", fixup, text)


def ordinal(day):
    """ Thank you to: http://stackoverflow.com/a/739266
    """
    if 4 <= day <= 20 or 24 <= day <= 30:
        suffix = "th"
    else:
        suffix = ["st", "nd", "rd"][day % 10 - 1]
    return suffix


def _filename(s):
    return s.path[1:].split('?')[0]


def _gets(s):
    _gets = s.path[1:].split('?')
    if len(_gets) == 1:
        return None
    return _gets[1]


def _content_type(filename):
    ct, _ = mimetypes.guess_type(filename)
    if ct is None:
        ct = "text/html"
    return ct

