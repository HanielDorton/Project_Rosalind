question = ''

reversed = question[::-1]





def reverse(strand):
    answer= []
    comp = {'A': 'T', 'T':'A', 'C':'G', 'G':'C', 'X':'Y'}
    reversed = strand[::-1]
    for a in reversed:
        answer.append(comp[a])
    return(''.join(answer))
    
