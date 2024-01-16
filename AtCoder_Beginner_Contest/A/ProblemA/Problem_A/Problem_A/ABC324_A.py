n = int(input())
A = list(map(int, input().split())) # A をすべて読み込む


for a in A:
    for b in A:
        if b != a: # 違うペアがあったら
            print('No') # No と出力して
            break # ループを抜ける
    else: # 違うペアがなかったら
        continue # 探索を続ける
    break
else: # 最後まで違うペアがなかったら
    print('Yes') # Yes と出力