###
#
# Annotated Variant File Generation (Variant File Format 1.01)
#
#
###

import argparse

parser = argparse.ArgumentParser()

parser.add_argument(
        'infile',
        help = 'Annotated variant file, annotated by ANNOVAR.',
        type = str)
parser.add_argument(
        'outfile',
        help = 'Outfile with annotated variants in input format for IRMA.',
        type = str)

args = parser.parse_args()



header = '#chr\tstart\tend\tref\tobs\tgenotype\tsnp_q\tdepth\tmap_q\tvariant\tvariant_frequency\tregion\tgene\tvariant_details\tcoding\t1000g_2012feb\tdbSNP_137\tljb2_phylop\tljb2_mt\tljb2_sift\tljb2_pp2hvar\tljb2_pp2hdiv\tesp6500si_ea\tcosmic64\tRepeatMasker\tOMIM\tClinVar\thdb_hom_24\tihdb_het_24\tihdb_wt_24\tihdb_allsys\tclassification\tvalidated\ttum_variant_freq\ttum_variant_depth\tref_variant_freq\tref_variant_depth\trna_tum_freq\trna_tum_depth\n'

newLine = '%s\t%s\t%s\t%s\t%s\t.\t%s\t%s\t.\t%s\t%s\t%s\t%s\t%s\t%s\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\n'

with open(args.infile, 'r') as variants:
        with open(args.outfile, 'w') as outVariants:
                outVariants.write(header)
                for line in variants:
                        variantInfo = line.split('\t')
                        variantDetails = variantInfo[1]
                        coding = variantInfo[2]
                        gene = coding.split(':')[0]
                        chromosome = variantInfo[3]
                        start = variantInfo[4]
                        end = variantInfo[5]
                        ref = variantInfo[6]
                        obs = variantInfo[7]
                        freq = variantInfo[8]
                        depth = variantInfo[10]
                        region = 'exonic'

                        outVariants.write(newLine % (chromosome, start, end, ref, obs, 0, depth, 'SNV', freq, region, gene, variantDetails, coding))
