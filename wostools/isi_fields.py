"""
The wos fields definitions.
"""

import collections


IsiField = collections.namedtuple(
    'IsiField',
    ['key', 'description', 'parse', 'aliases']
)

FIELDS = {
    'AB': IsiField(
        'AB',
        'Abstract',
        lambda seq: ' '.join(seq),
        ['abstract']
    ),
    'AF': IsiField(
        'AF',
        'Author Full Name',
        lambda seq: ' '.join(seq),
        ['author_full_name']
    ),
    'AR': IsiField(
        'AR',
        'Article Number',
        lambda seq: ' '.join(seq),
        ['article_number']
    ),
    'AU': IsiField(
        'AU',
        'Authors',
        lambda seq: ' '.join(seq),
        ['authors']
    ),
    'BA': IsiField(
        'BA',
        'Book Authors',
        lambda seq: ' '.join(seq),
        ['book_authors']
    ),
    'BE': IsiField(
        'BE',
        'Editors',
        lambda seq: ' '.join(seq),
        ['editors']
    ),
    'BF': IsiField(
        'BF',
        'Book Authors Full Name',
        lambda seq: ' '.join(seq),
        ['book_authors_full_name']
    ),
    'BN': IsiField(
        'BN',
        'International Standard Book Number (ISBN)',
        lambda seq: ' '.join(seq),
        ['international_standard_book_number']
    ),
    'BP': IsiField(
        'BP',
        'Beginning Page',
        lambda seq: ' '.join(seq),
        ['beginning_page']
    ),
    'BS': IsiField(
        'BS',
        'Book Series Subtitle',
        lambda seq: ' '.join(seq),
        ['book_series_subtitle']
    ),
    'C1': IsiField(
        'C1',
        'Author Address',
        lambda seq: ' '.join(seq),
        ['author_address']
    ),
    'CA': IsiField(
        'CA',
        'Group Authors',
        lambda seq: ' '.join(seq),
        ['group_authors']
    ),
    'CL': IsiField(
        'CL',
        'Conference Location',
        lambda seq: ' '.join(seq),
        ['conference_location']
    ),
    'CR': IsiField(
        'CR',
        'Cited References',
        lambda seq: ' '.join(seq),
        ['cited_references']
    ),
    'CT': IsiField(
        'CT',
        'Conference Title',
        lambda seq: ' '.join(seq),
        ['conference_title']
    ),
    'CY': IsiField(
        'CY',
        'Conference Date',
        lambda seq: ' '.join(seq),
        ['conference_date']
    ),
    'CL': IsiField(
        'CL',
        'Conference Location',
        lambda seq: ' '.join(seq),
        ['conference_location']
    ),
    'DE': IsiField(
        'DE',
        'Author Keywords',
        lambda seq: ' '.join(seq),
        ['author_keywords']
    ),
    'DI': IsiField(
        'DI',
        'Digital Object Identifier (DOI)',
        lambda seq: ' '.join(seq),
        ['digital_object_identifier']
    ),
    'DT': IsiField(
        'DT',
        'Document Type',
        lambda seq: ' '.join(seq),
        ['document_type']
    ),
    'D2': IsiField(
        'D2',
        'Book Digital Object Identifier (DOI)',
        lambda seq: ' '.join(seq),
        ['book_digital_object_identifier']
    ),
    'ED': IsiField(
        'ED',
        'Editors',
        lambda seq: ' '.join(seq),
        ['editors']
    ),
    'EM': IsiField(
        'EM',
        'E-mail Address',
        lambda seq: ' '.join(seq),
        ['e-mail_address']
    ),
    'EI': IsiField(
        'EI',
        'Electronic International Standard Serial Number (eISSN)',
        lambda seq: ' '.join(seq),
        ['eissn']
    ),
    'EP': IsiField(
        'EP',
        'Ending Page',
        lambda seq: ' '.join(seq),
        ['ending_page']
    ),
    'FU': IsiField(
        'FU',
        'Funding Agency and Grant Number',
        lambda seq: ' '.join(seq),
        ['funding_agency_and_grant_number']
    ),
    'FX': IsiField(
        'FX',
        'Funding Text',
        lambda seq: ' '.join(seq),
        ['funding_text']
    ),
    'GA': IsiField(
        'GA',
        'Document Delivery Number',
        lambda seq: ' '.join(seq),
        ['document_delivery_number']
    ),
    'GP': IsiField(
        'GP',
        'Book Group Authors',
        lambda seq: ' '.join(seq),
        ['book_group_authors']
    ),
    'HO': IsiField(
        'HO',
        'Conference Host',
        lambda seq: ' '.join(seq),
        ['conference_host']
    ),
    'ID': IsiField(
        'ID',
        'Keywords Plus',
        lambda seq: ' '.join(seq),
        ['keywords_plus']
    ),
    'IS': IsiField(
        'IS',
        'Issue',
        lambda seq: ' '.join(seq),
        ['issue']
    ),
    'J9': IsiField(
        'J9',
        '29-Character Source Abbreviation',
        lambda seq: ' '.join(seq),
        ['source_abbreviation']
    ),
    'JI': IsiField(
        'JI',
        'ISO Source Abbreviation',
        lambda seq: ' '.join(seq),
        ['iso_source_abbreviation']
    ),
    'LA': IsiField(
        'LA',
        'Language',
        lambda seq: ' '.join(seq),
        ['language']
    ),
    'MA': IsiField(
        'MA',
        'Meeting Abstract',
        lambda seq: ' '.join(seq),
        ['meeting_abstract']
    ),
    'NR': IsiField(
        'NR',
        'Cited Reference Count',
        lambda seq: ' '.join(seq),
        ['cited_reference_count']
    ),
    'OI': IsiField(
        'OI',
        'ORCID Identifier (Open Researcher and Contributor ID)',
        lambda seq: ' '.join(seq),
        ['orcid_identifier']
    ),
    'P2': IsiField(
        'P2',
        'Chapter count (Book Citation Index)',
        lambda seq: ' '.join(seq),
        ['chapter_count']
    ),
    'PA': IsiField(
        'PA',
        'Publisher Address',
        lambda seq: ' '.join(seq),
        ['publisher_address']
    ),
    'PD': IsiField(
        'PD',
        'Publication Date',
        lambda seq: ' '.join(seq),
        ['publication_date']
    ),
    'PG': IsiField(
        'PG',
        'Page Count',
        lambda seq: ' '.join(seq),
        ['page_count']
    ),
    'PI': IsiField(
        'PI',
        'Publisher City',
        lambda seq: ' '.join(seq),
        ['publisher_city']
    ),
    'PM': IsiField(
        'PM',
        'PubMed ID',
        lambda seq: ' '.join(seq),
        ['pubmed_id']
    ),
    'PN': IsiField(
        'PN',
        'Part Number',
        lambda seq: ' '.join(seq),
        ['part_number']
    ),
    'PT': IsiField(
        'PT',
        'Publication Type (J=Journal; B=Book; S=Series; P=Patent)',
        lambda seq: ' '.join(seq),
        ['publication_type']
    ),
    'PU': IsiField(
        'PU',
        'Publisher',
        lambda seq: ' '.join(seq),
        ['publisher']
    ),
    'PY': IsiField(
        'PY',
        'Year Published',
        lambda seq: ' '.join(seq),
        ['year_published']
    ),
    'RI': IsiField(
        'RI',
        'ResearcherID Number',
        lambda seq: ' '.join(seq),
        ['researcherid_number']
    ),
    'RP': IsiField(
        'RP',
        'Reprint Address',
        lambda seq: ' '.join(seq),
        ['reprint_address']
    ),
    'SC': IsiField(
        'SC',
        'Research Areas',
        lambda seq: ' '.join(seq),
        ['research_areas']
    ),
    'SE': IsiField(
        'SE',
        'Book Series Title',
        lambda seq: ' '.join(seq),
        ['book_series_title']
    ),
    'SI': IsiField(
        'SI',
        'Special Issue',
        lambda seq: ' '.join(seq),
        ['special_issue']
    ),
    'SN': IsiField(
        'SN',
        'International Standard Serial Number (ISSN)',
        lambda seq: ' '.join(seq),
        ['issn']
    ),
    'SO': IsiField(
        'SO',
        'Publication Name',
        lambda seq: ' '.join(seq),
        ['publication_name']
    ),
    'SP': IsiField(
        'SP',
        'Conference Sponsors',
        lambda seq: ' '.join(seq),
        ['conference_sponsors']
    ),
    'SU': IsiField(
        'SU',
        'Supplement',
        lambda seq: ' '.join(seq),
        ['supplement']
    ),
    'TC': IsiField(
        'TC',
        'Web of Science Core Collection Times Cited Count',
        lambda seq: ' '.join(seq),
        ['wos_times_cited_count']
    ),
    'TI': IsiField(
        'TI',
        'Document Title',
        lambda seq: ' '.join(seq),
        ['title']
    ),
    'U1': IsiField(
        'U1',
        'Usage Count (Last 180 Days)',
        lambda seq: ' '.join(seq),
        ['usage_count']
    ),
    'U2': IsiField(
        'U2',
        'Usage Count (Since 2013)',
        lambda seq: ' '.join(seq),
        ['usage_count']
    ),
    'UT': IsiField(
        'UT',
        'Unique Article Identifier',
        lambda seq: ' '.join(seq),
        ['unique_article_identifier']
    ),
    'VL': IsiField(
        'VL',
        'Volume',
        lambda seq: ' '.join(seq),
        ['volume']
    ),
    'WC': IsiField(
        'WC',
        'Web of Science Categories',
        lambda seq: ' '.join(seq),
        ['web_of_science_categories']
    ),
    'Z9': IsiField(
        'Z9',
        'Total Times Cited Count (WoS Core, BCI, and CSCD)',
        lambda seq: ' '.join(seq),
        ['total_times_cited_count']
    ),
}
