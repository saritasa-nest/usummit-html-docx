from docx import Document

from html_to_docx import add_html, create_document_from_html

example_html = """
<h1>Header level 1</h1>
Unwrapped text
<h2>Header level 2</h2>
<p><u>u <em>u+em <strong>u+em+strong </em>u+strong </strong>u</u></p>
<p><u>u <em>u+em <strike>u+em+strike </em>u+strike </strike>u</u></p>
<p><u>u <span style="font-size: 24px;">u+span </span></u></p>
<p><span style="font-size: 24px;">CHAIR: Jorge Cortes</span></p>
<p><span style="font-size: 44px;">CHAIR: Jorge Cortes</span>
<br>PRESENTER: Lars Bullinger (Charité University Berlin, Germany)
<a href="https://github.com/">github link</a></p>
<p><i><b>attendance</b></i><em>(Low attendance)<strong>traffic</strong></em></p>
<p>Full room, <strong>300 attendees</strong> <em>approximately.&nbsp;</em></p>
<blockquote><p>Block quoted paragraph</p></blockquote>
<br>PRESENTER: Lars Bullinger
<p>before link <a href="https://github.com/">github link</a> link tail</p>
<ul><li>one</li><li>two</li></ul>
<ol><li>one</li><li>two</li></ol>
"""

document = Document()
document = add_html(document, example_html)
document.save('added.docx')

new_document = create_document_from_html(example_html)
new_document.save('new.docx')

new_document = create_document_from_html(example_html, plain_links=True)
new_document.save('new_plain_links.docx')
