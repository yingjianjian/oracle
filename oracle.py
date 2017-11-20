# coding: UTF-8
#!/usr/bin/python
import  cx_Oracle
import os
import csv,time
import datetime
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn=cx_Oracle.connect('user','pass','IP/lcds')
cr=conn.cursor()
sql="""select case ecl_tasks.status_id when 1 then '待办' when 3 then '处理中' end  流程状态 ,ecl_request_sheet.request_desc 流程名称,
ecl_request_sheet.str_att_1 流程流水号,to_char(ecl_tasks.create_date, 'yyyy-mm-dd') 审批起点,to_char(sysdate,'YYYY-MM-DD')as 当前日期,
trunc(sysdate-ecl_tasks.create_date) 流程耗时,ecl_request_sheet.create_user_id 流程发起人,ecl_tasks.assignee_name 审批人 ,
user_table.user_id 审批人ID,user_table.mi 审批人姓名
from ecl_request_sheet
inner join ecl_tasks on ecl_tasks.request_id=ecl_request_sheet.request_id inner join user_table on ecl_tasks.assignee = user_table.myws_id where ecl_request_sheet.folder_id=0 and ecl_request_sheet.status_id=1
and ecl_tasks.status_id in (1,3) AND user_table.mi not in ('过锦涛','莫紫枫','廖文华','章亮','孙刘涛','鲍程成','孙刘涛')
and ecl_tasks.create_date between '1-8月-17' and sysdate and to_char(trunc(sysdate-ecl_tasks.create_date))<>0 order by user_table.mi
"""

cr.execute(sql)
rs=cr.fetchall()
count=0
Time=time.strftime("%Y%m%d")
for x in rs:
    count = count + 1
TC="截止到"+str(Time)+"_17点大于一天以上未审批的流程"+"共"+str(count)+"条"+".csv"
with open(TC, "w",encoding='gb18030') as f:
    csvwriter = csv.writer(f,dialect=("excel"))
    csvwriter.writerow(["流程状态","流程名称","流程流水号","审批起点","当前日期","流程耗时","流程发起人","审批人","审批人ID","审批人姓名"])
    for x in rs:
        csvwriter.writerow(x)
        count=count+1
cr.close()