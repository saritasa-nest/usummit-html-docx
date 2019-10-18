"""
Converter recursively iterating over HTML ElementTree(etree)
mapping HTML tags to their corresponding python-docx functions.
Appending full HTML structure to the given document.
"""
from .dispatcher import get_tag_dispatcher
from .utils import html_element_is_paragraph


class DocxBuilder(object):
    """Appends HTML parsed as a string to a `Document` container."""
    def __init__(self, container):
        """Takes the root container the html should be appended to.

        Args:
            container (Document): Container for appending HTML content.

        """
        self._root_container = container

    def from_html_tree(self, root, plain_links=False):
        """Appending all the HTML elements, beginning at root object.

        Args:
            root (str): String with parsed HTML.

        """
        self._append_docx_elements(root, self._root_container, plain_links)

    def _append_docx_elements(self, html_element, container, plain_links):
        """Append elements parsed from HTML to the docx container.

        Retrieving and calling a creating object for the given HTML tag.
        Recursive call for all children of the element.

        Args:
            html_element (str): String with parsed HTML.
            container (Document): Container for appending HTML content.

        """
        dispatcher = get_tag_dispatcher(html_element.tag, plain_links)
        if dispatcher:
            container = dispatcher.append_head(html_element, container)

        children = list(html_element)
        for child in children:
            container = self._append_docx_elements(child, container, plain_links)

        tail = '' if not html_element.tail else html_element.tail.strip()
        if not tail:
            return container

        parent = html_element.getparent()
        if parent and not html_element_is_paragraph(parent):
            dispatcher = get_tag_dispatcher(parent.tag, plain_links)
            if not dispatcher:
                return container

            container = dispatcher.append_tail(html_element, container)
            return container

        container = dispatcher.append_tail(html_element, container)
        return container
