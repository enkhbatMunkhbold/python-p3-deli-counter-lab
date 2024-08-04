def line(data):
  start = 'The line is currently'
  text = []
  if len(data) == 0:
    print(f"{start} empty.")
  else:
    for i in range(len(data)):
      text.append(f"{i + 1}. {data[i]}")
    print(": ".join([start, ' '.join(text)])) 

def take_a_number(data, name):
  data.append(name)
  print(f"Welcome, {name}. You are number {len(data)} in line.")

def now_serving(data):
    if len(data) == 0:
      print("There is nobody waiting to be served!")
    else:
      next_customer = data.pop(0)
      print(f"Currently serving {next_customer}.")
  