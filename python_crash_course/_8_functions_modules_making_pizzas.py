import _8_functions_modules_pizza as pizza
# Alternatively we can write:
from _8_functions_modules_pizza import make_pizza
# Or to give the function name an alias
from _8_functions_modules_pizza import make_pizza as mp

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'peppers', 'cheese')
make_pizza(12, 'sausage')
mp(16, 'onion', 'celery')

# The second import statement above would then mean we would not need to prefix
# the function call with the module name or alias