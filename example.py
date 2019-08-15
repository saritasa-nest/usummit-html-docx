from html import add_html

from docx import Document

example_html = """
<h1 fr-original-style=\'\\"\\"\'>header 1</h1><h2>header 2</h2><h3>header 3
</h3><h4>header 4</h4><span style="font-size: 18px;">Some text</span><p
 fr-original-style=\'\\"\\"\'>When covering a <em>session, plea<strong>se follow
 these 4 steps. </strong>Be brief and concis</em>e with answers:</p><p 
 fr-original-style=\'\\"\\"\'>1. Select priority (high, mediu<em>m or low) in 
 th<strong>e ‘select tags’ drop down menu located above</strong></em></p><p 
 fr-original-style=\'\\"\\"\'><strong><em>2. What are the 2-3 key takeaways 
 (please keep it brief by using bullet points, not long paragraphs)?</em>
 </strong></p><ul style="list-style-type: disc;"><li><p 
 fr-original-style=\'\\"\\"\'><strong><em>Nucleic acid</em> aptamer with high 
 solubility and small molecular weight (~15 kDa)</strong></p></li><li><p 
 fr-original-style=\'\\"\\"\'><strong>Previous anti-VEGF a</strong>ptamer 
 (Macugen) fails to recognize all VEGF-A isoforms and contained natural RNA 
 bases which limit its in vivo stability, which AMS0421 has addressed</p></li>
 <li><p fr-original-style=\'\\"\\"\'>Tested in rat laser-induced CNV model and 
 demonstrated potent efficacy comparable to Combercept, with a formulated 
 concentration of 200mg/mL, ~50 fold higher molar dose than current anti-VEGF 
 drugs <a href="https://github.com/fr0mhell/html_docx">Here you can find all 
 the details</a></p></li></ul><p fr-original-style=\'\\"\\"\'>3. What is the 
 near or long term impact to Novartis?</p><p fr-original-style=\'\\"\\"\'>- 
 A long way out, but could be something seen on the competitive landscape</p>
 <p fr-original-style=\'\\"\\"\'>4. Now, click on icon in top right hand corner
  of screen and select <strong fr-original-style=\'\\"\\"\'>PUBLISH</strong>
  </p>
"""

document = Document()
document = add_html(document, example_html)
document.save('example.docx')
