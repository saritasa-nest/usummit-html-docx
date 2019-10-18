from . import (CharacterTailMixin, ParentTagMixin, TagDispatcher,
               replace_whitespaces)


class StrongDispatcher(
    ParentTagMixin,
    CharacterTailMixin,
    TagDispatcher,
):
    @classmethod
    def append_head(cls, element, container):
        return cls._append_strong(element.text, element, container)

    @classmethod
    def _append_strong(cls, text, element, container):
        """
        <strong> Creates a bold text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.bold = True
        cls._apply_parent_formatting(element, run)
        return container
