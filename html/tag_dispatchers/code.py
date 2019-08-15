# encoding: utf-8
from . import TagDispatcher


class CodeDispatcher(TagDispatcher):
    @classmethod
    def append_head(cls, element, container):
        return cls._append_code(element.text, container)

    @classmethod
    def append_tail(cls, element, container):
        return cls._append_code(element.tail, container)

    @classmethod
    def _append_code(cls, text, container):
        """
        <code> Creates a specially styled run inside the given container.
        """
        paragraph = cls.get_new_paragraph(container)
        paragraph.text = text

        return paragraph
