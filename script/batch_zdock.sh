#!/bin/bash

# === 目录设置 ===
RECEPTOR="./Protein/6k4j_clean_m.pdb"
LIGAND_DIR="./Aptamer_m"
OUT_DIR="./zdock_results_3"

# === 创建输出目录 ===
mkdir -p "${OUT_DIR}"

# === 对每个配体执行zdock + create.pl ===
for LIGAND in "${LIGAND_DIR}"/*.pdb; do
    BASENAME=$(basename "${LIGAND}" .pdb)
    OUTFILE="${OUT_DIR}/${BASENAME}_zdock.out"
    MODELFILE="${OUT_DIR}/${BASENAME}_models.pdb"

    echo "对接 ${BASENAME} ..."

    # 运行 zdock
    ./zdock -R "${RECEPTOR}" -L "${LIGAND}" -o "${OUTFILE}"

    # 生成模型结构
    ./create.pl "${OUTFILE}" > "${MODELFILE}"
done

echo "✅ 批量 ZDOCK 对接完成，结果保存在 ${OUT_DIR}/"
