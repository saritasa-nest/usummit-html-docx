from . import (CharacterTailMixin, ParentTagMixin, TagDispatcher,
               replace_whitespaces)


class EmphasisDispatcher(
    ParentTagMixin,
    CharacterTailMixin,
    TagDispatcher
):
    @classmethod
    def append_head(cls, element, container):
        return cls._append_emphasis(element.text, element, container)

    @classmethod
    def _append_emphasis(cls, text, element, container):
        """
        <em> Creates an italic text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.italic = True
        cls._apply_parent_formatting(element, run)
        return container
