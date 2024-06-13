def is_palindrome(something):
  word_list= []
  for word in something:
    if word.isalpha() == True:
      word_list.append(word.lower())
  new_list = word_list[::-1]
  return new_list == word_list

print(is_palindrome('race car'))


