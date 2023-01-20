def create_combinations(items, k):
  if k == 0:
    return [ [] ]
  if k > len(items):
    return []
  
  first = items[0]
  # print("items", items, "k--", k)
  partial_combos = create_combinations(items[1:], k-1)
  # print("partial_combos", partial_combos)
  with_first = []
  for partial in partial_combos:
    with_first.append([first, *partial])
  # print("come here", with_first, )
  # print("k", k, "array,", items[1:])
  without_first = create_combinations(items[1:], k)
  # print("without_first~~~~", without_first)
  return with_first + without_first


# print(create_combinations(["q", "r", "s", "t"], 2))

create_combinations(["a", "b", "c"], 2)