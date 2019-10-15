"""
Wrapper methods used for mapping HTML to docx objects
"""

from docx import Document
from lxml.html import fromstring

from .converter import DocxBuilder
from .utils import tails_to_paragraphs


def add_html(container, html_string, plain_links=False):
    """Adds HTML-formatted content to a document.

    Args:
        container (Document): docx container to add HTML to.
        html_string (str): HTML string to add.
        plain_links (bool): Parse HTML hyperlinks as docx hyperlinks or as
            plain text. Enable if you have any problems with received DOCX
            hyperlinks.

    Returns:
        container (Document): docx container with added HTML content.

    """
    root = fromstring(html_string)
    root = tails_to_paragraphs(root)
    builder = DocxBuilder(container=container)
    builder.from_html_tree(root=root, plain_links=plain_links)
    return container


def create_document_from_html(html_string, plain_links=False):
    """Creates new document from HTML.

    Args:
        html_string (str): HTML string to add.
        plain_links (bool): Parse HTML hyperlinks as docx hyperlinks or as
            plain text. Enable if you have any problems with received DOCX
            hyperlinks.

    Returns:
        container (Document): docx container with added HTML content.

    """
    document = Document()
    return add_html(document, html_string, plain_links=plain_links)
