import json, re
from pathlib import Path
from difflib import SequenceMatcher
_DATA=json.loads((Path(__file__).parent/"data.json").read_text(encoding="utf-8"))
def _norm(s): return re.sub(r"[^a-z0-9]+"," ",str(s).lower()).strip()
def list_questions(module=None):
    for x in _DATA:
        if module is None or x["module"]==module: print(f'M{x["module"]} Q{x["number"]:02} — {x["question"]}')
def search(query,module=None,limit=10):
    q=_norm(query); scored=[]
    for x in _DATA:
        if module is not None and x["module"]!=module: continue
        t=_norm(x["question"]); qw=set(q.split()); tw=set(t.split())
        score=1 if q==t else (0.98 if q and q in t else max(len(qw&tw)/max(1,len(qw))*0.85,SequenceMatcher(None,q,t).ratio()*0.65))
        if score>0.12: scored.append((score,x))
    scored.sort(key=lambda p:p[0],reverse=True); found=[x for _,x in scored[:limit]]
    for x in found: print(f'M{x["module"]} Q{x["number"]:02} [{x["kind"]}] {x["question"]}')
    if not found: print("No match found. Try answers.search('some keywords').")
    return found
def _resolve(query,module=None):
    s=str(query).strip().lower()
    m=re.fullmatch(r"m([12])q0*(\d+)",s)
    if m: num,mod=int(m.group(2)),int(m.group(1))
    else:
        m=re.fullmatch(r"q0*(\d+)",s)
        if m: num,mod=int(m.group(1)),module
        elif s.isdigit(): num,mod=int(s),module
        else: num=mod=None
    if num is not None:
        return next((x for x in _DATA if x["number"]==num and (mod is None or x["module"]==mod)),None)
    norm=_norm(query)
    exact=[x for x in _DATA if _norm(x["question"])==norm and (module is None or x["module"]==module)]
    if exact:return exact[0]
    contains=[x for x in _DATA if norm and norm in _norm(x["question"]) and (module is None or x["module"]==module)]
    if len(contains)==1:return contains[0]
    return None
def show(query,module=None):
    x=_resolve(query,module)
    if x is None:
        matches=search(query,module=module,limit=5)
        if len(matches)==1:x=matches[0]
        else:
            if matches: print("\nSeveral matches found. Copy/paste more of the question, or choose one of the listed results.")
            return matches or None
    print(f'\nMODULE {x["module"]} — QUESTION {x["number"]}\n{x["question"]}\n\n{"CODE" if x["kind"]=="python" else "STEPS / ANSWER"}\n'+"-"*60)
    print(x["answer"]); return x["answer"]
class _Answers:
    def show(self,question): return show(question)
    def search(self,query,module=None,limit=10): return search(query,module,limit)
    def list(self,module=None): return list_questions(module)
answers=_Answers()
