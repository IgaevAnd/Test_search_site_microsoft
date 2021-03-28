# Test_search_site_microsoft
Testing search functionality on docs.microsoft.com

Данный тест предусматривает проверку корректности поиска на веб-сайте docs.microsoft.com.

Основной задачей являлось:
- произвести проверку первых 50 результатов поиска,
- учесть не восприимчивость к регистру искомого слова,
- иметь возможность проведения анализа поиска (достигается путем сохранения необходимой информации с соответствующих словарях),
- по результатам теста визуально представлять качество работы поиска (достигается путем вывода исчерпывающей информации на экран по результатам поиска).

Данный тест выполнен при помощи фрэймворка pytest и библиотеки requests

Тест в терминале можно вызвать командой: pytest -s -v test_search.py 

Приятного ознакомления с проектом!!!
