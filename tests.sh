#! /usr/bin/env bash

echo
echo
echo
echo
echo
echo
echo "===================================================================="
echo
echo
echo
echo "                 TEST: simple example" 
echo
echo
echo
echo "===================================================================="
echo
echo
echo

(
	set -ex -o pipefail; 

	rm -fR ~/.smbl
	cd examples
	snakemake -p
)

echo
echo
echo
echo
echo
echo
echo "===================================================================="
echo
echo
echo
echo "                 TEST: single-threading installation" 
echo
echo
echo
echo "===================================================================="
echo
echo
echo

(
	exit 0
	set -ex -o pipefail; 

	rm -fR ~/.smbl
	snakemake -p -s ./smbl/prog/prog.snake
	rm -fR ~/.smbl
	snakemake -p -s ./smbl/fasta/fasta.snake
)

echo
echo
echo
echo
echo
echo
echo "===================================================================="
echo
echo
echo
echo "                 TEST: multi-threading installation" 
echo
echo
echo
echo "===================================================================="
echo
echo
echo

(
	set -ex -o pipefail; 

	snakemake -s tests/Snakefile.all_programs -p --cores 16
)
