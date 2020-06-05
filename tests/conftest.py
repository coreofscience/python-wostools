"""
Configuration file for python-wostools tests.
"""

from wostools import Article, CollectionLazy, Collection

import pytest
import io


@pytest.fixture
def article():
    file = io.StringIO(
        "PT J\n"
        "AU Wodarz, S\n"
        "   Hasegawa, T\n"
        "   Ishio, S\n"
        "   Homma, T\n"
        "AF Wodarz, Siggi\n"
        "   Hasegawa, Takashi\n"
        "   Ishio, Shunji\n"
        "   Homma, Takayuki\n"
        "TI Structural control of ultra-fine CoPt nanodot arrays via\n"
        "   electrodeposition process\n"
        "SO JOURNAL OF MAGNETISM AND MAGNETIC MATERIALS\n"
        "LA English\n"
        "DT Article\n"
        "DE Electrodeposition; Structural control; Nanodot array; Bit-patterned\n"
        "   media; CoPt alloy\n"
        "ID BIT-PATTERNED MEDIA; ELECTRON-BEAM LITHOGRAPHY; RECORDING MEDIA;\n"
        "   MAGNETIC MEDIA; DENSITY; FILMS; ANISOTROPY; STORAGE\n"
        "AB CoPt nanodot arrays were fabricated by combining electrodeposition and electron beam lithography (EBL) for the use of bit-patterned media (BPM). To achieve precise control of deposition uniformity and coercivity of the CoPt nanodot arrays, their crystal structure and magnetic properties were controlled by controlling the diffusion state of metal ions from the initial deposition stage with the application of bath agitation. Following bath agitation, the composition gradient of the CoPt alloy with thickness was mitigated to have a near-ideal alloy composition of Co:Pt =80:20, which induces epitaxial-like growth from Ru substrate, thus resulting in the improvement of the crystal orientation of the hcp (002) structure from its initial deposition stages. Furthermore, the cross-sectional transmission electron microscope (TEM) analysis of the nanodots deposited with bath agitation showed CoPt growth along its c-axis oriented in the perpendicular direction, having uniform lattice fringes on the hcp (002) plane from the Ru underlayer interface, which is a significant factor to induce perpendicular magnetic anisotropy. Magnetic characterization of the CoPt nanodot arrays showed increase in the perpendicular coercivity and squareness of the hysteresis loops from 2.0 kOe and 0.64 (without agitation) to 4.0 kOe and 0.87 with bath agitation. Based on the detailed characterization of nanodot arrays, the precise crystal structure control of the nanodot arrays with ultra-high recording density by electrochemical process was successfully demonstrated.\n"
        "C1 [Wodarz, Siggi; Homma, Takayuki] Waseda Univ, Dept Appl Chem, Shinjuku Ku, Tokyo 1698555, Japan.\n"
        "   [Hasegawa, Takashi; Ishio, Shunji] Akita Univ, Dept Mat Sci, Akita 0108502, Japan.\n"
        "RP Homma, T (reprint author), Waseda Univ, Dept Appl Chem, Shinjuku Ku, Tokyo 1698555, Japan.\n"
        "EM t.homma@waseda.jp\n"
        "OI Hasegawa, Takashi/0000-0002-8178-4980\n"
        "FU JSPS KAKENHI Grant [25249104]\n"
        "FX This work was supported in part by JSPS KAKENHI Grant Number 25249104.\n"
        "CR Albrecht TR, 2013, IEEE T MAGN, V49, P773, DOI 10.1109/TMAG.2012.2227303\n"
        "   BUSCHOW KHJ, 1983, J MAGN MAGN MATER, V38, P1, DOI 10.1016/0304-8853(83)90097-5\n"
        "   Gapin AI, 2006, J APPL PHYS, V99, DOI 10.1063/1.2163289\n"
        "   Homma Takayuki, 2015, ECS Transactions, V64, P1, DOI 10.1149/06431.0001ecst\n"
        "   Kryder MH, 2008, P IEEE, V96, P1810, DOI 10.1109/JPROC.2008.2004315\n"
        "   Kubo T, 2005, J APPL PHYS, V97, DOI 10.1063/1.1855572\n"
        "   Lodder JC, 2004, J MAGN MAGN MATER, V272, P1692, DOI 10.1016/j.jmmm.2003.12.259\n"
        "   Mitsuzuka K, 2007, IEEE T MAGN, V43, P2160, DOI 10.1109/TMAG.2007.893129\n"
        "   Ouchi T, 2010, ELECTROCHIM ACTA, V55, P8081, DOI 10.1016/j.electacta.2010.02.073\n"
        "   Pattanaik G, 2006, J APPL PHYS, V99, DOI 10.1063/1.2150805\n"
        "   Pattanaik G, 2007, ELECTROCHIM ACTA, V52, P2755, DOI 10.1016/j.electacta.2006.07.062\n"
        "   Piramanayagam SN, 2009, J MAGN MAGN MATER, V321, P485, DOI 10.1016/j.jmmm.2008.05.007\n"
        "   Ross CA, 2008, MRS BULL, V33, P838, DOI 10.1557/mrs2008.179\n"
        "   Shiroishi Y, 2009, IEEE T MAGN, V45, P3816, DOI 10.1109/TMAG.2009.2024879\n"
        "   Sirtori V, 2011, ACS APPL MATER INTER, V3, P1800, DOI 10.1021/am200267u\n"
        "   Sohn JS, 2009, NANOTECHNOLOGY, V20, DOI 10.1088/0957-4484/20/2/025302\n"
        "   Sun SH, 2000, SCIENCE, V287, P1989, DOI 10.1126/science.287.5460.1989\n"
        "   Terris BD, 2007, MICROSYST TECHNOL, V13, P189, DOI 10.1007/s00542-006-0144-9\n"
        "   Wang JP, 2008, P IEEE, V96, P1847, DOI 10.1109/JPROC.2008.2004318\n"
        "   Weller D, 1999, IEEE T MAGN, V35, P4423, DOI 10.1109/20.809134\n"
        "   Weller D, 2000, IEEE T MAGN, V36, P10, DOI 10.1109/20.824418\n"
        "   Wodarz S, 2016, ELECTROCHIM ACTA, V197, P330, DOI 10.1016/j.electacta.2015.11.136\n"
        "   Xu X, 2012, J ELECTROCHEM SOC, V159, pD240, DOI 10.1149/2.090204jes\n"
        "   Yang X, 2007, J VAC SCI TECHNOL B, V25, P2202, DOI 10.1116/1.2798711\n"
        "   Yang XM, 2009, ACS NANO, V3, P1844, DOI 10.1021/nn900073r\n"
        "   Yasui N, 2003, APPL PHYS LETT, V83, P3347, DOI 10.1063/1.1622787\n"
        "   Yua H., 2009, J APPL PHYS, V105\n"
        "   Zhu JG, 2008, IEEE T MAGN, V44, P125, DOI 10.1109/TMAG.2007.911031\n"
        "NR 28\n"
        "TC 0\n"
        "Z9 0\n"
        "U1 21\n"
        "U2 21\n"
        "PU ELSEVIER SCIENCE BV\n"
        "PI AMSTERDAM\n"
        "PA PO BOX 211, 1000 AE AMSTERDAM, NETHERLANDS\n"
        "SN 0304-8853\n"
        "EI 1873-4766\n"
        "J9 J MAGN MAGN MATER\n"
        "JI J. Magn. Magn. Mater.\n"
        "PD MAY 15\n"
        "PY 2017\n"
        "VL 430\n"
        "BP 52\n"
        "EP 58\n"
        "DI 10.1016/j.jmmm.2017.01.061\n"
        "PG 7\n"
        "WC Materials Science, Multidisciplinary; Physics, Condensed Matter\n"
        "SC Materials Science; Physics\n"
        "GA EP2GP\n"
        "UT WOS:000397201600008\n"
        "ER"
    )
    article_text = file.read()
    return Article.from_isi_text(article_text)


@pytest.fixture
def filename_single_document():
    return "docs/examples/single-article.txt"


@pytest.fixture
def filename_many_documents():
    return "docs/examples/bit-pattern-savedrecs.txt"


@pytest.fixture(params=[Collection, CollectionLazy])
def collection_single_document(request, filename_single_document):
    return request.param.from_filenames(filename_single_document)


@pytest.fixture(params=[Collection, CollectionLazy])
def collection_many_documents(request, filename_many_documents):
    return request.param.from_filenames(filename_many_documents)
