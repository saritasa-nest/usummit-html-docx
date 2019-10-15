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
