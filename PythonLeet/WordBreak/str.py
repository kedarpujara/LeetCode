def substr012(s):
	n = len(s)

	mp = {}
	mp[(0,0)] = 1
	zc = 0
	oc = 0
	tc = 0

	res = 0

	for i in range(n):
		if s[i] == '0': 
			zc += 1
		elif s[i] == '1': 
			oc += 1
		else:
			tc += 1

		tmp = (zc-oc, zc-tc)

		res = res + mp.get(tmp,0)
		mp[tmp] = mp.get(tmp,0) + 1
		#print res

	print res
	return res

substr012("012210")


# def zot(str):
#     n = len(str)

#     mp = {}
#     mp[(0,0)] = 1

#     zc, oc, tc = 0,0,0

#     res = 0

#     for i in range(n):
#         if str[i] == '0': zc += 1
#         elif str[i] == '1': oc += 1
#         else: tc += 1

#         tmp = (zc-oc, zc-tc)

#         res = res + mp.get(tmp, 0)

#         mp[tmp] = mp.get(tmp, 0) + 1

#     print(mp, res)
