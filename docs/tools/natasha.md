# Natasha

## Определение

Natasha — это open-source библиотека на языке Python для обработки естественного языка (NLP) на русском языке. Она предоставляет готовые модели для сегментации текста на предложения и токены, морфологического анализа, лемматизации, распознавания именованных сущностей (NER) и извлечения фактов.

## Зачем нужно

Русский язык обладает сложной морфологией, высокой вариативностью словоформ и свободным порядком слов, что делает стандартные NLP-инструменты, ориентированные на английский, малоэффективными. Natasha решает эту проблему, предоставляя простой API для решения типовых задач анализа русскоязычных текстов. Она позволяет разработчикам быстро добавлять в свои приложения такие функции, как извлечение имен, дат, адресов, компаний, а также определение грамматических характеристик слов — без необходимости обучать модели с нуля.

## Пример

```python
from natasha import (
    Segmenter,
    MorphVocab,
    NewsEmbedding,
    NewsMorphTagger,
    NewsSyntaxParser,
    NewsNERTagger,
    NamesExtractor,
    DatesExtractor,
    MoneyExtractor,
    AddrExtractor,
    Doc
)

segmenter = Segmenter()
morph_vocab = MorphVocab()

emb = NewsEmbedding()
morph_tagger = NewsMorphTagger(emb)
syntax_parser = NewsSyntaxParser(emb)
ner_tagger = NewsNERTagger(emb)

names_extractor = NamesExtractor(morph_vocab)
dates_extractor = DatesExtractor(morph_vocab)
money_extractor = MoneyExtractor(morph_vocab)
addr_extractor = AddrExtractor(morph_vocab)

text = 'Путин родился 7 октября 1952 года в Ленинграде.'
doc = Doc(text)
doc.segment(segmenter)
doc.tag_morph(morph_tagger)

tokens = doc.tokens
for token in tokens:
    token.lemmatize(morph_vocab)
    print(token.lemma)

doc.tag_ner(ner_tagger)
for span in doc.spans:
    print(span.type, span.text)

dates = dates_extractor(text)
for date in dates:
    print(date.normalized)
```

## Проекты
- [ai_guardrails_system](https://github.com/andand44/ai_guardrails_system)
