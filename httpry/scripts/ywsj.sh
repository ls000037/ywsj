#!/bin/bash
sleep 2
output1=common_log_
output2=$(date -d "1 minutes ago" +"%Y_%m%d_%H%M.txt")
output=${output1}${output2}
echo $output
cd /root/httpry/scripts/
sed -r -i "s/common_log.*.txt/$output/g" common_log.cfg
output3=/root/httpry/
output4=${output3}${output2}
echo $output4
perl /root/httpry/scripts/parse_log.pl -d ./ $output4
rm -rf $output4
