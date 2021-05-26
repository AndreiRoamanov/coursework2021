import time
start_time = time.time()

signal = 0
while True:
#    n = int(input())
    fullpol = input() #полином задаётся в формате x1x2..xn + !x1x2x3 + ... xn и т.д.
    i = 0
    thismon = 0
    pol = 0
    maxsymb = 0
    lenthismon = 0
    cntallminpols = 0
    cycles = 0 # проверка на зацикленность
    mon = []
    lenmon = []
    allminfullpols = -1
    allminfulllens = 1000
    while i < len(fullpol):
        bufneg = 1
        if fullpol[i] == '!':
            bufneg = 2
            i = i + 1
        if fullpol[i] == 'x':
            i = i + 1
            symb = int(fullpol[i])
            maxsymb = max(maxsymb, symb)
            lenthismon = lenthismon + 1
            thismon = thismon + bufneg * 10 ** (symb - 1)
            i = i + 1
        elif fullpol[i] == '+':
            mon.append(thismon)
            lenmon.append(lenthismon)
            lenthismon = 0
            thismon = 0
            thismon = 0
            i = i + 1
        elif fullpol[i] == ' ':
            i = i + 1
        elif fullpol[i] == '1':
            thismon = 3
            lenthismon = 1
            i = i + 1
    mon.append(thismon)
    lenmon.append(lenthismon)
            
    n = maxsymb
    print(n)
    pol = 0
    for s in range (0, len(mon)):
        pol = pol * 10 ** n + mon[s]
    
    print(pol)
    firstlen = len(str(pol)) // n
    if len(str(pol)) % n != 0:
        firstlen = firstlen + 1
    lenpol = 0
    bufpol = pol
    while bufpol != 0:
        bufpol = bufpol // 10
        lenpol = lenpol + 1
    if lenpol % n == 0:
        cntmon = lenpol // n
    else:
        cntmon = lenpol // n + 1
    mon.reverse()
    lenmon.reverse()
    print(mon)
    print(lenmon)
    
    
    # Сортировка по lenmon, вместе с mon
    notnow='''for ki in range (0, len(lenmon) - 1):
        for kj in range (ki + 1, len(lenmon)):
            if lenmon[kj] < lenmon[ki]:
                lenmon[ki], lenmon[kj] = lenmon[kj], lenmon[ki]
                mon[ki], mon[kj] = mon[kj], mon[ki]'''
    
    print(mon)
    print(lenmon)

### ЧАСТЬ С ОТЖИГОМ - ФОРМИРОВАНИЕ МАССИВА
    kkbuf = 0
    maxlenbuf = lenmon[0]
    for ki in range (0, len(lenmon)):
        if lenmon[ki] > maxlenbuf:
            maxlenbuf = lenmon[ki]
            kkbuf = ki
    maxmonbuf = mon[kkbuf]
    strmaxonbuf = str(maxmonbuf)
    newstrmaxonbuf = ''
    for sksk in range(0, len(strmaxonbuf)):
        if strmaxonbuf[sksk] != '0':
            newstrmaxonbuf = '1' + newstrmaxonbuf
        else:
            newstrmaxonbuf = '0' + newstrmaxonbuf
    newmaxmonbuf = int(newstrmaxonbuf)
    print(newstrmaxonbuf)
    
    strmaxonbufrev = newstrmaxonbuf[::-1]
    print("strmaxonbufrev = ", strmaxonbufrev)

    bufofmonbuf = newmaxmonbuf
    havelits = []
    for ssss in range(0, n):
        havelits.append(0)
    ssss = 0
    while bufofmonbuf > 0:
        havelits[ssss] = bufofmonbuf % 10
        bufofmonbuf = bufofmonbuf // 10
        ssss += 1
    print(havelits)
    
    bufb = 0
    bufofmonbuf = newmaxmonbuf
    resofbuf = bufofmonbuf
    ssss = 0
    bufskk = 1
    badnow = 0
    mons_from_max = []
    # получение массива без наибольшего монома - с ним см bufskk
    while resofbuf != 0:
        skk = bufskk
        b_in2 = ''
        while skk > 0:
            b_in2 = str(skk % 2) + b_in2
            skk = skk // 2
        b_in2_rev = b_in2[::-1]
        for rkk in range(0, len(b_in2_rev)):
            if b_in2_rev[rkk] == '1' and strmaxonbufrev[rkk] == '0':
                badnow = 1
                break
        #print(b_in2, 'badnow = ', badnow)
        if badnow == 0:
            int_b_in2 = int(b_in2)
            resofbuf = bufofmonbuf - int_b_in2
            if resofbuf != 0:
                mons_from_max.append(resofbuf)
            else:
                mons_from_max.append(3)
        else:
            badnow = 0
        bufskk += 1
    print(mons_from_max)
########################################
    ###################################


    ourminpol = pol
    minmons = []
    bufpol = ourminpol
    j = 0
    while (bufpol != 0):
        minmons.append(bufpol % 10 ** n)
        bufpol = bufpol // 10 ** n       
    tabl = []
    for i in range (0, n):
        tabl.append(0)
    bad = 0
    vect = 0
    fortabl = ''
    polzn = 0
#    print(minmons)
#    print("len = ", minnlen)
    for i in range (0, 2 ** n):
        for k in range (0, firstlen):
            for j in range (0, n):
                if (minmons[k] // 10 ** j % 10 == 2 and tabl[j] == 1) or (minmons[k] // 10 ** j % 10 == 1 and tabl[j] == 0):
                    bad = 1
            if bad == 1:
                polzn = polzn
            else:
                polzn = (polzn + 1) % 2
            bad = 0
        vect = vect * 10 + polzn
        polzn = 0
        nexti = i + 1
        ue = n - 1
        while ue > -1:
            tabl[ue] = nexti % 2
            ue = ue - 1
            nexti = nexti // 2

    ######### ZHEGALKIN
    strvect = str(vect)
    endzn = len(strvect)
    razn = 2 ** n - endzn
    if razn != 0:
        strvect = '0' * razn + strvect
    endzn = 2 ** n
    stepnow = ''
    fsts = []
    fsts.append(int(strvect[0]))
    while endzn > 1:
        stepnow = ''
        for ss in range(0, endzn - 1):
            thistep = (int(strvect[ss]) + int(strvect[ss + 1])) % 2
            strthistep = str(thistep)
            stepnow = stepnow + strthistep
        strvect = str(stepnow)
        endzn = len(stepnow)
        fsts.append(int(stepnow[0]))
    if n == 3:
        monshere = [3, 100, 10, 110, 1, 101, 11, 111]
    if n == 4:
        monshere = [3, 1000, 100, 1100, 10, 1010, 110, 1110, 1, 1001, 101, 1101, 11, 1011, 111, 1111]
    elif n == 5:
        monshere = [3, 10000, 1000, 11000, 100, 10100, 1100, 11100, 10, 10010, 1010, 11010, 110, 10110, 1110, 11110,
            1, 10001, 1001, 11001, 101, 10101, 1101, 11101, 11, 10011, 1011, 11011, 111, 10111, 1111, 11111]
    elif n == 6:
        monshere = [3, 100000, 10000, 110000, 1000, 101000, 11000, 111000, 100, 100100, 10100, 110100, 1100, 101100, 11100, 111100,
            10, 100010, 10010, 110010, 1010, 101010, 11010, 111010, 110, 100110, 10110, 110110, 1110, 101110, 11110, 111110,
                    1, 100001, 10001, 110001, 1001, 101001, 11001, 111001, 101, 100101, 10101, 110101, 1101, 101101, 11101, 111101,
            11, 100011, 10011, 110011, 1011, 101011, 11011, 111011, 111, 100111, 10111, 110111, 1111, 101111, 11111, 111111]
    elif n == 7:
        monshere = [3, 1000000, 100000, 1100000, 10000, 1010000, 110000, 1110000, 1000, 1001000, 101000, 1101000, 11000, 1011000, 111000, 1111000,
                    100, 1000100, 100100, 1100100, 10100, 1010100, 110100, 1110100, 1100, 1001100, 101100, 1101100, 11100, 1011100, 111100, 1111100,
                    10, 1000010, 100010, 1100010, 10010, 1010010, 110010, 1110010, 1010, 1001010, 101010, 1101010, 11010, 1011010, 111010, 1111010,
                    110, 1000110, 100110, 1100110, 10110, 1010110, 110110, 1110110, 1110, 1001110, 101110, 1101110, 11110, 1011110, 111110, 1111110,
                    1, 1000001, 100001, 1100001, 10001, 1010001, 110001, 1110001, 1001, 1001001, 101001, 1101001, 11001, 1011001, 111001, 1111001,
                    101, 1000101, 100101, 1100101, 10101, 1010101, 110101, 1110101, 1101, 1001101, 101101, 1101101, 11101, 1011101, 111101, 1111101,
                    11, 1000011, 100011, 1100011, 10011, 1010011, 110011, 1110011, 1011, 1001011, 101011, 1101011, 11011, 1011011, 111011, 1111011,
                    111, 1000111, 100111, 1100111, 10111, 1010111, 110111, 1110111, 1111, 1001111, 101111, 1101111, 11111, 1011111, 111111, 1111111]
    elif n == 8:
        monshere = [3, 10000000, 1000000, 11000000, 100000, 10100000, 1100000, 11100000, 10000, 10010000, 1010000, 11010000, 110000, 10110000, 1110000, 11110000, 1000, 10001000, 1001000, 11001000, 101000, 10101000, 1101000, 11101000, 11000, 10011000, 1011000, 11011000, 111000, 10111000, 1111000, 11111000, 100, 10000100, 1000100, 11000100, 100100, 10100100, 1100100, 11100100, 10100, 10010100, 1010100, 11010100, 110100, 10110100, 1110100, 11110100, 1100, 10001100, 1001100, 11001100, 101100, 10101100, 1101100, 11101100, 11100, 10011100, 1011100, 11011100, 111100, 10111100, 1111100, 11111100, 10, 10000010, 1000010, 11000010, 100010, 10100010, 1100010, 11100010, 10010, 10010010, 1010010, 11010010, 110010, 10110010, 1110010, 11110010, 1010, 10001010, 1001010, 11001010, 101010, 10101010, 1101010, 11101010, 11010, 10011010, 1011010, 11011010, 111010, 10111010, 1111010, 11111010, 110, 10000110, 1000110, 11000110, 100110, 10100110, 1100110, 11100110, 10110, 10010110, 1010110, 11010110, 110110, 10110110, 1110110, 11110110, 1110, 10001110, 1001110, 11001110, 101110, 10101110, 1101110, 11101110, 11110, 10011110, 1011110, 11011110, 111110, 10111110, 1111110, 11111110, 1, 10000001, 1000001, 11000001, 100001, 10100001, 1100001, 11100001, 10001, 10010001, 1010001, 11010001, 110001, 10110001, 1110001, 11110001, 1001, 10001001, 1001001, 11001001, 101001, 10101001, 1101001, 11101001, 11001, 10011001, 1011001, 11011001, 111001, 10111001, 1111001, 11111001, 101, 10000101, 1000101, 11000101, 100101, 10100101, 1100101, 11100101, 10101, 10010101, 1010101, 11010101, 110101, 10110101, 1110101, 11110101, 1101, 10001101, 1001101, 11001101, 101101, 10101101, 1101101, 11101101, 11101, 10011101, 1011101, 11011101, 111101, 10111101, 1111101, 11111101, 11, 10000011, 1000011, 11000011, 100011, 10100011, 1100011, 11100011, 10011, 10010011, 1010011, 11010011, 110011, 10110011, 1110011, 11110011, 1011, 10001011, 1001011, 11001011, 101011, 10101011, 1101011, 11101011, 11011, 10011011, 1011011, 11011011, 111011, 10111011, 1111011, 11111011, 111, 10000111, 1000111, 11000111, 100111, 10100111, 1100111, 11100111, 10111, 10010111, 1010111, 11010111, 110111, 10110111, 1110111, 11110111, 1111, 10001111, 1001111, 11001111, 101111, 10101111, 1101111, 11101111, 11111, 10011111, 1011111, 11011111, 111111, 10111111, 1111111, 11111111]
    elif n == 9:
        monshere = [3, 100000000, 10000000, 110000000, 1000000, 101000000, 11000000, 111000000, 100000, 100100000, 10100000, 110100000, 1100000, 101100000, 11100000, 111100000, 10000,
                    100010000, 10010000, 110010000, 1010000, 101010000, 11010000, 111010000, 110000, 100110000, 10110000, 110110000, 1110000, 101110000, 11110000, 111110000, 1000,
                    100001000, 10001000, 110001000, 1001000, 101001000, 11001000, 111001000, 101000, 100101000, 10101000, 110101000, 1101000, 101101000, 11101000, 111101000, 11000,
                    100011000, 10011000, 110011000, 1011000, 101011000, 11011000, 111011000, 111000, 100111000, 10111000, 110111000, 1111000, 101111000, 11111000, 111111000, 100, 100000100,
                    10000100, 110000100, 1000100, 101000100, 11000100, 111000100, 100100, 100100100, 10100100, 110100100, 1100100, 101100100, 11100100, 111100100, 10100, 100010100,
                    10010100, 110010100, 1010100, 101010100, 11010100, 111010100, 110100, 100110100, 10110100, 110110100, 1110100, 101110100, 11110100, 111110100, 1100, 100001100, 10001100,
                    110001100, 1001100, 101001100, 11001100, 111001100, 101100, 100101100, 10101100, 110101100, 1101100, 101101100, 11101100, 111101100, 11100, 100011100, 10011100,
                    110011100, 1011100, 101011100, 11011100, 111011100, 111100, 100111100, 10111100, 110111100, 1111100, 101111100, 11111100, 111111100, 10, 100000010, 10000010, 110000010,
                    1000010, 101000010, 11000010, 111000010, 100010, 100100010, 10100010, 110100010, 1100010, 101100010, 11100010, 111100010, 10010, 100010010, 10010010, 110010010,
                    1010010, 101010010, 11010010, 111010010, 110010, 100110010, 10110010, 110110010, 1110010, 101110010, 11110010, 111110010, 1010, 100001010, 10001010, 110001010, 1001010,
                    101001010, 11001010, 111001010, 101010, 100101010, 10101010, 110101010, 1101010, 101101010, 11101010, 111101010, 11010, 100011010, 10011010, 110011010, 1011010,
                    101011010, 11011010, 111011010, 111010, 100111010, 10111010, 110111010, 1111010, 101111010, 11111010, 111111010, 110, 100000110, 10000110, 110000110, 1000110, 101000110,
                    11000110, 111000110, 100110, 100100110, 10100110, 110100110, 1100110, 101100110, 11100110, 111100110, 10110, 100010110, 10010110, 110010110, 1010110, 101010110,
                    11010110, 111010110, 110110, 100110110, 10110110, 110110110, 1110110, 101110110, 11110110, 111110110, 1110, 100001110, 10001110, 110001110, 1001110, 101001110,
                    11001110, 111001110, 101110, 100101110, 10101110, 110101110, 1101110, 101101110, 11101110, 111101110, 11110, 100011110, 10011110, 110011110, 1011110, 101011110,
                    11011110, 111011110, 111110, 100111110, 10111110, 110111110, 1111110, 101111110, 11111110, 111111110, 1, 100000001, 10000001, 110000001, 1000001, 101000001, 11000001,
                    111000001, 100001, 100100001, 10100001, 110100001, 1100001, 101100001, 11100001, 111100001, 10001, 100010001, 10010001, 110010001, 1010001, 101010001, 11010001,
                    111010001, 110001, 100110001, 10110001, 110110001, 1110001, 101110001, 11110001, 111110001, 1001, 100001001, 10001001, 110001001, 1001001, 101001001, 11001001,
                    111001001, 101001, 100101001, 10101001, 110101001, 1101001, 101101001, 11101001, 111101001, 11001, 100011001, 10011001, 110011001, 1011001, 101011001, 11011001,
                    111011001, 111001, 100111001, 10111001, 110111001, 1111001, 101111001, 11111001, 111111001, 101, 100000101, 10000101, 110000101, 1000101, 101000101, 11000101, 111000101,
                    100101, 100100101, 10100101, 110100101, 1100101, 101100101, 11100101, 111100101, 10101, 100010101, 10010101, 110010101, 1010101, 101010101, 11010101, 111010101, 110101,
                    100110101, 10110101, 110110101, 1110101, 101110101, 11110101, 111110101, 1101, 100001101, 10001101, 110001101, 1001101, 101001101, 11001101, 111001101, 101101, 100101101,
                    10101101, 110101101, 1101101, 101101101, 11101101, 111101101, 11101, 100011101, 10011101, 110011101, 1011101, 101011101, 11011101, 111011101, 111101, 100111101, 10111101,
                    110111101, 1111101, 101111101, 11111101, 111111101, 11, 100000011, 10000011, 110000011, 1000011, 101000011, 11000011, 111000011, 100011, 100100011, 10100011, 110100011,
                    1100011, 101100011, 11100011, 111100011, 10011, 100010011, 10010011, 110010011, 1010011, 101010011, 11010011, 111010011, 110011, 100110011, 10110011, 110110011, 1110011,
                    101110011, 11110011, 111110011, 1011, 100001011, 10001011, 110001011, 1001011, 101001011, 11001011, 111001011, 101011, 100101011, 10101011, 110101011, 1101011, 101101011,
                    11101011, 111101011, 11011, 100011011, 10011011, 110011011, 1011011, 101011011, 11011011, 111011011, 111011, 100111011, 10111011, 110111011, 1111011, 101111011, 11111011,
                    111111011, 111, 100000111, 10000111, 110000111, 1000111, 101000111, 11000111, 111000111, 100111, 100100111, 10100111, 110100111, 1100111, 101100111, 11100111, 111100111,
                    10111, 100010111, 10010111, 110010111, 1010111, 101010111, 11010111, 111010111, 110111, 100110111, 10110111, 110110111, 1110111, 101110111, 11110111, 111110111, 1111, 100001111, 10001111,
                    110001111, 1001111, 101001111, 11001111, 111001111, 101111, 100101111, 10101111, 110101111, 1101111, 101101111, 11101111, 111101111, 11111, 100011111, 10011111, 110011111, 1011111,
                    101011111, 11011111, 111011111, 111111, 100111111, 10111111, 110111111, 1111111, 101111111, 11111111, 111111111]
        
    notnow='''monshere = [3, 1000, 100, 1100, 10, 1010, 110, 1110, 1, 1001, 101, 1101, 11, 1011, 111, 1111]
    for sssss in range(n - 4):
        mascnt1 = []
        mascnt2 = []
        for s in range(len(monshere)):
            if monshere[s] == 3:
                monshere[s] = 0
            thismonstr = str(monshere[s])
            mascnt1.append(int(thismonstr + '0'))
            mascnt2.append(int(thismonstr + '1'))
            if s == 0:
                mascnt1[s] = 3

        for s in range(len(mascnt2)):
            mascnt1.append(mascnt2[s])
        monshere = []
        for s in range(len(mascnt1)):
            monshere.append(mascnt1[s])'''
    zhegpol = 0
    for tt in range(0, len(fsts)):
        if fsts[tt] == 1:
            zhegpol = zhegpol * 10 ** n + monshere[tt]

    pol = zhegpol
    firstlen = len(str(pol)) // n
    if len(str(pol)) % n != 0:
        firstlen = firstlen + 1
    buffirstlen = firstlen
    print("now here = ", zhegpol)

    mon = []
    lenmon = []
    lenpol = 0
    bufpol = pol
    while bufpol != 0:
        bufpol = bufpol // 10
        lenpol = lenpol + 1
    if lenpol % n == 0:
        cntmon = lenpol // n
    else:
        cntmon = lenpol // n + 1
    bufpol = pol
    for i in range (0, cntmon):
        mon.append(bufpol % 10 ** n)
        lenm = 0
        thismon = bufpol % 10 ** n
        for j in range (0, n):
            if (thismon // 10 ** j) % 10 != 0:
                lenm = lenm + 1
        lenmon.append(lenm)
        bufpol = bufpol // 10 ** n
        
        
        
        

    lenprodterm = []
    prodterm = []

    m1 = 2 ** (n * 2)
    m2 = 2 ** (n * 2)
    ways = []
    ways.append([])
    ways[0].append(0) # первое значение отвечает за длину/количество, вносим сразу
    numofpols = []
    numoflens = []
    cnums = 0 # число путей
    firsttry = 1 # составляет путь в первый раз
    cntvars = 0 # отвечает, какой по счёту вариант сокращений

    tozhd = 2

#
    # здесь начинаем всеобщий цикл - заканчиваем, пока не пройдём весь полином без всяких сокращений.
    #prodterm - мономы - в курсовом варианте получаю их из mon
    nextloop = 0
    minpolswas = []
    buflastourminpol = -1
    af = open('b.txt', 'w')
    firstly = 1 # в первый раз заходим и избавляемся от отрицаний (здесь, только 1 раз)
    while nextloop < 19:

        if nextloop % 2 == 1: # в тождестве с длиной n - 2
            predlen = minlen - 1
            modes = 0
            wasfst = -1
            wasscnd = 0
            u = wasfst
            skipflag = 0
            t2pols = []
            prodterm = []
            lenprodterm = []
            for formon in range (0, cntmon):
                prodterm.append(mon[formon])
                lenprodterm.append(lenmon[formon])
            bigalllens = []
            bigallprodterms = []   # массив массивов prodterm - туда заносим, чтобы потом взять
            bufterm = []
            for kkk in range(0, len(prodterm)):
                bufterm.append(prodterm[kkk])
            bigallprodterms.append(bufterm)
            bigalllens.append(cntmon - 1)
            bigallinds = []
            bigallinds.append(0)
            bigallcnt = 0 # счётчик все таких массивов
            bigallcntpred = 0
            prommlen = 0
            while (True):
                newprodscnt = cntmon
                nowlen = cntmon - 1
                newprodterm = []
                newlenprodterm = []
                for formon in range (0, cntmon):
                    newprodterm.append(mon[formon])
                    newlenprodterm.append(lenmon[formon])
                gotobeg = 0
                while u < predlen - 1:
                    u = u + 1
                    if prodterm[u] == 4:
                        skipflag = 0
                        continue
                    z = u
                    if skipflag == 1:
                        z = wasscnd
                        skipflag = 0
                    while z < predlen:
                        stopf = 0
                        if gotobeg == 1:
                            gotobeg = 0
                            break
                        z = z + 1
                        if prodterm[u] == 4:
                            break
                        if prodterm[z] == 4:
                            continue
                        prodterm1 = prodterm[u]
                        prodterm2 = prodterm[z]
                        bufprodterm1 = prodterm1
                        bufprodterm2 = prodterm2
                        ravn = 0 # число равных переменных в мономах
                        notravn = 0 # число неравных переменных в мономах
                        newliter = -1
                        newliters = [] # новые литеры в массивах при >= 2 несоответствиях
                        notravnpers = [] # не равные литеры в массивах, чтобы было проще ориентироваться при >= 2 несоотв
                        ex = 1
                        if prodterm1 == 3 and lenprodterm[z] == 1 or prodterm2 == 3 and lenprodterm[u] == 1:
                            ravn = n - 1
                            for i in range (0, n):
                                if bufprodterm1 % 10 == 1 or bufprodterm2 % 10 == 1:
                                    newliter = 2
                                    notravnper = i
                                elif bufprodterm1 % 10 == 2 or bufprodterm1 % 10 == 2:
                                    newliter = 1
                                    notravnper = i
                                notravn = 1
                                bufprodterm1 = bufprodterm1 // 10
                                bufprodterm2 = bufprodterm2 // 10
                            ex = 2
                        else:
                            ravnper = []   # массив, отвечающий за равные переменные
                            for rpers in range (0, n):
                                ravnper.append(-1)
                            rpers = 0   
                            
                            for i in range (0, n):
                                if bufprodterm1 % 10 == bufprodterm2 % 10:
                                    ravnper[rpers] = i
                                    rpers = rpers + 1
                                    ravn = ravn + 1
                                else:
                                    notravnpers.append(i)
                                    notravnper = i
                                    if bufprodterm1 % 10 == 0 and bufprodterm2 % 10 == 1 or bufprodterm1 % 10 == 1 and bufprodterm2 % 10 == 0: # новая литера в новом мономе
                                        newliter = 2
                                        newliters.append(2)
                                    if bufprodterm1 % 10 == 0 and bufprodterm2 % 10 == 2 or bufprodterm1 % 10 == 2 and bufprodterm2 % 10 == 0:
                                        newliter = 1
                                        newliters.append(1)
                                    if bufprodterm1 % 10 == 1 and bufprodterm2 % 10 == 2 or bufprodterm1 % 10 == 2 and bufprodterm2 % 10 == 1:
                                        newliter = 0
                                        newliters.append(0)
                                    notravn = notravn + 1
                                bufprodterm1 = bufprodterm1 // 10
                                bufprodterm2 = bufprodterm2 // 10
                        litcnt = 0
                        if ravn == n - 2:
                            prodterm1 = prodterm[u]
                            prodterm2 = prodterm[z]
                            newprodterm1 = prodterm1
                            newprodterm2 = prodterm2
                            nrvind = 0

                            strnewprodterm1 = strnewprodterm2 = strnewprodterm3 = ''
                            strprodterm1 = str(prodterm1)
                            if strprodterm1 == '3':
                                strprodterm1 = '0'
                            strprodterm2 = str(prodterm2)
                            if strprodterm2 == '3':
                                strprodterm2 = '0'
                            if len(strprodterm1) < len(strprodterm2):
                                razn = len(strprodterm2) - len(strprodterm1)
                                strprodterm1 = '0' * razn + strprodterm1
                            elif len(strprodterm1) > len(strprodterm2):
                                razn = len(strprodterm1) - len(strprodterm2)
                                strprodterm2 = '0' * razn + strprodterm2
                            for zzz in range (len(strprodterm1)):
                                if strprodterm1[zzz] == strprodterm2[zzz]:
                                    strnewprodterm1 = strnewprodterm1 + strprodterm2[zzz]
                                    strnewprodterm2 = strnewprodterm2 + strprodterm2[zzz]
                                elif strprodterm1[zzz] != strprodterm2[zzz]:
                                    if modes == 0:
                                        if nrvind == 0:
                                            if strprodterm1[zzz] == '1' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '1':
                                                strnewprodterm1 = strnewprodterm1 + '0'
                                            elif strprodterm1[zzz] == '0' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '0':
                                                strnewprodterm1 = strnewprodterm1 + '1'
                                            elif strprodterm1[zzz] == '1' and strprodterm2[zzz] == '0' or strprodterm1[zzz] == '0' and strprodterm2[zzz] == '1':
                                                strnewprodterm1 = strnewprodterm1 + '2'
                                            strnewprodterm2 = strnewprodterm2 + strprodterm2[zzz]
                                            
                                        elif nrvind == 1:
                                            strnewprodterm1 = strnewprodterm1 + strprodterm1[zzz]
                                            
                                            if strprodterm1[zzz] == '1' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '1':
                                                strnewprodterm2 = strnewprodterm2 + '0'
                                            elif strprodterm1[zzz] == '0' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '0':
                                                strnewprodterm2 = strnewprodterm2 + '1'
                                            elif strprodterm1[zzz] == '1' and strprodterm2[zzz] == '0' or strprodterm1[zzz] == '0' and strprodterm2[zzz] == '1':
                                                strnewprodterm2 = strnewprodterm2 + '2'
                                                
                                            
                                        nrvind = nrvind + 1
                                    elif modes == 1:
                                        if nrvind == 0:
                                            if strprodterm1[zzz] == '1' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '1':
                                                strnewprodterm1 = strnewprodterm1 + '0'
                                            elif strprodterm1[zzz] == '0' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '0':
                                                strnewprodterm1 = strnewprodterm1 + '1'
                                            elif strprodterm1[zzz] == '1' and strprodterm2[zzz] == '0' or strprodterm1[zzz] == '0' and strprodterm2[zzz] == '1':
                                                strnewprodterm1 = strnewprodterm1 + '2'
                                            strnewprodterm2 = strnewprodterm2 + strprodterm1[zzz]
                                            
                                            
                                        elif nrvind == 1:
                                            strnewprodterm1 = strnewprodterm1 + strprodterm2[zzz]
                                            
                                            if strprodterm1[zzz] == '1' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '1':
                                                strnewprodterm2 = strnewprodterm2 + '0'
                                            elif strprodterm1[zzz] == '0' and strprodterm2[zzz] == '2' or strprodterm1[zzz] == '2' and strprodterm2[zzz] == '0':
                                                strnewprodterm2 = strnewprodterm2 + '1'
                                            elif strprodterm1[zzz] == '1' and strprodterm2[zzz] == '0' or strprodterm1[zzz] == '0' and strprodterm2[zzz] == '1':
                                                strnewprodterm2 = strnewprodterm2 + '2'
                                                
                                            
                                        nrvind = nrvind + 1 
                            newprodterm1 = int(strnewprodterm1)
                            newprodterm2 = int(strnewprodterm2)
                            
                            nowlen = nowlen + 2
                            if newprodscnt < len(prodterm):
                                prodterm[newprodscnt] = newprodterm1
                                prodterm[newprodscnt+1] = newprodterm2
                            else:
                                 prodterm.append(newprodterm1)
                                 prodterm.append(newprodterm2)
                            newprodscnt = newprodscnt + 2
                            prodterm[z] = 4
                            prodterm[u] = 4
                            lenprodterm[z] = 0
                            lenprodterm[u] = 0
                            thislen = 0
                            thisesop = 0
                            for sch in range (0, nowlen + 1):
                                if prodterm[sch] != 4:
                                    thislen = thislen + 1
                                    thisesop = thisesop * 10 ** n + prodterm[sch]
                            numoflens.append(thislen)
                            lenesopnow = len(str(thisesop)) // n
                            if len(str(thisesop)) % n != 0:
                                lenesopnow = lenesopnow + 1
                            if lenesopnow != thislen:
                                razzn = thislen - lenesopnow
                                thisesop = thisesop * 10 ** (n * razzn)
                            t2pols.append(thisesop)
                            modes = (modes + 1) % 2
                            bigallprodterms.append([])
                            for kkk in range(0, len(prodterm)):
                                bigallprodterms[bigallcnt + 1].append(prodterm[kkk])
                            bigalllens.append(nowlen)
                            bftrm = []
                            for ss in range(0, len(bigallprodterms[bigallcntpred])):
                                bftrm.append(bigallprodterms[bigallcntpred][ss])
                            prodterm = bftrm
                            nowlen = bigalllens[bigallcntpred]
                            bigallcnt = bigallcnt + 1
                            if modes == 1: # в следующий раз будем брать новый элемент, при mode = 0 берём старый
                                bigallcntpred = bigallcntpred + 1
                        
                            u = wasfst
                            z = wasfst
                            gotobeg = 1
                            skipflag = 1
                                

                        if z == predlen and u == predlen - 1 and modes == 1: # находимся на конечных значениях
                            prodterm = []
                            for formon in range (0, cntmon):
                                prodterm.append(mon[formon])
                                lenprodterm.append(lenmon[formon])
                            nowlen = cntmon - 1
                            wasscnd = wasscnd + 1
                            skipflag = 1
                            if wasscnd == predlen:
                                wasfst = wasfst + 1
                                wasscnd = wasfst + 1
                            u = wasfst
                            stopf = 1

                        if z == predlen and stopf == 0 and modes == 1:
                            if u - 1 > wasfst: # был скачок на подобии 1-2 3-4, где 1 и 2 стали 4 и 4, поэтому случай 1 и 3 даже не рассматривался. это стоит вернуть..
                                wasscnd = wasscnd + 1 # как разе переход от 1-2 3-4 к 1-3
                                u = wasfst
                                skipflag = 1
                                if wasscnd == predlen: # в случае последнего монома - например, когда начало подразумевается со старта 1 - max, бы заходим на след. круг и 2 - 3
                                    wasfst = wasfst + 1
                                    wasscnd = wasfst + 1
                                u - wasfst
                                prodterm = []
                                for formon in range (0, cntmon):
                                    prodterm.append(mon[formon])
                                    lenprodterm.append(lenmon[formon])
                                nowlen = cntmon - 1

                if len(bigallprodterms) != prommlen:
                    u = wasfst
                    z = wasfst
        #            gotobeg = 1
                    skipflag = 1
                    prommlen = len(bigallprodterms)
                    continue
                else:
                          
                    prommlen = len(bigallprodterms)
                    
                    prodterm = []
                    for formon in range (0, cntmon):
                        prodterm.append(mon[formon])
                        lenprodterm.append(lenmon[formon])
                    nowlen = cntmon - 1
                    wasscnd = wasscnd + 1
                    skipflag = 1
                    if wasscnd == predlen:
                        wasfst = wasfst + 1
                        wasscnd = wasfst + 1
                    u = wasfst

                    bigallprodterms.append([])
                    for kkk in range(0, len(prodterm)):
                        bigallprodterms[bigallcnt + 1].append(prodterm[kkk])
                    bigalllens.append(nowlen)
                    bigallcnt = bigallcnt + 1
                    bigallcntpred = bigallcnt
                    stopf = 1

                    if wasfst == nowlen - 1:
                        newnumofpols = []
                        [newnumofpols.append(item) for item in t2pols if item not in newnumofpols]
                        #print(newnumofpols)
                        break



    
        
        while (True) and nextloop % 2 == 0:
            prodterm = []
            cntmon = len(mon)
            for formon in range (0, cntmon):
                prodterm.append(mon[formon])
                lenprodterm.append(lenmon[formon])
            newprodscnt = cntmon
            itwas = 0
            wind = 1 # индекс путей
            # один проход
            nowlen = cntmon - 1        
            u = -1
            gotobeg = 0
            # избавление от первоначальных отрицаний
            if firstly == 1:
                otrnowlen = nowlen
                while u < otrnowlen:
                    u = u + 1
                    prodterm0 = prodterm[u]
                    bufprodterm0 = prodterm0
                    cntforneg = -1
                    flagout = 0  # возможно, нужно для синхронизации отрицаний - пока не используется
                    while bufprodterm0 > 0:
                        cntforneg = cntforneg + 1
                        litnow = bufprodterm0 % 10
                        if litnow == 2:
                            prodterm[u] = prodterm[u] - litnow * 10 ** cntforneg
                            lenprodterm[u] = lenprodterm[u] - 1 # так как уменьшается длина - мы вычёркиваем один литерал
                            mon[u] = prodterm[u]
                            lenmon[u] = lenprodterm[u] # так как уменьшается длина - мы вычёркиваем один литерал
                            prodterm.append(prodterm[u] + 10 ** cntforneg)
                            lenprodterm.append(lenprodterm[u] + 1)
                            mon.append(prodterm[u] + 10 ** cntforneg)
                            lenmon.append(lenprodterm[u] + 1)
                            newprodscnt = newprodscnt + 1
                            otrnowlen = otrnowlen + 1
                            flagout = 1
                        bufprodterm0 = bufprodterm0 // 10
                nowlen = otrnowlen # редактиеруем на основании новых длин
                print("after negs remove prodterm = ", prodterm, " nowlen = ", nowlen)
                u = -1
                firstly = 0
                
            while u < nowlen - 1:
                u = u + 1
                if prodterm[u] == 4:
                    continue
                z = u
                while z < nowlen:
                    if gotobeg == 1:
                        gotobeg = 0
                        break
                    z = z + 1
                    if prodterm[u] == 4:
                        break
                    if prodterm[z] == 4:
                        continue
                    prodterm1 = prodterm[u]
                    prodterm2 = prodterm[z]
                    bufprodterm1 = prodterm1
                    bufprodterm2 = prodterm2
                    ravn = 0 # число равных переменных в мономах
                    notravn = 0 # число неравных переменных в мономах
                    newliter = -1
                    newliters = [] # новые литеры в массивах при >= 2 несоответствиях
                    notravnpers = [] # не равные литеры в массивах, чтобы было проще ориентироваться при >= 2 несоотв
                    ex = 1
                    if prodterm1 == 3 and lenprodterm[z] == 1 or prodterm2 == 3 and lenprodterm[u] == 1:
                        ravn = n - 1
                        for i in range (0, n):
                            if bufprodterm1 % 10 == 1 or bufprodterm2 % 10 == 1:
                                newliter = 2
                                notravnper = i
                            elif bufprodterm1 % 10 == 2 or bufprodterm1 % 10 == 2:
                                newliter = 1
                                notravnper = i
                            notravn = 1
                            bufprodterm1 = bufprodterm1 // 10
                            bufprodterm2 = bufprodterm2 // 10
                        ex = 2
                    else:
                        ravnper = []   # массив, отвечающий за равные переменные
                        for rpers in range (0, n):
                            ravnper.append(-1)
                        rpers = 0   
                        
                        for i in range (0, n):
                            if bufprodterm1 % 10 == bufprodterm2 % 10:
                                ravnper[rpers] = i
                                rpers = rpers + 1
                                ravn = ravn + 1
                            else:
                                notravnpers.append(i)
                                notravnper = i
                                if bufprodterm1 % 10 == 0 and bufprodterm2 % 10 == 1 or bufprodterm1 % 10 == 1 and bufprodterm2 % 10 == 0: # новая литера в новом мономе
                                    newliter = 2
                                    newliters.append(2)
                                if bufprodterm1 % 10 == 0 and bufprodterm2 % 10 == 2 or bufprodterm1 % 10 == 2 and bufprodterm2 % 10 == 0:
                                    newliter = 1
                                    newliters.append(1)
                                if bufprodterm1 % 10 == 1 and bufprodterm2 % 10 == 2 or bufprodterm1 % 10 == 2 and bufprodterm2 % 10 == 1:
                                    newliter = 0
                                    newliters.append(0)
                                notravn = notravn + 1
                            bufprodterm1 = bufprodterm1 // 10
                            bufprodterm2 = bufprodterm2 // 10



# ! ЕСЛИ УБРАТЬ НИЖНЕЕ УСЛОВИЕ, ВРЕМЯ РАБОТЫ АЛГОРИТМА ОЧЕНЬ СИЛЬНО УВЕЛИЧИВАЕТСЯ
                    if ravn == n: # 2 одинаковых полинома, значит удаляем равные слагаемые
                        prodterm[z] = 4 # те значения, которые были старыми, стираем, так как они соединены в новое # 4 - символ, что его вовсе нет
                        prodterm[u] = 4
                        lenprodterm[z] = 0
                        lenprodterm[u] = 0
                  
                    
                    if (ravn == n - 1) and nextloop % 2 == 0: # здесь равных литералов на 1 меньше, то есть отличие в 1 литерале и мы можем сокращать
                        if firsttry == 1:
                            ways[cntvars].append(u)
                            ways[cntvars].append(z)
                            wind = wind + 1
                            wind = wind + 1
                        else:
                            for checkt in range (0, cntvars):
                                last = ways[checkt][0] # в нуле будем хранить содержательную информацию
                                if (ways[checkt][last] == z and ways[checkt][last - 1] == u) and wind == last - 1: # последнее условие - что в путях одинаковое число элементов
                                    itwas = 1                           
                                    break # не вносим, продолжаем чтение дальше
                            if itwas == 1:
                                itwas = 0
                                continue
                            else:
                                ways[cntvars].append(u)
                                ways[cntvars].append(z)
                                wind = wind + 1
                                wind = wind + 1
                        if ravn == n - 1:
                            if ex == 1:
                                newprodterm = prodterm1
                            if ex == 2:
                                if prodterm1 == 3:
                                    newprodterm = prodterm2
                                else:
                                    newprodterm = prodterm1
                            for k in range(0, n):
                                if k == notravnper: # отправляем в новый массив с новыми мономами с учётом изменений
                                    newprodterm = newprodterm - ((newprodterm // 10 ** k % 10) * 10 ** k) + (newliter * 10 ** k)
                                    break
                            # ниже добавляем моном в конец списка
                            nowlen = nowlen + 1
                            if newprodscnt < len(prodterm):
                                prodterm[newprodscnt] = newprodterm
                                if newliter == 0:                                
                                    lenprodterm[newprodscnt] = lenprodterm[u] - 1
                                else:
                                    lenprodterm[newprodscnt] = max(lenprodterm[u], lenprodterm[z])
                            else:
                                prodterm.append(newprodterm)
                                if newliter == 0:                                
                                    lenprodterm.append(lenprodterm[u] - 1)
                                else:
                                    lenprodterm.append(max(lenprodterm[u], lenprodterm[z]))
                            newprodscnt = newprodscnt + 1                        
                        prodterm[z] = 4 # те значения, которые были старыми, стираем, так как они соединены в новое # 4 - символ, что его вовсе нет
                        prodterm[u] = 4
                        lenprodterm[z] = 0
                        lenprodterm[u] = 0                                     
                        u = -1
                        z = -1
                        gotobeg = 1

                                  
            for sk in range (0, len(prodterm) - 1):
                if prodterm[sk] == 4:
                    continue
                for jk in range (sk + 1, len(prodterm)):
                    if prodterm[jk] == 4:
                        continue
                    if prodterm[sk] == prodterm[jk]:
                        prodterm[sk] = 4
                        prodterm[jk] = 4
                        lenprodterm[sk] = 0
                        lenprodterm[jk] = 0
                        break
                    

            
            thislen = 0
            thisesop = 0
            #sorting
            sortprodterm = prodterm
            sortprodterm.sort(reverse = True)
            
            for sch in range (0, nowlen + 1):
                if prodterm[sch] != 4:
                    thislen = thislen + 1
                    thisesop = thisesop * 10 ** n + prodterm[sch]
            numoflens.append(thislen)
            numofpols.append(thisesop)
            af.write("thisesop = " + str(thisesop) + " with thislen = " + str(thislen) + '\n')
            cnums = cnums + 1
            if wind == 1: # не было сокращений, конец алгоритма
                break
            else:
                ways[cntvars][0] = wind - 1 # в первый элемент записываем, сколько всего членов в массиве - для простоты
            cntvars = cntvars + 1
            ways.append([])
            ways[cntvars].append(0) # первое значение отвечает за длину/количество, вносим сразу
            if firsttry == 1:
                last = wind # сколько элементов в нашем пути - при x1x2x3 + x1x2 это число равно двум
    #       else: # уже прочитали хотя бы 1 раз
            firsttry = 0 # уже был 1 проход
            wind = 1 # путь строим с нуля
            prodterm = []
            lenprodterm = []

        cntlens = []
        for cnt in range (0, 2 ** (2 * n)):
            cntlens.append(0)
        minpol = pol
        ourminpol = pol
        minlen = cntmon
        firstent = 1
        mod = 1
        if mod == 1:
            numofpols.sort()
            numoflens.sort()
            for ik in range (0, cnums - 1):
                if numofpols[ik] == 4:
                    continue
                for jk in range (ik + 1, cnums):
                    if numofpols[ik] == numofpols[jk]:
                        numofpols[jk] = 4
                        numoflens[jk] = -1

                        
            for ik in range (0, cnums):   # оставим для вывода только 1 из минимальных полиномов  - для наглядности
                if numofpols[ik] != 4 and numoflens[ik] <= allminfulllens:
                    bufpol = numofpols[ik]
                    if  numoflens[ik] < allminfulllens:
                        while bufpol != 0:
                            if bufpol % 10 ** n == 0:
                                print('1', end = '')
                                bufpol = bufpol // 10 ** n   ### был 1000?!
                            else:
                                for il in range (0, n):
                                    if bufpol % 10 == 1:
                                        print('x', end = '')
                                        print(il + 1, end = '')
                                    elif bufpol % 10 == 2:
                                        print('!x', end = '')
                                        print(il + 1, end = '')
                                    bufpol = bufpol // 10
                            if bufpol != 0:
                                print(' + ', end = '')
                        print(' with len =', numoflens[ik])
                    if allminfulllens > numoflens[ik]:
                        allminfulllens = numoflens[ik]
                        allminfullpols = numofpols[ik]
                    break # оставим только 1 вывод'''


        if nextloop % 2 == 1:
            allminpols = []
            cntallminpols = 0
        for alllens in range (0, cnums): # cnums - всего esop форм получено из данной при помощи тождеств
            nowlen = numoflens[alllens]
            if nowlen < minlen and nowlen >= 0:                    
                minlen = numoflens[alllens]
                minpol = numofpols[alllens]
                if firstent == 1:
                    ourminpol = minpol
                    firstent = 0
            if nowlen == minlen and nextloop % 2 == 1 and nowlen >= 0:
                minpol = numofpols[alllens]
                for ui in range(0, len(minpolswas)):
                    if minpolswas[ui] != minpol:
                        minlen = numoflens[alllens]
                        minpol = numofpols[alllens]
                        allminpols.append(minpol)
                        if firstent == 1:
                            ourminpol = minpol
                            firstent = 0
                        break
            cntlens[nowlen] = cntlens[nowlen] + 1
        if nextloop % 2 == 1:
            for att in range(0, len(newnumofpols)):
                allminpols.append(newnumofpols[att])
        firstent = 1
        for stats in range (0, cntmon + 1):
            if cntlens[stats] != 0 and firstent == 1:
                if (nextloop % 2 == 1 or cycles == 1) and cntallminpols < len(allminpols):
                    ourminpol = allminpols[cntallminpols]
                    cntallminpols = cntallminpols + 1
                    cycles = 0
                minnlen = stats
                firstent = 0
        minpolswas.append(ourminpol)
        if nextloop % 2 == 0 and nextloop > 0:
            if cntallminpols > len(allminpols):
                nextloop = nextloop + 1
                af.write("############################ nextloop = " + str(nextloop) + '\n')
            else:
                cycles = 1
            if buflastourminpol == ourminpol:
                nextloop = nextloop + 1 # зацикленность - все минимальные полиномы проверены
                af.write("############################ nextloop = " + str(nextloop) + '\n')
            else:
                buflastourminpol = ourminpol
                
        else:
            nextloop = nextloop + 1
            af.write("############################ nextloop = " + str(nextloop) + '\n')
        mon = []
        lenmon = []
        pol = ourminpol
        lenpol = 0
        bufpol = pol
        buffpol = pol
        while buffpol != 0:
            monpol = buffpol % 10 ** n
            buffpol = buffpol // 10 ** n
            mon.append(monpol)
            lenmn = 0
            while monpol != 0:
                if monpol % 10 != 0:
                    lenmn = lenmn + 1
                monpol = monpol // 10    
            lenmon.append(lenmn)
        cntmon = len(mon)
        wasminim = []
        for uu in range(0, len(mon) * n):
            wasminim.append(0)
        mon.reverse()
        lenmon.reverse()
        
        
        # Сортировка по lenmon, вместе с mon
        for ki in range (0, len(lenmon) - 1):
            for kj in range (ki + 1, len(lenmon)):
                if lenmon[kj] < lenmon[ki]:
                    lenmon[ki], lenmon[kj] = lenmon[kj], lenmon[ki]
                    mon[ki], mon[kj] = mon[kj], mon[ki]        

        lenprodterm = []
        prodterm = []
        ways = []
        ways.append([])
        ways[0].append(0) # первое значение отвечает за длину/количество, вносим сразу
        numofpols = []
        numoflens = []
        cnums = 0 # число путей
        firsttry = 1 # составляет путь в первый раз
        cntvars = 0 # отвечает, какой по счёту вариант сокращений
        
        if nextloop == 17:  # отвечает за рассматриваемые тождества
            break
    
    # вычисление булевого вектора, реализуюшего полином
    minmons = []
    bufpol = ourminpol
    j = 0
    while (bufpol != 0):
        minmons.append(bufpol % 10 ** n)
        bufpol = bufpol // 10 ** n       
    tabl = []
    for i in range (0, n):
        tabl.append(0)
    bad = 0
    vect = 0
    fortabl = ''
    polzn = 0
    for i in range (0, 2 ** n):
        for k in range (0, minnlen):
            for j in range (0, n):
                if (minmons[k] // 10 ** j % 10 == 2 and tabl[j] == 1) or (minmons[k] // 10 ** j % 10 == 1 and tabl[j] == 0):
                    bad = 1
            if bad == 1:
                polzn = polzn
            else:
                polzn = (polzn + 1) % 2
            bad = 0
        vect = vect * 10 + polzn
        polzn = 0
        nexti = i + 1
        ue = n - 1
        while ue > -1:
            tabl[ue] = nexti % 2
            ue = ue - 1
            nexti = nexti // 2
    print(vect)
    print("final min is ", ourminpol)
    ##### FINAL OUTPUT #####
    bufpol = allminfullpols
    finlen = allminfulllens
    print("FINAL OUTPUT: ")
    while bufpol != 0:
        #            if bufpol % 10 == 3:
        if bufpol % 10 ** n == 0:
            print('1', end = '')
            bufpol = bufpol // 10 ** n   ### был 1000?!
        else:
            for il in range (0, n):
                if bufpol % 10 == 1:
                    print('x', end = '')
                    print(il + 1, end = '')
                elif bufpol % 10 == 2:
                    print('!x', end = '')
                    print(il + 1, end = '')
                bufpol = bufpol // 10
        if bufpol != 0:
            print(' + ', end = '')
    print(' with len =', finlen)
    af.close()

    print("--- %s seconds --- " % (time.time() - start_time))
        


    
