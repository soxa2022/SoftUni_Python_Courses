lst_population = [int(num) for num in input().split(", ")]
min_wealth = int(input())
for i in range(len(lst_population)):
    if sum(lst_population) // len(lst_population) < min_wealth:
        print("No equal distribution possible")
        break
    index = lst_population.index(max(lst_population))
    if lst_population[i] < min_wealth:
        social_distance = min_wealth - lst_population[i]
        lst_population[index] -= social_distance
        lst_population[i] = min_wealth
else:
    print(lst_population)

