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

        Does not implement custom formatting from <span> tag
        """
        text = replace_whitespaces(text)
        container.add_run(text=text)
        return container
