import re

from docx.document import Document
from lxml import etree


def tails_to_paragraphs(element):
    """Wraps tails of HTML elements with `<p>` HTML tag.

    When converting HTML content into DOCX, unwrapped content is skipped, so
    it's required to wrap them in some HTML tag.
    Tag `<p>` selected because unwrapped text is expected to be displayed as a
    paragraph.

    Args:
        element (lxml.html.HtmlElement): HTML element to process.

    Returns:
        element (lxml.html.HtmlElement): HTML element with wrapped tails.

    """

    for el in element:
        if el.tail and el.tail.strip():
            p = etree.Element('p')
            p.text = el.tail.strip()
            el.tail = None
            el.addnext(p)

    return element


def parse_style(element):
    """Parse `style` attribute of HTML element.

    Args:
        element (HtmlElement): HTML element which style need to be parsed.

    Returns:
        style (dict): Parsed style parameters.

    """
    style_string = element.attrib.get('style', '')

    style = dict()
    style.update(parse_font_size(style_string))

    return style


def parse_font_size(style_string):
    """Parse `font-size` from HTML.style attribute.

    Args:
        style_string (str): Value of `style` attribute of HTML element.

    Returns:
        style (dict): Font size defined in HTML element.

    """
    font_size_re = re.compile(r'font\-size:\s*(?P<font_size>\d*)px')
    match = font_size_re.match(style_string)

    if not match:
        return dict()

    style = match.groupdict()
    style['font_size'] = int(style['font_size'])
    return style


def get_document(container):
    """Get `Document` instance of any docx container."""
    if isinstance(container, Document):
        return container

    return get_document(container._parent)


def get_or_add_style(document, style_name, style_type):
    """Get existent or create new style for a document.

    Args:
        document (Document): DOCX document.
        style_name (str): Name of DOCX style.
        style_type (int): Type of DOCX style. Taken from
            `docx.enum.style.WD_STYLE_TYPE`.

    Returns:
        (_CharacterStyle or _ParagraphStyle): New or existent style.

    """
    # `get_by_id` returns default style if a style with defined name not found
    existent_style = document.styles.get_by_id(style_name, style_type)

    if style_name == existent_style.name:
        return existent_style, False

    return document.styles.add_style(style_name, style_type), True
