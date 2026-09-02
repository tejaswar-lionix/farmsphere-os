"""analytics exporters - added after feedback"""
import csv, io
def to_csv(rows):
    out=io.StringIO()
    w=csv.writer(out); w.writerows(rows)
    return out.getvalue()
