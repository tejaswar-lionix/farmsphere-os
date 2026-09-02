"""farms geo utils - GDAL fallback helpers - added organically"""
import re
def parse_wkt(wkt):
    if not wkt: return None
    m=re.search(r"POLYGON\(\((.+)\)\)", wkt)
    return m.group(1) if m else None
