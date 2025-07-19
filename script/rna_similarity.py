

import csv
from itertools import product

# 读取序列
with open('统计序列相似性.csv', 'r', encoding='utf-8') as f:
    sequences = [line.strip() for line in f if line.strip()]

# 计算两条序列的相似度（按较短长度对齐）
def sequence_similarity(seq1, seq2):
    min_len = min(len(seq1), len(seq2))
    if min_len == 0:
        return 0.0
    matches = sum(1 for a, b in zip(seq1[:min_len], seq2[:min_len]) if a == b)
    return matches / min_len

# 计算所有序列对的相似度（包括自身）
results = []
for (i, seq1), (j, seq2) in product(enumerate(sequences), repeat=2):
    sim = sequence_similarity(seq1, seq2)
    results.append((i+1, j+1, seq1, seq2, sim))

# 按相似度降序排序
results.sort(key=lambda x: x[-1], reverse=True)

# 输出结果
with open('rna_sequence_similarity_results.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['序列1编号', '序列2编号', '序列1', '序列2', '相似度'])
    for row in results:
        writer.writerow(row)

print('已输出所有序列对（含自身）的相似度到 rna_sequence_similarity_results.csv') 