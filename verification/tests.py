SPECIFICS = '''
6x6:IdBbhdbacb

8x8:eaBaCFdCaekafDABaEc

12x8:AKCABbCBIGabdbicDFCCAdBaEf

10x10:iaFABdaHBBAcHBaDBFAbBcjbbBfGa

16x8:fEeACjHAbBDcGDFcamBcaCcBLeaFbaBb

14x16:AIFbECiabaCCCgEmbdhEdABDIbDBbHcadBlDeABCeMeAbbOABAHBa

20x20:BEbfkeBbBAbBBgGeGdKBAldCGBcbaghEAMMbaCDhgdEAcbaCigcdBGBCECLaHFbGACABDIAkbabGEhJcCCcCABeaEbde

26x20:ABdCAhGeEfACeEedDdBdCcHAGheCGBCEcFCBfbDbCeClDchihdagcakBgNAhFcEAfbkcAEbEdcDbDABdcBgffmCaiCBcDDeBBDcAcaCdBdBNmCAEBdbcafdbBBBBa

18x40:ABDfjCbEFcBEEebFAfFBFEgBDCBACKbjbabDEBDEdbABBqCAbbCbaFBeaeAbfAajaHaCAHBfCbCDAbADAfhABFgaFbdeCcJcEACdeafabcaIGgBmEcDgbDfBGBACBPaDDcdfABaCeDdfgjabDCOBcaBAEIgfcebeBhFBBADCeiccAcfbcaCfBDCa

30x30:AddFbBEABbBabbBBADDXACECcaeCAbDfcFCDiFDIEcFCbgAbEEBbbdaCDfcbabaDhdCnDAEAdBADDBIDaJgbbaCICdbNcccFaIabbeabdeaeiGAeEccbcDBlADCCDgecKBfBbkadCACghfEJdBACDDcdaCDGAPDcbcidCMeBaGfaCBFdBddbbebdceMAfDcDAbaBiiRDBAcabFeBAceeLfAdCeCAdaa

26x40:dDdcEDfBgEcdaJEdcDBbAfGBdCnCcHAGlhaceBbahhbbabfaEECgbAeaaDjhcbadcBABbCDJiAjCAdbABDCJEJCdabCEgCAbAcbcfDDcKADCCcbcbBbcdKdlgdBddeakGFCdDDBbbaChadAeGfLmGgBAbebbdDAGcagFcABiDaBcADDKCAFgcJEEcBBDDcgFeFAFCLbafHcaBDcaCfcDghFbjagagADfaCdajbBAebIBcCDBcbaELefcdabaBd

30x40:BEBFAgGacBbKBfbBADCCCADECiEbbbGJfhefaidciCUAcCBhaDccCffCEAccGccBbCbcFFjBbgkbohafBdCBfbaHfEBADcFECBCeiEjjdBAgbhcAbcaHGeACHAfCacsbbCjBFbbcChFbhFdEckdadFgabgDDbEbaHABClaHCABAEoaPdaCFJCDBCbaCEAgeJdDbFBbaGicLBBdacahbaLJACgfaDaBFBDAfJACbiefgTADBADBbJAbFdCECncibccbDHCcAHBcaCCCAFeac
'''.strip().split('\n'*2)


def spec2grid(spec):
    dim, chars = spec.split(':')
    nb_cols, nb_rows = map(int, dim.split('x'))
    L = []
    for char in chars:
        L.extend('.' * (ord(char.lower()) - ord('a')))
        L.append('WB'[char.isupper()])
    lines = (L[k * nb_cols: (k + 1) * nb_cols] for k in range(nb_rows))
    return tuple(map(''.join, lines))


GRIDS = tuple(map(spec2grid, SPECIFICS))
# from pprint import pprint
# pprint(GRIDS, width=60)

TESTS = {'Basic': [], 'Extra': []}
for n, grid in enumerate(GRIDS):
    category = ('Basic', 'Extra')[n >= 3]
    TESTS[category].append({'input': grid, 'answer': grid})
