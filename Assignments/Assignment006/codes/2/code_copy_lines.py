def copy_lines(input_file,output_file,i=0):
    import os
    input_file = os.path.join(folder,input_file)
    output_file = os.path.join(folder,output_file)
    with open(input_file) as f:
        with open(output_file,"w") as o:
            lineno = 1
            for line in f:
                if(lineno==i+1):
                    continue
                lineno += 1
                o.write(line)
    
    
