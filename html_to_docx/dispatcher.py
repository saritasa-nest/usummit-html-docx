"""
Returns corresponding objects to call for creating
the different docx elements.
"""

from .tag_dispatchers.blockquote import BlockquoteDispatcher
from .tag_dispatchers.code import CodeDispatcher
from .tag_dispatchers.emphasis import EmphasisDispatcher
from .tag_dispatchers.heading import HeadingDispatcher
from .tag_dispatchers.img import ImgDispatcher
from .tag_dispatchers.linebreak import LineBreakDispatcher
from .tag_dispatchers.link import LinkAsTextDispatcher, LinkDispatcher
from .tag_dispatchers.list_item import ListItemDispatcher
from .tag_dispatchers.paragraph import (
    ParagraphDispatcher,
    UnsupportedTagDispatcher,
)
from .tag_dispatchers.span import SpanDispatcher
from .tag_dispatchers.strike import StrikeDispatcher
from .tag_dispatchers.strong import StrongDispatcher
from .tag_dispatchers.underline import UnderlineDispatcher


def get_tag_dispatcher(html_tag, plain_links=False):
    """
    Returning the object creating OOXML for the given HTML tag
    """
    if plain_links:
        _dispatch_html['a'] = LinkAsTextDispatcher
    else:
        _dispatch_html['a'] = LinkDispatcher

    return _dispatch_html.get(html_tag, unsupported_tag_dispatcher)


# map of HTML tags and their corresponding objects
heading_dispatcher = HeadingDispatcher()

unsupported_tag_dispatcher = UnsupportedTagDispatcher()

_dispatch_html = dict(
    p=ParagraphDispatcher(),
    h1=heading_dispatcher,
    h2=heading_dispatcher,
    h3=heading_dispatcher,
    h4=heading_dispatcher,
    h5=heading_dispatcher,
    h6=heading_dispatcher,
    li=ListItemDispatcher(),
    code=CodeDispatcher(),
    blockquote=BlockquoteDispatcher(),
    img=ImgDispatcher(),
    br=LineBreakDispatcher(),
    a=LinkDispatcher(),
    b=StrongDispatcher(),
    strong=StrongDispatcher(),
    em=EmphasisDispatcher(),
    i=EmphasisDispatcher(),
    span=SpanDispatcher(),
    u=UnderlineDispatcher(),
    # Both `<strike>` and `<s>` tags will be converted
    # into striketrough text
    strike=StrikeDispatcher(),
    s=StrikeDispatcher(),
    # Convert <div>, <ul> and <ol> into line breaks.
    # This is done because these tags cannot be converted directly into any
    # element of docx, and paragraph allows saving unwrapped content inside
    # these tags.
    div=ParagraphDispatcher(),
    ul=ParagraphDispatcher(),
    ol=ParagraphDispatcher(),
)
