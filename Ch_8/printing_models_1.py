import printing_functions as p

import имя_модуля
from имя_модуля import имя_функции
from имя_модуля import имя_функции as псевдоним
import имя_модуля as псевдоним
from имя_модуля import *

unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
p.print_models(unprinted_designs[:], completed_models)
p.show_completed_models(completed_models)
