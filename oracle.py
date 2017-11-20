# coding: UTF-8
#!/usr/bin/python
import  cx_Oracle
import os
import csv,time
import datetime
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'
conn=cx_Oracle.connect('user','pass','IP/lcds')
cr=conn.cursor()
sql="""select case ecl_tasks.status_id when 1 then '����' when 3 then '������' end  ����״̬ ,ecl_request_sheet.request_desc ��������,
ecl_request_sheet.str_att_1 ������ˮ��,to_char(ecl_tasks.create_date, 'yyyy-mm-dd') �������,to_char(sysdate,'YYYY-MM-DD')as ��ǰ����,
trunc(sysdate-ecl_tasks.create_date) ���̺�ʱ,ecl_request_sheet.create_user_id ���̷�����,ecl_tasks.assignee_name ������ ,
user_table.user_id ������ID,user_table.mi ����������
from ecl_request_sheet
inner join ecl_tasks on ecl_tasks.request_id=ecl_request_sheet.request_id inner join user_table on ecl_tasks.assignee = user_table.myws_id where ecl_request_sheet.folder_id=0 and ecl_request_sheet.status_id=1
and ecl_tasks.status_id in (1,3) AND user_table.mi not in ('������','Ī�Ϸ�','���Ļ�','����','������','���̳�','������')
and ecl_tasks.create_date between '1-8��-17' and sysdate and to_char(trunc(sysdate-ecl_tasks.create_date))<>0 order by user_table.mi
"""

cr.execute(sql)
rs=cr.fetchall()
count=0
Time=time.strftime("%Y%m%d")
for x in rs:
    count = count + 1
TC="��ֹ��"+str(Time)+"_17�����һ������δ����������"+"��"+str(count)+"��"+".csv"
with open(TC, "w",encoding='gb18030') as f:
    csvwriter = csv.writer(f,dialect=("excel"))
    csvwriter.writerow(["����״̬","��������","������ˮ��","�������","��ǰ����","���̺�ʱ","���̷�����","������","������ID","����������"])
    for x in rs:
        csvwriter.writerow(x)
        count=count+1
cr.close()