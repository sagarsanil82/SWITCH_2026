# def analyze_logs(filename):
#     err_cnt=0
#     warn_cnt=0
#     info_cnt=0
#     err_list=[]
#     warn_list=[]
#     info_list=[]
#     err_keyword=['error','warning','info']

#     with open(filename,"r") as f:
#         for line_no,line in enumerate(f,start=1):     
#             if 'error' in line.lower():
#                     err_cnt+=1
#                     err_list.append((line_no,line.strip()))
#             if 'warning' in line.lower():
#                     warn_cnt+=1
#                     warn_list.append((line_no,line.strip()))
#             if 'info' in line.lower():
#                     info_cnt+=1
#                     info_list.append((line_no,line.strip()))

#         # return err_list,warn_list,info_list,err_cnt,warn_cnt,info_cnt
#         summary={"error":err_cnt,"warning":warn_cnt,"info":info_cnt}
#         summary_list={"error_list":err_list,"warning_list":warn_list,"info_list":info_list}
#         return summary,summary_list

# cnt,lis_summary=analyze_logs('file.txt')
# print(f"{cnt}:{lis_summary}")    



# # #############Q2 ###############
# for line_no,err_cn in lis_summary["error_list"][:2]:
#     print(f"{line_no}:{err_cn}")

# lop=analyze_logs("file.txt")
# print(lop)

# with open("summary.txt","w") as f:
#       f.write("----LOG SUMMARY----- \n\n")
#       f.write(f"Errors: {lis_summary['error_list']}\n\n")
#       f.write(f"Warning: {lis_summary['warning_list']}\n\n")
#       f.write(f"Info: {lis_summary['info_list']}\n\n")
#     #   f.write(f"{lop}" + "\n")
#       f.write("------- FIRST 3 ERRORS ----\n")
#       for line,sum in lis_summary["error_list"][:3]:
#            f.write(f"{line}:{sum}\n")
#       if len(lis_summary['error_list']) >3:
#         f.write("Too many errors")
import sys            

def err_log(filename):
    err_count=0
    warn_count=0
    info_count=0
    err_list=[]
    warn_list=[]
    info_list=[]
    time_list=[]
    keyword=[]

    with open(filename,"r") as f:

        for lineno,line in enumerate(f,start=1):
            clean_Line=line.strip()
            lower_line=line.lower()
            parts=line.split()
            if 'error'.lower() in lower_line:
                err_count+=1
                err_list.append((lineno,line.strip()))
                
                if len(parts)>1:
                    time_list.append((parts[1]))
                
            elif 'warn'.lower() in lower_line:
                warn_count+=1
                warn_list.append((lineno,line.strip()))
            elif 'info'.lower() in lower_line:
                info_count+=1
                info_list.append((lineno,line.strip()))
        
        return err_count,err_list,warn_count,warn_list,info_count,info_list,time_list

if len(sys.argv)<2:
    print("Usage: python script.py <filename>")
    sys.exit()

filename=sys.argv[1]

ecnt,elist,wcnt,wlist,icnt,ilist,tlist=err_log(filename)

with open(filename,"w") as f:
    f.write("--- SUMMARY ---\n")
    f.write(f"Errors:{ecnt}\nWarnings:{wcnt}\nInfo:{icnt}\n\n")
    f.write("--- ERROR TIMES ---\n")
    for t in tlist:
        f.write(f"{t}\n")
    f.write(f"--- LAST 2 ERRORS ---\n")
    for line_no,text in elist[-2:]:
        f.write(f"Line {line_no}:{text}\n")
    if ecnt>3 and 'disk'.lower() in elist:
        f.write("\nCRITICAL: Disk-related errors detected!\n")