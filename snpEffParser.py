import vcf
import re

def snpeff_annotation_to_gsvar_1(file, outfile):
	gsvarheader='#chr	start	end	ref	obs	genotype	snp_q	depth	map_q	variant	variant_frequency	region	gene	variant_type	coding_and_splicing	1000g_2012feb	dbSNP_137	ljb2_phylop	ljb2_mt	ljb2_sift	ljb2_pp2hvar	ljb2_pp2hdiv	esp6500si_ea	cosmic64	RepeatMasker	OMIM	ClinVar	hdb_hom_24	ihdb_het_24	ihdb_wt_24	ihdb_allsys	classification	validated	tum_variant_freq	tum_variant_depth	ref_variant_freq	ref_variant_depth	rna_tum_freq	rna_tum_depth'
	gsvarline='%s\t%s\t%s\t%s\t%s\t.\t%s\t%s\t.\t%s\t%s\t%s\t%s\t%s\t%s\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\t.\n'
	vcf_reader = vcf.Reader(open(file, 'r'))
	with open(outfile, 'w') as output:
		output.write('%s\n' % gsvarheader)
		for record in vcf_reader:
			depth = ''
			for sample in record.samples:
				depth += "{}:{},".format(sample.sample, sample['DP'])
			depth = depth[:-1]
			if 'ANN' in record.INFO:
				coding = []
                                variant = []
                                region = []
                                variantDetails = []
				for a in record.INFO['ANN']:
					cCoding = ''
					pCoding = ''
					annotations = a.split('|')
					variantDetails.append(annotations[1])
                                        variant.append(annotations[1])
					region.append(annotations[5])
					if 'HOM' in record.INFO and record.INFO['HOM'] == 1:
						frequency = 1
					elif 'AF' in record.INFO:
						frequency = record.INFO['AF'][0]
					else:
						frequency = 0.5
					gene = annotations[3]
					transcript = annotations[6]
					featureNum = annotations[8].split('/')[0]
					cCoding = annotations[9]
					pCoding = annotations[10]
                                        mod = annotations[2] 
					coding.append('%s:%s:%s:%s:exon%s:%s:%s,' % (gene,transcript,annotations[1],mod,featureNum,cCoding,pCoding))
				if coding != '':
					output.write(gsvarline % (record.CHROM, record.POS, record.POS, record.REF, record.ALT[0], 0, depth, ','.join(set(variant)), frequency, ','.join(set(region)), gene, ','.join(set(variantDetails)), ','.join(coding)))
			elif 'LOF' in record.INFO:
				pass
			elif 'NMD' in record.INFO:
				pass
			
		
