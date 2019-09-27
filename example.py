from docx import Document

from html_to_docx import add_html, create_document_from_html

example_html = """
<h1>Header level 1</h1>
<h2>Header level 2</h2>
<p fr-original-style='\"\"'><strong fr-original-style='\"\"'>Presenting author
</strong></p><p fr-original-style='\"\"'>
<span style="font-size: 24px;">CHAIR: Jorge Cortes</span>
<br>PRESENTERS: Lars Bullinger (Charité University Berlin, Germany), 
Adriano Venditti (University ofRome Tor Vergata, Italy), Niel Russell 
(University of Nottingham, UK), Pau Montesinos (Hospital Universitari i 
Politècnic La Fe, Spain). &nbsp; 
<a href="https://github.com/">github link</a>
</p>
<p fr-original-style='\"\"'><i><b fr-original-style='\"\"'>
Please note the estimated audience attendance&nbsp;</b></i>
<em fr-original-style='\"\"'>(Low attendance, half-full, full, 
overflowing)<strong fr-original-style='\"\"'>/traffic at the poster&nbsp;
</strong></em></p><p fr-original-style='\"\"'>Full room, 
<strong>300 attendees</strong> 
<em>approximately.&nbsp;</em></p>
"""

document = Document()
document = add_html(document, example_html)
document.save('added.docx')

new_document = create_document_from_html(example_html)
new_document.save('new.docx')

new_document = create_document_from_html(example_html, plain_links=True)
new_document.save('new_plain_links.docx')
