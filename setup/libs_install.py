a =    [
        'mkdocs-bootstrap  beautifulsoup4 requests filemagic  passlib hexdump pymysql cx_Oracle psycopg2 pymongo wget python-nmap GitPython nclib paramiko mako pyelftools capstone ropgadget pyserial requests pip tox rarfile pygments pysocks python-dateutil packaging psutil intervaltree unicorn',
        'pycurl ajpy pyopenssl cx_Oracle psycopg2 pycrypto dnspython IPy pysnmp pyasn1 pysmb mkdocs ipgetterfuture requests paramiko pysnmp pycryptodome',
        ]

for  i in a:
        from os import system
        print ("\ninstall => %s\n"%i)
        system("pip3 install "+i)
