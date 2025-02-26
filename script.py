
usia_siswa = [13, 14, 14, 13, 15]
usia_siswa.append(20)
print(usia_siswa)

a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']
print(a[-1])


[s1, s2, s3, s4] = ["faa", "fee", "fuu", "fee"]
print(s1)


ketoprak = 14000
batagor = 8000
nasigoreng = 15000
uang = 20000

if uang >= 15000:
    print("Nasi Goreng")
elif uang >= 10000 and uang < 15000:
    print("Ketoprak")
elif uang >= 5000 and uang < 10000:
    print("Batagor")
elif uang < 5000:
    print("Air mineral")
else:
    print("Anda harus memiliki uang")