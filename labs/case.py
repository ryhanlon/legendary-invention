"""
>>> which_case('this_test_text')
'snake_case.'

>>> which_case('this_is_snake_case')
'snake_case.'

>>> which_case('ThisIsCamelCase')
'CamelCase.'

### Advanced ###

# >>> snake_to_camel('this_is_snake_case')
# 'ThisIsSnakeCase'


"""


def which_case(case):
     # file_name = case.index('_')

     if '_' in case and case.islower():   # islower() is True or False
         return 'snake_case.'

     elif '_' not in case and not case.islower():
         return 'CamelCase.'


# def which_case(case):
#      file_name = case.find('_')
#
#      if '_' in case:
#          return 'snake_case.'
#
#      elif '_' not in case:
#          return 'CamelCase.'
#


