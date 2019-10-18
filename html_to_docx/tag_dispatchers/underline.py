from docx.enum.text import WD_UNDERLINE

from . import (CharacterTailMixin, ParentTagMixin, TagDispatcher,
               replace_whitespaces)


class UnderlineDispatcher(
    ParentTagMixin,
    CharacterTailMixin,
    TagDispatcher
):
    @classmethod
    def append_head(cls, element, container):
        return cls._append_underline(element.text, element, container)

    @classmethod
    def _append_underline(cls, text, element, container):
        """
        <u> Creates a bold text run inside the paragraph container.
        Appends remainder of text as an additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.underline = WD_UNDERLINE.SINGLE
        cls._apply_parent_formatting(element, run)
        return container
