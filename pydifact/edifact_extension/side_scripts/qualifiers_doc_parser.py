# -*- coding: utf-8 -*-

import pprint


def get_qualifiers(filename="/home/enapps/Downloads/EDI/d96a/UNCL/UNCL-1.96A"):
    filename2 = filename[0:-5] + "2" + filename[-4:]
    with open(filename, encoding="CP437") as file:
        text1 = file.read()
    with open(filename2, encoding="CP437") as file:
        text2 = file.read()
    text = text1 + text2
    res = {}
    text = text.split("\n\n" + "─"*70 + "\n\n")
    for element_data in text[1:]:
        element_tag = element_data[2:6]
        res[element_tag] = []
        if element_data[0] == "-":
            continue
        details = element_data.split("\n\n")
        lines = details[-1].split("\n")
        for line in lines:
            if not line:
                continue
            if line[0] == "-":
                continue
            if line.startswith(" "*10):
                continue
            line_details = line.split()
            if line_details[0][0] in ("+", "*", "#", "|", "-", "X") and line[0] != " ":
                line_details = line_details[1:]
            if line_details[0] == "ZZZ":
                continue
            qualifier = line_details[0]
            res[element_tag].append(qualifier)
    return res


def main():
    pprint.pprint(get_qualifiers(), width=116, indent=4, compact=True)


if __name__ == "__main__":
    main()
