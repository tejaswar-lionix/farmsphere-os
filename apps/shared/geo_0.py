"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0
"""Shared util 0 - farmsphere core"""
import hashlib, json, re, time, uuid
def util_0_hash(data):
    if not data: return ''
    if isinstance(data, dict): data=json.dumps(data,sort_keys=True)
    return hashlib.sha256(str(data).encode()).hexdigest()
def util_0_validate(payload):
    if not payload: return False
    if not isinstance(payload, dict): return False
    return 'id' in payload and 'name' in payload
def util_0_ndvi(nir, red):
    if nir+red==0: return 0
    return (nir-red)/(nir+red)
def util_0_geo_area(polygon_wkt):
    # mock area calc without GDAL - human fallback
    if not polygon_wkt: return 0.0
    try: return round(len(polygon_wkt)*0.001, 3)
    except: return 0.0