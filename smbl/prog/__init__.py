import os
import smbl
import smbl.prog.plugins


all_platforms = ["linux","windows","macos","cygwin"]

from smbl.prog.plugins import *

ART_454            = os.path.join(smbl.bin_dir,"art_454")
ART_ILLUMINA       = os.path.join(smbl.bin_dir,"art_illumina")
ART_SOLID          = os.path.join(smbl.bin_dir,"art_solid")
BCFTOOLS           = os.path.join(smbl.bin_dir,"bcftools")
BFAST              = os.path.join(smbl.bin_dir,"bfast")
BGZIP              = os.path.join(smbl.bin_dir,"bgzip")
BOWTIE2            = os.path.join(smbl.bin_dir,"bowtie2")
BOWTIE2_ALIGN_L    = os.path.join(smbl.bin_dir,"bowtie2-align-l")
BOWTIE2_ALIGN_S    = os.path.join(smbl.bin_dir,"bowtie2-align-s")
BOWTIE2_BUILD      = os.path.join(smbl.bin_dir,"bowtie2-build")
BOWTIE2_BUILD_L    = os.path.join(smbl.bin_dir,"bowtie2-build-l")
BOWTIE2_BUILD_S    = os.path.join(smbl.bin_dir,"bowtie2-build-s")
BOWTIE2_INSPECT    = os.path.join(smbl.bin_dir,"bowtie2-inspect")
BOWTIE2_INSPECT_L  = os.path.join(smbl.bin_dir,"bowtie2-inspect-l")
BOWTIE2_INSPECT_S  = os.path.join(smbl.bin_dir,"bowtie2-inspect-s")
CURESIM            = os.path.join(smbl.bin_dir,"curesim.jar")
CURESIM_EVAL       = os.path.join(smbl.bin_dir,"curesim_eval.jar")
DRFAST             = os.path.join(smbl.bin_dir,"drfast")
#DWGSIM             = os.path.join(smbl.bin_dir,"dwgsim")
#DWGSIM_EVAL        = os.path.join(smbl.bin_dir,"dwgsim_eval")
#FREEC              = os.path.join(smbl.bin_dir,"freec")
GEM_INDEXER        = os.path.join(smbl.bin_dir,"gem-indexer")
GEM_MAPPER         = os.path.join(smbl.bin_dir,"gem-mapper")
GEM_2_SAM          = os.path.join(smbl.bin_dir,"gem-2-sam")
GNUPLOT4           = os.path.join(smbl.bin_dir,"gnuplot4")
GNUPLOT5           = os.path.join(smbl.bin_dir,"gnuplot5")
LASTAL             = os.path.join(smbl.bin_dir,"lastal")
LASTDB             = os.path.join(smbl.bin_dir,"lastdb")
MASON_FRAG_SEQUENCING   = os.path.join(smbl.bin_dir,"mason_frag_sequencing")
MASON_GENOME            = os.path.join(smbl.bin_dir,"mason_genome")
MASON_MATERIALIZER      = os.path.join(smbl.bin_dir,"mason_materializer")
MASON_METHYLATION       = os.path.join(smbl.bin_dir,"mason_methylation")
MASON_SIMULATOR         = os.path.join(smbl.bin_dir,"mason_simulator")
MASON_SPLICING          = os.path.join(smbl.bin_dir,"mason_splicing")
MASON_VARIATOR          = os.path.join(smbl.bin_dir,"mason_variator")
MRFAST             = os.path.join(smbl.bin_dir,"mrfast")
MRSFAST            = os.path.join(smbl.bin_dir,"mrsfast")
PERM               = os.path.join(smbl.bin_dir,"perm")
PBSIM              = os.path.join(smbl.bin_dir,"pbsim")
PICARD             = os.path.join(smbl.bin_dir,"picard.jar")
SAMBAMBA           = os.path.join(smbl.bin_dir,"sambamba")
SAMTOOLS           = os.path.join(smbl.bin_dir,"samtools")
SIRFAST            = os.path.join(smbl.bin_dir,"sirfast")
STORM_COLOR        = os.path.join(smbl.bin_dir,"storm-color")
STORM_NUCLEOTIDE   = os.path.join(smbl.bin_dir,"storm-nucleotide")
TABIX              = os.path.join(smbl.bin_dir,"tabix")
TWOBITTOFA         = os.path.join(smbl.bin_dir,"twoBitToFa")
XS                 = os.path.join(smbl.bin_dir,"xs")

ALL = [
		ART_454,
		ART_ILLUMINA,
		ART_SOLID,
		BCFTOOLS,
		BFAST,
		BGZIP,

		BOWTIE2,
		BOWTIE2_ALIGN_L,
		BOWTIE2_ALIGN_S,
		BOWTIE2_BUILD,
		BOWTIE2_BUILD_L,
		BOWTIE2_BUILD_S,
		BOWTIE2_INSPECT,
		BOWTIE2_INSPECT_L,
		BOWTIE2_INSPECT_S,

#		BWA,
		CURESIM,
		CURESIM_EVAL,
#		DWGSIM,
#		DWGSIM_EVAL,
#		FREEC,
		GEM_INDEXER,
		GEM_MAPPER,
		GEM_2_SAM,
		GNUPLOT4,
		GNUPLOT5,
		LASTAL,
		LASTDB,
		MASON_FRAG_SEQUENCING,
		MASON_GENOME,
		MASON_MATERIALIZER,
		MASON_METHYLATION,
		MASON_SIMULATOR,
		MASON_SPLICING,
		MASON_VARIATOR,
		
		PBSIM,
		PERM,
		PICARD,
		SAMBAMBA,
		SAMTOOLS,
		STORM_COLOR,
		STORM_NUCLEOTIDE,
		TABIX,
		TWOBITTOFA,
#		WGSIM,
#		WGSIM_EVAL,

		MRFAST,
		MRSFAST,
		DRFAST,
		SIRFAST,

		XS,
	]

def correct_samtools_make(makefile_fn):
	makefile_backup_fn = makefile_fn+".backup"
	if not os.path.isfile(makefile_backup_fn):
		with open(makefile_fn, 'r') as makefile:
			content = makefile.read()
			if smbl.is_linux():
				content = content.replace("-lcurses","-lncurses")
			elif smbl.is_cygwin():
				content = content.replace("-D_FILE_OFFSET_BITS=64","-D_FILE_OFFSET_BITS=64 -Dexpl=exp -Dlogl=log")
		with open(makefile_fn, 'w') as makefile:
			makefile.write(content)
