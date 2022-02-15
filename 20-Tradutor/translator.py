from translate import Translator

translator = Translator(from_lang = 'Portuguese',to_lang='english')
result = translator.translate('bora lá')
print(result)