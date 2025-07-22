import os

def convert_rna_to_dna_in_file(input_file, output_file):
    """
    读取包含RNA序列的输入文件，将其转换为DNA序列 (U -> T),
    并将结果写入新的文件。

    此脚本假定RNA序列是每行中第一个逗号前的部分。
    """
    try:
        with open(input_file, 'r', encoding='gbk') as infile, \
             open(output_file, 'w', encoding='utf-8') as outfile:
            
            line_count = 0
            for line in infile:
                line_count += 1
                # 按第一个逗号分割行来获取RNA序列
                parts = line.split(',', 1)
                rna_sequence = parts[0]
                
                # 将 RNA 序列中的 'U' 替换为 'T'
                dna_sequence = rna_sequence.replace('U', 'T')
                
                if len(parts) > 1:
                    # 用转换后的DNA序列重新组合行
                    new_line = dna_sequence + ',' + parts[1]
                else:
                    # 如果行中没有逗号，则假定整行都是序列
                    new_line = dna_sequence
                
                outfile.write(new_line)

        print(f"处理完成! 共处理 {line_count} 行。")
        print(f"文件 '{input_file}' 已成功转换为 '{output_file}'")

    except FileNotFoundError:
        print(f"错误: 输入文件 '{input_file}' 未找到。")
    except UnicodeDecodeError:
        print(f"错误: 文件 '{input_file}' 的编码不是 'gbk'。请尝试其他编码。")
    except Exception as e:
        print(f"处理文件时发生错误: {e}")

if __name__ == "__main__":
    # 设定输入和输出文件名
    # 默认使用 '207_candidates.csv'，因为这是用户当前打开的文件。
    input_filename = '207_candidates.csv'
    
    # 检查输入文件是否存在
    if not os.path.exists(input_filename):
        print(f"错误: 输入文件 '{input_filename}' 不存在。")
    else:
        # 基于输入文件名创建输出文件名
        file_name, file_ext = os.path.splitext(input_filename)
        output_filename = f"{file_name}_dna.csv"
        
        # 执行转换
        convert_rna_to_dna_in_file(input_filename, output_filename) 