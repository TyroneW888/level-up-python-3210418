def get_prime(num):
  prime_list = [2]
  for i in range(3,num):
    is_prime = True
    for j in prime_list:
      if i % j ==0:
        is_prime = False
    if is_prime:
      prime_list.append(i)
  return prime_list


def get_prime_factor(num):
  prime_list = get_prime(num)
  prime_factor_list = []
  now_value = num
  for factor in prime_list:
    while now_value % factor ==0:
      prime_factor_list.append(factor)
      now_value = now_value / factor
  
  
  return prime_factor_list


def get_prime_factor_2(num):
  factor_list = []
  now_value = num
  factor = 2
  while factor < now_value:
    if now_value % factor ==0:
      factor_list.append(factor)
      now_value = now_value / factor
    else:
      factor +=1
  factor_list.append(factor)
  return factor_list
  


  


print(get_prime_factor_2(630))