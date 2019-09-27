"""
Converter recursively iterating over HTML ElementTree(etree)
mapping HTML tags to their corresponding python-docx functions.
Appending full HTML structure to the given document.
"""
from docx.text.paragraph import Paragraph

from .dispatcher import get_tag_dispatcher


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
        # only call when a function is attached to tag
        new_container = container
        if dispatcher:
            new_container = dispatcher.append_head(html_element, container)

        children = list(html_element)

        # paragraph flow seems bugged, maybe this check container will fix it]
        check_container = None

        for child in children:
            if isinstance(check_container, Paragraph):
                new_container = check_container
            check_container = self._append_docx_elements(child, new_container, plain_links)

        dispatcher = get_tag_dispatcher(html_element.getparent().tag, plain_links)
        if html_element.tail and dispatcher:
            dispatcher.append_tail(html_element, container)
        return new_container
