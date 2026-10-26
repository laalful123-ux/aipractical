import argparse
from .api import show,search,list_questions
def main():
 p=argparse.ArgumentParser(prog="answers"); sub=p.add_subparsers(dest="cmd")
 l=sub.add_parser("list"); l.add_argument("--module",type=int,choices=[1,2])
 s=sub.add_parser("show"); s.add_argument("query",nargs="+"); s.add_argument("--module",type=int,choices=[1,2])
 f=sub.add_parser("search"); f.add_argument("query",nargs="+"); f.add_argument("--module",type=int,choices=[1,2])
 a=p.parse_args()
 if a.cmd=="list": list_questions(a.module)
 elif a.cmd=="show": show(" ".join(a.query),a.module)
 elif a.cmd=="search": search(" ".join(a.query),a.module)
 else: p.print_help()
if __name__=="__main__": main()
