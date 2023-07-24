def get_cats_with_hats(num_cats, num_rounds):
    cats = [False] * num_cats

    for round_number in range(1, num_rounds + 1):
        for i in range(round_number, num_cats + 1, round_number):
            cats[i - 1] = not cats[i - 1]

    cats_with_hats = [i + 1 for i, has_hat in enumerate(cats) if has_hat]
    return cats_with_hats


num_cats = 100
num_rounds = 100

cats_with_hats_at_end = get_cats_with_hats(num_cats, num_rounds)
print("Cats with hats at the end:", cats_with_hats_at_end)
