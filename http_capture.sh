#!/bin/bash
ID=`ps -ef | grep "tcpdump -i" |grep -v "grep" | awk '{print $2}'`
if [[ ! $ID ]];
then
nohup /usr/local/sbin/tcpdump -i enp3s0 -X -G 60 -s0 -w /root/httpflow/%Y_%m%d_%H%M.pcap >/dev/null 2>&1 &
fi
