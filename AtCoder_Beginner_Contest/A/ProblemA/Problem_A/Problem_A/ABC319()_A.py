top10_str = """tourist 3858
ksun48 3679
Benq 3658
Um_nik 3648
apiad 3638
Stonefeang 3630
ecnerwala 3613
mnbvmar 3555
newbiedmy 3516
semiexp 3481"""

top10_dict = dict()
for info in top10_str.split('\n'):
    name, rate_str = info.split(' ')
    top10_dict[name] = rate_str

S = input()

ans = top10_dict[S]
print(ans)
