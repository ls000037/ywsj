#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
import os,datetime,time 
import psycopg2
#time.sleep(1)
str3=(datetime.datetime.now()+datetime.timedelta(minutes=-1)).strftime('%Y_%m%d_%H%M')
outdir1="/root/httpflow/httpdir/"
outdir2="/root/httpry/"
outdir_httpry=outdir2+str3+".txt"
outdir_httpflow=outdir1+str3
fromfile="/root/httpflow/"+str3+".pcap"
#print (fromfile)
#print (outdir_httpflow)
#conn = psycopg2.connect(database="was", user="postgres", password="Waner123456", host="127.0.0.1", port="5432")
#print ('connect successful!')
#cursor=conn.cursor()

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
conn.close()
host2="'host ("
host3=" or ".join(host1)
host=host2+host3+")'"

#host1=['172.16.1.243','www.qq.com']
#host2="'host ("
#host3=" or ".join(host1)
#host=host2+host3+")'"
#print (host)
#flow_str="/home/waner/httpflow/httpflow -r "+fromfile+" -f "+host+" -w "+outdir_httpflow
flow_str="/root/httpflow/httpflow -r "+fromfile+" -f "+host+" -w "+outdir_httpflow
ry_str="/root/httpry/httpry -r "+fromfile+" -f 'timestamp,source-ip,dest-ip,direction,method,host,request-uri,http-version,user-agent,status-code,reason-phrase'"+" -o "+outdir_httpry+" "+host
print (flow_str)
#ry_str="/home/waner/httpry/httpry -r "+fromfile+" "+host+" -o "+outdir_httpry
#echo $hosturl
#os.system(ry_str)
#./httpry -i $device -o $output
#ID=`ps -ef | grep "httpflow" |grep -v "grep" | awk '{print $2}'`
#for id in $ID
#do
#kill -9 $id
#done
if not os.path.exists(outdir_httpflow) and (os.path.exists(fromfile)):
    os.system(ry_str)
    os.system(flow_str)
    os.remove(fromfile)
if not os.listdir(outdir_httpflow):
    os.rmdir(outdir_httpflow)
