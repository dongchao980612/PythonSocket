class DNA:
    def __init__(self, sequence=""):
        pass


# =============================
print('=== assignments ==')
dna1 = DNA()
print(dna1)  # 空字符串
dna1 = DNA('TTT')
print(dna1)  # TTT
dna2 = DNA('ACTGGCTAA')
print(dna2)  # ACTGGCTAA
dna3 = dna2
print(dna3)  # ACTGGCTAA

print('=== concatenations ===')
dna4 = dna1 + dna2
dna5 = dna1 + 'GGG'
dna6 = 'CCC' + dna1
print(dna4)  # TTTACTGGCTAA
print(dna5)  # TTTGGG
print(dna6)  # CCCTTT

print('=== indexing ===')
print(dna6[2:6])  # CTTT（切片：索引2到5）
for nt in dna6:
    print(nt)  # 逐行打印 C C C T T T
dna5 = dna2[2:6]
print(dna5)  # TGGC
