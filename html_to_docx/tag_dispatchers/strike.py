from . import (CharacterTailMixin, ParentTagMixin, TagDispatcher,
               replace_whitespaces)


class StrikeDispatcher(
    ParentTagMixin,
    CharacterTailMixin,
    TagDispatcher,
):
    @classmethod
    def append_head(cls, element, container):
        return cls._append_strike(element.text, element, container)

    @classmethod
    def _append_strike(cls, text, element, container):
        """
        <strike> Creates a `strike` text run inside the paragraph container.
        Appends remainder of text as a additional run
        """
        text = replace_whitespaces(text)
        run = container.add_run(text=text)
        run.font.strike = True
        cls._apply_parent_formatting(element, run)
        return container
