import re

m = re.match('foo','afoo on the table')
if m is not None:
	print(m.group())
else:
	print(' match no match')


m = re.search('foo','afoo on the table')
if m is not None:
	print(m.group())
else:
	print('search no match')


bt = 'bat|bet|bit'
m = re.search(bt,'bat')
if m is not None:
	print(m.group())
else:
	print('search no match')
	
anyend = '.end'
m = re.search(anyend,'bend')
if m is not None:
	print(m.group())
else:
	print('search no match')
	

patt314 = '3.14'
pi_patt = '3\.14'
m = re.match(pi_patt,'3014')
if m is not None:
	print(m.group())
else:
	print('search no match')
	
anyword = '[ab][cd][23][xy]'
m = re.search(anyword,'bc3y')
if m is not None:
	print(m.group())
else:
	print('search no match')
	
	
patt = '\w+@(\w+\.)?\w+\.com'
print(re.match(patt,'shi@abc.innotron.com').group())


print(re.match('(a(b))','ab').group())
print(re.match('(a(b))','ab').group(1))
print(re.match('(a(b))','ab').group(2))
print(re.match('(a(b))','ab').groups())


print(re.match('^The','The end').group())

print(re.findall('(c)(ar)','car'))


s = 'This and that'
print(re.findall(r'(th\w+) and (th\w+)',s,re.I))
m = re.finditer(r'(th\w+) and (th\w+)',s,re.I).next()
print(m.group(0))
print(m.group(1))
print(m.group(2))

print('-------------------------------------------------')
s = 'This and that'
m = re.finditer(r'(th\w+) and (th\w+)',s,re.I)
g = m.next()
print(g.group(0))
print(g.group(1))
print(g.group(2))