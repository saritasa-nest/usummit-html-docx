"""
Wrapper methods used for mapping HTML to docx objects
"""

from docx import Document
from lxml.html import fromstring

from .converter import DocxBuilder


def add_html(container, html_string):
    """Adds HTML-formatted content to a document.

    Args:
        container (Document): docx container to add HTML to.
        html_string (str): HTML string to add.

    Returns:
        container (Document): docx container with added HTML content.

    """
    root = fromstring(html_string)
    builder = DocxBuilder(container=container)
    builder.from_html_tree(root=root)
    return container


def create_document_from_html(html_string):
    """Creates new document from HTML.

    Args:
        html_string (str): HTML string to add.

    Returns:
        container (Document): docx container with added HTML content.

    """
    document = Document()
    return add_html(document, html_string)
