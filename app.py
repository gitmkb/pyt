import sys
print('*' * 5, end='\t')
print('Hello World', ' How are you?', sep='!', \
      end='\t', file=sys.stdout, flush=False)
print('*' * 5)
print('...The End')
x = 25+35
