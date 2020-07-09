# ContentDetector


Detect hard/soft skills from resumes in Russian.

Это — модуль, который из текста резюме/вакансии вычленяет профессиональные навыки (например, 1C, .NET) и "мягкие" навыки (обучаемость, коммуникабельность и т. п.). Однако концепции, на которых основан алгоритм, годятся для самых разных рекомедательных систем.

**Наиболее оптимальный сценарий использования** этого модуля заключается в том, чтобы произвести анализ созданной вакансии/резюме и предложить пользователю (как работнику, так и работодателю) набор выявленных навыков, из которого тот уберёт на свой взгляд лишние.

# Как этим пользоваться

Основная функция модуля — это ```get_content_from_text``` из файла [detector.py](https://github.com/PasaOpasen/ContentDetector/blob/master/content_detector/detector.py). Она принимает на вход список из строк резюме и возвращает список навыков (каждый навык — это просто строка).

```python
lines = ['Программист сайтов Битрикс и Битрикс 24.',
             'Партнёр Битрикс и Битрикс 24, интеграция Битрикс 24.',
             'Создание и продвижение сайтов, интернет магазина, лендинга.',
             'Дизайн, верстка, интернет маркетинг. Seo, топ 10, директ, соц сети.',
             'Так же работаю с любыми другими движками сайтов.',
             'Парсинг сайтов.','Стаж более 15 лет на фрилансе.']
    
print(get_content_from_text(lines))
# ['дизайн', 'дизайн сайтов', 'рекламные сервисы', 'разработка сайтов', 'верстка сайтов', 'оптимизация сайтов', 'Битрикс']
    
lines = ['Профессиональный опыт в сфере IT 10 лет.',
         'Опыт работы и поддержки информационных систем (сервисов) в крупных компаниях, предприятиях и гос. учреждениях.',
         '"KSB" "Россконгресс" "Burger King" "KFC"',
         'Высокая обучаемость.',
         'Грамотная речь, умение вести переговоры.',
         'Знание Английского языка: базовые знания.',
         'Управление персоналом, распределение задач.',
         'Умение самостоятельно проводить анализ и выявлять причины возникновения ошибок, и проблем.',
         'Коммуникабелен, стрессоустойчив. Без вредных привычек.']
    
 print(get_content_from_text(lines))
 # ['информационные системы', 'английский', 'грамотность', 'дружелюбность', 'организованность', 'обучаемость', 
 #'стрессоустойчивость', 'коммуникабельность', 'лидерские качества', 'умение убеждать', 'Burger King', 'KFC', 'KSB']   
    
 lines = ['Студент Тольяттинской Академии управления',
          'В данный момент нахожусь на дистанционной форме обучения, поэтому ищу работу с графиком полной рабочей загруженности.',
          'Имею четкую профессиональную траекторию и всегда ответственно подхожу к выполнению возложенных на меня задач.']
    
 print(get_content_from_text(lines))
 #['обучаемость', 'лидерские качества', 'ответственность']
 
```

Фактически выделение навыков выполяется с помощью *двух алгоритмов*, которые будем называть **основным** и **дополнительным**. На долю основного алгоритма может приходиться от 60% до 100% результата.

Функция имеет необязательный аргумент ```use_wiki = True```. Его назначение в том, чтобы активировать/дезактивировать поиск неизвестных основному алгоритму понятий с помощью [**wikipedia API**](https://github.com/goldsmith/Wikipedia). Это имеет смысл, если резюме/вакансия изобилует IT-терминами, однако поиск может занять несколько секунд. В первом из приведённых примеров с помощью этого дополнительного алгоритма были найдены признаки 'Burger King', 'KFC', 'KSB' (результаты дополнительного алгоритма, если они есть, записываются в конец списка).

Также функция имеет аргумент ```vocab = None```, что значит — использовать для основого алгоритма [словарь по умолчанию](https://github.com/PasaOpasen/ContentDetector/blob/master/content_detector/graph_skills.json). Через этот аргумент можно передать функции любой другой словарь, представляющий собой ассоциативный массив, в котором строке (маркеру) ставится в соотвествие список строк (список навыков).

Строки резюме можно прочесть из текстового файла:

```python
with open("my_resume.txt", 'r', encoding = 'utf-8') as f:
     lines = f.readlines()
print(get_content_from_text(lines, use_wiki = False))

#['научная деятельность', 'Adobe Illustrator', 'TypeScript', 'mathcad', 'Microsoft Office', 'plotly', 'Keras', 'верстка сайтов', 'HTML', 'пакет Adobe', 'грамотность',
#'программирование', 'Java', 'SQL', 'Data Science', 'LINQ', 'математические пакеты', 'Python', 'D', 'Scikit-learn', 'Delphi', 'статистика', 'Visual Studio', 'C++', 'фарси',
#'высшая математика', 'английский', 'LaTeX', '.NET Framework', 'Windows Forms', 'чистый код', 'документация', 'разработка сайтов', 'гибкость', 'Developing', 'базы данных',
#'Windows', 'JavaScript', '.NET', 'R (programming language)', 'Desktop', 'Microsoft Excel', 'git', 'тестирование кода', 'Numpy', 'обучаемость', 'ООП', 'Pandas', 
#'Microsoft Word', 'Машинное обучение'

```

Здесь считывается [файл с моим резюме](https://github.com/PasaOpasen/ContentDetector/blob/master/my_resume.txt) ([источник](https://github.com/PasaOpasen/PasaOpasen.github.io)).

# Как это работает

Задача выполняется в два этапа:

1. Очистка текста резюме/вакансии и создание n-грамм
2. Преобразование n-грамм в набор признаков с использованием одного или двух алгоритмов в зависимости от значения аргумента ```use_wiki```. 

## Преобразование текста в набор n-грамм

Функция принимает на вход список строк (вместе — *текст*). После этого:

1. Для каждой строки **удаляются пробельные символы** по краям, **удаляются пустые строки**

1. Из текста **удаляются все ссылки, адреса электронной почты, имена телеграм-ботов** и т. п.

1. **Удаляются (заменяются пробелом) все символы, которые не являются символами алфавита, числами или некоторыми потенциально несущими смысл символами** ('.' и ',' говорят о сепарации смысла, '+' может быть частью 'C++', '#' может быть частью 'C#', 'F#')

1. Набор строк увеличивается за счёт **разбиения каждой строки по запятым (',')**. Здесь мы исходим из того, что конструкции, перечисляемые через запятую, не несут особой информации в совокупности — только отдельно друг от друга.

1. Аналогично происходит **разбиение по стоп-словам** (то есть если в строке есть стоп-слово, оно удаляется, а то, что было слева, и то, что было справа, становятся отдельными строками). Используемые стоп-слова хранятся [в файле](https://github.com/PasaOpasen/ContentDetector/blob/master/content_detector/stopwords(used).txt); сперва использовались только стоп-слова русского и английского языков из **NLTK**, потом были добавлены основные русские предлоги и русские символы сами по себе. Этот список можно легко расширять, если потребуется.

1. Как и с запятыми, происходит **разбиение по точкам**, однако с учётом сокращений: в строках "мат. алгоритмы", "это, это и т. д и т. п." содержится по одному предложению, несмотря на наличие точки.

1. **Удаляются конструкции типа "т.", "п.", "1.", "2."**

1. Для каждой полученной строки **создаются 1- и 2-граммы** (ничего не мешает добавить 3-граммы, 4-граммы и т. д., если это целесообразно).

1. Среди полученного *множества* n-грамм **удаляются те, что не содержат алфавитных символов**. Считается, что они не несут информации о навыках.

### Пример

Возьмём следующее резюме:

```
Портфолио: www.behance.net/umkabear

Showreels: https://vimeo.com/341297601, https://vimeo.com/423526551



Знания пакета Adobe: Photoshop, Illustrator, InDesign.

Поверхностные знания Figma, Adobe After Effect.



Важное: к работе могу приступить с июля-августа. В приоритете вакансии с указанием зп, но готова обсуждать.
```
После удаления пустых строк и ссылок оно выглядит так:
```
Портфолио: 
Showreels: , 
Знания пакета Adobe: Photoshop, Illustrator, InDesign.
Поверхностные знания Figma, Adobe After Effect.
Важное: к работе могу приступить с июля-августа. В приоритете вакансии с указанием зп, но готова обсуждать.
```

После удаления лишних символов и разбиения по запятым:
```
Портфолио
Showreels 

Знания пакета Adobe Photoshop
 Illustrator
 InDesign.
Поверхностные знания Figma
 Adobe After Effect.
Важное к работе могу приступить с июля августа. В приоритете вакансии с указанием зп
 но готова обсуждать.
```

После разбиения по точкам и стоп-словам:
```
Портфолио
Showreels
Знания пакета Adobe Photoshop
Illustrator
InDesign
Поверхностные знания Figma
Adobe After Effect
Важное
работе могу приступить
июля августа
приоритете вакансии
указанием зп
готова обсуждать
```

В результате получены n-граммы:
```
готова обсуждать
пакета Adobe
вакансии
Adobe After
Знания
зп
приступить
Photoshop
обсуждать
After
работе могу
знания Figma
Adobe Photoshop
Figma
июля
Знания пакета
Поверхностные
знания
приоритете вакансии
Adobe
могу приступить
августа
Поверхностные знания
Важное
могу
InDesign
приоритете
готова
After Effect
пакета
Effect
работе
указанием зп
июля августа
Illustrator
Showreels
указанием
Портфолио
```

Этот же процесс для большого резюме можно посмотреть [в этом файле](https://github.com/PasaOpasen/ContentDetector/blob/master/resume_report.txt).

## Алгоритм на основе графов

### Концепция графа

Для определения смысла n-граммы используется **ориентированный несвязный граф понятий**. Он похож на дерево, но является несвязным, поскольку многие пары навыков никак не связаны друг с другом (например, 1С и пунктуальность); в то же время узлы этого графа могут иметь нескольких родителей: например, известный фреймворк ```tensorflow``` означает не только машинное обучение, но и язык Python как таковой.

По факту, имеется набор фраз (строк), которые тесно связаны друг с другом и являются либо значимыми (навыками, которые можно выводить), либо незначимыми (маркерами, вариациями навыков, которые связаны с конкретными значимыми признаками). Например, "Microsoft Office" — это значимый признак (навык), который является родителем "ms office" и "майкрософт офис", поэтому, если мы встречаем "ms office" внутри n-граммы, это означает "Microsoft Office".  

Кусок такого графа понятий представлен на рисунке:

![1](https://github.com/PasaOpasen/ContentDetector/blob/master/images/graph.PNG)

Это часть реального графа, с которым работает алгоритм. Целиком этот граф можно посмотреть [по ссылке](https://github.com/PasaOpasen/ContentDetector/blob/master/content_detector/gpaph.gv.pdf). Записывается этот граф при помощи [такого файла](https://github.com/PasaOpasen/ContentDetector/blob/master/content_detector/graph_skills.txt). Потенциально для удобного расширения графа можно разработать язык программирования с умным компилятором, подсветкой синтаксиса и т. п.

На самом деле этот граф — абстракция над некоторой базой данных, хранящей взаимосвязи между понятиями (навыками и их маркерами). **При реальной работе не происходит поиска на графе с рекурсиями и т. п. — вся эта работа выполняется при "компиляции" графа** и её результаты кешируются в [файл с ассоциативным массивом](https://github.com/PasaOpasen/ContentDetector/blob/master/content_detector/graph_skills.json), а уже этот массив передаётся функции ```get_content_from_text``` через массив ```voc```. Благодаря этому функция обрабатывает резюме очень быстро.

### Как это используется на практике

## Запасной алгоритм




