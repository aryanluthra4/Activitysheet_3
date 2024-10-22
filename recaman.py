length = int(input("enter the lenght of the sequence that you want = "))
recaman_sequence = [0]

if length > 0:
    
    for k in range(1,length):
        term_previous = recaman_sequence [-1]
        term_next = term_previous - k
    
        if term_next > 0 and term_next not in recaman_sequence:
            recaman_sequence.append(term_next)
        
        else:
            recaman_sequence.append(term_previous + k)


else:
    recaman_sequence = []

print(recaman_sequence)
