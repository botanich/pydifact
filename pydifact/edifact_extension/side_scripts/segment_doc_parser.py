# -*- coding: utf-8 -*-


def pretty_print(dct):
    indent = " " * 4
    print("{")
    for key in dct:
        print(indent, '"', key[0], '": [  # ', key[1], sep="")
        for elem in dct[key]:
            print(indent*2, str(elem).replace("'", '"'), ",", sep="")
        print(indent + "],")
    print("}")


def get_segment_structure(filename):
    print(filename)
    with open(filename, encoding="CP437") as file:
        text = file.read().strip().split("\n\n" + "─" * 70 + "\n\n")[1:]
        res = {}
        for segment_data in text:
            details = segment_data.split("\n")
            segment_tag = details[0][6:9]
            segment_short_desc = details[0][13:].strip()
            res[(segment_tag, segment_short_desc)] = []
            for line in details:
                if line[0:3].isnumeric():
                    element_tag = line[6:10]
                    if element_tag[0] == "C":
                        mandatory = line.strip()[-1]
                    else:
                        mandatory = line.split()[-2]
                    res[(segment_tag, segment_short_desc)].append([element_tag, mandatory])
        return res


def main():
    pretty_print(get_segment_structure(input("filepath to TRSD file: ")))


if __name__ == "__main__":
    main()
