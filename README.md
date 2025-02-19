# pydifact

A Python library to parse and serialize UN/EDIFACT interchanges.

## Preamble

This is a port of [metroplex-systems/edifact](https://github.com/metroplex-systems/edifact) to Python. Thanks here at the start to [Craig Duncan](https://github.com/duncan3dc) for this cool piece of software. Porting was like a breeze due to the high code quality there. All credits for the initial code here go to him, I just did the translation to Python(3), some "pythonifications" of the code and little improvements.

### Why another EDIFACT library?

Because I did not find a decent UN/EDIFACT library for Python, so I decided to port one of the available good PHP libraries to Python. Here is the result.

ATM this is a Work In Progress, the API is not stable yet.
Feel free to help.

## Install

As usual, use a virtualenv, and install via pip or pipenv:

```bash
pip install pydifact
```

However, it is not stable yet, so the pypi version, including documentation and code examples, could differ from the latest git code. If in doubt, use the git version:
```bash
git clone https://github.com/nerdocs/pydifact.git
cd pydifact
pip install -e .
```


## Usage

To read a full Interchange from a file or string, take the `Interchange` class and
iter over the messages and segments:

```python
from pydifact.segmentcollection import Interchange
interchange = Interchange.from_file("./tests/data/order.edi")
interchange = Interchange.from_str(
  "UNA:+,? 'UNB+UNOC:1+1234+3333+200102:2212+42'UNH+42z42+PAORES:93:1:IA'UNT+2+42z42'UNZ+2+42'"
)
for message in interchange.get_messages():
    for segment in message.segments:
        print('Segment tag: {}, content: {}'.format(
            segment.tag, segment.elements))
```

You may also want to iterate directly on segments :

```python
from pydifact.segmentcollection import Interchange
interchange = Interchange.from_file("./tests/data/order.edi")
interchange = Interchange.from_str("UNA:+,? 'UNH+1+ORDERS:D:96A:UN:EAN008'")

for segment in interchange.segments:
    print('Segment tag: {}, content: {}'.format(
        segment.tag, segment.elements))
```

Or you can create an EDI interchange on the fly:

```python
from pydifact.segmentcollection import Interchange
from pydifact.segments import Segment
interchange = Interchange()
interchange.add_segment(Segment('QTY', ['12', '3']))
print(interchange.serialize())
```

You may also want to parse a « raw » segment bunch which is not an interchange :

```
from pydifact.segmentcollection import RawSegmentCollection
collection = RawSegmentCollection.from_str("UNH+1+ORDERS:D:96A:UN:EAN008'")

for segment in collection.segments:
    print('Segment tag: {}, content: {}'.format(
        segment.tag, segment.elements))

```


## Extension
Added extension for further parsing EDIFACT file into object. Has support of Segment Groups. Included parsing
and validating of Interchanges by EDIFACT message structure standards per versions. Also Composites consisting
of single Element are parsed as composites.

Usage:
```python
# demo is for file pydifact/tests/data/invoice2.edi

from pydifact.edifact_extension.edifact_directory \
    import EdifactInterchange, EdifactMessage, EdifactSegmentGroup, EdifactSegment, EdifactComposite, EdifactElement

interchange = EdifactInterchange.from_file("pydifact/tests/data/invoice2.edi")

for message in interchange.messages:  # message is an instance of EdifactMessage
    segment_group25_lst = message["SG25"]  # list of all segment groups with tag SG25 in current message
    for sg25 in segment_group25_lst:
        segment_lin_lst = sg25["LIN"]  # list of all segments with tag LIN in current segment group
        # both SG25 in demo file consist of segments: LIN, PIA, QTY, and segment groups SG28, SG38 afterwards
        segment_pia = sg25[1]

        element4347_lst = segment_pia["4347"]  # list of all elements with tag 4347
        compositeC212_lst = segment_pia["C212"]  # list of all composites with tag C212

        element0 = segment_pia[0]  # PIA in demo file consists of element on pos 0
        composite1 = segment_pia[1]  # and composite on pos 1, they are accessible by integer index

        element_value = element0.value
```

Using extension should be more convenient if you want to validate the document or if you are not sure about
which segments/composites/elements will be present - that way you can rely on data units' tags and positions
in the document by EDIFACT documentation, as they may shift using simple Interchange class.

## Limitations

- No support of optional functional groups (`UNG`→`UNE`),

## Alternatives

In python ecosystem:

- [python-edifact](https://github.com/FriedrichK/python-edifact) - simpler, IMHO less clean code, less flexible. may be faster though (not tested). Seems unmaintained.
- [bots](https://github.com/bots-edi/bots) - huge, with webinterface (bots-monitor), webserver, bots-engine.
- [edicat](https://github.com/notpeter/edicat) - simple, only for separating lines/segments for CLI-piping.


## Development

To develop pydifact, install the dev requirements with `pipenv install --dev`. This installs all the python packages needed for development and testing.

Format all python files using [black](https://black.readthedocs.io).

Happy coding, PR are more than welcome to make this library better, or to add a feature that matches your needs. Nevertheless, don't forget adding tests for every aspect you add in code.

### Testing

pydifact uses [pytest](http://pytest.org) for testing.
Just exec `pytest` within the project folder to execute the unit tests.

There is one test to check the performance of parsing huge files, named `test_huge_message` - you can skip that test by calling

```bash
pytest --ignore tests/test_huge_message.py
```
This is recommended for fast testing.


## License

This library is licensed under the
*MIT* license, see the
[LICENSE file](LICENSE).
