# -*- coding: utf-8 -*-

def get_composites(filename="/home/enapps/Downloads/EDI/d96a/TRCD/TRCD.96A"):
    with open(filename, encoding="ISO-8859-1") as file:
        text = file.read().strip().split("\n\n" + "Ä"*70 + "\n\n")[1:]
        res = {}
        for composite in text:
            details = composite.split("\n\n")
            details[0] = details[0].strip()
            if len(details[0].split()[0]) != 4:
                details[0] = details[0][2:]
            res[details[0]] = []
            flag_first = True
            short_desc = ""
            for line in details[-1].split("\n"):
                line = line[6:]
                if line[0] == " ":
                    short_desc += " " + line.strip()
                if line[0] != " ":
                    if not flag_first:
                        res[details[0]].append((element_tag, mandatory, short_desc))
                    line_details = line.split()
                    element_tag = line_details[0]
                    mandatory = line_details[-2]
                    short_desc = " ".join(line_details[1: -2])
                    flag_first = False
            if line[0] == " ":
                short_desc += " " + line.strip()
            res[details[0]].append((element_tag, mandatory, short_desc))
    return res


def pretty_print(dct):
    print("{")
    indent = " " * 4
    for key in dct:
        splt = key.split()
        print(indent, '"', splt[0], '": [  # ', " ".join(splt[1:]), sep="")
        for tup in dct[key]:
            print(indent*2 + str(tup[: -1]).replace("'", '"') + ",  # " + tup[-1])
        print(indent + "], ")
    print("}")


def check_smth(dct):
    for key in dct:
        value = dct[key]
        prev = "M"
        for line in value:
            if line[1] == "M" and prev == "C":
                print("YEEEP", key)
            prev = line[1]


def main():
    pretty_print(get_composites())
    print("____________")
    check_smth(get_composites())
    print("____________")


if __name__ == "__main__":
    main()
