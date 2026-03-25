'''
Znaleźć takie liczby A[i], A[j], ze po posortowaniu były by obok siebie, 
ale |A[i] - A[j]| jest maksymalna.
'''

def divide(tab):
    n = len(tab)
    max_val = max(tab)
    min_val = min(tab)

    bucket_size = (max_val-min_val)/(n)

    buckets_min = [float('inf')]*(n+1)
    buckets_max = [-float('inf')]*(n+1)

    for el in tab:
        if el ==max_val:
            ind = n
        else:
            ind = (el - min_val)//bucket_size

        buckets_max[ind] = max(buckets_max[ind], el)
        buckets_min[ind] = min(buckets_min[ind], el)


    max_dis = 0
    last_max = buckets_max[0]

    for i in range(1, n+1):
        if buckets_min == float('inf'):
            continue
        max_dis = max(max_dis, buckets_min[i]-last_max)
        last_max = buckets_max[i]