#!/bin/bash
module load qbic/anaconda2/2.1.0
module load qbic/annovar/0.1

convert2annovar.pl -format vcf4 $1 -outfile $2'/variants.avinput' -allsample -withfreq -includeinfo
annotate_variation.pl -buildver hg19 $2'/variants.avinput' /lustre_cfc/qbic/reference_genomes/humandb_annovar/ --otherinfo --infoasscore

python generateAnnotatedVariants.py $2'/variants.avinput'.exonic_variant_function /lustre_cfc/qbic/chris/variantAnno/testVariants.annotated
