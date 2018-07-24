from pathlib import Path

import spacy
from spacy import displacy


def visualize_doc(doc, output_dir, input_name, options={'compact':True}):
    figures = [('dep', f'{input_name}_dependency_parse.html'),
               ('ent', f'{input_name}_entity_recognition.html')]
    for style, file_name in figures:
        vis_html = displacy.render(doc, style=style, page=True, options=options)
        output_path = Path(f'{output_dir}/{file_name}')
        output_path.open('w', encoding='utf-8').write(vis_html)


def file_name(input_text):
    return Path(input_text).stem


def nlp_spacy(input_text, output_dir):
    text = ''
    with open(input_text.name, 'r') as input_file:
        text = input_file.read()
    nlp = spacy.load('en_core_web_sm')

    # Run spacy's nlp.
    doc = nlp(text)

    text_file_name = file_name(input_text.name)
    # Generate visualizations from the document.
    visualize_doc(doc, output_dir, text_file_name)
