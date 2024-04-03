def read_list(filename: str) -> list[str]:
  with open(filename, "r", encoding="utf-8") as file:
    list_sheet = [line.strip() for line in file]
    
    file_list = [] #En lista med sublists för varje del (frågor/svar)
    temp = []
    for item in list_sheet:
      if item != "":
        temp.append(item)
      else:
        if temp:
          file_list.append(temp)
          temp = []
    if temp:
      file_list.append(temp)
      
  return file_list