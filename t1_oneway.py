from random import randint

n = 4
everypols = 30
cntallpols = 0
inputpols = []
ff1 = open('pols.txt', 'r') # полиномы представлены в виде, например 102201011 - x1x2 + x1!x3 + !x1x3
for line in ff1:
    inputpols.append(int(line))
print(inputpols)
ff1.close()
counterall = 0

outputs = []
outputs.append([])
for sss in range (0, 10): # 10 - имеется ввиду максимальная длина из введённых
    for jjj in range (0, 10): # 10 - имеется ввиду максимальная длина из введённых
        outputs[sss].append(0) # первое значение отвечает за длину/количество, вносим сразу
    outputs.append([])

while True:

    if cntallpols == everypols:
        break
    pol = inputpols[cntallpols]
    firstlen = len(str(pol)) // n
    if len(str(pol)) % n != 0:
        firstlen = firstlen + 1

    
    cntallpols = cntallpols + 1
    if cntallpols > everypols:
        break
    mon = []
    lenmon = []
    lenpol = 0
    firstpol = pol
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
    
    # Сортировка по lenmon, вместе с mon
    for ki in range (0, len(lenmon) - 1):
        for kj in range (ki + 1, len(lenmon)):
            if lenmon[kj] < lenmon[ki]:
                lenmon[ki], lenmon[kj] = lenmon[kj], lenmon[ki]
                mon[ki], mon[kj] = mon[kj], mon[ki]
    print(mon)
    print(lenmon)        

    lenprodterm = []
    prodterm = []
    firstly = 1
    
    if 1 == 1:

        while (True):
            prodterm = []
            cntmon = len(mon)
            for formon in range (0, cntmon):
                prodterm.append(mon[formon])
                lenprodterm.append(lenmon[formon])
            newprodscnt = cntmon
            itwas = 0
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
                    flagout = 0
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
               

                    if ravn == n - 1:
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
            finlen = thislen
            finpol = thisesop
            break
        print("final min is ", finpol, " with finlen = ", finlen, " and firstpol = ", firstpol, " and firstlen = ", firstlen)
        outputs[firstlen][finlen] += 1

for jjj in range(len(outputs)):
    print("firstlen = ", jjj, " and finlens = ", outputs[jjj])






































