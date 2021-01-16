def text_count(directory,name,op1='True',op2='True'):
    import os
    file = os.path.join(directory,name)
    waqar = []
    with open(file) as f:
        for line in f:
            if len(line) == 1:
                continue
            waqar.append(line.strip().split(" "))
    khan = []
    for i in waqar:
        summ = 0
        for j in i:
            summ += 1
            khan.append(summ)
    s = 0
    for k in khan:
        s+=1
        
        
        if op1 == True:
            kashif = []
            with open(file) as f:
                for line in f:
                    kashif.append(line.strip().split(" "))

                khan2 = []
            for i in kashif:
                s = 0
                for j in i:
                    if j.islower() == True:
                        s+=1
                khan2.append(s)
            summ2 = 0
            for i in khan2:
                summ2 += i
            return summ2
        
        if op2 == True:
            khan3 = []
            with open(file) as f:
                for line in f:
                    for word in line:
                        khan3.append(word)
            summ3 = 0
            for i in khan3:
                summ3 += 1
            return summ3

    return s
        
