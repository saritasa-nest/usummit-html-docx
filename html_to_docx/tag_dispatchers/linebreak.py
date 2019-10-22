from . import ParagraphTailMixin, TagDispatcher


class LineBreakDispatcher(ParagraphTailMixin, TagDispatcher):
    @classmethod
    def append_head(cls, element, container):
        paragraph = cls.get_new_paragraph(container)
        return paragraph
