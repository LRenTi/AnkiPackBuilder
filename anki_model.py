import genanki

class APBModel:
    model_id = 9876543210
    model_name = 'APB Model'
    model_fields = [{'name': 'Question'}, {'name': 'Answer'}]
    model_templates = [{'name': 'Card 1', 'qfmt': '{{Question}}', 'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}'}]

    model = genanki.Model(model_id, model_name, model_fields, model_templates)
