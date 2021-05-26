import time
start_time = time.time()

while True:
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
    #print("len ", len(strmaxonbufrev))

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

#
    # здесь начинаем всеобщий цикл - заканчиваем, пока не пройдём весь полином без всяких сокращений.
    nextloop = 0
    minpolswas = []
    buflastourminpol = -1
    af = open('b.txt', 'w')
    firstly = 1 # в первый раз заходим и избавляемся от отрицаний (здесь, только 1 раз)
    while nextloop < 19:

        if nextloop % 2 == 1:
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
                            #modess = 1

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
                            prodterm[z] = 4 # те значения, которые были старыми, стираем, так как они соединены в новое # 4 - символ, что его вовсе нет
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

                    bigallprodterms.append([])  ###
                    for kkk in range(0, len(prodterm)):
                        bigallprodterms[bigallcnt + 1].append(prodterm[kkk])
                    bigalllens.append(nowlen)
                    bigallcnt = bigallcnt + 1
                    bigallcntpred = bigallcnt
                    stopf = 1

                    if wasfst == nowlen - 1:
                        #print("ENDING WITH FIN POLS ", t2pols)
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
                #print("here now prodterm = ", prodterm)
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
                    #if prodterm1 == 3 and lenprodterm[z] == 1 or prodterm2 == 3 and lenprodterm[u] == 1 or prodterm1 == 0 and lenprodterm[z] == 0 or prodterm2 == 0 and lenprodterm[u] == 0:
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
               #     print("prodterm[u] = ", prodterm[u], "prodterm[z] = ", prodterm[z], " ravn = ", ravn)



#ЕСЛИ УБРАТЬ НИЖНЕЕ УСЛОВИЕ, ВРЕМЯ РАБОТЫ АЛГОРИТМА ОЧЕНЬ СИЛЬНО УВЕЛИЧИВАЕТСЯ
                    if ravn == n
                        prodterm[z] = 4 # те значения, которые были старыми, стираем, так как они соединены в новое # 4 - символ, что его вовсе нет
                        prodterm[u] = 4
                        lenprodterm[z] = 0
                        lenprodterm[u] = 0
                  
                    
                    if (ravn == n - 1) and nextloop % 2 == 0:
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
                                    break
                            if itwas == 1:
                                itwas = 0
                                continue
                            else:
                            # ЕСЛИ МЫ ПОНЯЛИ, ЧТО ПУТЬ УНИКАЛЕН - ПРОДОЛЖАЕМ ВНОСИТЬ
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
                  #      print("ok now prodterm is = ", prodterm)
                        lenprodterm[z] = 0
                        lenprodterm[u] = 0                                     
                         # в этом случае - добавляем в конец, и чтобы не упустить возможность его соединения с другим мономом, который раньше, начинаем с нуля процесс проверки
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
                        #print("clean was with sk = ", sk)
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
            #print("thisesop = ", thisesop," with this len = ", thislen)
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
                        
            for ik in range (0, cnums):
                if numofpols[ik] != 4 and numoflens[ik] <= allminfulllens:
                    bufpol = numofpols[ik]
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
     #       buflastourminpol = ourminpol
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
#        print(tabl)
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

    
