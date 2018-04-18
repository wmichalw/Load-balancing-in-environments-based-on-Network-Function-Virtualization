#! /bin/bash
ps aux  | grep -v bash | awk {'if(NR>1) print $2'} | xargs kill
