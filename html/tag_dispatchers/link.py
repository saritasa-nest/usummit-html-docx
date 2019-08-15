# encoding: utf-8
from html_docx.html.tag_dispatchers import TagDispatcher
import docxext

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
        if text is None or  text =='':
            text = href
        docxext.insert_hyperlink(container, text, href)
        return container
