macaddr = 'f430.b915.3a2c'
print(macaddr)
macaddr = macaddr.replace('.','')
print(macaddr[0:2],
      macaddr[2:4],
      macaddr[4:6],
      macaddr[6:8],
      macaddr[8:10],
      macaddr[10:12], 
      sep=':')

