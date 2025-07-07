#!/bin/bash

APTAMER_DIR="./Aptamer"
PROTEIN_DIR="./Protein"

APTAMER_OUT="./Aptamer_m"
PROTEIN_OUT="./Protein"

mkdir -p "${APTAMER_OUT}"

RECEPTOR_ORI="${PROTEIN_DIR}/6k4j_clean.pdb"
RECEPTOR_MOD="${PROTEIN_OUT}/6k4j_clean_m.pdb"

if [ ! -f "${RECEPTOR_MOD}" ]; then
    echo "Processing receptor: ${RECEPTOR_ORI} → ${RECEPTOR_MOD}"
    ./mark_sur "${RECEPTOR_ORI}" "${RECEPTOR_MOD}"
else
    echo "Receptor already processed: ${RECEPTOR_MOD}"
fi

for LIGAND in "${APTAMER_DIR}"/*.pdb; do
    BASENAME=$(basename "${LIGAND}" .pdb)
    LIGAND_OUT="${APTAMER_OUT}/${BASENAME}_m.pdb"
    echo "Processing ligand: ${LIGAND} → ${LIGAND_OUT}"
    ./mark_sur "${LIGAND}" "${LIGAND_OUT}"
done
