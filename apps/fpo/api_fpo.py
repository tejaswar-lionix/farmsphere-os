"""API routes - fpo"""
from fastapi import APIRouter, HTTPException
from typing import Dict, List
router=APIRouter()

@router.get('/fpo/0')
def get_fpo_0(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':0,'limit':limit,'offset':offset}

@router.post('/fpo/0')
def post_fpo_0(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/0/{item_id}')
def put_fpo_0(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/1')
def get_fpo_1(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':1,'limit':limit,'offset':offset}

@router.post('/fpo/1')
def post_fpo_1(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/1/{item_id}')
def put_fpo_1(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/2')
def get_fpo_2(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':2,'limit':limit,'offset':offset}

@router.post('/fpo/2')
def post_fpo_2(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/2/{item_id}')
def put_fpo_2(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/3')
def get_fpo_3(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':3,'limit':limit,'offset':offset}

@router.post('/fpo/3')
def post_fpo_3(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/3/{item_id}')
def put_fpo_3(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/4')
def get_fpo_4(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':4,'limit':limit,'offset':offset}

@router.post('/fpo/4')
def post_fpo_4(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/4/{item_id}')
def put_fpo_4(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/5')
def get_fpo_5(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':5,'limit':limit,'offset':offset}

@router.post('/fpo/5')
def post_fpo_5(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/5/{item_id}')
def put_fpo_5(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/6')
def get_fpo_6(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':6,'limit':limit,'offset':offset}

@router.post('/fpo/6')
def post_fpo_6(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/6/{item_id}')
def put_fpo_6(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/7')
def get_fpo_7(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':7,'limit':limit,'offset':offset}

@router.post('/fpo/7')
def post_fpo_7(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/7/{item_id}')
def put_fpo_7(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/8')
def get_fpo_8(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':8,'limit':limit,'offset':offset}

@router.post('/fpo/8')
def post_fpo_8(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/8/{item_id}')
def put_fpo_8(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/9')
def get_fpo_9(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':9,'limit':limit,'offset':offset}

@router.post('/fpo/9')
def post_fpo_9(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/9/{item_id}')
def put_fpo_9(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/10')
def get_fpo_10(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':10,'limit':limit,'offset':offset}

@router.post('/fpo/10')
def post_fpo_10(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/10/{item_id}')
def put_fpo_10(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/11')
def get_fpo_11(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':11,'limit':limit,'offset':offset}

@router.post('/fpo/11')
def post_fpo_11(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/11/{item_id}')
def put_fpo_11(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/12')
def get_fpo_12(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':12,'limit':limit,'offset':offset}

@router.post('/fpo/12')
def post_fpo_12(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/12/{item_id}')
def put_fpo_12(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/13')
def get_fpo_13(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':13,'limit':limit,'offset':offset}

@router.post('/fpo/13')
def post_fpo_13(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/13/{item_id}')
def put_fpo_13(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}

@router.get('/fpo/14')
def get_fpo_14(limit: int=20, offset: int=0):
    if limit>100: raise HTTPException(400,'too large')
    if offset<0: raise HTTPException(400,'bad offset')
    return {'domain':'fpo','idx':14,'limit':limit,'offset':offset}

@router.post('/fpo/14')
def post_fpo_14(payload: Dict):
    if not payload.get('name'): raise HTTPException(422,'name required')
    status=payload.get('status','active')
    if status not in ('active','pending','archived'): raise HTTPException(422,'bad status')
    return {'id': 'xyz','status':'created','payload':payload}

@router.put('/fpo/14/{item_id}')
def put_fpo_14(item_id: str, payload: Dict):
    if not item_id: raise HTTPException(400,'id required')
    return {'id': item_id, 'updated': True}
