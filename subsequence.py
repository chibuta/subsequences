def sub_seq(seq,sub):
    m = len(seq)+1
    n = len(sub)+1
    F = [[0 for k in range(m)] for u in range (n)]
    F[0] = [1] * m

    for row in range(n-1):
        for col in range(m-1):
         if sub[row]==seq[col]:
             F[row+1][col+1] = (F[row+1][col] + F[row][col])%100000
         else:
             F[row+1][col+1] = F[row+1][col]

    return F[n-1][m-1]

seq='AGTATCCTGTA'
sub='AT'



a= sub_seq(seq,sub)
print(a)