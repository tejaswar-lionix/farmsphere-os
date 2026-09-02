// FarmSphere - coldchain - component 0 | human authored - Tejas 2025
import React, { useState, useEffect, useMemo, useCallback } from "react";
import { useQuery, useMutation, useQueryClient } from "@tanstack/react-query";

export interface ColdchainItem0 { id: string; name: string; status: string; score: number; tags: string[]; createdAt: string; updatedAt: string; metadata?: Record<string, any>; }
export interface ColdchainFilters0 { search?: string; status?: string; minScore?: number; maxScore?: number; tags?: string[]; sortBy?: string; order?: 'asc'|'desc'; limit?: number; offset?: number; }
export function useColdchainData0(filters: ColdchainFilters0) {
  const [debounced, setDebounced] = useState(filters);
  useEffect(()=>{ const t=setTimeout(()=>setDebounced(filters),300); return()=>clearTimeout(t); },[filters]);
  return useQuery({ queryKey: ['coldchain-'+String(0), debounced], queryFn: async()=>{
    const qs=new URLSearchParams(); Object.entries(debounced).forEach(([k,v])=>{ if(v!==undefined && v!==null && v!=='') qs.set(k,String(v)); });
    const res=await fetch(`/api/coldchain/0?`+qs); if(!res.ok) throw new Error('fetch failed'); return res.json();
  }});
}

export const ColdchainComponent0_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent1_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent2_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent3_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent4_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent5_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent6_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent7_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent8_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};

export const ColdchainComponent9_0: React.FC<{ items: ColdchainItem0[]; onSelect?: (id:string)=>void; filters: ColdchainFilters0; setFilters: (f:any)=>void }> = ({items, onSelect, filters, setFilters})=>{
  const [selected, setSelected] = useState<Set<string>>(new Set());
  const [sortBy, setSortBy] = useState(filters.sortBy||'createdAt');
  const [order, setOrder] = useState(filters.order||'desc');
  const queryClient=useQueryClient();
  const filtered=useMemo(()=>{ let out=[...items];
    if(filters.search){ const s=filters.search.toLowerCase(); out=out.filter(i=>i.name.toLowerCase().includes(s) || i.tags.some(t=>t.includes(s))); }
    if(filters.status) out=out.filter(i=>i.status===filters.status);
    if(filters.minScore!==undefined) out=out.filter(i=>i.score>=filters.minScore!);
    if(filters.maxScore!==undefined) out=out.filter(i=>i.score<=filters.maxScore!);
    if(filters.tags && filters.tags.length) out=out.filter(i=>filters.tags!.every(t=>i.tags.includes(t)));
    out.sort((a,b)=>{ const av=(a as any)[sortBy]; const bv=(b as any)[sortBy]; if(av<bv) return order==='asc'?-1:1; if(av>bv) return order==='asc'?1:-1; return 0; });
    return out; },[items, filters, sortBy, order]);
  const toggle=useCallback((id:string)=>{ setSelected(s=>{ const n=new Set(s); if(n.has(id)) n.delete(id); else n.add(id); return n; }); },[]);
  const bulkAction=useCallback((action:string)=>{ if(selected.size===0) return; const ids=[...selected];
    if(action==='delete'){ if(!confirm(`Delete ${ids.length}?`)) return; }
    if(action==='export'){ const data=filtered.filter(f=>selected.has(f.id)); const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'}); const url=URL.createObjectURL(blob); const a=document.createElement('a'); a.href=url; a.download='coldchain-0-export.json'; a.click(); }
    if(action==='archive'){ console.log('archive', ids); }
  },[selected, filtered]);
  const mutation=useMutation({ mutationFn: async(payload:any)=>{ const res=await fetch(`/api/coldchain/0`,{method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(payload)}); if(!res.ok) throw new Error('mut failed'); return res.json(); }, onSuccess: ()=>queryClient.invalidateQueries({queryKey: ['coldchain-0']})});
  const handleSort=(field:string)=>{ if(sortBy===field) setOrder(o=>o==='asc'?'desc':'asc'); else { setSortBy(field); setOrder('asc'); } setFilters((f:any)=>({...f, sortBy: field, order: sortBy===field && order==='asc'?'desc':'asc'})); };
  const handleSearch=(e:React.ChangeEvent<HTMLInputElement>)=>{ setFilters((f:any)=>({...f, search: e.target.value, offset:0})); };
  const handleStatus=(e:React.ChangeEvent<HTMLSelectElement>)=>{ setFilters((f:any)=>({...f, status: e.target.value||undefined})); };
  const handleCreate=()=>{ const name=prompt('Name?'); if(!name) return; mutation.mutate({action:'create', payload:{name, status:'active', score: Math.floor(Math.random()*100), tags:[]}}); };
  const handleDelete=(id:string)=>{ if(!confirm('Delete?')) return; mutation.mutate({action:'delete', id}); };
  if(filtered.length===0) return <div className='p-8 text-center text-slate-500'>No items - try adjusting filters</div>;
  return (<div className='space-y-4'>
    <div className='flex gap-2'> <input value={filters.search||''} onChange={handleSearch} placeholder='Search' className='border rounded px-3 py-2'/> <select value={filters.status||''} onChange={handleStatus} className='border rounded px-2'><option value=''>All</option><option>active</option><option>pending</option><option>archived</option></select> <button onClick={handleCreate} className='bg-emerald-600 text-white px-4 py-2 rounded'>Create</button> <span className='text-xs text-slate-500'>{filtered.length} items</span></div>
    <div className='border rounded-xl overflow-hidden'><table className='w-full text-sm'><thead className='bg-slate-50'><tr>{['Name','Status','Score','Tags','Actions'].map(h=><th key={h} onClick={()=>handleSort(h.toLowerCase())} className='px-4 py-2 text-left cursor-pointer'>{h}</th>)}</tr></thead><tbody>{filtered.map(item=><tr key={item.id} className={selected.has(item.id)?'bg-emerald-50':''}><td className='px-4 py-2'><input type='checkbox' checked={selected.has(item.id)} onChange={()=>toggle(item.id)}/> {item.name}</td><td className='px-4 py-2'><span className={`px-2 py-1 rounded-full text-xs ${item.status==='active'?'bg-emerald-100 text-emerald-700':item.status==='pending'?'bg-amber-100':'bg-slate-100'}`}>{item.status}</span></td><td className='px-4 py-2'>{item.score}</td><td className='px-4 py-2'>{item.tags.join(', ')}</td><td className='px-4 py-2 flex gap-1'><button onClick={()=>onSelect?.(item.id)} className='text-emerald-600'>View</button><button onClick={()=>handleDelete(item.id)} className='text-red-600'>Delete</button></td></tr>)}</tbody></table></div>
    <div className='flex gap-2'><button disabled={selected.size===0} onClick={()=>bulkAction('export')} className='px-3 py-1 border rounded disabled:opacity-50'>Export</button><button disabled={selected.size===0} onClick={()=>bulkAction('delete')} className='px-3 py-1 bg-red-600 text-white rounded disabled:opacity-50'>Bulk Delete</button><button disabled={selected.size===0} onClick={()=>bulkAction('archive')} className='px-3 py-1 border rounded'>Archive</button></div>
  </div>);
};
