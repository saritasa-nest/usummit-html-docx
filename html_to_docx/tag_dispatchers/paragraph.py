from docx.shared import RGBColor
from lxml.etree import tostring
from . import ParagraphTailMixin, TagDispatcher, replace_whitespaces


class ParagraphDispatcher(ParagraphTailMixin, TagDispatcher):
    @classmethod
    def append_head(cls, element, container):
        paragraph = cls.get_new_paragraph(container)
        return cls._append_paragraph(element.text, element, paragraph)

    @classmethod
    def _append_paragraph(cls, text, element, container):
        """
        <p> creates a paragraph element inside a docx container element.
        """
        text = replace_whitespaces(text)
        if not text:
            return container

        style = None
        if element.getparent().tag == 'blockquote':
            style = 'Intense Quote Char'

        container.style = 'Normal'
        container.add_run(text=text, style=style)
        return container


class UnsupportedTagDispatcher(ParagraphDispatcher):
    """Dispatch unsupported tags.

    Dispatch as a paragraph with raw HTML and red font color.

    """
    @classmethod
    def _append_paragraph(cls, text, element, container):
        """Append content as raw HTML with red font color."""
        text = str(tostring(element), 'utf-8')
        text = replace_whitespaces(text)

        container.style = 'Normal'
        run = container.add_run(text=text)
        font = run.font
        font.color.rgb = RGBColor(0xff, 0x00, 0x00)

        return container
