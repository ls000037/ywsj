#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import psycopg2,os
import datetime,time
time.sleep(6)

conn = psycopg2.connect(database="was", user="postgres", password="Waner123456", host="172.16.1.100", port="5432")
print ('connect successful!')
cursor=conn.cursor()
cursor.execute("select assets_ip from public.assets")
rows=cursor.fetchall()
#print (rows)
host1=[]
for row in rows:
#    print (row[0])
    host1.append(row[0])
#print (host1)
cursor.execute("SELECT assets_ip, assets_pcap_name FROM public.assets")
ip_table={}
rows=cursor.fetchall()
for row in rows:
#    print (row)
    ip_table[row[0]]=str(row[1])
#print (ip_table)
#print (rows)
#table05=ip_table['172.16.1.211']
#print (table05)
conn.close()
host2="'host ("
host3=" or ".join(host1)
host=host2+host3+")'"


path="/root/httpflow/httpdir/"
"""
if (os.path.exists(path)):
    files = os.listdir(path)
    for file in files:
        #print (file)
        m = os.path.join(path,file)
        if (os.path.isdir(m)):
            h = os.path.split(m)
           
            if h[1][0]==".":
                continue
            #print (m)
            #print (h)
"""
date1=(datetime.datetime.now()+datetime.timedelta(minutes=-1)).strftime(path+'%Y_%m%d_%H%M')


print (date1)
#date1=path+"2018_0408_1715"
#print (date1)
if os.path.exists(date1):
    files = os.listdir(date1)
    for fromfile in files:        
        m = os.path.join(date1,fromfile)
   #     print (m)
        h = os.path.split(m)
    #    print (h)
        if h[1][0]==".":
            continue
        #print (fromfile)
        fromfile2=date1+"/"+fromfile
#fromfile='/root/httpflow/httpdir/2018_0408_1046/tj.kpzip.com'
        with open(fromfile2, 'r',encoding='ISO-8859-15') as f:
            data = f.readlines()
            data="".join(data)

            datalist=data.split('\n\n\n')
#print (datalist)
            datalen=len(datalist)-1
#print (datalen)
        datafinal=[]
        for i in range(datalen):
            datastr="".join(datalist[i])
    #print (datastr)
            sip=(datastr.split('\n')[0]).split(':')[1].strip()
            sport=(datastr.split('\n')[0]).split(':')[2].strip()
            dip=(datastr.split('\n')[1]).split(':')[1].strip()
            dport=(datastr.split('\n')[1]).split(':')[2].strip()
            #hostname=(datastr.split('\n')[3]).split(':')[1].strip()
            hostname=str(fromfile)
            url=(datastr.split('\n')[2]).split(' ')[1].strip()
            method=(datastr.split('\n')[2]).split(' ')[0].strip()
            request=""
    #html=datastr.split('\n\n')[2]
            if "Content-Type: text/html" in datastr:
                html=datastr.split('\n\n')[2]    
            else:
                html=""
            if dip in host1:
                table05=ip_table[dip]
            else:
                table05=ip_table[sip]
            datafinal1=sip+"|"+sport+"|"+dip+"|"+dport+"|"+hostname+"|"+url+"|"+method+"|"+request+"|"+html+"\n"
            datafinal.append(datafinal1)
        #print (datafinal)

        fromfile1='/tmp/sql'
        with open(fromfile1+'.txt', 'a+') as f:
            f.writelines(datafinal)
         
    #print (html)
        conn = psycopg2.connect(database="was", user="postgres", password="Waner123456", host="172.16.1.100", port="5432")
#print ('connect successful!')
        cursor=conn.cursor()
#cursor.execute('GRANT ALL PRIVILEGES ON TABLE "1522813944" TO postgres;')
       # cursor.execute('GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO postgres;')
        sqlstr="copy "+'"'+table05+'"('+'"pcap_s_ip","pcap_s_port","pcap_d_ip","pcap_d_port","pcap_host","pcap_url","pcap_method","pcap_request","pcap_html")'+" FROM '"+fromfile1+".txt'  DELIMITER '|'"
        #print (sqlstr)
        cursor.execute(sqlstr)
        conn.commit()
        os.remove('/tmp/sql.txt')
#rows=cursor.fetchall()
        conn.close()

