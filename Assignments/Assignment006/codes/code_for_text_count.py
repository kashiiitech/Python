def text_count(directory,name):
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
    return s
        
