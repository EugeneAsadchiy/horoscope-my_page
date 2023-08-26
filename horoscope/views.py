from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template.loader import render_to_string

zodiac_dict = {
    'aries': 'Овен - первый знак зодиака, планета Марс (с 21 марта по 20 апреля).',
    'taurus': 'Телец - второй знак зодиака, планета Венера (с 21 апреля по 21 мая).',
    'gemini': 'Близнецы - третий знак зодиака, планета Меркурий (с 22 мая по 21 июня).',
    'cancer': 'Рак - четвёртый знак зодиака, Луна (с 22 июня по 22 июля).',
    'leo': ' Лев - пятый знак зодиака, солнце (с 23 июля по 21 августа).',
    'virgo': 'Дева - шестой знак зодиака, планета Меркурий (с 22 августа по 23 сентября).',
    'libra': 'Весы - седьмой знак зодиака, планета Венера (с 24 сентября по 23 октября).',
    'scorpio': 'Скорпион - восьмой знак зодиака, планета Марс (с 24 октября по 22 ноября).',
    'sagittarius': 'Стрелец - девятый знак зодиака, планета Юпитер (с 23 ноября по 22 декабря).',
    'capricorn': 'Козерог - десятый знак зодиака, планета Сатурн (с 23 декабря по 20 января).',
    'aquarius': 'Водолей - одиннадцатый знак зодиака, планеты Уран и Сатурн (с 21 января по 19 февраля).',
    'pisces': 'Рыбы - двенадцатый знак зодиака, планеты Юпитер (с 20 февраля по 20 марта).',
}
# Create your views here.
types = {
    'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'libra', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']
}
zodiac_dates = {
    1: {'capricorn': (1, 20), 'aquarius': (21, 31)},
    2: {'aquarius': (1, 19), 'pisces': (20, 29)},
    3: {'pisces': (1, 20), 'aries': (21, 31)},
    4: {'aries': (1, 20), 'taurus': (21, 30)},
    5: {'taurus': (1, 21), 'gemini': (22, 31)},
    6: {'gemini': (1, 21), 'cancer': (22, 30)},
    7: {'cancer': (1, 22), 'leo': (23, 31)},
    8: {'leo': (1, 21), 'virgo': (22, 31)},
    9: {'virgo': (1, 22), 'libra': (23, 30)},
    10: {'libra': (1, 23), 'scorpio': (24, 31)},
    11: {'scorpio': (1, 22), 'sagittarius': (23, 30)},
    12: {'sagittarius': (1, 22), 'capricorn': (23, 31)}
}


def index(request):
    zodiacs = list(zodiac_dict)
    context = {
        "menu_zodiac": zodiacs
    }
    # f"<li><a href='{redirect_path}'>{sign.title()}</a></li>"
    return render(request, "horoscope/index.html", context)


def get_info_about_types(request):
    li_elements = ""
    for elem in types.keys():
        redirect_path = reverse("types_name", args=[elem])

        li_elements += f"<li><a href='{redirect_path}'>{elem.title()}</a></li>"
    response = f"""
            <ol>
                {li_elements}
            </ol>"""
    return HttpResponse(response)


def get_info_about_types_and_elements(request, elem):
    li_elements = ""
    sp = types.get(elem)
    for elements in sp:
        redirect_path = reverse("horoscope_name", args=[elements])

        li_elements += f"<li><a href='{redirect_path}'>{elements.title()}</a></li>"
    response = f"""
                <ol>
                    {li_elements}
                </ol>"""
    return HttpResponse(response)


def get_info_by_date(request, month, day):
    if month > 12 or 31 < day < 28:
        return HttpResponse(f"Такого месяца не существует")
    dates = zodiac_dates.get(month)
    for zodiac, days in dates.items():
        print(days)
        if days[0] <= day <= days[1]:
            return HttpResponseRedirect(reverse('horoscope_name', args=(zodiac,)))
            # return HttpResponse(f"{zodiac}")


def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac)
    data = {
        "description_zodiac": description,
        "sign": sign_zodiac.title(),
        "sign_name": description.split()[0],

        "zodiacs": zodiac_dict

    }
    return render(request, "horoscope/info_zodiac.html", data)


def get_info_about_sign_zodiac_by_number(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f"Был передан неправильный порядковый номер {sign_zodiac}")
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope_name", args=(name_zodiac,))
    return HttpResponseRedirect(redirect_url)
