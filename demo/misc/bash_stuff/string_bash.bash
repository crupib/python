#!/bin/bash

str="2023-10-12"

echo "${str:5:2}" # 10
echo "${str::4}" # 2023
echo "2022-${str:5}" # 2022-10-12

str="backup.sql"

echo "original${str:(-4)}" # original.sql


str="obin-linux_x64_bin"

echo "${str/x64/armhf}" # obin-linux_armhf_bin
echo "${str/bin/dist}" # odist-linux_x64_bin
echo "${str//bin/dist}" # odist-linux_x64_dist


str="db_config_backup.zip"

echo "${str/%.zip/.conf}" # db_config_backup.conf
echo "${str/#db/settings}" # settings_config_backup.zip


str="db_config_backup.zip"

echo "${str/%.*/.bak}" # db_config_backup.conf
echo "${str/#*_/new}" # newbackup.zip


str="db_backup_2003.zip"

if [[ $str =~ 200[0-5]+ ]]; then
    echo "regex_matched"
fi
[[ $str =~ 200[0-5]+ ]] && echo "regex_matched"


str="db_backup_2003.zip"

if [[ $str =~ (200[0-5])(.*)$ ]]; then
    echo "${BASH_REMATCH[0]}" # 2003.zip
    echo "${BASH_REMATCH[1]}" # 2003
    echo "${BASH_REMATCH[2]}" # .zip
fi

str="db_backup_2003.zip"
re="200[0-3].zip"

echo "${str/$re/new}.bak" # db_backup_new.bak

str="ver5.02-2224.e2"

ver="${str#ver}"
echo $ver # 5.02-2224.e2

maj="${ver/.*}"
echo $maj # 5

str="ver5.02-2224_release"

ver="${str//[a-z_]}"
echo $ver # 5.02-2224

str="Hello Bash!"

lower=`echo "$str" | tr '[:upper:]' '[:lower"]'`
#upper="${str^^}"
UPPER=`echo "${str}" | tr '[a-z]' '[A-Z]'`
echo $UPPER
LOWER=`echo "${str}" | tr '[A-Z]' '[a-z]'`
echo $LOWER
ver1="V2.0-release"
ver2="v4.0-release"

echo "${ver1}" # v2.0-release
echo "${ver2}" # V4.0-release

#declare -l ver1
#declare -u ver2

ver1="V4.02.2"
ver2="v2.22.1"

echo $ver1 # v4.02.2
echo $ver2 #V2.22.1

str="C,C++,JavaScript,Python,Bash"

IFS=',' read -ra arr <<< "$str"

echo "${#arr[@]}" # 5
echo "${arr[0]}" # C
echo "${arr[4]}" # Bash

# WARNING: This code has several hidden issues.

str="C,Bash,*"

arr=(${str//,/ })

echo "${#arr[@]}" # contains current directory content
