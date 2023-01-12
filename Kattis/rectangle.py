import math

t = int(input())
cases = []
for _ in range(t):
    cases.append(input().strip())

case = 1
for k in cases:
    alien, source, target = k.split()
    base_source = len(source)
    base_target = len(target)
    
    source_numb = list(range(0,len(source),1))
    target_numb = list(range(0,len(target),1))

    value_source = list(alien)
    value_source_decimal= 0
    value_source.reverse()
    power = 0

    for i in value_source:
        value_source_decimal += (base_source**power * (source_numb[list(source).index(i)]))
        power += 1

    target_value = []

    while math.floor(value_source_decimal) != 0:
        target_value.append(list(target)[(math.floor(value_source_decimal) % base_target)])
        value_source_decimal = math.floor(value_source_decimal) / base_target
        
    target_value.reverse()
    print("Case # " + str(case) + ": " + "".join(target_value))
    case += 1

    