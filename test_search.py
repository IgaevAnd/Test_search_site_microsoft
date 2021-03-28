import locators
import requests

list_without_title = []
list_without_description = []
list_without_title_and_description = []
list_good_search = []


def test_microsoft_search():
    success_of_test = 0
    print()

    # Итерация по страницам поиска
    for page in range(5):
        response = requests.get(
            f"https://docs.microsoft.com/api/search?search={locators.word}&locale=ru-ru&facet=category&%24top=10"
            f"&%24skip={locators.url50[page]}&expandScope=true")
        data = response.json()
        dic = {}
        lst = []

        # Итерация по позициям на странице поиска
        for item in range(10):
            success_in_title_of_header = 0
            success_in_descriptions_of_position = 0
            length_descriptions = len(data['results'][item]['descriptions'])

            print(f'    # {page * 10 + item + 1} (Page - {page + 1}, position - {item + 1}):')
            dic['page'] = str(page + 1)
            dic['position'] = str(item + 1)

            # Логика проверки наличия искомого слова в заголовке позиции
            if locators.word.lower() in data['results'][item]['title'].lower():
                success_in_title_of_header += 1
            else:
                print(f'    The word "{locators.word}" IS NOT in title header:\n    {data["results"][item]["title"]}.')
            dic['title'] = data['results'][item]['title']

            # Логика проверки наличия искомого слова в описании позиции
            for length in range(length_descriptions):
                if 'content' in data['results'][item]['descriptions'][length]:
                    if locators.word.lower() in data['results'][item]['descriptions'][length]["content"].lower():
                        success_in_descriptions_of_position += 1
                        lst.append(data['results'][item]['descriptions'][length]["content"])
                    else:
                        print(f'    The word "{locators.word}" IS NOT in descriptions position:\n    '
                              f'{data["results"][item]["descriptions"][length]["content"]}.')
                        lst.append(data['results'][item]['descriptions'][length]["content"])
                else:
                    print(f'    Descriptions position IS NOT.')
                    lst.append("null")
                dic["description"] = lst

            # Логига подведения результатов проверки искомого слова в заголовке и описании позиции
            if success_in_descriptions_of_position >= 1 == success_in_title_of_header:
                success_of_test += 1
                list_good_search.append(dic)
                print(f'    RESULT: This is OK!')
                print('    Added to list_good_search')
            elif success_in_descriptions_of_position >= 1 > success_in_title_of_header:
                success_of_test += 1
                list_without_title.append(dic)
                print(
                    f'    RESULT: The word "{locators.word}" IS in descriptions position, but IS NOT in title header.')
                print('    Added to list_list_without_title')
            elif success_in_descriptions_of_position < 1 == success_in_title_of_header:
                success_of_test += 1
                list_without_description.append(dic)
                print(
                    f'    RESULT: The word "{locators.word}" IS NOT in descriptions position, but IS in title header.')
                print('    Added to list_without_description.')
            else:
                list_without_title_and_description.append(dic)
                print(f'    RESULT: The word "{locators.word}" IS NOT in descriptions position and title header.')
                print('    Added to list_without_title_and_description.')
            print()

    # Вывод результатов
    print(F'\n\n    --------------------------------------\n'
          F'    Added to list_good_search: {len(list_good_search)};\n'
          f'    Added to list_without_title: {len(list_without_title)};\n'
          f'    Added to list_without_description: {len(list_without_description)};\n'
          f'    Added to list_without_title_and_description: {len(list_without_title_and_description)}.\n'
          f'    --------------------------------------\n\n')

    assert success_of_test == 50, f"{locators.error_search}"
