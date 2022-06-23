#Тема:17.Массивы. Использование массивов
# Р”Р°РЅ РѕРґРЅРѕРјРµСЂРЅС‹Р№ РјР°СЃСЃРёРІ С‡РёСЃР»РѕРІС‹С… Р·РЅР°С‡РµРЅРёР№, РЅР°СЃС‡РёС‚С‹РІР°СЋС‰РёР№ N СЌР»РµРјРµРЅС‚РѕРІ. РЎСѓРјРјСѓ СЌР»РµРјРµРЅС‚РѕРІ РјР°СЃСЃРёРІР° Рё РєРѕР»РёС‡РµСЃС‚РІРѕ РїРѕР»РѕР¶РёС‚РµР»СЊРЅС‹С… СЌР»РµРјРµРЅС‚РѕРІ РїРѕСЃС‚Р°РІРёС‚СЊ РЅР° РїРµСЂРІРѕРµ Рё РІС‚РѕСЂРѕРµ РјРµСЃС‚Рѕ.
# https://is19-2017.susu.ru/matveev/2018/12/23/zadacha-37/
def sumList(li):
    summa = 0
    for i in li:
        if i > 0:
            summa += 1
    li.insert(0, sum(li))
    li.insert(1, summa)
    return li


def test_sumList():
    data = [1, 2, 3, -4]
    dat = sumList(data)
    if dat == [2, 3, 1, 2, 3, -4]:
        return True


if test_sumList():
    print("TEST PASS")
else:
    print("TEST FAILED")


# Р”Р°РЅ РѕРґРЅРѕРјРµСЂРЅС‹Р№ РјР°СЃСЃРёРІ С‡РёСЃР»РѕРІС‹С… Р·РЅР°С‡РµРЅРёР№, РЅР°СЃС‡РёС‚С‹РІР°СЋС‰РёР№ N СЌР»РµРјРµРЅС‚РѕРІ. РџРѕСЃР»Рµ РєР°Р¶РґРѕРіРѕ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅРѕРіРѕ СЌР»РµРјРµРЅС‚Р° РІСЃС‚Р°РІРёС‚СЊ РЅРѕРІС‹Р№ СЌР»РµРјРµРЅС‚, СЂР°РІРЅС‹Р№ РєРІР°РґСЂР°С‚Сѓ СЌС‚РѕРіРѕ РѕС‚СЂРёС†Р°С‚РµР»СЊРЅРѕРіРѕ СЌР»РµРјРµРЅС‚Р°.
# https://is19-2017.susu.ru/matveev/2018/12/23/zadacha-40/
def otricChis(li):
    for i in range(len(li)):
        if li[i] < 0:
            li.insert(i + 1, li[i] ** 2)
    if li[-1] < 0:
        li.append(li[-1] ** 2)
    return li


def test_otricChis():
    dataT = [2, -5, 4, -2, -4]
    if otricChis(dataT) == [2, -5, 25, 4, -2, 4, -4, 16]:
        return True


if test_otricChis():
    print("TEST PASS")
else:
    print("TEST FAILED")


def polMas(li):
    for i in range(0, len(li), 2):
        if len(li) - 1 == i:
            continue
        x = li[i]
        li[i] = li[i + 1]
        li[i + 1] = x
    return li

#Р”Р°РЅ РѕРґРЅРѕРјРµСЂРЅС‹Р№ РјР°СЃСЃРёРІ С‡РёСЃР»РѕРІС‹С… Р·РЅР°С‡РµРЅРёР№, РЅР°СЃС‡РёС‚С‹РІР°СЋС‰РёР№ N СЌР»РµРјРµРЅС‚РѕРІ. РџРѕРјРµРЅСЏС‚СЊ РјРµСЃС‚Р°РјРё СЌР»РµРјРµРЅС‚С‹, СЃС‚РѕСЏС‰РёРµ РЅР° С‡С‘С‚РЅС‹С… Рё РЅРµС‡С‘С‚РЅС‹С… РјРµСЃС‚Р°С…
#https://is19-2017.susu.ru/matveev/2018/12/23/zadacha-32/
def test_polMas():
    data = [1, 2, 3, 4, 5, 6]
    if polMas(data) == [2, 1, 4, 3, 6, 5]:
        return True


if test_polMas():
    print("TEST PASS")
else:
    print("TEST FAILED")