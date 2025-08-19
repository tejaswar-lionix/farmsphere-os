"""API routes - subsidies"""
from fastapi import APIRouter, HTTPException
from typing import Dict, List
router=APIRouter()

@router.get('/subsidies/0')
def get_subsidies_0(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':0,'limit':limit,'offset':offset}

@router.post('/subsidies/0')
def post_subsidies_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/0/{item_id}')
def put_subsidies_0(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/1')
def get_subsidies_1(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':1,'limit':limit,'offset':offset}

@router.post('/subsidies/1')
def post_subsidies_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/1/{item_id}')
def put_subsidies_1(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/2')
def get_subsidies_2(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':2,'limit':limit,'offset':offset}

@router.post('/subsidies/2')
def post_subsidies_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/2/{item_id}')
def put_subsidies_2(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/3')
def get_subsidies_3(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':3,'limit':limit,'offset':offset}

@router.post('/subsidies/3')
def post_subsidies_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/3/{item_id}')
def put_subsidies_3(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/4')
def get_subsidies_4(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':4,'limit':limit,'offset':offset}

@router.post('/subsidies/4')
def post_subsidies_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/4/{item_id}')
def put_subsidies_4(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/5')
def get_subsidies_5(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':5,'limit':limit,'offset':offset}

@router.post('/subsidies/5')
def post_subsidies_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/5/{item_id}')
def put_subsidies_5(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/6')
def get_subsidies_6(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':6,'limit':limit,'offset':offset}

@router.post('/subsidies/6')
def post_subsidies_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/6/{item_id}')
def put_subsidies_6(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/7')
def get_subsidies_7(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':7,'limit':limit,'offset':offset}

@router.post('/subsidies/7')
def post_subsidies_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/7/{item_id}')
def put_subsidies_7(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/8')
def get_subsidies_8(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':8,'limit':limit,'offset':offset}

@router.post('/subsidies/8')
def post_subsidies_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/8/{item_id}')
def put_subsidies_8(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/9')
def get_subsidies_9(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':9,'limit':limit,'offset':offset}

@router.post('/subsidies/9')
def post_subsidies_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/9/{item_id}')
def put_subsidies_9(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/10')
def get_subsidies_10(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':10,'limit':limit,'offset':offset}

@router.post('/subsidies/10')
def post_subsidies_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/10/{item_id}')
def put_subsidies_10(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/11')
def get_subsidies_11(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':11,'limit':limit,'offset':offset}

@router.post('/subsidies/11')
def post_subsidies_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/11/{item_id}')
def put_subsidies_11(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/12')
def get_subsidies_12(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':12,'limit':limit,'offset':offset}

@router.post('/subsidies/12')
def post_subsidies_12(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/12/{item_id}')
def put_subsidies_12(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/13')
def get_subsidies_13(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':13,'limit':limit,'offset':offset}

@router.post('/subsidies/13')
def post_subsidies_13(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/13/{item_id}')
def put_subsidies_13(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/subsidies/14')
def get_subsidies_14(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'subsidies','idx':14,'limit':limit,'offset':offset}

@router.post('/subsidies/14')
def post_subsidies_14(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/subsidies/14/{item_id}')
def put_subsidies_14(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}
