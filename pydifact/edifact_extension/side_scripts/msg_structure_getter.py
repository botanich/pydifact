import urllib.request
import re


def rec_print(lst, depth=0):
    indent1 = " " * 4*(depth+1)
    indent2 = " " * 4*depth

    if lst is False:
        print(lst, end="")
        return

    print("[")
    for value in lst:
        print(indent1 + f'("{value[0]}", "{value[1]}", {value[2]}, ', end="")
        rec_print(value[3], depth+1)
        print("),")
    print(indent2 + "]", end="")


def generate_structure_list(version="D96A", doc_type="ORDERS"):
    fp = urllib.request.urlopen(f"https://www.edifactory.de/edifact/directory/{version}/message/{doc_type}")
    text = fp.read()

    text = text.decode("utf8")
    fp.close()

    pattern = re.compile(r'(<h3 data-toggle.*</h3>|'
                         rf'<a href="/edifact/directory/{version}/segment/.../popup">...</a>.*|'
                         r'<div|</div>)')
    matches = re.findall(pattern, text)

    nesting = 0
    stack = []
    res = []
    indices = []
    for match in matches:
        if match == "<div":
            nesting += 1
        elif match == "</div>":
            nesting -= 1
        else:
            name_start = match.find(">") + 1
            end_str = "</a>" if "<a" in match else " "
            name_end = match.find(end_str, name_start)
            name = match[name_start: name_end]
            mc = match[match.find("(", name_end) - 1]
            rep_cnt = int(match[match.find("(", name_end)+1: match.find(")", name_end)])
            seg_lst = (name, mc, rep_cnt, False if "<a" in match else [])
            curr_lst = res
            while stack and nesting <= stack[-1][1]:
                del stack[-1]
                del indices[-1]
            for index in indices:
                curr_lst = curr_lst[index][3]
            curr_lst.append(seg_lst)
            if "<h3" in match and (not stack or stack and nesting > stack[-1][1]):
                stack.append((name, nesting))
                indices.append(len(curr_lst) - 1)

    return res


def main():
    rec_print(generate_structure_list())


if __name__ == "__main__":
    main()
