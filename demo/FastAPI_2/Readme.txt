dd if=/dev/zero of=static/zero.bin bs=1m count=10000
curl -O 'http://127.0.0.1:8000/static/zero.bin'
siege -b -c 50 -r 5 'http://127.0.0.1:8000/static/zero.bin'

