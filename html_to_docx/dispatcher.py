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
from .tag_dispatchers.link import LinkDispatcher, LinkAsTextDispatcher
from .tag_dispatchers.list_item import ListItemDispatcher
from .tag_dispatchers.paragraph import ParagraphDispatcher
from .tag_dispatchers.span import SpanDispatcher
from .tag_dispatchers.strong import StrongDispatcher


def get_tag_dispatcher(html_tag, plain_links=False):
    """
    Returning the object creating OOXML for the given HTML tag
    """
    if plain_links:
        _dispatch_html['a'] = LinkAsTextDispatcher
    else:
        _dispatch_html['a'] = LinkDispatcher

    return _dispatch_html.get(html_tag)


# map of HTML tags and their corresponding objects
heading_dispatcher = HeadingDispatcher()

_dispatch_html = dict(
    p=ParagraphDispatcher(),
    a=LinkDispatcher(),
    li=ListItemDispatcher(),
    br=LineBreakDispatcher(),
    code=CodeDispatcher(),
    b=StrongDispatcher(),
    strong=StrongDispatcher(),
    em=EmphasisDispatcher(),
    i=EmphasisDispatcher(),
    span=SpanDispatcher(),
    h1=heading_dispatcher,
    h2=heading_dispatcher,
    h3=heading_dispatcher,
    h4=heading_dispatcher,
    h5=heading_dispatcher,
    h6=heading_dispatcher,
    blockquote=BlockquoteDispatcher(),
    img=ImgDispatcher()
)
