length = int(input("enter the lenght of the sequenve that you want"))

if lenght <= 0:
    return []
    
recaman_sequence = [0]

for k in range(1,lenght):
    term_previous = recaman_sequence [-1]
    term_next = term_previous - k
    
    if term_next > 0 and term_next not in recaman_sequence:
        recaman_sequence.append(term_next)
        
    else:
        recaman_sequence.append(term_previous + k)
return recaman_sequence

print(recaman_sequence)