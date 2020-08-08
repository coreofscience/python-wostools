import io
from typing import Collection, Dict, Tuple

from pytest import fixture
from pytest_bdd import scenario, given, when, then

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
""".strip()


@scenario("features/cached.feature", "citation pairs")
def test_preheat_cache():
    pass


@fixture
def collection_context() -> Context[CachedCollection]:
    return Context()


@fixture
def two_collections_context() -> Tuple[Context, Context]:
    return Context(), Context()


@fixture
def isi_text():
    return ISI_TEXT


@given("some valid isi text")
def valid_isi_text(isi_text):
    return isi_text


@fixture
def create_valid_collection(isi_text, collection_context: Context[CachedCollection]):
    with collection_context.capture():
        collection = CachedCollection(io.StringIO(isi_text))
        collection_context.push(collection)
    return collection_context


@when("I create a collection from that text")
def create_collection(create_valid_collection):
    pass


@given("a valid collection")
def context_valid_collection(create_valid_collection):
    return create_valid_collection


@then("the collection's cache is preheated")
def the_collection_cache_is_preheated(collection_context: Context[CachedCollection]):
    with collection_context.assert_data() as collection:
        assert collection._cache


@when("I iterate over the collection")
@then("all articles and references are present")
def iterate_over_collection(context_valid_collection: Context[CachedCollection]):
    with context_valid_collection.assert_data() as collection:
        assert len(collection) == 38
        for article in collection:
            assert article
            assert article.label


@when("I iterate over the collection authors")
@then("all authors are included")
@then("the author list include duplicates")
def iterate_over_collection_authors(
    context_valid_collection: Context[CachedCollection],
):
    with context_valid_collection.assert_data() as collection:
        assert collection.authors

        authors: Dict[str, int] = {}
        for author in collection.authors:
            authors[author] = authors.get(author, 0) + 1
            assert author

        for author, count in authors.items():
            assert author in ISI_TEXT
            assert count >= 1


@when("I iterate over the collection coauthors")
@then("all coauthor pairs are included")
@then("the coauthor list include duplicates")
def iterate_over_collection_coauthors(
    context_valid_collection: Context[CachedCollection],
):
    with context_valid_collection.assert_data() as collection:
        assert collection.coauthors

        coauthors: Dict[Tuple[str, str], int] = {}
        for pair in collection.coauthors:
            coauthors[pair] = coauthors.get(pair, 0) + 1

            author, coauthor = pair
            assert author
            assert coauthor

        for pair, count in coauthors.items():
            author, coauthor = pair
            assert author in ISI_TEXT
            assert coauthor in ISI_TEXT
            assert count >= 1


@when("I create a collection from that text")
@when("I create a collection from twice that text")
def create_two_collections(isi_text, two_collections_context):
    first_context, second_context = two_collections_context
    buffer = io.StringIO(isi_text)

    with first_context.capture():
        first_collection = CachedCollection(buffer)
        first_context.push(first_collection)

    with second_context.capture():
        second_collection = CachedCollection(buffer, buffer)
        second_context.push(second_collection)


@then("both collections have the same number of articles")
def same_number_of_articles(two_collections_context):
    first_context, second_context = two_collections_context

    with first_context.assert_data() as first_collection:
        with second_context.assert_data() as second_collection:
            assert len(first_collection) == len(second_collection)
            assert sorted([art.label for art in first_collection]) == sorted(
                [art.label for art in second_collection]
            )


@when("I list the collection's citation pairs")
@then("all citation pairs are included")
def list_collection_citation_pairs(context_valid_collection: Context[CachedCollection]):
    with context_valid_collection.assert_data() as collection:
        assert len(list(collection.citation_pairs())) == 37
        for article, reference in collection.citation_pairs():
            assert isinstance(article, Article)
            assert isinstance(reference, Article)
