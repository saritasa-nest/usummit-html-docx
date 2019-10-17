from docx.enum.text import WD_UNDERLINE

from . import ParentTagMixin, TagDispatcher, replace_whitespaces


class UnderlineDispatcher(ParentTagMixin, TagDispatcher):
    @classmethod
    def append_head(cls, element, container):
        return cls._append_underline(element.text, element, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_underline(element.tail, element, container)

    @classmethod
    def _append_underline(cls, text, element, container):
        """
        <u> Creates a bold text run inside the paragraph container.
        Appends remainder of text as an additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.underline = WD_UNDERLINE.SINGLE
        run = cls._apply_parent_formatting(element, run)
        return container
