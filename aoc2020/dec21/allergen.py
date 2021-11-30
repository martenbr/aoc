from collections import defaultdict

import aocutils


def main(file):
    print("RUNNING", file)
    possible_allergen = defaultdict(set)
    recipies = []
    ingredients_by_allergen = dict()
    for line in aocutils.readlines(file):
        parts = aocutils.multisplit(line, [" (contains ", ")"])
        ingredients = parts[0].split(" ")
        recipies.append(ingredients)
        allergen = parts[1].split(", ")
        for allergen in allergen:
            if allergen not in ingredients_by_allergen:
                ingredients_by_allergen[allergen] = set(ingredients)
            else:
                ingredients_by_allergen[allergen].intersection_update(ingredients)
        for i in ingredients:
            possible_allergen[i].add(i)

    ingredients_with_known_allergen = set()
    for _ in range(10):  # arbitrary limit which was enough
        for ingredient_set in ingredients_by_allergen.values():
            if len(ingredient_set) == 1:
                ingredients_with_known_allergen.update(ingredient_set)
            else:
                ingredient_set.difference_update(ingredients_with_known_allergen)

    safe = 0
    for recipe in recipies:
        for i in recipe:
            if i not in ingredients_with_known_allergen:
                safe += 1
    print("part1", safe)

    d = []
    for allergen, ingredient_set in ingredients_by_allergen.items():
        assert len(ingredient_set) == 1
        i = list(ingredient_set)[0]
        d.append((i, allergen))
    d.sort(key=lambda x: x[1])
    print("part2", ",".join(x[0] for x in d))


if __name__ == '__main__':
    main("example.txt")
    main("input.txt")
