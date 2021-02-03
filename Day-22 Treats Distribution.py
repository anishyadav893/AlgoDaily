def treats_distribution(snacks):
    empty = list()
    
    for i in snacks:
        if i not in empty:
          empty.append(i)
          
    if len(empty) >= len(snacks) / 2:
      return len(snacks) / 2
    else:
      return len(empty)