def Lag_difn2(x,a,b):
    sum = 0

    for j in range(len(a)):
        sum_1=0

        for l in range(len(a)):
            if l==j:
                continue
            sum_2=0
            for w in range(len(a)):
                if w==j or w==l:
                    continue
                l_diff=1

                for i in range(len(a)):
                    if i==j or i==l or i==w:
                        continue
                    l_diff*= (x-a[i])/(a[j]-a[i])

                sum_2+=l_diff/(a[j]-a[w])
                print(sum_2)

            sum_1+=sum_2/(a[j]-a[w])
        
        sum+=b[j]*sum_1
    
    return sum