users = [
  {'username': 'Даша', 'posts': 25},
  {'username': 'Валера', 'posts': 10},
  {'username': 'Ибрагим', 'posts': 56},
]

print(min(users, key=lambda x: -x['username']))