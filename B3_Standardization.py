def Standardization( data = None ):
    if not data: return None

    maxLine = 0
    maxWord = 0
    maxWOL = 0

    for i in data:
        if i[ 0 ] > maxLine: maxLine = i[ 0 ]
        if i[ 1 ] > maxWord: maxWord = i[ 1 ]
        if i[ 2 ] > maxWOL: maxWOL = i[ 2 ]

    line = {
        '0.0 - 0.2': 0,
        '0.2 - 0.4': 0,
        '0.4 - 0.6': 0,
        '0.6 - 0.8': 0,
        '0.8 - 1.0': 0,
    }

    word = {
        '0.0 - 0.2': 0,
        '0.2 - 0.4': 0,
        '0.4 - 0.6': 0,
        '0.6 - 0.8': 0,
        '0.8 - 1.0': 0,
    }

    wol = {
        '0.0 - 0.2': 0,
        '0.2 - 0.4': 0,
        '0.4 - 0.6': 0,
        '0.6 - 0.8': 0,
        '0.8 - 1.0': 0,
    }

    for i in data:
        curLine = i[ 0 ] / maxLine
        curWord = i[ 1 ] / maxWord
        curWOL = i[ 2 ] / maxWOL

        if 0 <= curLine <= 0.2: line[ '0.0 - 0.2' ] += 1
        elif 0.2 < curLine <= 0.4: line[ '0.2 - 0.4' ] += 1
        elif 0.4 < curLine <= 0.6: line[ '0.4 - 0.6' ] += 1
        elif 0.6 < curLine <= 0.8: line[ '0.6 - 0.8' ] += 1
        elif 0.8 < curLine <= 1: line[ '0.8 - 1.0' ] += 1

        if 0 <= curWord <= 0.2: word[ '0.0 - 0.2' ] += 1
        elif 0.2 < curWord <= 0.4: word[ '0.2 - 0.4' ] += 1
        elif 0.4 < curWord <= 0.6: word[ '0.4 - 0.6' ] += 1
        elif 0.6 < curWord <= 0.8: word[ '0.6 - 0.8' ] += 1
        elif 0.8 < curWord <= 1: word[ '0.8 - 1.0' ] += 1

        if 0 <= curWOL <= 0.2: wol[ '0.0 - 0.2' ] += 1
        elif 0.2 < curWOL <= 0.4: wol[ '0.2 - 0.4' ] += 1
        elif 0.4 < curWOL <= 0.6: wol[ '0.4 - 0.6' ] += 1
        elif 0.6 < curWOL <= 0.8: wol[ '0.6 - 0.8' ] += 1
        elif 0.8 < curWOL <= 1: wol[ '0.8 - 1.0' ] += 1

    return [ ( line, 'Line', maxLine, 'green' ), ( word, 'Word', maxWord, 'yellow' ), ( wol, 'WoL', maxWOL, 'brown' ) ]
