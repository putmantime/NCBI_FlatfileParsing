import urllib.request
import pandas as pd
import gzip

__author__ = 'timputman'

def get_ref_ftp_path(taxid):
    """
    download genome.fasta file form NCBI FTP site by taxid
    :param taxid: str ex. '471472'
    :return: genome.fna.gz
    """
    #  Find the ftp path for the file in assembly_summary.txt using taxid as lookup key
    assembly = urllib.request.urlretrieve("ftp://ftp.ncbi.nlm.nih.gov/genomes/refseq/bacteria/assembly_summary.txt")
    columns = ['assembly_accession', 'bioproject', 'biosample', 'wgs_master', 'refseq_category', 'taxid',
               'species_taxid', 'organism_name', 'infraspecific_name', 'isolate', 'version_status', 'assembly_level',
               'release_type', 'genome_rep', 'seq_rel_date', 'asm_name', 'submitter', 'gbrs_paired_asm',
               'paired_asm_comp', 'ftp_path', 'excluded_from_refseq']
    # load into pandas dataframe with ammended columns
    data = pd.read_csv(assembly[0], sep="\t", dtype=object, skiprows=2, names=columns)
    # select row by taxid
    selected = data[data['taxid'] == taxid]
    # get ftp file path
    ftp_path = selected.iloc[0]['ftp_path']
    file_name = ftp_path.split('/')[-1]

    url = ftp_path + '/' + file_name + '_genomic.fna.gz'
    #download ftp file to current directory
    genome = urllib.request.urlretrieve(url, file_name + '_genomic.fna.gz')

    return genome


genome = get_ref_ftp_path('471472')