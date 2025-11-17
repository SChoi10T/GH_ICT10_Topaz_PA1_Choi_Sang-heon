# Drill 2
from pyscript import display # pyright: ignore[reportMissingImports]

# Students in Clubs
Glee_Club = {'Jalainie', 'Carl', 'Skyler', 'Sang-heon'}
Commarts_Club = {'AJ', 'Shino', 'Carl', 'Miguel'}

display(f'Glee Club: {Glee_Club}', target='output')
display(f'Commarts Club: {Commarts_Club}', target='output')

display(Glee_Club & Commarts_Club, target='output') # Students who belong to both clubs: Intersection
display(Glee_Club - Commarts_Club, target='output') # Students only in Glee: Difference
display(Commarts_Club - Glee_Club, target='output') # Students only in Commarts: Difference, but switched Commarts Club as the first
display(Glee_Club ^ Commarts_Club, target='output') # Students who are in exactly one club: Exclusive Or