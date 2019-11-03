"""Tests for `wostools` package."""

from click.testing import CliRunner

from wostools import CollectionLazy
from wostools import cli
from wostools import Article
import pytest
import io


def test_article_label(article):
    """
    Test label value of article.
    """
    assert article.label == (
        "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061"
    )


def test_aliases(article):
    if hasattr(article, "AB"):
        assert article.AB == article.abstract
    else:
        with pytest.raises(AttributeError):
            article.AB
    if hasattr(article, "AF"):
        assert article.AF == article.author_full_names
    else:
        with pytest.raises(AttributeError):
            article.AF
    if hasattr(article, "AR"):
        assert article.AR == article.article_number
    else:
        with pytest.raises(AttributeError):
            article.AR
    if hasattr(article, "AU"):
        assert article.AU == article.authors
    else:
        with pytest.raises(AttributeError):
            article.AU
    if hasattr(article, "BA"):
        assert article.BA == article.book_authors
    else:
        with pytest.raises(AttributeError):
            article.BA
    if hasattr(article, "BE"):
        assert article.BE == article.editors
    else:
        with pytest.raises(AttributeError):
            article.BE
    if hasattr(article, "BF"):
        assert article.BF == article.book_authors_full_name
    else:
        with pytest.raises(AttributeError):
            article.BF
    if hasattr(article, "BN"):
        assert article.BN == article.international_standard_book_number
    else:
        with pytest.raises(AttributeError):
            article.BN
    if hasattr(article, "BP"):
        assert article.BP == article.beginning_page
    else:
        with pytest.raises(AttributeError):
            article.BP
    if hasattr(article, "BS"):
        assert article.BS == article.book_series_subtitle
    else:
        with pytest.raises(AttributeError):
            article.BS
    if hasattr(article, "C1"):
        assert article.C1 == article.author_address
    else:
        with pytest.raises(AttributeError):
            article.C1
    if hasattr(article, "CA"):
        assert article.CA == article.group_authors
    else:
        with pytest.raises(AttributeError):
            article.CA
    if hasattr(article, "CL"):
        assert article.CL == article.conference_location
    else:
        with pytest.raises(AttributeError):
            article.CL
    if hasattr(article, "CR"):
        assert article.CR == article.cited_references
    else:
        with pytest.raises(AttributeError):
            article.CR
    if hasattr(article, "CR"):
        assert article.CR == article.references
    else:
        with pytest.raises(AttributeError):
            article.CR
    if hasattr(article, "CR"):
        assert article.CR == article.citations
    else:
        with pytest.raises(AttributeError):
            article.CR
    if hasattr(article, "CT"):
        assert article.CT == article.conference_title
    else:
        with pytest.raises(AttributeError):
            article.CT
    if hasattr(article, "CY"):
        assert article.CY == article.conference_date
    else:
        with pytest.raises(AttributeError):
            article.CY
    if hasattr(article, "DE"):
        assert article.DE == article.author_keywords
    else:
        with pytest.raises(AttributeError):
            article.DE
    if hasattr(article, "DI"):
        assert article.DI == article.digital_object_identifier
    else:
        with pytest.raises(AttributeError):
            article.DI
    if hasattr(article, "DT"):
        assert article.DT == article.document_type
    else:
        with pytest.raises(AttributeError):
            article.DT
    if hasattr(article, "D2"):
        assert article.D2 == article.book_digital_object_identifier
    else:
        with pytest.raises(AttributeError):
            article.D2
    if hasattr(article, "ED"):
        assert article.ED == article.editors
    else:
        with pytest.raises(AttributeError):
            article.ED
    if hasattr(article, "EM"):
        assert article.EM == article.email_address
    else:
        with pytest.raises(AttributeError):
            article.EM
    if hasattr(article, "EI"):
        assert article.EI == article.eissn
    else:
        with pytest.raises(AttributeError):
            article.EI
    if hasattr(article, "EP"):
        assert article.EP == article.ending_page
    else:
        with pytest.raises(AttributeError):
            article.EP
    if hasattr(article, "FU"):
        assert article.FU == article.funding_agency_and_grant_number
    else:
        with pytest.raises(AttributeError):
            article.FU
    if hasattr(article, "FX"):
        assert article.FX == article.funding_text
    else:
        with pytest.raises(AttributeError):
            article.FX
    if hasattr(article, "GA"):
        assert article.GA == article.document_delivery_number
    else:
        with pytest.raises(AttributeError):
            article.GA
    if hasattr(article, "GP"):
        assert article.GP == article.book_group_authors
    else:
        with pytest.raises(AttributeError):
            article.GP
    if hasattr(article, "HO"):
        assert article.HO == article.conference_host
    else:
        with pytest.raises(AttributeError):
            article.HO
    if hasattr(article, "ID"):
        assert article.ID == article.keywords_plus
    else:
        with pytest.raises(AttributeError):
            article.ID
    if hasattr(article, "ID"):
        assert article.ID == article.keywords
    else:
        with pytest.raises(AttributeError):
            article.ID
    if hasattr(article, "IS"):
        assert article.IS == article.issue
    else:
        with pytest.raises(AttributeError):
            article.IS
    if hasattr(article, "J9"):
        assert article.J9 == article.source_abbreviation
    else:
        with pytest.raises(AttributeError):
            article.J9
    if hasattr(article, "JI"):
        assert article.JI == article.iso_source_abbreviation
    else:
        with pytest.raises(AttributeError):
            article.JI
    if hasattr(article, "LA"):
        assert article.LA == article.language
    else:
        with pytest.raises(AttributeError):
            article.LA
    if hasattr(article, "MA"):
        assert article.MA == article.meeting_abstract
    else:
        with pytest.raises(AttributeError):
            article.MA
    if hasattr(article, "NR"):
        assert article.NR == article.cited_reference_count
    else:
        with pytest.raises(AttributeError):
            article.NR
    if hasattr(article, "OI"):
        assert article.OI == article.orcid_identifier
    else:
        with pytest.raises(AttributeError):
            article.OI
    if hasattr(article, "P2"):
        assert article.P2 == article.chapter_count
    else:
        with pytest.raises(AttributeError):
            article.P2
    if hasattr(article, "PA"):
        assert article.PA == article.publisher_address
    else:
        with pytest.raises(AttributeError):
            article.PA
    if hasattr(article, "PD"):
        assert article.PD == article.publication_date
    else:
        with pytest.raises(AttributeError):
            article.PD
    if hasattr(article, "PG"):
        assert article.PG == article.page_count
    else:
        with pytest.raises(AttributeError):
            article.PG
    if hasattr(article, "PI"):
        assert article.PI == article.publisher_city
    else:
        with pytest.raises(AttributeError):
            article.PI
    if hasattr(article, "PM"):
        assert article.PM == article.pubmed_id
    else:
        with pytest.raises(AttributeError):
            article.PM
    if hasattr(article, "PN"):
        assert article.PN == article.part_number
    else:
        with pytest.raises(AttributeError):
            article.PN
    if hasattr(article, "PT"):
        assert article.PT == article.publication_type
    else:
        with pytest.raises(AttributeError):
            article.PT
    if hasattr(article, "PU"):
        assert article.PU == article.publisher
    else:
        with pytest.raises(AttributeError):
            article.PU
    if hasattr(article, "PY"):
        assert article.PY == article.year_published
    else:
        with pytest.raises(AttributeError):
            article.PY
    if hasattr(article, "RI"):
        assert article.RI == article.researcherid_number
    else:
        with pytest.raises(AttributeError):
            article.RI
    if hasattr(article, "RP"):
        assert article.RP == article.reprint_address
    else:
        with pytest.raises(AttributeError):
            article.RP
    if hasattr(article, "SC"):
        assert article.SC == article.research_areas
    else:
        with pytest.raises(AttributeError):
            article.SC
    if hasattr(article, "SE"):
        assert article.SE == article.book_series_title
    else:
        with pytest.raises(AttributeError):
            article.SE
    if hasattr(article, "SI"):
        assert article.SI == article.special_issue
    else:
        with pytest.raises(AttributeError):
            article.SI
    if hasattr(article, "SN"):
        assert article.SN == article.issn
    else:
        with pytest.raises(AttributeError):
            article.SN
    if hasattr(article, "SP"):
        assert article.SP == article.conference_sponsors
    else:
        with pytest.raises(AttributeError):
            article.SP
    if hasattr(article, "SU"):
        assert article.SU == article.supplement
    else:
        with pytest.raises(AttributeError):
            article.SU
    if hasattr(article, "TC"):
        assert article.TC == article.wos_times_cited_count
    else:
        with pytest.raises(AttributeError):
            article.TC
    if hasattr(article, "TC"):
        assert article.TC == article.wos_times_cited
    else:
        with pytest.raises(AttributeError):
            article.TC
    if hasattr(article, "TI"):
        assert article.TI == article.title
    else:
        with pytest.raises(AttributeError):
            article.TI
    if hasattr(article, "U1"):
        assert article.U1 == article.usage_count
    else:
        with pytest.raises(AttributeError):
            article.U1
    if hasattr(article, "U2"):
        assert article.U2 == article.usage_count
    else:
        with pytest.raises(AttributeError):
            article.U2
    if hasattr(article, "UT"):
        assert article.UT == article.unique_article_identifier
    else:
        with pytest.raises(AttributeError):
            article.UT
    if hasattr(article, "VL"):
        assert article.VL == article.volume
    else:
        with pytest.raises(AttributeError):
            article.VL
    if hasattr(article, "WC"):
        assert article.WC == article.web_of_science_categories
    else:
        with pytest.raises(AttributeError):
            article.WC
    if hasattr(article, "Z9"):
        assert article.Z9 == article.total_times_cited_count
    else:
        with pytest.raises(AttributeError):
            article.Z9
    if hasattr(article, "Z9"):
        assert article.Z9 == article.times_cited
    else:
        with pytest.raises(AttributeError):
            article.Z9


def test_parsers(article):
    assert article.PT == "J"
    assert article.AU == ["Wodarz, S", "Hasegawa, T", "Ishio, S", "Homma, T"]
    assert article.AF == [
        "Wodarz, Siggi",
        "Hasegawa, Takashi",
        "Ishio, Shunji",
        "Homma, Takayuki",
    ]
    assert (
        article.TI
        == "Structural control of ultra-fine CoPt nanodot arrays via electrodeposition process"
    )
    assert article.SO == "JOURNAL OF MAGNETISM AND MAGNETIC MATERIALS"
    assert article.LA == "English"
    assert article.DT == "Article"
    assert article.DE == [
        "Electrodeposition",
        "Structural control",
        "Nanodot array",
        "Bit-patterned media",
        "CoPt alloy",
    ]
    assert article.ID == [
        "BIT-PATTERNED MEDIA",
        "ELECTRON-BEAM LITHOGRAPHY",
        "RECORDING MEDIA",
        "MAGNETIC MEDIA",
        "DENSITY",
        "FILMS",
        "ANISOTROPY",
        "STORAGE",
    ]
    assert (
        article.AB
        == "CoPt nanodot arrays were fabricated by combining electrodeposition and electron beam lithography (EBL) for the use of bit-patterned media (BPM). To achieve precise control of deposition uniformity and coercivity of the CoPt nanodot arrays, their crystal structure and magnetic properties were controlled by controlling the diffusion state of metal ions from the initial deposition stage with the application of bath agitation. Following bath agitation, the composition gradient of the CoPt alloy with thickness was mitigated to have a near-ideal alloy composition of Co:Pt =80:20, which induces epitaxial-like growth from Ru substrate, thus resulting in the improvement of the crystal orientation of the hcp (002) structure from its initial deposition stages. Furthermore, the cross-sectional transmission electron microscope (TEM) analysis of the nanodots deposited with bath agitation showed CoPt growth along its c-axis oriented in the perpendicular direction, having uniform lattice fringes on the hcp (002) plane from the Ru underlayer interface, which is a significant factor to induce perpendicular magnetic anisotropy. Magnetic characterization of the CoPt nanodot arrays showed increase in the perpendicular coercivity and squareness of the hysteresis loops from 2.0 kOe and 0.64 (without agitation) to 4.0 kOe and 0.87 with bath agitation. Based on the detailed characterization of nanodot arrays, the precise crystal structure control of the nanodot arrays with ultra-high recording density by electrochemical process was successfully demonstrated."
    )
    assert article.C1 == [
        "[Wodarz, Siggi; Homma, Takayuki] Waseda Univ, Dept Appl Chem, Shinjuku Ku, Tokyo 1698555, Japan.",
        "[Hasegawa, Takashi; Ishio, Shunji] Akita Univ, Dept Mat Sci, Akita 0108502, Japan.",
    ]
    assert (
        article.RP
        == "Homma, T (reprint author), Waseda Univ, Dept Appl Chem, Shinjuku Ku, Tokyo 1698555, Japan."
    )
    assert article.EM == ["t.homma@waseda.jp"]
    assert article.OI == ["Hasegawa, Takashi/0000-0002-8178-4980"]
    assert article.FU == ["JSPS KAKENHI Grant [25249104]"]
    assert (
        article.FX
        == "This work was supported in part by JSPS KAKENHI Grant Number 25249104."
    )
    assert article.CR == [
        "Albrecht TR, 2013, IEEE T MAGN, V49, P773, DOI 10.1109/TMAG.2012.2227303",
        "BUSCHOW KHJ, 1983, J MAGN MAGN MATER, V38, P1, DOI 10.1016/0304-8853(83)90097-5",
        "Gapin AI, 2006, J APPL PHYS, V99, DOI 10.1063/1.2163289",
        "Homma Takayuki, 2015, ECS Transactions, V64, P1, DOI 10.1149/06431.0001ecst",
        "Kryder MH, 2008, P IEEE, V96, P1810, DOI 10.1109/JPROC.2008.2004315",
        "Kubo T, 2005, J APPL PHYS, V97, DOI 10.1063/1.1855572",
        "Lodder JC, 2004, J MAGN MAGN MATER, V272, P1692, DOI 10.1016/j.jmmm.2003.12.259",
        "Mitsuzuka K, 2007, IEEE T MAGN, V43, P2160, DOI 10.1109/TMAG.2007.893129",
        "Ouchi T, 2010, ELECTROCHIM ACTA, V55, P8081, DOI 10.1016/j.electacta.2010.02.073",
        "Pattanaik G, 2006, J APPL PHYS, V99, DOI 10.1063/1.2150805",
        "Pattanaik G, 2007, ELECTROCHIM ACTA, V52, P2755, DOI 10.1016/j.electacta.2006.07.062",
        "Piramanayagam SN, 2009, J MAGN MAGN MATER, V321, P485, DOI 10.1016/j.jmmm.2008.05.007",
        "Ross CA, 2008, MRS BULL, V33, P838, DOI 10.1557/mrs2008.179",
        "Shiroishi Y, 2009, IEEE T MAGN, V45, P3816, DOI 10.1109/TMAG.2009.2024879",
        "Sirtori V, 2011, ACS APPL MATER INTER, V3, P1800, DOI 10.1021/am200267u",
        "Sohn JS, 2009, NANOTECHNOLOGY, V20, DOI 10.1088/0957-4484/20/2/025302",
        "Sun SH, 2000, SCIENCE, V287, P1989, DOI 10.1126/science.287.5460.1989",
        "Terris BD, 2007, MICROSYST TECHNOL, V13, P189, DOI 10.1007/s00542-006-0144-9",
        "Wang JP, 2008, P IEEE, V96, P1847, DOI 10.1109/JPROC.2008.2004318",
        "Weller D, 1999, IEEE T MAGN, V35, P4423, DOI 10.1109/20.809134",
        "Weller D, 2000, IEEE T MAGN, V36, P10, DOI 10.1109/20.824418",
        "Wodarz S, 2016, ELECTROCHIM ACTA, V197, P330, DOI 10.1016/j.electacta.2015.11.136",
        "Xu X, 2012, J ELECTROCHEM SOC, V159, pD240, DOI 10.1149/2.090204jes",
        "Yang X, 2007, J VAC SCI TECHNOL B, V25, P2202, DOI 10.1116/1.2798711",
        "Yang XM, 2009, ACS NANO, V3, P1844, DOI 10.1021/nn900073r",
        "Yasui N, 2003, APPL PHYS LETT, V83, P3347, DOI 10.1063/1.1622787",
        "Yua H., 2009, J APPL PHYS, V105",
        "Zhu JG, 2008, IEEE T MAGN, V44, P125, DOI 10.1109/TMAG.2007.911031",
    ]
    assert article.NR == 28
    assert article.TC == 0
    assert article.Z9 == 0
    assert article.U1 == 21
    assert article.U2 == 21
    assert article.PU == "ELSEVIER SCIENCE BV"
    assert article.PI == "AMSTERDAM"
    assert article.PA == "PO BOX 211, 1000 AE AMSTERDAM, NETHERLANDS"
    assert article.SN == "0304-8853"
    assert article.EI == "1873-4766"
    assert article.J9 == "J MAGN MAGN MATER"
    assert article.JI == "J. Magn. Magn. Mater."
    assert article.PD == "MAY 15"
    assert article.PY == 2017
    assert article.VL == "430"
    assert article.BP == "52"
    assert article.EP == "58"
    assert article.DI == "10.1016/j.jmmm.2017.01.061"
    assert article.PG == 7
    assert article.WC == [
        "Materials Science, Multidisciplinary",
        "Physics, Condensed Matter",
    ]
    assert article.SC == ["Materials Science", "Physics"]
    assert article.GA == "EP2GP"
    assert article.UT == "WOS:000397201600008"


def test_article_attributes(article):
    assert set(article.keys()) == {
        "PT",
        "AU",
        "AF",
        "TI",
        "SO",
        "LA",
        "DT",
        "DE",
        "ID",
        "AB",
        "C1",
        "RP",
        "EM",
        "OI",
        "FU",
        "FX",
        "CR",
        "NR",
        "TC",
        "Z9",
        "U1",
        "U2",
        "PU",
        "PI",
        "PA",
        "SN",
        "EI",
        "J9",
        "JI",
        "PD",
        "PY",
        "VL",
        "BP",
        "EP",
        "DI",
        "PG",
        "WC",
        "SC",
        "GA",
        "UT",
    }


def test_article_raw_data(article):
    raw_data = article.raw_data
    assert "ER" not in raw_data
    assert raw_data["PT"] == ["J"]
    assert raw_data["AU"] == ["Wodarz, S", "Hasegawa, T", "Ishio, S", "Homma, T"]
    assert raw_data["AF"] == [
        "Wodarz, Siggi",
        "Hasegawa, Takashi",
        "Ishio, Shunji",
        "Homma, Takayuki",
    ]
    assert raw_data["TI"] == [
        "Structural control of ultra-fine CoPt nanodot arrays via",
        "electrodeposition process",
    ]
    assert raw_data["SO"] == ["JOURNAL OF MAGNETISM AND MAGNETIC MATERIALS"]
    assert raw_data["LA"] == ["English"]
    assert raw_data["DT"] == ["Article"]
    assert raw_data["DE"] == [
        "Electrodeposition; Structural control; Nanodot array; Bit-patterned",
        "media; CoPt alloy",
    ]
    assert raw_data["ID"] == [
        "BIT-PATTERNED MEDIA; ELECTRON-BEAM LITHOGRAPHY; RECORDING MEDIA;",
        "MAGNETIC MEDIA; DENSITY; FILMS; ANISOTROPY; STORAGE",
    ]
    assert raw_data["AB"] == [
        "CoPt nanodot arrays were fabricated by combining electrodeposition and electron beam lithography (EBL) for the use of bit-patterned media (BPM). To achieve precise control of deposition uniformity and coercivity of the CoPt nanodot arrays, their crystal structure and magnetic properties were controlled by controlling the diffusion state of metal ions from the initial deposition stage with the application of bath agitation. Following bath agitation, the composition gradient of the CoPt alloy with thickness was mitigated to have a near-ideal alloy composition of Co:Pt =80:20, which induces epitaxial-like growth from Ru substrate, thus resulting in the improvement of the crystal orientation of the hcp (002) structure from its initial deposition stages. Furthermore, the cross-sectional transmission electron microscope (TEM) analysis of the nanodots deposited with bath agitation showed CoPt growth along its c-axis oriented in the perpendicular direction, having uniform lattice fringes on the hcp (002) plane from the Ru underlayer interface, which is a significant factor to induce perpendicular magnetic anisotropy. Magnetic characterization of the CoPt nanodot arrays showed increase in the perpendicular coercivity and squareness of the hysteresis loops from 2.0 kOe and 0.64 (without agitation) to 4.0 kOe and 0.87 with bath agitation. Based on the detailed characterization of nanodot arrays, the precise crystal structure control of the nanodot arrays with ultra-high recording density by electrochemical process was successfully demonstrated."
    ]
    assert raw_data["C1"] == [
        "[Wodarz, Siggi; Homma, Takayuki] Waseda Univ, Dept Appl Chem, Shinjuku Ku, Tokyo 1698555, Japan.",
        "[Hasegawa, Takashi; Ishio, Shunji] Akita Univ, Dept Mat Sci, Akita 0108502, Japan.",
    ]
    assert raw_data["RP"] == [
        "Homma, T (reprint author), Waseda Univ, Dept Appl Chem, Shinjuku Ku, Tokyo 1698555, Japan."
    ]
    assert raw_data["EM"] == ["t.homma@waseda.jp"]
    assert raw_data["OI"] == ["Hasegawa, Takashi/0000-0002-8178-4980"]
    assert raw_data["FU"] == ["JSPS KAKENHI Grant [25249104]"]
    assert raw_data["FX"] == [
        "This work was supported in part by JSPS KAKENHI Grant Number 25249104."
    ]
    assert raw_data["CR"] == [
        "Albrecht TR, 2013, IEEE T MAGN, V49, P773, DOI 10.1109/TMAG.2012.2227303",
        "BUSCHOW KHJ, 1983, J MAGN MAGN MATER, V38, P1, DOI 10.1016/0304-8853(83)90097-5",
        "Gapin AI, 2006, J APPL PHYS, V99, DOI 10.1063/1.2163289",
        "Homma Takayuki, 2015, ECS Transactions, V64, P1, DOI 10.1149/06431.0001ecst",
        "Kryder MH, 2008, P IEEE, V96, P1810, DOI 10.1109/JPROC.2008.2004315",
        "Kubo T, 2005, J APPL PHYS, V97, DOI 10.1063/1.1855572",
        "Lodder JC, 2004, J MAGN MAGN MATER, V272, P1692, DOI 10.1016/j.jmmm.2003.12.259",
        "Mitsuzuka K, 2007, IEEE T MAGN, V43, P2160, DOI 10.1109/TMAG.2007.893129",
        "Ouchi T, 2010, ELECTROCHIM ACTA, V55, P8081, DOI 10.1016/j.electacta.2010.02.073",
        "Pattanaik G, 2006, J APPL PHYS, V99, DOI 10.1063/1.2150805",
        "Pattanaik G, 2007, ELECTROCHIM ACTA, V52, P2755, DOI 10.1016/j.electacta.2006.07.062",
        "Piramanayagam SN, 2009, J MAGN MAGN MATER, V321, P485, DOI 10.1016/j.jmmm.2008.05.007",
        "Ross CA, 2008, MRS BULL, V33, P838, DOI 10.1557/mrs2008.179",
        "Shiroishi Y, 2009, IEEE T MAGN, V45, P3816, DOI 10.1109/TMAG.2009.2024879",
        "Sirtori V, 2011, ACS APPL MATER INTER, V3, P1800, DOI 10.1021/am200267u",
        "Sohn JS, 2009, NANOTECHNOLOGY, V20, DOI 10.1088/0957-4484/20/2/025302",
        "Sun SH, 2000, SCIENCE, V287, P1989, DOI 10.1126/science.287.5460.1989",
        "Terris BD, 2007, MICROSYST TECHNOL, V13, P189, DOI 10.1007/s00542-006-0144-9",
        "Wang JP, 2008, P IEEE, V96, P1847, DOI 10.1109/JPROC.2008.2004318",
        "Weller D, 1999, IEEE T MAGN, V35, P4423, DOI 10.1109/20.809134",
        "Weller D, 2000, IEEE T MAGN, V36, P10, DOI 10.1109/20.824418",
        "Wodarz S, 2016, ELECTROCHIM ACTA, V197, P330, DOI 10.1016/j.electacta.2015.11.136",
        "Xu X, 2012, J ELECTROCHEM SOC, V159, pD240, DOI 10.1149/2.090204jes",
        "Yang X, 2007, J VAC SCI TECHNOL B, V25, P2202, DOI 10.1116/1.2798711",
        "Yang XM, 2009, ACS NANO, V3, P1844, DOI 10.1021/nn900073r",
        "Yasui N, 2003, APPL PHYS LETT, V83, P3347, DOI 10.1063/1.1622787",
        "Yua H., 2009, J APPL PHYS, V105",
        "Zhu JG, 2008, IEEE T MAGN, V44, P125, DOI 10.1109/TMAG.2007.911031",
    ]
    assert raw_data["NR"] == ["28"]
    assert raw_data["TC"] == ["0"]
    assert raw_data["Z9"] == ["0"]
    assert raw_data["U1"] == ["21"]
    assert raw_data["U2"] == ["21"]
    assert raw_data["PU"] == ["ELSEVIER SCIENCE BV"]
    assert raw_data["PI"] == ["AMSTERDAM"]
    assert raw_data["PA"] == ["PO BOX 211, 1000 AE AMSTERDAM, NETHERLANDS"]
    assert raw_data["SN"] == ["0304-8853"]
    assert raw_data["EI"] == ["1873-4766"]
    assert raw_data["J9"] == ["J MAGN MAGN MATER"]
    assert raw_data["JI"] == ["J. Magn. Magn. Mater."]
    assert raw_data["PD"] == ["MAY 15"]
    assert raw_data["PY"] == ["2017"]
    assert raw_data["VL"] == ["430"]
    assert raw_data["BP"] == ["52"]
    assert raw_data["EP"] == ["58"]
    assert raw_data["DI"] == ["10.1016/j.jmmm.2017.01.061"]
    assert raw_data["PG"] == ["7"]
    assert raw_data["WC"] == [
        "Materials Science, Multidisciplinary; Physics, Condensed Matter"
    ]
    assert raw_data["SC"] == ["Materials Science; Physics"]
    assert raw_data["GA"] == ["EP2GP"]
    assert raw_data["UT"] == ["WOS:000397201600008"]


def test_article_data(article):
    data = article.data
    assert data.get("AB") == data.get("abstract")
    assert data.get("AF") == data.get("author_full_names")
    assert data.get("AR") == data.get("article_number")
    assert data.get("AU") == data.get("authors")
    assert data.get("BA") == data.get("book_authors")
    assert data.get("BE") == data.get("editors")
    assert data.get("BF") == data.get("book_authors_full_name")
    assert data.get("BN") == data.get("international_standard_book_number")
    assert data.get("BP") == data.get("beginning_page")
    assert data.get("BS") == data.get("book_series_subtitle")
    assert data.get("C1") == data.get("author_address")
    assert data.get("CA") == data.get("group_authors")
    assert data.get("CL") == data.get("conference_location")
    assert data.get("CR") == data.get("cited_references")
    assert data.get("CR") == data.get("references")
    assert data.get("CR") == data.get("citations")
    assert data.get("CT") == data.get("conference_title")
    assert data.get("CY") == data.get("conference_date")
    assert data.get("DE") == data.get("author_keywords")
    assert data.get("DI") == data.get("digital_object_identifier")
    assert data.get("DT") == data.get("document_type")
    assert data.get("D2") == data.get("book_digital_object_identifier")
    assert data.get("ED") == data.get("editors")
    assert data.get("EM") == data.get("email_address")
    assert data.get("EI") == data.get("eissn")
    assert data.get("EP") == data.get("ending_page")
    assert data.get("FU") == data.get("funding_agency_and_grant_number")
    assert data.get("FX") == data.get("funding_text")
    assert data.get("GA") == data.get("document_delivery_number")
    assert data.get("GP") == data.get("book_group_authors")
    assert data.get("HO") == data.get("conference_host")
    assert data.get("ID") == data.get("keywords_plus")
    assert data.get("ID") == data.get("keywords")
    assert data.get("IS") == data.get("issue")
    assert data.get("J9") == data.get("source_abbreviation")
    assert data.get("JI") == data.get("iso_source_abbreviation")
    assert data.get("LA") == data.get("language")
    assert data.get("MA") == data.get("meeting_abstract")
    assert data.get("NR") == data.get("cited_reference_count")
    assert data.get("OI") == data.get("orcid_identifier")
    assert data.get("P2") == data.get("chapter_count")
    assert data.get("PA") == data.get("publisher_address")
    assert data.get("PD") == data.get("publication_date")
    assert data.get("PG") == data.get("page_count")
    assert data.get("PI") == data.get("publisher_city")
    assert data.get("PM") == data.get("pubmed_id")
    assert data.get("PN") == data.get("part_number")
    assert data.get("PT") == data.get("publication_type")
    assert data.get("PU") == data.get("publisher")
    assert data.get("PY") == data.get("year_published")
    assert data.get("RI") == data.get("researcherid_number")
    assert data.get("RP") == data.get("reprint_address")
    assert data.get("SC") == data.get("research_areas")
    assert data.get("SE") == data.get("book_series_title")
    assert data.get("SI") == data.get("special_issue")
    assert data.get("SN") == data.get("issn")
    assert data.get("SP") == data.get("conference_sponsors")
    assert data.get("SU") == data.get("supplement")
    assert data.get("TC") == data.get("wos_times_cited_count")
    assert data.get("TC") == data.get("wos_times_cited")
    assert data.get("TI") == data.get("title")
    assert data.get("U1") == data.get("usage_count")
    assert data.get("U2") == data.get("usage_count")
    assert data.get("UT") == data.get("unique_article_identifier")
    assert data.get("VL") == data.get("volume")
    assert data.get("WC") == data.get("web_of_science_categories")
    assert data.get("Z9") == data.get("total_times_cited_count")
    assert data.get("Z9") == data.get("times_cited")


def test_article_properties(article):
    assert isinstance(article.text, str)
    assert isinstance(article.raw_data, dict)
    assert isinstance(article.data, dict)


def test_collection_from_filenames(collection_many_documents):
    for article in collection_many_documents.articles:
        assert isinstance(article, Article)

    for file in collection_many_documents.files:
        assert hasattr(file, "read")
        assert isinstance(file, (io.StringIO, io.TextIOWrapper))
        assert file.tell() == 0


def test_collection_from_glob():
    collection = CollectionLazy.from_glob("docs/examples/*.txt")
    for article in collection.articles:
        assert isinstance(article, Article)

    assert len(list(collection.articles)) == 500

    for file in collection.files:
        assert hasattr(file, "read")
        assert isinstance(file, (io.StringIO, io.TextIOWrapper))
        assert file.tell() == 0


def test_collection_from_streams(filename_single_document):
    with open(filename_single_document) as file:
        _ = file.read()

        collection = CollectionLazy(file)
        for article in collection.articles:
            assert isinstance(article, Article)

        for file in collection.files:
            assert hasattr(file, "read")
            assert isinstance(file, (io.StringIO, io.TextIOWrapper))
            assert file.tell() == 0


def test_collection_with_duplicated(filename_single_document, filename_many_documents):
    collection = CollectionLazy.from_filenames(
        filename_single_document, filename_single_document, filename_single_document
    )
    assert len(list(collection.files)) == 3
    assert len(list(collection.articles)) == 1

    collection = CollectionLazy.from_filenames(
        filename_many_documents, filename_many_documents, filename_many_documents
    )
    assert len(list(collection.files)) == 3
    assert len(list(collection.articles)) == 500


def test_collection_authors(collection_single_document):
    authors = collection_single_document.authors
    assert next(authors) == "Wodarz, Siggi"
    assert next(authors) == "Hasegawa, Takashi"
    assert next(authors) == "Ishio, Shunji"
    assert next(authors) == "Homma, Takayuki"


def test_collection_coauthors(collection_single_document):
    coauthors = collection_single_document.coauthors
    assert next(coauthors) == ("Hasegawa, Takashi", "Homma, Takayuki")
    assert next(coauthors) == ("Hasegawa, Takashi", "Ishio, Shunji")
    assert next(coauthors) == ("Hasegawa, Takashi", "Wodarz, Siggi")
    assert next(coauthors) == ("Homma, Takayuki", "Ishio, Shunji")
    assert next(coauthors) == ("Homma, Takayuki", "Wodarz, Siggi")
    assert next(coauthors) == ("Ishio, Shunji", "Wodarz, Siggi")


def test_collection_completeness_single_article(collection_single_document):
    assert collection_single_document.completeness() == {
        "PT": 1,
        "AU": 1,
        "AF": 1,
        "TI": 1,
        "SO": 1,
        "LA": 1,
        "DT": 1,
        "DE": 1,
        "ID": 1,
        "AB": 1,
        "C1": 1,
        "RP": 1,
        "EM": 1,
        "OI": 1,
        "FU": 1,
        "FX": 1,
        "CR": 1,
        "NR": 1,
        "TC": 1,
        "Z9": 1,
        "U1": 1,
        "U2": 1,
        "PU": 1,
        "PI": 1,
        "PA": 1,
        "SN": 1,
        "EI": 1,
        "J9": 1,
        "JI": 1,
        "PD": 1,
        "PY": 1,
        "VL": 1,
        "BP": 1,
        "EP": 1,
        "DI": 1,
        "PG": 1,
        "WC": 1,
        "SC": 1,
        "GA": 1,
        "UT": 1,
    }


def test_collection_completeness_many_articles(collection_many_documents):
    assert collection_many_documents.completeness() == {
        "AB": 497 / 500,
        "AF": 500 / 500,
        "AR": 216 / 500,
        "AU": 500 / 500,
        "BP": 281 / 500,
        "C1": 500 / 500,
        "CL": 152 / 500,
        "CR": 500 / 500,
        "CT": 152 / 500,
        "CY": 152 / 500,
        "DE": 336 / 500,
        "DI": 486 / 500,
        "DT": 500 / 500,
        "EI": 262 / 500,
        "EM": 469 / 500,
        "EP": 281 / 500,
        "FU": 270 / 500,
        "FX": 270 / 500,
        "GA": 500 / 500,
        "HO": 24 / 500,
        "ID": 440 / 500,
        "IS": 458 / 500,
        "J9": 500 / 500,
        "JI": 500 / 500,
        "LA": 500 / 500,
        "NR": 500 / 500,
        "OI": 168 / 500,
        "PA": 500 / 500,
        "PD": 469 / 500,
        "PG": 500 / 500,
        "PI": 500 / 500,
        "PM": 60 / 500,
        "PN": 60 / 500,
        "PT": 500 / 500,
        "PU": 500 / 500,
        "PY": 500 / 500,
        "RI": 172 / 500,
        "RP": 498 / 500,
        "SC": 500 / 500,
        "SI": 23 / 500,
        "SN": 500 / 500,
        "SO": 500 / 500,
        "SP": 88 / 500,
        "SU": 2 / 500,
        "TC": 500 / 500,
        "TI": 500 / 500,
        "U1": 500 / 500,
        "U2": 500 / 500,
        "UT": 500 / 500,
        "VL": 495 / 500,
        "WC": 500 / 500,
        "Z9": 500 / 500,
    }


def test_collection_citation_pairs(collection_single_document):
    pairs = [
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Albrecht TR, 2013, IEEE T MAGN, V49, P773, DOI 10.1109/TMAG.2012.2227303",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "BUSCHOW KHJ, 1983, J MAGN MAGN MATER, V38, P1, DOI 10.1016/0304-8853(83)90097-5",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Gapin AI, 2006, J APPL PHYS, V99, DOI 10.1063/1.2163289",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Homma Takayuki, 2015, ECS Transactions, V64, P1, DOI 10.1149/06431.0001ecst",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Kryder MH, 2008, P IEEE, V96, P1810, DOI 10.1109/JPROC.2008.2004315",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Kubo T, 2005, J APPL PHYS, V97, DOI 10.1063/1.1855572",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Lodder JC, 2004, J MAGN MAGN MATER, V272, P1692, DOI 10.1016/j.jmmm.2003.12.259",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Mitsuzuka K, 2007, IEEE T MAGN, V43, P2160, DOI 10.1109/TMAG.2007.893129",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Ouchi T, 2010, ELECTROCHIM ACTA, V55, P8081, DOI 10.1016/j.electacta.2010.02.073",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Pattanaik G, 2006, J APPL PHYS, V99, DOI 10.1063/1.2150805",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Pattanaik G, 2007, ELECTROCHIM ACTA, V52, P2755, DOI 10.1016/j.electacta.2006.07.062",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Piramanayagam SN, 2009, J MAGN MAGN MATER, V321, P485, DOI 10.1016/j.jmmm.2008.05.007",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Ross CA, 2008, MRS BULL, V33, P838, DOI 10.1557/mrs2008.179",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Shiroishi Y, 2009, IEEE T MAGN, V45, P3816, DOI 10.1109/TMAG.2009.2024879",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Sirtori V, 2011, ACS APPL MATER INTER, V3, P1800, DOI 10.1021/am200267u",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Sohn JS, 2009, NANOTECHNOLOGY, V20, DOI 10.1088/0957-4484/20/2/025302",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Sun SH, 2000, SCIENCE, V287, P1989, DOI 10.1126/science.287.5460.1989",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Terris BD, 2007, MICROSYST TECHNOL, V13, P189, DOI 10.1007/s00542-006-0144-9",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Wang JP, 2008, P IEEE, V96, P1847, DOI 10.1109/JPROC.2008.2004318",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Weller D, 1999, IEEE T MAGN, V35, P4423, DOI 10.1109/20.809134",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Weller D, 2000, IEEE T MAGN, V36, P10, DOI 10.1109/20.824418",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Wodarz S, 2016, ELECTROCHIM ACTA, V197, P330, DOI 10.1016/j.electacta.2015.11.136",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Xu X, 2012, J ELECTROCHEM SOC, V159, pD240, DOI 10.1149/2.090204jes",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Yang X, 2007, J VAC SCI TECHNOL B, V25, P2202, DOI 10.1116/1.2798711",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Yang XM, 2009, ACS NANO, V3, P1844, DOI 10.1021/nn900073r",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Yasui N, 2003, APPL PHYS LETT, V83, P3347, DOI 10.1063/1.1622787",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Yua H., 2009, J APPL PHYS, V105",
        ),
        (
            "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061",
            "Zhu JG, 2008, IEEE T MAGN, V44, P125, DOI 10.1109/TMAG.2007.911031",
        ),
    ]

    assert collection_single_document.citation_pairs() == pairs


def test_command_line_interface():
    """Test the CLI."""
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert "A little cli for wos tools" in result.output
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert "--help  Show this message and exit." in help_result.output


def test_command_line_interface_citation_pairs(filename_single_document):
    runner = CliRunner()
    result = runner.invoke(cli.citation_pairs)
    assert result.exit_code == 0
    assert "You should give at least a file with documents." in result.output

    result = runner.invoke(cli.citation_pairs, filename_single_document)
    assert (
        "Wodarz S, 2017, J MAGN MAGN MATER, V430, P7, DOI 10.1016/j.jmmm.2017.01.061"
        in result.output
    )
