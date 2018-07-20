import spacy


def nlp_spacy(input_text, output_dir):
    text = ''
    with open(input_text.name, 'r') as input_file:
        text = input_file.read()
    nlp = spacy.load('en_core_web_sm')

    doc = nlp(text)
    doc.to_disk(f"{output_dir}/spacy_document.bin")
