code = open('mnist.py')
code = code.read()

if 'keras' or 'tensorflow' in code:
  if 'Conv2D' in code:
    print('ok')
  else:
    print('not ok')
    
else:
  print('not ok')
