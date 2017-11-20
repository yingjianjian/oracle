wget http://downloads.sourceforge.net/project/cx-oracle/5.1.2/cx_Oracle-5.1.2-10g-py26-1.x86_64.rpm
rpm -ivh cx_Oracle-5.1.2-10g-py26-1.x86_64.rpm
ls /usr/lib/python2.6/site-packages/cx_Oracle.so#有这个文件表示安装成功，根据python的位置，也可能在其他地方，自己找一下吧
$python
>>import cx_Oracle
若报错：import cx_Oracle gave ImportError: libclntsh.so.10.1: cannot open shared object file: No such file or directory
表示没有找到instant client的动态库，check一下环境变量是否配置，是否生效，版本是否正确。