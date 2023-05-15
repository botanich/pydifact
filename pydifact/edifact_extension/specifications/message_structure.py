# -*- coding: utf-8 -*-

"""
    File with the documents' structure, specified for each supported version/document

    _msg_structure contents: {
        version: {
            message_type: [
                (segment_tag, Mandatory/Conditional, max_repetition_count, False),
                (segment_group, Mandatory/Conditional, max_repetition_count, [...same_contents_as_this_list...]]),
    ]}}
    :type _message_structure: dict(
        str: dict(
            str: list(
                tuple(str, str, int, bool/list(...))
    )))
"""

_message_structure = {
    "D96A": {
        "ORDERS": [
            # UNH segment is parsed separately
            # ("UNH", "M", 1, False),
            ("BGM", "M", 1, False),
            ("DTM", "M", 35, False),
            ("PAI", "C", 1, False),
            ("ALI", "C", 5, False),
            ("IMD", "C", 1, False),
            ("FTX", "C", 99, False),
            ("SG1", "C", 10, [
                ("RFF", "M", 1, False),
                ("DTM", "C", 5, False),
            ]),
            ("SG2", "C", 99, [
                ("NAD", "M", 1, False),
                ("LOC", "C", 25, False),
                ("FII", "C", 5, False),
                ("SG3", "C", 10, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG4", "C", 5, [
                    ("DOC", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG5", "C", 5, [
                    ("CTA", "M", 1, False),
                    ("COM", "C", 5, False),
                ]),
            ]),
            ("SG6", "C", 5, [
                ("TAX", "M", 1, False),
                ("MOA", "C", 1, False),
                ("LOC", "C", 5, False),
            ]),
            ("SG7", "C", 5, [
                ("CUX", "M", 1, False),
                ("PCD", "C", 5, False),
                ("DTM", "C", 5, False),
            ]),
            ("SG8", "C", 10, [
                ("PAT", "M", 1, False),
                ("DTM", "C", 5, False),
                ("PCD", "C", 1, False),
                ("MOA", "C", 1, False),
            ]),
            ("SG9", "C", 10, [
                ("TDT", "M", 1, False),
                ("SG10", "C", 10, [
                    ("LOC", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
            ]),
            ("SG11", "C", 5, [
                ("TOD", "M", 1, False),
                ("LOC", "C", 2, False),
            ]),
            ("SG12", "C", 10, [
                ("PAC", "M", 1, False),
                ("MEA", "C", 5, False),
                ("SG13", "C", 5, [
                    ("PCI", "M", 1, False),
                    ("RFF", "C", 1, False),
                    ("DTM", "C", 5, False),
                    ("GIN", "C", 10, False),
                ]),
            ]),
            ("SG14", "C", 10, [
                ("EQD", "M", 1, False),
                ("HAN", "C", 5, False),
                ("MEA", "C", 5, False),
                ("FTX", "C", 5, False),
            ]),
            ("SG15", "C", 10, [
                ("SCC", "M", 1, False),
                ("FTX", "C", 5, False),
                ("RFF", "C", 5, False),
                ("SG16", "C", 10, [
                    ("QTY", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
            ]),
            ("SG17", "C", 25, [
                ("APR", "M", 1, False),
                ("DTM", "C", 5, False),
                ("RNG", "C", 1, False),
            ]),
            ("SG18", "C", 15, [
                ("ALC", "M", 1, False),
                ("ALI", "C", 5, False),
                ("DTM", "C", 5, False),
                ("SG19", "C", 1, [
                    ("QTY", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG20", "C", 1, [
                    ("PCD", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG21", "C", 2, [
                    ("MOA", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG22", "C", 1, [
                    ("RTE", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG23", "C", 5, [
                    ("TAX", "M", 1, False),
                    ("MOA", "C", 1, False),
                ]),
            ]),
            ("SG24", "C", 100, [
                ("RCS", "M", 1, False),
                ("RFF", "C", 5, False),
                ("DTM", "C", 5, False),
                ("FTX", "C", 5, False),
            ]),
            ("SG25", "C", 200000, [
                ("LIN", "M", 1, False),
                ("PIA", "C", 25, False),
                ("IMD", "C", 99, False),
                ("MEA", "C", 5, False),
                ("QTY", "C", 10, False),
                ("PCD", "C", 5, False),
                ("ALI", "C", 5, False),
                ("DTM", "C", 35, False),
                ("MOA", "C", 10, False),
                ("GIN", "C", 1000, False),
                ("GIR", "C", 1000, False),
                ("QVR", "C", 1, False),
                ("DOC", "C", 5, False),
                ("PAI", "C", 1, False),
                ("FTX", "C", 99, False),
                ("SG26", "C", 999, [
                    ("CCI", "M", 1, False),
                    ("CAV", "C", 10, False),
                    ("MEA", "C", 10, False),
                ]),
                ("SG27", "C", 10, [
                    ("PAT", "M", 1, False),
                    ("DTM", "C", 5, False),
                    ("PCD", "C", 1, False),
                    ("MOA", "C", 1, False),
                ]),
                ("SG28", "C", 25, [
                    ("PRI", "M", 1, False),
                    ("CUX", "C", 1, False),
                    ("APR", "C", 1, False),
                    ("RNG", "C", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG29", "C", 10, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG30", "C", 10, [
                    ("PAC", "M", 1, False),
                    ("MEA", "C", 5, False),
                    ("QTY", "C", 5, False),
                    ("DTM", "C", 5, False),
                    ("SG31", "C", 1, [
                        ("RFF", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                    ("SG32", "C", 5, [
                        ("PCI", "M", 1, False),
                        ("RFF", "C", 1, False),
                        ("DTM", "C", 5, False),
                        ("GIN", "C", 10, False),
                    ]),
                ]),
                ("SG33", "C", 9999, [
                    ("LOC", "M", 1, False),
                    ("QTY", "C", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG34", "C", 10, [
                    ("TAX", "M", 1, False),
                    ("MOA", "C", 1, False),
                    ("LOC", "C", 5, False),
                ]),
                ("SG35", "C", 99, [
                    ("NAD", "M", 1, False),
                    ("LOC", "C", 5, False),
                    ("SG36", "C", 5, [
                        ("RFF", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                    ("SG37", "C", 5, [
                        ("DOC", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                    ("SG38", "C", 5, [
                        ("CTA", "M", 1, False),
                        ("COM", "C", 5, False),
                    ]),
                ]),
                ("SG39", "C", 99, [
                    ("ALC", "M", 1, False),
                    ("ALI", "C", 5, False),
                    ("DTM", "C", 5, False),
                    ("SG40", "C", 1, [
                        ("QTY", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG41", "C", 1, [
                        ("PCD", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG42", "C", 2, [
                        ("MOA", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG43", "C", 1, [
                        ("RTE", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG44", "C", 5, [
                        ("TAX", "M", 1, False),
                        ("MOA", "C", 1, False),
                    ]),
                ]),
                ("SG45", "C", 10, [
                    ("TDT", "M", 1, False),
                    ("SG46", "C", 10, [
                        ("LOC", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                ]),
                ("SG47", "C", 5, [
                    ("TOD", "M", 1, False),
                    ("LOC", "C", 2, False),
                ]),
                ("SG48", "C", 10, [
                    ("EQD", "M", 1, False),
                    ("HAN", "C", 5, False),
                    ("MEA", "C", 5, False),
                    ("FTX", "C", 5, False),
                ]),
                ("SG49", "C", 100, [
                    ("SCC", "M", 1, False),
                    ("FTX", "C", 5, False),
                    ("RFF", "C", 5, False),
                    ("SG50", "C", 10, [
                        ("QTY", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                ]),
                ("SG51", "C", 100, [
                    ("RCS", "M", 1, False),
                    ("RFF", "C", 5, False),
                    ("DTM", "C", 5, False),
                    ("FTX", "C", 5, False),
                ]),
                ("SG52", "C", 10, [
                    ("STG", "M", 1, False),
                    ("SG53", "C", 3, [
                        ("QTY", "M", 1, False),
                        ("MOA", "C", 1, False),
                    ]),
                ]),
            ]),
            ("UNS", "M", 1, False),
            ("MOA", "C", 12, False),
            ("CNT", "C", 10, False),
            ("SG54", "C", 10, [
                ("ALC", "M", 1, False),
                ("ALI", "C", 1, False),
                ("MOA", "M", 2, False),
            ]),
            # UNT segment is parsed separately
            # ("UNT", "M", 1, False),
        ],
        "DESADV": [
            # UNH segment is parsed separately
            # ("UNH", "M", 1, False),
            ("BGM", "M", 1, False),
            ("DTM", "C", 10, False),
            ("ALI", "C", 5, False),
            ("MEA", "C", 5, False),
            ("MOA", "C", 5, False),
            ("SG1", "C", 10, [
                ("RFF", "M", 1, False),
                ("DTM", "C", 1, False),
            ]),
            ("SG2", "C", 10, [
                ("NAD", "M", 1, False),
                ("LOC", "C", 10, False),
                ("SG3", "C", 10, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 1, False),
                ]),
                ("SG4", "C", 10, [
                    ("CTA", "M", 1, False),
                    ("COM", "C", 5, False),
                ]),
            ]),
            ("SG5", "C", 10, [
                ("TOD", "M", 1, False),
                ("LOC", "C", 5, False),
                ("FTX", "C", 5, False),
            ]),
            ("SG6", "C", 10, [
                ("TDT", "M", 1, False),
                ("PCD", "C", 6, False),
                ("SG7", "C", 10, [
                    ("LOC", "M", 1, False),
                    ("DTM", "C", 10, False),
                ]),
            ]),
            ("SG8", "C", 10, [
                ("EQD", "M", 1, False),
                ("MEA", "C", 5, False),
                ("SEL", "C", 25, False),
                ("EQA", "C", 5, False),
                ("SG9", "C", 10, [
                    ("HAN", "M", 1, False),
                    ("FTX", "C", 10, False),
                ]),
            ]),
            ("SG10", "C", 9999, [
                ("CPS", "M", 1, False),
                ("FTX", "C", 5, False),
                ("SG11", "C", 9999, [
                    ("PAC", "M", 1, False),
                    ("MEA", "C", 10, False),
                    ("QTY", "C", 10, False),
                    ("SG12", "C", 10, [
                        ("HAN", "M", 1, False),
                        ("FTX", "C", 10, False),
                    ]),
                    ("SG13", "C", 1000, [
                        ("PCI", "M", 1, False),
                        ("RFF", "C", 1, False),
                        ("DTM", "C", 5, False),
                        ("GIR", "C", 99, False),
                        ("SG14", "C", 99, [
                            ("GIN", "M", 1, False),
                            ("DLM", "C", 10, False),
                        ]),
                    ]),
                ]),
                ("SG15", "C", 9999, [
                    ("LIN", "M", 1, False),
                    ("PIA", "C", 10, False),
                    ("IMD", "C", 25, False),
                    ("MEA", "C", 10, False),
                    ("QTY", "C", 10, False),
                    ("ALI", "C", 10, False),
                    ("GIN", "C", 100, False),
                    ("GIR", "C", 100, False),
                    ("DLM", "C", 100, False),
                    ("DTM", "C", 5, False),
                    ("FTX", "C", 5, False),
                    ("MOA", "C", 5, False),
                    ("SG16", "C", 10, [
                        ("RFF", "M", 1, False),
                        ("DTM", "C", 1, False),
                    ]),
                    ("SG17", "C", 10, [
                        ("DGS", "M", 1, False),
                        ("QTY", "C", 1, False),
                        ("FTX", "C", 5, False),
                    ]),
                    ("SG18", "C", 100, [
                        ("LOC", "M", 1, False),
                        ("NAD", "C", 1, False),
                        ("DTM", "C", 1, False),
                        ("QTY", "C", 10, False),
                    ]),
                    ("SG19", "C", 1000, [
                        ("SGP", "M", 1, False),
                        ("QTY", "C", 10, False),
                    ]),
                    ("SG20", "C", 9999, [
                        ("PCI", "M", 1, False),
                        ("DTM", "C", 5, False),
                        ("MEA", "C", 10, False),
                        ("QTY", "C", 1, False),
                        ("SG21", "C", 10, [
                            ("GIN", "M", 1, False),
                            ("DLM", "C", 100, False),
                        ]),
                        ("SG22", "C", 10, [
                            ("HAN", "M", 1, False),
                            ("FTX", "C", 5, False),
                            ("GIN", "C", 1000, False),
                        ]),
                    ]),
                    ("SG23", "C", 10, [
                        ("QVR", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                ]),
            ]),
            ("CNT", "C", 5, False),
            # UNT segment is parsed separately
            # ("UNT", "M", 1, False),
        ],
        "INVOIC": [
            # UNH segment is parsed separately
            # ("UNH", "M", 1, False),
            ("BGM", "M", 1, False),
            ("DTM", "M", 35, False),
            ("PAI", "C", 1, False),
            ("ALI", "C", 5, False),
            ("IMD", "C", 1, False),
            ("FTX", "C", 10, False),
            ("SG1", "C", 99, [
                ("RFF", "M", 1, False),
                ("DTM", "C", 5, False),
            ]),
            ("SG2", "C", 99, [
                ("NAD", "M", 1, False),
                ("LOC", "C", 25, False),
                ("FII", "C", 5, False),
                ("SG3", "C", 9999, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG4", "C", 5, [
                    ("DOC", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG5", "C", 5, [
                    ("CTA", "M", 1, False),
                    ("COM", "C", 5, False),
                ]),
            ]),
            ("SG6", "C", 5, [
                ("TAX", "M", 1, False),
                ("MOA", "C", 1, False),
                ("LOC", "C", 5, False),
            ]),
            ("SG7", "C", 5, [
                ("CUX", "M", 1, False),
                ("DTM", "C", 5, False),
            ]),
            ("SG8", "C", 10, [
                ("PAT", "M", 1, False),
                ("DTM", "C", 5, False),
                ("PCD", "C", 1, False),
                ("MOA", "C", 1, False),
                ("PAI", "C", 1, False),
                ("FII", "C", 1, False),
            ]),
            ("SG9", "C", 10, [
                ("TDT", "M", 1, False),
                ("SG10", "C", 10, [
                    ("LOC", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG11", "C", 9999, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
            ]),
            ("SG12", "C", 5, [
                ("TOD", "M", 1, False),
                ("LOC", "C", 2, False),
            ]),
            ("SG13", "C", 1000, [
                ("PAC", "M", 1, False),
                ("MEA", "C", 5, False),
                ("SG14", "C", 5, [
                    ("PCI", "M", 1, False),
                    ("RFF", "C", 1, False),
                    ("DTM", "C", 5, False),
                    ("GIN", "C", 5, False),
                ]),
            ]),
            ("SG15", "C", 9999, [
                ("ALC", "M", 1, False),
                ("ALI", "C", 5, False),
                ("SG16", "C", 5, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG17", "C", 1, [
                    ("QTY", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG18", "C", 1, [
                    ("PCD", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG19", "C", 2, [
                    ("MOA", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG20", "C", 1, [
                    ("RTE", "M", 1, False),
                    ("RNG", "C", 1, False),
                ]),
                ("SG21", "C", 5, [
                    ("TAX", "M", 1, False),
                    ("MOA", "C", 1, False),
                ]),
            ]),
            ("SG22", "C", 100, [
                ("RCS", "M", 1, False),
                ("RFF", "C", 5, False),
                ("DTM", "C", 5, False),
                ("FTX", "C", 5, False),
            ]),
            ("SG23", "C", 1, [
                ("AJT", "M", 1, False),
                ("FTX", "C", 5, False),
            ]),
            ("SG24", "C", 1, [
                ("INP", "M", 1, False),
                ("FTX", "C", 5, False),
            ]),
            ("SG25", "C", 9999999, [
                ("LIN", "M", 1, False),
                ("PIA", "C", 25, False),
                ("IMD", "C", 10, False),
                ("MEA", "C", 5, False),
                ("QTY", "C", 5, False),
                ("PCD", "C", 1, False),
                ("ALI", "C", 5, False),
                ("DTM", "C", 35, False),
                ("GIN", "C", 1000, False),
                ("GIR", "C", 1000, False),
                ("QVR", "C", 1, False),
                ("EQD", "C", 1, False),
                ("FTX", "C", 5, False),
                ("SG26", "C", 5, [
                    ("MOA", "M", 1, False),
                    ("CUX", "C", 1, False),
                ]),
                ("SG27", "C", 10, [
                    ("PAT", "M", 1, False),
                    ("DTM", "C", 5, False),
                    ("PCD", "C", 1, False),
                    ("MOA", "C", 1, False),
                ]),
                ("SG28", "C", 25, [
                    ("PRI", "M", 1, False),
                    ("APR", "C", 1, False),
                    ("RNG", "C", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG29", "C", 10, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG30", "C", 10, [
                    ("PAC", "M", 1, False),
                    ("MEA", "C", 10, False),
                    ("SG31", "C", 10, [
                        ("PCI", "M", 1, False),
                        ("RFF", "C", 1, False),
                        ("DTM", "C", 5, False),
                        ("GIN", "C", 10, False),
                    ]),
                ]),
                ("SG32", "C", 9999, [
                    ("LOC", "M", 1, False),
                    ("QTY", "C", 100, False),
                    ("DTM", "C", 5, False),
                ]),
                ("SG33", "C", 99, [
                    ("TAX", "M", 1, False),
                    ("MOA", "C", 1, False),
                    ("LOC", "C", 5, False),
                ]),
                ("SG34", "C", 20, [
                    ("NAD", "M", 1, False),
                    ("LOC", "C", 5, False),
                    ("SG35", "C", 5, [
                        ("RFF", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                    ("SG36", "C", 5, [
                        ("DOC", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                    ("SG37", "C", 5, [
                        ("CTA", "M", 1, False),
                        ("COM", "C", 5, False),
                    ]),
                ]),
                ("SG38", "C", 15, [
                    ("ALC", "M", 1, False),
                    ("ALI", "C", 5, False),
                    ("DTM", "C", 5, False),
                    ("SG39", "C", 1, [
                        ("QTY", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG40", "C", 1, [
                        ("PCD", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG41", "C", 2, [
                        ("MOA", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG42", "C", 1, [
                        ("RTE", "M", 1, False),
                        ("RNG", "C", 1, False),
                    ]),
                    ("SG43", "C", 5, [
                        ("TAX", "M", 1, False),
                        ("MOA", "C", 1, False),
                    ]),
                ]),
                ("SG44", "C", 10, [
                    ("TDT", "M", 1, False),
                    ("SG45", "C", 10, [
                        ("LOC", "M", 1, False),
                        ("DTM", "C", 5, False),
                    ]),
                ]),
                ("SG46", "C", 5, [
                    ("TOD", "M", 1, False),
                    ("LOC", "C", 2, False),
                ]),
                ("SG47", "C", 100, [
                    ("RCS", "M", 1, False),
                    ("RFF", "C", 5, False),
                    ("DTM", "C", 5, False),
                    ("FTX", "C", 5, False),
                ]),
            ]),
            ("UNS", "M", 1, False),
            ("CNT", "C", 10, False),
            ("SG48", "M", 100, [
                ("MOA", "M", 1, False),
                ("SG49", "C", 1, [
                    ("RFF", "M", 1, False),
                    ("DTM", "C", 5, False),
                ]),
            ]),
            ("SG50", "C", 10, [
                ("TAX", "M", 1, False),
                ("MOA", "C", 2, False),
            ]),
            ("SG51", "C", 15, [
                ("ALC", "M", 1, False),
                ("ALI", "C", 1, False),
                ("MOA", "C", 2, False),
            ]),
            # UNT segment is parsed separately
            # ("UNT", "M", 1, False),
        ],
    }
}
