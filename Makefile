run:
	/usr/bin/env python main.py -a 172.16.1.254 -p 19191

debug:
	/usr/bin/env python main.py -a 172.16.1.254 -p 19191 -d

debug-watch:
	/usr/bin/env python main.py -a 172.16.1.254 -p 19191 -d -r

local:
	/usr/bin/env python main.py -a localhost -p 8081 -d

test:
	echo "No tests yet."