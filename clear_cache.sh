#!/bin/sh

#内存总量
total=$( free -m | grep Mem | awk '{print $2}')
#已使用内存
used=$( free -m | grep Mem | awk '{print $3}')
#内存使用率
rate=$(($used*100/$total))

time=date
echo "############$(date)###############"
#使用的最大百分百
percent=70

if [ $rate -gt $percent ]
then
    echo "rate=$rate    freeMemory start!"
    sync
    echo  3 >> /proc/sys/vm/drop_caches
    echo "FreeMemory Success!" 
else
    echo "rate=$rate  Memory is normal"
fi