import os
import glob
import re

input_folder = 'candidate_sorted'
output_file = 'merged_sorted_candidates.csv'

all_rows = []

# 匹配分数的正则
score_pattern = re.compile(r'\[\[(.*?)\]\]')

for csv_file in glob.glob(os.path.join(input_folder, '*.csv')):
    with open(csv_file, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            # 解析格式: sequence,[[score]]
            try:
                seq, score_str = line.split(',', 1)
                match = score_pattern.search(score_str)
                if match:
                    score = float(match.group(1))
                    all_rows.append((seq, score))
            except Exception as e:
                print(f"跳过行: {line}，原因: {e}")

# 按score降序排序
all_rows.sort(key=lambda x: x[1], reverse=True)

with open(output_file, 'w', encoding='utf-8') as f:
    for seq, score in all_rows:
        f.write(f"{seq},[[{score:.10f}]]\n")

print(f"合并并排序完成，结果已保存到 {output_file}") 