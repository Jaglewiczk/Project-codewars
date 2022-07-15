def reverse_words(str):
  List = []
  for word in str.split(""):
      List.append(word[::-1])
  return " ".join(List)