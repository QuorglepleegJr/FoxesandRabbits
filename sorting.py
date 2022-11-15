class BubbleSort:
  def __init__(self, *useless_args):
    raise NotImplementedError("BubbleSort is a factory class to create sorted lists or dictionaries")
  
  def sort(container):
    if isinstance(container, list):
      return BubbleSort.__sortList(container)
    if isinstance(container, dict):
      return BubbleSort.__sortDict(container)
    if isinstance(container, set):
      return BubbleSort.__sortSet(container)
    raise NotImplementedError("Unsupported container for sorting: Must be a set, list, or dict")

  def __sortList(input_list):
    output_list = list(input_list)
    finished = False
    while not finished:
        swap_made = False
        for index in range(len(input_list)-1):
            item1 = output_list[index]
            item2 = output_list[index+1]
            if item2 < item1:
                swap_made = True
                output_list[index] = item2
                output_list[index+1] = item1
        if not swap_made:
            finished = True
    return output_list
  
  def __sortDict(input_dict):
    output_pairs = []
    for element in input_dict:
      output_pairs.append((element, input_dict[element]))
    finished = False
    while not finished:
      swap_made = False
      for index in range(len(input_dict)-1):
        item1 = output_pairs[index]
        item2 = output_pairs[index+1]
        if item2[1] < item1[1]:
          swap_made = True
          output_pairs[index] = item2
          output_pairs[index+1] = item1
      if not swap_made:
        finished = True
    output_list = []
    for item_pair in output_pairs:
      output_list.append(item_pair[0])
    return output_list
  
  def __sortSet(input_set):
    arbitrary_item = next(iter(input_set))
    if isinstance(arbitrary_item, tuple) and len(arbitrary_item) == 2:
      return BubbleSort.__sortPairsSet(input_set)
    raise NotImplementedError("Unsupported set format for BubbleSort")

  def __sortPairsSet(input_set):
    output_pairs = list(input_set)
    finished = False
    while not finished:
      swap_made = False
      for index in range(len(output_pairs)-1):
        item1 = output_pairs[index]
        item2 = output_pairs[index+1]
        if item2[1] < item1[1]:
          swap_made = True
          output_pairs[index] = item2
          output_pairs[index+1] = item1
      if not swap_made:
        finished = True
    return output_pairs