from random import randint


def deliver_pizzas(fp):
    first = True
    pizzas_list = []
    no_of_pizzas = 0
    n_t2 = 0
    n_t3 = 0
    n_t4 = 0
    for line in fp:
        line = line.split()
        if first:
            no_of_pizzas = int(line[0])                # reads file
            n_t2 = int(line[1])
            n_t3 = int(line[2])
            n_t4 = int(line[3])
            first = False
        else:
            pizza_ingredients = dict()
            pizza_ingredients['length'] = int(line[0])
            pizza_ingredients['ingredients'] = []
            for i in range(1, len(line)):
                pizza_ingredients['ingredients'].append(line[i])
            pizzas_list.append(pizza_ingredients)
    subarray_list = []
    c = 0
    brk = False
    for i in range(len(pizzas_list) - 1):  # finds all different combinations for  teams of 2,and stores the ingredients count between them
        # if brk:
        #     break
        for j in range(i + 1, len(pizzas_list)):
            # i = randint(0, len(pizzas_list) - 1)
            # j = randint(i + 1, len(pizzas_list))
            subarray = dict()
            subarray['indices'] = [i, j]
            subarray['ingredients_count'] = 0
            dupes = 0
            # if c == n_t2 * 2:
            #     brk = True
            #     break
            # c += 1
            for ingredient in range(len(pizzas_list[i]['ingredients'])):
                if pizzas_list[i]['ingredients'][ingredient] in pizzas_list[j]['ingredients']:
                    dupes += 1
            subarray['ingredients_count'] = len(pizzas_list[i]['ingredients']) + len(pizzas_list[j]['ingredients']) - dupes
            subarray_list.append(subarray)
    c = 0
    brk = False
    for i in range(len(pizzas_list) - 2):  # finds all different combinations for  teams of 3,and stores the ingredients count between them
        # if brk:
        #     break
        for j in range(i + 1, len(pizzas_list) - 1):
            for k in range(j + 1, len(pizzas_list)):
                # i = randint(0, len(pizzas_list) - 2)
                # j = randint(i + 1, len(pizzas_list)-1)
                # k = randint(j + 1, len(pizzas_list))
                subarray = dict()
                subarray['indices'] = [i, j, k]
                subarray['ingredients_count'] = 0
                dupes = 0
                # if c == n_t3 * 3:
                #     brk = True
                #     break
                # c += 1
                for ingredient in range(len(pizzas_list[i]['ingredients'])):
                    if pizzas_list[i]['ingredients'][ingredient] in pizzas_list[j]['ingredients']:
                        dupes += 1
                    elif pizzas_list[i]['ingredients'][ingredient] in pizzas_list[k]['ingredients']:
                        dupes += 1
                for ingredient in range(len(pizzas_list[j]['ingredients'])):
                    if pizzas_list[j]['ingredients'][ingredient] in pizzas_list[k]['ingredients']:
                        dupes += 1
                subarray['ingredients_count'] = len(pizzas_list[i]['ingredients']) + len(pizzas_list[j]['ingredients']) + len(pizzas_list[k]['ingredients']) - dupes
                subarray_list.append(subarray)
    c = 0
    brk = False
    for i in range(len(pizzas_list) - 3):  # finds all different combinations for  teams of 4,and stores the ingredients count between them
        # if brk:
        #     break
        for j in range(i + 1, len(pizzas_list) - 2):
            for k in range(j + 1, len(pizzas_list) - 1):
                for l in range(k + 1, len(pizzas_list)):
                    # i = randint(0, len(pizzas_list) - 3)
                    # j = randint(i + 1, len(pizzas_list) - 2)
                    # k = randint(j + 1, len(pizzas_list)-1)
                    # l = randint(k + 1, len(pizzas_list))
                    subarray = dict()
                    subarray['indices'] = [i, j, k, l]
                    subarray['ingredients_count'] = 0
                    dupes = 0
                    # if c == n_t4 * 4:
                    #     brk = True
                    #     break
                    # c += 1
                    for ingredient in range(len(pizzas_list[i]['ingredients'])):  # finds duplicates between pizzas to remove them from ingredients count
                        if pizzas_list[i]['ingredients'][ingredient] in pizzas_list[j]['ingredients']:
                            dupes += 1
                        elif pizzas_list[i]['ingredients'][ingredient] in pizzas_list[k]['ingredients']:
                            dupes += 1
                        elif pizzas_list[i]['ingredients'][ingredient] in pizzas_list[l]['ingredients']:
                            dupes += 1
                    for ingredient in range(len(pizzas_list[j]['ingredients'])):
                        if pizzas_list[j]['ingredients'][ingredient] in pizzas_list[k]['ingredients']:
                            dupes += 1
                        elif pizzas_list[j]['ingredients'][ingredient] in pizzas_list[l]['ingredients']:
                            dupes += 1
                    for ingredient in range(len(pizzas_list[k]['ingredients'])):
                        if pizzas_list[k]['ingredients'][ingredient] in pizzas_list[l]['ingredients']:
                            dupes += 1
                    subarray['ingredients_count'] = len(pizzas_list[i]['ingredients']) + len(pizzas_list[j]['ingredients']) + len(pizzas_list[k]['ingredients']) + len(pizzas_list[l]['ingredients']) - dupes
                    subarray_list.append(subarray)
    subarray_list.sort(reverse=True, key=lambda x: x['ingredients_count'])  # arranges different combinations of pizza descendingly according to ingredients count
    delivered_pizzas = []  # keeps track of delivered pizzas so that they wont be delivered again
    count = 0
    deliveries = ''  # keeps track of details of deliveries made
    delivery_count = 0  # counts the number of deliveries made
    while no_of_pizzas != 0:
        available = True
        team_size = len(subarray_list[count]['indices'])
        for i in range(team_size):
            if (team_size == 2 and n_t2 == 0) or (team_size == 3 and n_t3 == 0) or (team_size == 4 and n_t4 == 0):
                available = False
                break
            if subarray_list[count]['indices'][
                i] in delivered_pizzas or no_of_pizzas - team_size < 2 and no_of_pizzas - team_size != 0:
                available = False
                break
        if available:
            if team_size == 2:
                n_t2 -= 1
            if team_size == 3:
                n_t3 -= 1
            if team_size == 4:
                n_t4 -= 1
            delivery_count += 1
            pizzas = ''
            for i in range(team_size):
                delivered_pizzas.append(subarray_list[count]['indices'][i])
                if i == team_size - 1:
                    pizzas += str(subarray_list[count]['indices'][i])
                else:
                    pizzas += str(subarray_list[count]['indices'][i]) + ' '
            no_of_pizzas -= team_size
            deliveries += f"{team_size} {pizzas}\n"
        if count == len(subarray_list) - 1:
            break
        count += 1
    output_fp = open(fp.name + '_output.txt', 'w')
    deliveries = deliveries[:-1]
    output_fp.write(f'{delivery_count}\n')
    output_fp.write(deliveries)


fps = []
fps.append(open('a_example'))
# fps.append(open('b_little_bit_of_everything.in'))
# fps.append(open('c_many_ingredients.in'))
# fps.append(open('d_many_pizzas.in'))
# fps.append(open('e_many_teams.in'))
for fp in fps:
    deliver_pizzas(fp)
