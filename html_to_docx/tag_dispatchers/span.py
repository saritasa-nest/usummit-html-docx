from docx.enum.style import WD_STYLE_TYPE
from docx.shared import Pt

from ..utils import get_document, get_or_add_style, parse_style
from . import TagDispatcher, replace_whitespaces


class SpanDispatcher(TagDispatcher):

    @classmethod
    def append_head(cls, element, container):
        return cls._append_span(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_span(element.tail, element, container)

    @classmethod
    def _append_span(cls, text, element, container):
        """
        <span> Creates simple text run inside the paragraph container.
        Appends remainder of text as a additional run.

        Implements custom font size defined in a span.

        """
        text = replace_whitespaces(text)
        html_style = parse_style(element)

        if html_style.get('font_size'):
            doc = get_document(container)

            style_name = f'Span {str(html_style["font_size"])}'
            span_style, is_new = get_or_add_style(doc, style_name, WD_STYLE_TYPE.CHARACTER)

            # Set font size for new style
            if is_new:
                span_style.font.size = Pt(html_style['font_size'])

            container.add_run(text=text, style=span_style)
        else:
            container.add_run(text=text)

        return container
