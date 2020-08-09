import io
from typing import List, Dict, Tuple

from pytest import fixture
from pytest_bdd import scenarios, given, when, then

from wostools import CachedCollection, Article
from wostools._testutils import Context

ISI_TEXT = """
FN Thomson Reuters Web of Science™
VR 1.0
PT J
AU Sun, ZW
   Russell, TP
AF Sun, Zhiwei
   Russell, Thomas P.
TI In situ grazing incidence small-angle X-ray scattering study of solvent
   vapor annealing in lamellae-forming block copolymer thin films:
   Trade-off of defects in deswelling
SO JOURNAL OF POLYMER SCIENCE PART B-POLYMER PHYSICS
LA English
DT Article
DE annealing; block copolymers; self-assembly; thin films; X-ray
ID BIT-PATTERNED MEDIA; LITHOGRAPHY; GRAPHENE; ARRAYS; ORIENTATION;
   NANOWIRES; PARALLEL; BEHAVIOR; INPLANE; DENSITY
AB Solvent vapor annealing (SVA) is one route to prepare block copolymer (BCP) thin films with long-range lateral ordering. The lattice defects in the spin-coated BCP thin film can be effectively and rapidly reduced using SVA. The solvent evaporation after annealing was shown to have a significant impact on the in-plane ordering of BCP microdomains. However, the effect of solvent evaporation on the out-of-plane defects in BCPs has not been considered. Using grazing-incidence x-ray scattering, the morphology evolution of lamellae-forming poly(2-vinlypyridine)-b-polystyrene-b-poly(2vinylpyridine) triblock copolymers, having lamellar microdomains oriented normal to substrate surface during SVA, was studied in this work. A micelle to lamellae transformation was observed during solvent uptake. The influence of solvent swelling ratio and solvent removal rate on both the in-plane and out-of-plane defect density was studied. It shows that there is a trade-off between the in-plane and out-of-plane defect densities during solvent evaporation. (c) 2017 Wiley Periodicals, Inc. J. Polym. Sci., Part B: Polym. Phys. 2017, 55, 980-989
C1 [Sun, Zhiwei; Russell, Thomas P.] Univ Massachusetts Amherst, Dept Polymer Sci & Engn, Amherst, MA 01003 USA.
   [Russell, Thomas P.] Lawrence Berkeley Natl Lab, Div Mat Sci, Berkeley, CA 94720 USA.
   [Russell, Thomas P.] Beijing Univ Chem Technol, Beijing Adv Innovat Ctr Soft Matter Sci & Engn, Beijing, Peoples R China.
RP Russell, TP (reprint author), Univ Massachusetts Amherst, Dept Polymer Sci & Engn, Amherst, MA 01003 USA.; Russell, TP (reprint author), Lawrence Berkeley Natl Lab, Div Mat Sci, Berkeley, CA 94720 USA.; Russell, TP (reprint author), Beijing Univ Chem Technol, Beijing Adv Innovat Ctr Soft Matter Sci & Engn, Beijing, Peoples R China.
EM russell@mail.pse.umass.edu
FU U.S. Department of Energy BES [BES-DE-FG02-96ER45612]; Director of the
   Office of Science, Office of Basic Energy Sciences, of the U.S.
   Department of Energy [DE-AC02-05CH11231]; Office of Science, Office of
   Basic Energy Sciences, of the U.S. Department of Energy
   [DE-AC02-05CH11231]
FX The authors acknowledge the facility support in Advanced Light Source
   and Molecular Foundry in Lawrence Berkeley National Laboratory. This
   work was supported by the U.S. Department of Energy BES under contract
   BES-DE-FG02-96ER45612. The GISAXS characterization in beamline 7.3.3 of
   the Advanced Light Source is supported by the Director of the Office of
   Science, Office of Basic Energy Sciences, of the U.S. Department of
   Energy under contract no. DE-AC02-05CH11231. The SEM and AFM
   characterization in the Molecular Foundry was supported by the Office of
   Science, Office of Basic Energy Sciences, of the U.S. Department of
   Energy under contract no. DE-AC02-05CH11231.
CR Bai W, 2015, MACROMOLECULES, V48, P8574, DOI 10.1021/acs.macromol.5b02174
   Bosworth JK, 2011, MACROMOLECULES, V44, P9196, DOI 10.1021/ma201967a
   Bosworth JK, 2010, J PHOTOPOLYM SCI TEC, V23, P145, DOI 10.2494/photopolymer.23.145
   Chai J, 2008, ACS NANO, V2, P489, DOI 10.1021/nn700341s
   Chai J, 2007, NAT NANOTECHNOL, V2, P500, DOI 10.1038/nnano.2007.227
   Choi S, 2012, SOFT MATTER, V8, P3463, DOI 10.1039/c2sm07297a
   Di ZY, 2012, MACROMOLECULES, V45, P5185, DOI 10.1021/ma3004136
   Farrell RA, 2012, NANOSCALE, V4, P3228, DOI 10.1039/c2nr00018k
   Gowd E. B., 2010, IOP C SER MAT SCI EN, V14
   Gu XD, 2014, ADV MATER, V26, P273, DOI 10.1002/adma.201302562
   Gunkel I, 2016, J POLYM SCI POL PHYS, V54, P331, DOI 10.1002/polb.23933
   Ilavsky J, 2012, J APPL CRYSTALLOGR, V45, P324, DOI 10.1107/S0021889812004037
   Jeong SJ, 2010, NANO LETT, V10, P3500, DOI 10.1021/nl101637f
   Ji S, 2008, MACROMOLECULES, V41, P9098, DOI 10.1021/ma801861h
   Khaira GS, 2014, ACS MACRO LETT, V3, P747, DOI 10.1021/mz5002349
   Kikitsu A, 2013, IEEE T MAGN, V49, P693, DOI 10.1109/TMAG.2012.2226566
   Kim BH, 2011, ADV MATER, V23, P5618, DOI 10.1002/adma.201103650
   Kim BH, 2010, ACS NANO, V4, P5464, DOI 10.1021/nn101491g
   Kurihara M, 2013, JPN J APPL PHYS, V52, DOI 10.7567/JJAP.52.086201
   Liu GX, 2012, ACS NANO, V6, P6786, DOI 10.1021/nn301515a
   Mahadevapuram N, 2016, J POLYM SCI POL PHYS, V54, P339, DOI 10.1002/polb.23937
   Paik MY, 2010, MACROMOLECULES, V43, P4253, DOI 10.1021/ma902646t
   Sinturel C, 2014, ACS APPL MATER INTER, V6, P12146, DOI 10.1021/am504086x
   Sun ZW, 2015, ADV MATER, V27, P4364, DOI 10.1002/adma.201501585
   Vu T, 2011, MACROMOLECULES, V44, P6121, DOI 10.1021/ma2009222
   Thurn-Albrecht T, 2000, SCIENCE, V290, P2126, DOI 10.1126/science.290.5499.2126
   Wan L., 2012, MOEMS, V11, P31405
   Wang JY, 2008, LANGMUIR, V24, P3545, DOI 10.1021/la703559q
   Xiao S., 2013, MOEMS, V12
   Xiao SG, 2014, ACS NANO, V8, P11854, DOI 10.1021/nn505630t
   Xiao SG, 2014, J POLYM SCI POL PHYS, V52, P361, DOI 10.1002/polb.23433
   Yamamoto R, 2014, IEEE T MAGN, V50, DOI 10.1109/TMAG.2013.2284474
   Yang X., 2014, MOEMS, V13
   Yang X., 2013, J MATER RES, V2013, P1
   Yang XM, 2014, NANOTECHNOLOGY, V25, DOI 10.1088/0957-4484/25/39/395301
   Yang XM, 2009, ACS NANO, V3, P1844, DOI 10.1021/nn900073r
   Zhang JQ, 2014, MACROMOLECULES, V47, P5711, DOI 10.1021/ma500633b
NR 37
TC 0
Z9 0
U1 1
U2 1
PU WILEY
PI HOBOKEN
PA 111 RIVER ST, HOBOKEN 07030-5774, NJ USA
SN 0887-6266
EI 1099-0488
J9 J POLYM SCI POL PHYS
JI J. Polym. Sci. Pt. B-Polym. Phys.
PD JUL 1
PY 2017
VL 55
IS 13
BP 980
EP 989
DI 10.1002/polb.24346
PG 10
WC Polymer Science
SC Polymer Science
GA EU7BQ
UT WOS:000401190100002
ER

EF
""".strip()

ISI_TEXT_DIFFERENT_RECORD = """
FN Thomson Reuters Web of Science™
VR 1.0
PT J
AU Bosworth, JK
   Dobisz, EA
   Hellwig, O
   Ruiz, R
AF Bosworth, Joan K.
   Dobisz, Elizabeth A.
   Hellwig, Olav
   Ruiz, Ricardo
TI Impact of Out-of-Plane Translational Order in Block Copolymer
   Lithography
SO MACROMOLECULES
LA English
DT Article
ID BIT-PATTERNED MEDIA; DENSITY MULTIPLICATION; TERNARY BLENDS; THIN-FILMS;
   DIMENSIONS; ROUGHNESS; DOMAINS; SHAPES
AB In block copolymer lithography, subtle distortions in the self-assembled domains, such as tilting or bending, have a strong impact on the quality of the lithographic features upon pattern transfer. We compared the feature size distribution observed at the top-surface of block copolymer thin films with the size distribution that the self-assembled structures project at the substrate interface, i.e., the lithographic image. We performed the comparison for films of perpendicularly oriented cylindrical block copolymer domains with various degrees of lateral order. We found that the size distribution of the projected image does not mimic the well-known Gaussian distribution observed at the top surface. Instead, the lithographic features display a skewed distribution with a long tail toward smaller feature dimensions, a shift of the median and a reduced number of transferred features. The distortions are more pronounced for films with shorter correlation lengths. We propose a simplified model that explains the observed shifts in the size distribution of the projected image by considering the tilting that cylinders undergo in the vicinity of dislocations. The presence of defects disrupting the in-plane orientational order riot only impacts the size distribution of the self-assembled features, but also induces nearby cylinder tilting and some general loss of out-of-plane translational order which, upon pattern transfer, is responsible for the observed distortions on the feature size distribution,
C1 [Bosworth, Joan K.; Dobisz, Elizabeth A.; Hellwig, Olav; Ruiz, Ricardo] Hitachi Global Storage Technol, San Jose Res Ctr, San Jose, CA 95135 USA.
RP Ruiz, R (reprint author), Hitachi Global Storage Technol, San Jose Res Ctr, 3403 Yerba Buena Rd, San Jose, CA 95135 USA.
EM ricardo.ruiz@hitachigst.com
OI Ruiz, Ricardo/0000-0002-1698-4281
CR ALBRECHT T, 2009, NANOSCALE MAGNETIC M
   BATES FS, 1990, ANNU REV PHYS CHEM, V41, P525, DOI 10.1146/annurev.pc.41.100190.002521
   Black CT, 2007, IBM J RES DEV, V51, P605
   Cheng JY, 2008, ADV MATER, V20, P3155, DOI 10.1002/adma.200800826
   Cheng JY, 2010, ACS NANO, V4, P4815, DOI 10.1021/nn100686v
   Detcheverry FA, 2010, MACROMOLECULES, V43, P3446, DOI 10.1021/ma902332h
   Edwards EW, 2007, MACROMOLECULES, V40, P90, DOI 10.1021/ma0607564
   Guarini KW, 2002, ADV MATER, V14, P1290, DOI 10.1002/1521-4095(20020916)14:18<1290::AID-ADMA1290>3.0.CO;2-N
   Hammond MR, 2003, MACROMOLECULES, V36, P8712, DOI 10.1021/ma026001o
   Harrison C, 2004, EUROPHYS LETT, V67, P800, DOI 10.1209/epl/i2004-10126-5
   Harrison C, 2002, PHYS REV E, V66, DOI 10.1103/PhysRevE.66.011706
   Hellwig O, 2010, APPL PHYS LETT, V96, DOI 10.1063/1.3293301
   HO CS, 1983, IEEE T PATTERN ANAL, V5, P593
   *INTRS, LITH
   Ji SX, 2011, MACROMOLECULES, V44, P4291, DOI 10.1021/ma2005734
   Kleman M., 2003, SOFT MATTER PHYS INT
   LIU CC, 2010, J VAC SCI TECHNOL B, V34
   Liu G, 2010, J VAC SCI TECHNOL B, V28
   Nagpal U, 2011, ACS NANO, V5, P5673, DOI 10.1021/nn201335v
   Ruiz R, 2008, PHYS REV B, V77, DOI 10.1103/PhysRevB.77.054204
   Ruiz R, 2008, SCIENCE, V321, P936, DOI 10.1126/science.1157626
   Segalman RA, 2005, MAT SCI ENG R, V48, P191, DOI 10.1016/j.mser.2004.12.003
   Segalman RA, 2003, PHYS REV LETT, V91, DOI 10.1103/PhysRevLett.91.196101
   Segalman RA, 2003, MACROMOLECULES, V36, P3272, DOI 10.1021/ma021367m
   Stipe BC, 2010, NAT PHOTONICS, V4, P484, DOI 10.1038/nphoton.2010.90
   Stoykovich MP, 2010, MACROMOLECULES, V43, P2334, DOI 10.1021/ma902494v
   Stuen KO, 2009, MACROMOLECULES, V42, P5139, DOI 10.1021/ma900520v
   Tada Y, 2009, POLYMER, V50, P4250, DOI 10.1016/j.polymer.2009.06.039
   Welander AM, 2008, MACROMOLECULES, V41, P2759, DOI 10.1021/ma800056s
   Welander AM, 2008, J VAC SCI TECHNOL B, V26, P2484, DOI 10.1116/1.2987963
   Xiao SG, 2007, J VAC SCI TECHNOL B, V25, P1953, DOI 10.1116/1.2801860
   Yang XM, 2009, ACS NANO, V3, P1844, DOI 10.1021/nn900073r
NR 32
TC 11
Z9 11
U1 4
U2 22
PU AMER CHEMICAL SOC
PI WASHINGTON
PA 1155 16TH ST, NW, WASHINGTON, DC 20036 USA
SN 0024-9297
J9 MACROMOLECULES
JI Macromolecules
PD DEC 13
PY 2011
VL 44
IS 23
BP 9196
EP 9204
DI 10.1021/ma201967a
PG 9
WC Polymer Science
SC Polymer Science
GA 855ZG
UT WOS:000297604200016
ER

EF
""".strip()

scenarios("features/cached.feature")


@fixture
def collection_context() -> Context[CachedCollection]:
    return Context()


@fixture
def iterate_collection_context() -> Context[List[Article]]:
    return Context()


@fixture
def iterate_authors_collection_context() -> Context[List[str]]:
    return Context()


@fixture
def iterate_coauthors_collection_context() -> Context[List[Tuple[str, str]]]:
    return Context()


@fixture
def iterate_citation_pairs_collection_context() -> Context[
    List[Tuple[Article, Article]]
]:
    return Context()


@given("some valid isi text", target_fixture="isi_text")
def valid_isi_text():
    return [ISI_TEXT]


@given("a diferent isi record that references the former", target_fixture="isi_text")
def isi_text_different_record(isi_text):
    return [*isi_text, ISI_TEXT_DIFFERENT_RECORD]


@when("I create a collection from that text")
def create_collection(isi_text, collection_context: Context[CachedCollection]):
    with collection_context.capture():
        collection = CachedCollection(*(io.StringIO(doc) for doc in isi_text))
        collection_context.push(collection)
    return collection_context


@given("a valid collection")
def context_valid_collection(collection_context):
    collection = CachedCollection(io.StringIO(ISI_TEXT))
    collection_context.push(collection)


@then("the collection's cache is preheated")
def the_collection_cache_is_preheated(collection_context: Context[CachedCollection]):
    with collection_context.assert_data() as collection:
        assert collection._cache


@when("I iterate over the collection")
def iterate_over_collection(
    collection_context: Context[CachedCollection],
    iterate_collection_context: Context[List[Article]],
):
    with collection_context.assert_data() as collection:
        with iterate_collection_context.capture():
            iterate_collection_context.push(list(collection))


@then("all articles and references are present")
def all_articles_and_references_are_present(
    iterate_collection_context: Context[List[Article]],
):
    with iterate_collection_context.assert_data() as articles:
        assert len(articles) == 38
        for article in articles:
            assert article
            assert article.label


@when("I iterate over the collection authors")
def iterate_over_collection_authors(
    collection_context: Context[CachedCollection],
    iterate_authors_collection_context: Context[List[str]],
):
    with collection_context.assert_data() as collection:
        with iterate_authors_collection_context.capture():
            iterate_authors_collection_context.push(list(collection.authors))


@then("all authors are included")
@then("the author list include duplicates")
def all_authors_included_even_duplicates(
    iterate_authors_collection_context: Context[List[str]],
):
    with iterate_authors_collection_context.assert_data() as authors:
        assert authors

        authors_count: Dict[str, int] = {}
        for author in authors:
            authors_count[author] = authors_count.get(author, 0) + 1
            assert author

        for author, count in authors_count.items():
            assert author in ISI_TEXT
            assert count >= 1


@when("I iterate over the collection coauthors")
def iterate_over_collection_coauthors(
    collection_context: Context[CachedCollection],
    iterate_coauthors_collection_context: Context[List[Tuple[str, str]]],
):
    with collection_context.assert_data() as collection:
        with iterate_coauthors_collection_context.capture():
            iterate_coauthors_collection_context.push(list(collection.coauthors))


@then("all coauthor pairs are included")
@then("the coauthor list include duplicates")
def all_coauthors_pairs_included_even_duplicates(
    iterate_coauthors_collection_context: Context[List[Tuple[str, str]]],
):
    with iterate_coauthors_collection_context.assert_data() as coauthors:
        assert coauthors

        coauthors_count: Dict[Tuple[str, str], int] = {}
        for pair in coauthors:
            coauthors_count[pair] = coauthors_count.get(pair, 0) + 1

            author, coauthor = pair
            assert author
            assert coauthor

        for pair, count in coauthors_count.items():
            author, coauthor = pair
            assert author in ISI_TEXT
            assert coauthor in ISI_TEXT
            assert count >= 1


@then("both collections have the same number of articles")
def same_number_of_articles(collection_context: Context[CachedCollection]):

    with collection_context.assert_data() as collection:
        with collection_context.assert_history(1) as latest:
            print(latest)
            assert len(collection) == len(latest[0])


@when("I list the collection's citation pairs")
def list_collection_citation_pairs(
    collection_context: Context[CachedCollection],
    iterate_citation_pairs_collection_context: Context[List[Tuple[Article, Article]]],
):
    with collection_context.assert_data() as collection:
        with iterate_citation_pairs_collection_context.capture():
            iterate_citation_pairs_collection_context.push(
                list(collection.citation_pairs())
            )


@then("all citation pairs are included")
def all_citation_pairs_are_included(
    iterate_citation_pairs_collection_context: Context[List[Tuple[Article, Article]]]
):
    with iterate_citation_pairs_collection_context.assert_data() as citation_pairs:
        assert len(citation_pairs) == 37
        for article, reference in citation_pairs:
            assert isinstance(article, Article)
            assert isinstance(reference, Article)


@then("the citation always include all the available data")
def iterate_over_citation_pairs_two_isi_files(
    iterate_citation_pairs_collection_context: Context[List[Tuple[Article, Article]]]
):
    with iterate_citation_pairs_collection_context.assert_data() as citation_pairs:
        assert len(citation_pairs) == 68

        having_keywords = False
        for article, reference in citation_pairs:
            assert isinstance(article, Article)
            assert isinstance(reference, Article)

            if (
                article.to_dict()["doi"] == "10.1002/polb.24346"
                and reference.to_dict()["doi"] == "10.1021/ma201967a"
            ):
                having_keywords = bool(article.keywords and reference.keywords)

        assert having_keywords
