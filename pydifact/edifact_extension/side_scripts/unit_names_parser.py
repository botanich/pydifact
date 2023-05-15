import sys
import json


def extract_names(filename):
    """
        Takes path to file with list of EDIFACT units (i.e. TRSDI.96A) and extracts all segments and their names
        respectfully.
    """
    with open(filename, encoding="CP437") as file:
        res = {}
        text = file.read().strip().split("   Tag   Name")[1].strip()
        for segment_data in text.split("\n"):
            tag_and_name = segment_data.split()
            if tag_and_name[0] == "-":
                continue
            if tag_and_name[0][0] in ("+", "*", "#", "|", "X"):
                del tag_and_name[0]

            tag = tag_and_name[0]
            raw_name = "_".join(tag_and_name[1:])

            name = []
            for char in raw_name:
                name.append(char if char.isalpha() else "_")

            res[tag] = "".join(name)
    return res


def main():
    segment_file_ind = composite_file_ind = element_file_ind = service_file_ind = None
    try:
        segment_file_ind = sys.argv.index("-s")
    except ValueError:
        pass

    try:
        composite_file_ind = sys.argv.index("-c")
    except ValueError:
        pass

    try:
        element_file_ind = sys.argv.index("-e")
    except ValueError:
        pass

    try:
        service_file_ind = sys.argv.index("-r")
    except ValueError:
        pass

    try:
        output_file_ind = sys.argv.index("-o")
    except ValueError:
        print("Format: python unit_names_parser [-s segments_filename] [-c composites_filename] [-e elements_filename] "
              "[-r service_list_filename] <-o output_filename>")
        exit()

    res = {}
    if segment_file_ind:
        res["segment_names"] = extract_names(sys.argv[segment_file_ind+1])
    if composite_file_ind:
        res["composite_names"] = extract_names(sys.argv[composite_file_ind+1])
    if element_file_ind:
        res["element_names"] = extract_names(sys.argv[element_file_ind+1])
    if service_file_ind:
        res["service_names"] = extract_names(sys.argv[element_file_ind+1])

    output_file = sys.argv[output_file_ind+1]
    with open(output_file, "w") as output_file:
        json.dump(res, output_file, indent=4)
    print("success")


if __name__ == "__main__":
    main()
