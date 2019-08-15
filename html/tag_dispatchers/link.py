from . import TagDispatcher
import docx


def add_hyperlink(paragraph, url, text, color='0000FF', underline=True):
    """A function that places a hyperlink within a paragraph object.

    Source: https://github.com/python-openxml/python-docx/issues/74#issuecomment-261169410  # noqa

    Args:
        paragraph (docx.Paragraph): The paragraph we are adding the hyperlink to.
        url (str): A string containing the required url.
        text (str): The text displayed for the url.
        color (str): Text color. If not passed, default value used.
        underline (bool): Underline link or not.

    Returns:
        paragraph (docx.Paragraph): Paragraph object with added link.

    """
    # This gets access to the document.xml.rels file
    # and gets a new relation id value
    part = paragraph.part
    r_id = part.relate_to(url, docx.opc.constants.RELATIONSHIP_TYPE.HYPERLINK,
                          is_external=True)

    # Create the w:hyperlink tag and add needed values
    hyperlink = docx.oxml.shared.OxmlElement('w:hyperlink')
    hyperlink.set(docx.oxml.shared.qn('r:id'), r_id, )

    # Create a w:r element
    new_run = docx.oxml.shared.OxmlElement('w:r')

    # Create a new w:rPr element
    rPr = docx.oxml.shared.OxmlElement('w:rPr')

    c = docx.oxml.shared.OxmlElement('w:color')
    c.set(docx.oxml.shared.qn('w:val'), color)
    rPr.append(c)

    # Remove underlining if it is requested
    if not underline:
        u = docx.oxml.shared.OxmlElement('w:u')
        u.set(docx.oxml.shared.qn('w:val'), 'none')
        rPr.append(u)

    # Join all the xml elements together
    # and add the required text to the w:r element
    new_run.append(rPr)
    new_run.text = text
    hyperlink.append(new_run)

    paragraph._p.append(hyperlink)

    return hyperlink


class LinkDispatcher(TagDispatcher):
    @classmethod
    def append_head(cls, element, container):
        test = cls._append_link(element, container)
        return test

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_link(element.tail, container)

    @classmethod
    def _append_link(cls, element, container):
        """
        <a> creates a link element inside a docx container element.
        """
        text = element.text
        href = element.attrib["href"]
        if text is None or text == '':
            text = href

        add_hyperlink(container, href, text)
        return container
