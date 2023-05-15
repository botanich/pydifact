# -*- coding: utf-8 -*-
import io
import json
from collections import OrderedDict
from typing import Union, Optional, Literal, TextIO
from enum import Enum

from ..segments import Segment
from ..segmentcollection import Interchange, EDISyntaxError
from .specifications.specification_getter import get_specs
from .specifications.char_set import alphabetic_char_set, numeric_char_set, alphanumeric_char_set


class CharType(Enum):
    ALPHA = 0
    ALPHANUMERIC = 1
    NUMERIC = 2


mesg_struc = get_specs("message_structure")
segm_struc = get_specs("segment_structure")
comp_struc = get_specs("composite_structure")
elem_restr = get_specs("element_restrictions")
unit_names = get_specs("unit_names")


def pretty_spaces(pretty, indent, depth):
    space = " " * pretty * indent * depth
    inner_space = space + " " * pretty * indent
    end_line = "\n" * pretty
    return space, inner_space, end_line


class SegmentList(list):
    def by_qualifier(self, qualifier, indices, path):
        if not indices and not path:
            raise ValueError("Can find qualifier only if its position is specified")
        if path:
            raise NotImplementedError("Use indices please")
        for segment in self:
            element = segment
            for index in indices:
                element = element[index]
            if element.value == qualifier:
                return segment
        return None


class EdifactInterchange:
    """
        Class, containing the whole interchange (that is usually contained in file). This class
        is top-level parent for all smaller EDIFACT elements and directly contains EdifactMessages as
        its children (in terms of presenting EDIFACT elements hierarchy as tree). It also provides validation
        on creation.
    """
    def __init__(self, interchange: Interchange) -> None:
        """
            Intended to be used from classmethods from_file and from_str, not directly.
            Takes already preparsed by pydifact library interchange, parses it further and validates
            during parsing.
        """
        self._interchange = interchange
        self._sender = \
            self._interchange.sender if isinstance(self._interchange.sender, list) else [self._interchange.sender]

        # seg_num shows the number of the segment so if the file is divided by line feeds then
        # failed segment can be easily tracked. The first segment is UNA (if present), the second - UNB,
        # numeration of the first message segment starts from 3
        seg_num = int(self._interchange.has_una_segment) + 2
        for segment in self._interchange.segments:
            segment.number = seg_num
            seg_num += 1

        self.messages = []
        message = []
        for segment in self._interchange.segments:
            message.append(segment)
            if segment.tag == "UNT":
                self.messages.append(EdifactMessage(message, self))
                message.clear()

    def __repr__(self) -> str:
        return f"EdifactInterchange{repr(self.messages)}"

    def __str__(self) -> str:
        return f"EdifactInterchange{[msg.type for msg in self.messages]}"

    def __getitem__(self, tag: str) -> list["EdifactMessage"]:
        return [msg for msg in self.messages if msg.tag == tag]

    def unb_to_dict(self):
        def list_get(lst, index):
            return lst[index] if len(lst) > index else None

        return {
            "Syntax_identifier": {
                "Syntax_identifier": list_get(self._interchange.syntax_identifier, 0),
                "Syntax_version_number": list_get(self._interchange.syntax_identifier, 1),
            },
            "Interchange_sender": {
                "Sender_identification": list_get(self._interchange.sender, 0),
                "Partner_identification_code_qualifier": list_get(self._interchange.sender, 1),
                "Address_for_reverse_routing": list_get(self._interchange.sender, 2),
            },
            "Interchange_recipient": {
                "Sender_identification": list_get(self._interchange.recipient, 0),
                "Partner_identification_code_qualifier": list_get(self._interchange.recipient, 1),
                "Address_for_reverse_routing": list_get(self._interchange.recipient, 2)
            },
            "Date_time_of_preparation": {
                "Date_of_preparation": self._interchange.timestamp.strftime("%y%m%d"),
                "Time_of_preparation": self._interchange.timestamp.strftime("%H%M"),
            },
            "Interchange_control_reference": self._interchange.control_reference,
        }

    def unz_to_dict(self):
        return {
            "Interchange_control_count": str(len(self.messages)),
            "Interchange_control_reference": self._interchange.control_reference,
        }

    def str_json(self, pretty=False, indent=4, depth=0):
        with io.StringIO() as res:
            self.file_json(res, pretty, indent, depth)
            return res.getvalue()

    def file_json(self, file, pretty=False, indent=4, depth=0) -> None:
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        file.write("{" + end_line)

        unb = self.unb_to_dict()
        if pretty:
            file.write(inner_space + '"Interchange_header": '
                       + json.dumps(unb, indent=indent).replace("\n", "\n" + inner_space) + "," + end_line)
        else:
            file.write('"Interchange_header":' + json.dumps(unb) + ",")

        file.write(inner_space + '"messages": [' + end_line)
        for i in range(len(self.messages)):
            if i != 0:
                file.write("," + end_line)
            self.messages[i].file_json(file, pretty, indent, depth + 2)
        file.write(end_line + inner_space + "]," + end_line)

        unz = self.unz_to_dict()
        if pretty:
            file.write(inner_space + '"Interchange_trailer": '
                       + json.dumps(unz, indent=indent).replace("\n", "\n" + inner_space) + end_line)
        else:
            file.write('"Interchange_trailer":' + json.dumps(unz))

        file.write("}")

    def str_xml(self, pretty=False, indent=4, depth=0):
        with io.StringIO() as res:
            self.file_xml(res, pretty, indent, depth)
            return res.getvalue()

    def file_xml(self, file, pretty=False, indent=4, depth=0):
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        double_space = inner_space + " "*pretty*indent
        triple_space = double_space + " "*pretty*indent
        file.write(f"<Interchange>" + end_line)

        unb = self.unb_to_dict()
        file.write(inner_space + "<Interchange_header>" + end_line)
        for comp_name in unb:
            if isinstance(unb[comp_name], dict):
                file.write(double_space + f"<{comp_name}>" + end_line)
                for elem_name in unb[comp_name]:
                    file.write(triple_space + f"<{elem_name}>{unb[comp_name][elem_name]}</{elem_name}>" + end_line)
                file.write(double_space + f"</{comp_name}>" + end_line)
            else:
                file.write(double_space + f"<{comp_name}>{unb[comp_name]}</{comp_name}>" + end_line)
        file.write(inner_space + f"</Interchange_header>" + end_line)

        for msg in self.messages:
            msg.file_xml(file, pretty, indent, depth + 1)

        unz = self.unz_to_dict()
        file.write(end_line + inner_space + "<Interchange_trailer>" + end_line)
        for elem_name in unz:
            file.write(double_space + f"<{elem_name}>{unz[elem_name]}</{elem_name}>" + end_line)
        file.write(inner_space + "</Interchange_trailer>" + end_line)

        file.write(f"</Interchange>")

    @classmethod
    def from_file(cls, file_path: str) -> "EdifactInterchange":
        return EdifactInterchange(Interchange.from_file(file_path))

    @classmethod
    def from_str(cls, string: str) -> "EdifactInterchange":
        return EdifactInterchange(Interchange.from_str(string))

    @property
    def sender(self) -> Union[str, list[str]]:
        return self._sender

    @property
    def interchange_str(self) -> str:
        """ Returns plain interchange text with linebreaks added after each segment for readability """
        str_terminator = self._interchange.delimiters.segment_terminator
        return str(self._interchange).replace(str_terminator, str_terminator+'\n')


class EdifactSegmentGroup:
    """
        Represents EDIFACT segment group - abstraction that contains segments directly and other segment groups,
        thus creating tree hierarchy of them.
    """
    def __init__(
        self,
        tag: str,
        parent: "EdifactSegmentGroup",
        struc: list[tuple[str, str, int, Union[Literal[False], list]]],
    ):
        """
            Takes struc - structure of the group (full description of what possibly
            can be there) which is different for every message type and, sometimes, version, which contained fully in
            specifications package; then uses it for parsing. This method is not intended to be used directly, but
            only on parsing the whole interchange, starting from constructor of EDIFACT Interchange.
        """
        # general message data
        self._tag = tag
        self._parent = parent
        self._parent_message = parent._parent_message

        self._version = self._parent_message.version
        self._struc = (value for value in struc)

        self.contents = OrderedDict()
        self._parse()

    def __repr__(self):
        return f"EdifactSegmentGroup {self._tag}: {self.contents}"

    def __str__(self):
        return f"EdifactSegmentGroup {self._tag}: [{', '.join(map(str, self.contents))}]"

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, key: Union[int, str]) -> \
            Union[list["EdifactSegmentGroup"], list["EdifactSegment"], "EdifactSegmentGroup", "EdifactSegment"]:
        """
            Returns contained segment or segment group. As there might be several of each, returns list of them
            if item is requested by tag and only one instance if it's requested by index.
        """
        if isinstance(key, int):
            for lst in self.contents.values():
                if len(lst) <= key:
                    key -= len(lst)
                else:
                    return lst[key]
            raise IndexError("Segment group index out of range")
        elif isinstance(key, str):
            return SegmentList(self.contents[key])
        else:
            raise KeyError("Key type must be int or str")

    def _look_up_segment(self, nested_list: list[tuple[str, str, int, Union[Literal[False], list]]]):
        """
            Returns True if nested_list contains current message segment without mandatory segments before it,
            False otherwise. Recursive.
        """
        res = False
        for segment_or_group in nested_list:
            struc_tag, mandatory, group_content = segment_or_group[0], segment_or_group[1] == "M", segment_or_group[3]
            if group_content is not False:  # so current list element is a group
                res |= self._look_up_segment(group_content)
            if struc_tag == self._parent_message._curr_segment.tag:
                return True
            if mandatory:
                break
        return res

    def _parse(self):
        for segment_or_group in self._struc:
            tag = segment_or_group[0]
            mandatory = segment_or_group[1] == "M"
            rep_cnt = segment_or_group[2]  # max times segment or group can occur in current segment group
            group_content = segment_or_group[3]

            parsed_on_struc_iteration = False
            parsed_on_file_iteration = True  # emulating do-while loop (only to get into it first time)
            while rep_cnt > 0 and parsed_on_file_iteration:
                parsed_on_file_iteration = False
                if group_content is not False:
                    # if currently parsed segment is not in the currently checked segment group,
                    # no need to visit it at all
                    if not self._look_up_segment(group_content):
                        # if segment is mandatory but can occur multiple times, should raise error only if
                        # there is no segment at all
                        if mandatory and not parsed_on_struc_iteration:
                            raise EDISyntaxError(
                                f"Mandatory group {tag} of message {self._parent_message._tag} is not found, last "
                                f"parsed segment number is {self._parent_message._curr_segment.number}, tag - "
                                f"{self._parent_message._curr_segment.tag}"
                            )
                    else:
                        self.contents.setdefault(tag, []).append(
                            EdifactSegmentGroup(tag, self, group_content))
                        rep_cnt -= 1
                        parsed_on_file_iteration = True
                        parsed_on_struc_iteration = True
                else:
                    if tag == self._parent_message._curr_segment.tag:
                        self.contents.setdefault(tag, []).append(
                            EdifactSegment(tag, self, self._parent_message._curr_segment, mandatory))
                        rep_cnt -= 1
                        try:
                            self._parent_message._curr_segment = next(self._parent_message._curr_seg_iter)
                        except StopIteration:
                            self._parent_message._out_of_segments = True
                            break
                        parsed_on_struc_iteration = True
                        parsed_on_file_iteration = True
                    elif mandatory:
                        if not parsed_on_struc_iteration:
                            raise EDISyntaxError(
                                f"Mandatory segment {tag} is absent, found while processing segment "
                                f"{self._parent_message._curr_segment.tag} of number "
                                f"{self._parent_message._curr_segment.number}"
                            )
                        else:
                            break
                if self._parent_message._out_of_segments:
                    break

    def file_json(self, file, pretty=False, indent=4, depth=0) -> None:
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        file.write(space + "{" + end_line)
        i = 0
        for tag in self.contents:
            if i != 0:
                file.write("," + end_line)
            try:
                unit_name = unit_names[self._version]["segment_names"][tag]
            except KeyError:
                unit_name = tag
            file.write(inner_space + f'"{unit_name}": [' + end_line)
            j = 0
            for child in self.contents[tag]:
                if j != 0:
                    file.write("," + end_line)
                child.file_json(file, pretty, indent, depth + 2)
                j += 1
            file.write(end_line + inner_space + "]")
            i += 1
        file.write(end_line + space + "}")

    def file_xml(self, file, pretty=False, indent=4, depth=0):
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        file.write(space + f'<{self._tag}>' + end_line)
        for tag in self.contents:
            for child in self.contents[tag]:
                child.file_xml(file, pretty, indent, depth + 1)
                file.write(end_line)
        file.write(space + f'</{self._tag}>')

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def version(self) -> str:
        return self._version

    @property
    def parent(self) -> "EdifactSegmentGroup":
        return self._parent


class EdifactMessage(EdifactSegmentGroup):
    """ Represents the EDIFACT message and consists of segment groups and segments """
    def __init__(self, message: list[Segment], parent: EdifactInterchange):
        # general message data
        self._version = None  # initialized on reading header segment (UNH)
        self._parent = parent
        self._parent_message = self
        self._message = message
        self._parse_validate_header_footer()

        self.contents = []

        # needed for parsing and shouldn't be accessed from outside
        self._curr_seg_iter = iter(self._message[1: -1])
        self._curr_segment = next(self._curr_seg_iter)
        self._out_of_segments = False

        # EdifactSegmentGroup is supposed to accept only its own instances as parent,
        # so actual parent is set after super().__init__ and before in case it will be used somehow
        super().__init__(
            self._tag, self, mesg_struc[self._version][self._tag])
        self._parent = parent

        self._parse()
        self.validate()

    def __repr__(self):
        return f"EdifactMessage['{self._tag}': {repr(self.contents)}"

    def __str__(self):
        return f"EdifactMessage {self._tag}: [{', '.join(map(str, self.contents))}]"

    def export_str(self):
        return "\n".join(self.export_str())

    def _parse_validate_header_footer(self):
        if not len(self._message):
            raise EDISyntaxError(f"Empty message")
        if self._message[0].tag != "UNH":
            raise EDISyntaxError(
                f"Message must start with segment UNH, found {self._message[0].tag}, "
                f"segment number: {self._message[0].number}"
            )
        if self._message[-1].tag != "UNT":
            raise EDISyntaxError(
                f"Message must end with segment UNT, found {self._message[-1].tag}, "
                f"segment number: {self._message[-1].number}"
            )
        self._tag = self._message[0][1][0]  # UNH0201
        self._version = self._message[0][1][1] + self._message[0][1][2]  # UNH0202 + UNH0203

        if self._tag not in mesg_struc[self._version]:
            raise EDISyntaxError(
                f"Wrong EDIFACT message type {self._tag}, "
                f"must be in {list(mesg_struc[self._version].keys())}"
            )
        self._msg_struc = mesg_struc[self._version][self._tag]

        if int(self._message[-1][0]) != len(self._message):
            raise EDISyntaxError(
                f"Expected segment count from UNT: {self._message[-1][0]}, actual count: {len(self._message)}, "
                f"UNH number: {self._message[-1].number}"
            )

    def validate(self):
        if not self._out_of_segments:
            raise EDISyntaxError(
                f"Unparsed segment(s) left in message {self._tag}, segment tag: {self._curr_segment.tag} "
                f"segment number: {self._curr_segment.number}"
            )

        for segment_or_group in self._struc:
            tag = segment_or_group[0]
            mandatory = segment_or_group[1] == "M"
            group_content = segment_or_group[3]
            if mandatory:
                raise EDISyntaxError(
                    f"Mandatory {'group' if group_content else 'segment'} {tag} of message "
                    f"{self._parent_message._tag} is not found, but all segments have already been processed"
                )

    @property
    def type(self) -> str:
        return self._tag

    @property
    def parent(self) -> EdifactInterchange:
        return self._parent


class EdifactSegment:
    """ Represents the EDIFACT segment and consists of composites and elements """
    def __init__(self, tag: str, parent: EdifactSegmentGroup, segment: Segment, mandatory: bool):
        self._tag = tag
        self._parent = parent
        self._version = self._parent.version
        self._number = segment.number
        self._mandatory = mandatory

        self._sgm_struc = segm_struc[self._version][self._tag]
        self.contents = []

        struc_gen = (elem_or_comp for elem_or_comp in self._sgm_struc)
        for value in segment.elements:
            try:
                elem_or_comp_tag, mandatory = next(struc_gen)
                if elem_or_comp_tag[0] == "C":
                    self.contents.append(EdifactComposite(
                        elem_or_comp_tag, self, value if isinstance(value, list) else [value], mandatory == "M"))
                else:
                    self.contents.append(EdifactElement(elem_or_comp_tag, self, value, mandatory == "M"))
            except StopIteration:
                raise EDISyntaxError(
                    f"Segment {self._tag} has too much elements/composites, {len(segment.elements)} overall"
                    f"\nSegment number: {self._number}, segment tag: {self._tag}\n"
                )

        self.validate()

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, key: Union[int, str]) -> \
            Union[list["EdifactComposite"], list["EdifactElement"], "EdifactComposite", "EdifactElement"]:
        """
            Returns contained composite or element. As there might be several of each, returns list of them
            if item is requested by tag and only one instance if it's requested by index.
        """
        if isinstance(key, int):
            return self.contents[key]
        elif isinstance(key, str):
            return [elem_or_comp for elem_or_comp in self.contents if elem_or_comp.tag == key]
        else:
            raise KeyError("Key type must be int or str")

    def __repr__(self):
        return f"EdifactSegment {self._tag}: [{', '.join(map(str, self.contents))}]"

    def validate(self) -> Optional[Literal[True]]:
        return True

    def file_json(self, file, pretty=False, indent=4, depth=0) -> None:
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        file.write(space + "{" + end_line)
        for i in range(len(self.contents)):
            if i != 0:
                file.write("," + end_line)
            self.contents[i].file_json(file, i+1, pretty, indent, depth + 1)
        file.write(end_line + space + "}")

    def file_xml(self, file, pretty=False, indent=4, depth=0):
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        try:
            segm_name = f'{unit_names[self._version]["segment_names"][self._tag]}'
        except KeyError:
            segm_name = self._tag
        file.write(space + f"<{segm_name}>" + end_line)
        for i in range(len(self.contents)):
            self.contents[i].file_xml(file, i+1, pretty, indent, depth + 1)
            file.write(end_line)
        file.write(space + f"</{segm_name}>")

    @property
    def tag(self):
        return self._tag

    @property
    def version(self):
        return self._version

    @property
    def number(self) -> str:
        return self._number

    @property
    def parent(self) -> EdifactSegmentGroup:
        return self._parent


class EdifactComposite:
    """ Represents the EDIFACT composites and consists of elements """
    def __init__(self, tag: str, parent: EdifactSegment, contents: list[str], mandatory: bool):
        self._tag = tag
        self._parent = parent
        self._version = self._parent.version
        self._mandatory = mandatory
        self._comp_struc = comp_struc[self._version][tag]

        self.contents = [
            EdifactElement(elem_tag, self, value, mandatory == "M")
            for (elem_tag, mandatory), value in zip(self._comp_struc, contents)]

        self.validate()

    def __repr__(self):
        return f"EdifactComposite[{', '.join(map(str, self.contents))}]"

    def __str__(self):
        return f"[{', '.join(map(str, self.contents))}]"

    def __len__(self):
        return len(self.contents)

    def __getitem__(self, key: Union[int, str]) -> \
            Union["EdifactElement", list["EdifactElement"]]:
        """
            Returns contained element. As there might be several of them, returns list of them
            if item is requested by tag and only one instance if it's requested by index.
        """
        if isinstance(key, int):
            return self.contents[key]
        elif isinstance(key, str):
            return [element for element in self.contents if element.tag == key]
        else:
            raise KeyError("Key type must be int or str")

    def validate(self) -> Optional[Literal[True]]:
        try:
            if self._mandatory and not self.contents:
                raise EDISyntaxError(f"Composite {self._tag} is mandatory, but empty")
            if len(self.contents) > len(self._comp_struc):
                raise EDISyntaxError(
                    f"Composite {self._tag} has {len(self.contents)} elements, "
                    f"max allowed count is {len(self._comp_struc)}")
        except EDISyntaxError as e:
            raise EDISyntaxError(str(e) + f"\nSegment number: {self._parent.number}, segment tag: {self._parent.tag}")

        return True

    def isempty(self) -> bool:
        return bool(self.contents)

    def file_json(self, file, number, pretty=False, indent=4, depth=0) -> None:
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        file.write(space + f'"{unit_names[self._version]["composite_names"][self._tag]}_{number}"' + ": {" + end_line)
        for i in range(len(self.contents)):
            if i != 0:
                file.write("," + end_line)
            self.contents[i].file_json(file, i+1, pretty, indent, depth + 1)
        file.write(end_line + space + "}")

    def file_xml(self, file, number, pretty=False, indent=4, depth=0):
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        comp_name = f'{unit_names[self._version]["composite_names"][self._tag]}_{number}'
        file.write(space + f"<{comp_name}>" + end_line)
        for i in range(len(self.contents)):
            self.contents[i].file_xml(file, i+1, pretty, indent, depth + 1)
            file.write(end_line)
        file.write(space + f"</{comp_name}>")

    @property
    def tag(self) -> str:
        return self._tag

    @property
    def parent(self) -> EdifactSegment:
        return self._parent

    @property
    def mandatory(self) -> bool:
        return self._mandatory

    @property
    def version(self) -> str:
        return self._version


class EdifactElement:
    """
        Class represents a single element of EDIFACT standard that belongs to the composite or directly to the segment.
        Essentially, it is just a string with some restrictions to its contents that are defined by the version and
        a position in the segment.
    """
    def __init__(self, tag: str, parent: Union[EdifactComposite, EdifactSegment], value: str, mandatory: bool) -> None:
        self._tag = tag
        self._parent = parent
        self._parent_segment = parent if isinstance(parent, EdifactSegment) else parent.parent
        self._version = self._parent.version
        self._value = value
        self._mandatory = mandatory

        restriction = elem_restr[self._version][tag]
        self._char_type = None
        if restriction[0] == "a":
            self._char_type = CharType.ALPHA
        elif restriction[0] == "an":
            self._char_type = CharType.ALPHANUMERIC
        elif restriction[0] == "n":
            self._char_type = CharType.NUMERIC
        self._min_len = restriction[1]
        self._max_len = restriction[2]

        self.validate()

    def __repr__(self):
        return f"EdifactElement['{self._tag}': '{self._value}']"

    def __str__(self):
        return f"'{self._value}'"

    def is_alphabetic(self):
        """ To check that element is meant alphabetic by EDIFACT standard """
        return all((char in alphabetic_char_set for char in self._value))

    def is_numeric(self):
        """ To check that element is meant numeric by EDIFACT standard """
        return all((char in numeric_char_set for char in self._value))

    def is_alphanumeric(self):
        """ To check that element is meant numeric by EDIFACT standard """
        return all((char in alphanumeric_char_set for char in self._value))

    def validate(self) -> Optional[Literal[True]]:
        try:
            if self._mandatory and isinstance(self._parent, EdifactComposite) and self._parent.mandatory \
                    and not self._value:
                raise EDISyntaxError(
                    f"Absent mandatory element {self._tag} for " +
                    ("composite" if isinstance(self._parent, EdifactComposite) else "segment") + " " + self._parent.tag
                )
            if self._char_type is None:
                raise EDISyntaxError(
                    f'Something went wrong in element {self._tag}, char type is not "a", "n", nor "an"')
            if not self.is_alphanumeric():
                raise EDISyntaxError(
                    f"Element {self._tag} is not alphanumeric, its constraint: {CharType(self._char_type)}")
            if self._char_type == CharType.ALPHA and not self.is_alphabetic():
                raise EDISyntaxError(f"Alphabetic constraint is not satisfied for element {self._tag}")
            if self._char_type == CharType.NUMERIC and not self.is_numeric():
                raise EDISyntaxError(f"Numeric constraint is not satisfied for element {self._tag}")

            if 0 < len(self._value) < self._min_len or len(self._value) > self._max_len:
                raise EDISyntaxError(
                    f"Length range of element {self._tag} is {self._min_len}..{self._max_len}, "
                    f"its actual length is {len(self._value)}"
                )
        except EDISyntaxError as e:
            raise EDISyntaxError(
                str(e) + f"\nSegment number: {self._parent_segment.number}, segment tag: {self._parent_segment.tag}")

        return True

    def file_json(self, file, number, pretty=False, indent=4, depth=0):
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        file.write(space + f'"{unit_names[self._version]["element_names"][self._tag]}_{number}": "{self._value}"')

    def file_xml(self, file, number, pretty=False, indent=4, depth=0):
        space, inner_space, end_line = pretty_spaces(pretty, indent, depth)
        elem_name = f'{unit_names[self._version]["element_names"][self._tag]}_{number}'
        if self._value:
            file.write(space + f'<{elem_name}>{self._value}</{elem_name}>')
        else:
            file.write(space + f'<{elem_name}/>')

    @property
    def parent(self) -> Union[EdifactComposite, EdifactSegment]:
        return self._parent

    @property
    def version(self) -> str:
        return self._version

    @property
    def value(self) -> str:
        return self._value

    @property
    def mandatory(self) -> bool:
        return self._mandatory

    @property
    def min_len(self) -> str:
        return self._min_len

    @property
    def max_len(self) -> str:
        return self._max_len
