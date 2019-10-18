from . import ParagraphTailMixin, TagDispatcher, replace_whitespaces

_list_style = dict(
    ol='ListNumber',
    ul='ListBullet',
)


class ListItemDispatcher(ParagraphTailMixin, TagDispatcher):
    @classmethod
    def append_head(cls, element, container):
        paragraph = cls.get_new_paragraph(container)
        return cls._append_list_item(element, element.text, paragraph)

    @classmethod
    def _append_list_item(cls, element, text, container):
        """
        <li> Create a list item element inside a docx container.
        Style it according to its parents list type.
        """
        text = replace_whitespaces(text)
        text = '' if text == ' ' else text

        style = _list_style.get(element.getparent().tag, 'ListBullet')
        container.style = style
        container.add_run(text)

        return container
