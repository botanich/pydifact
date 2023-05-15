# -*- coding: utf-8 -*-

def pretty_print(dct):
    indent = " "*4
    print("{")
    for key in dct:
        print(indent, '"', key[0], '": ', dct[key], ",",  sep="")
    print("}")


def get_elements_restrictions(filename="/home/enapps/Downloads/EDI/d96a/TRED/TRED.96A"):
    with open(filename, encoding="CP437") as file:
        res = {}
        text = file.read().split("\n\n" + "─"*70 + "\n\n")[1:]
        for element_data in text:
            details = element_data.split("\n")
            tag = details[0][3:7]
            short_desc = details[0][9:]
            for line in details:
                if line[3:8] == "Repr:":
                    restr = line[9:]

                    pointer = 1
                    if len(restr) >= 2 and restr[0:2] == "an":
                        an = "an"
                        pointer = 2
                    elif restr[0] == "a":
                        an = "a"
                    else:
                        an = "n"

                    if restr[pointer] == ".":
                        max_value = int(restr[pointer+2:])
                        min_value = 1
                    else:
                        max_value = int(restr[pointer])
                        min_value = max_value

                    res[(tag, short_desc)] = (an, min_value, max_value)
                    break
        return res


def main():
    pretty_print(get_elements_restrictions())


if __name__ == "__main__":
    main()
