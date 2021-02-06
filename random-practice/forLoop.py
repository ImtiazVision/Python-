name = 'Imtiaz Ahmed'
users = ("Rakeem", "John", "Rojert", "Saiful")
idNumber = 1
dictionary = {
    'fname': 'Iglesius',
    'lname': 'John',
    'income': 100_000
}
for element in name:
    print(element)
    
for i in users:
    print(f"idNum: {idNumber} | Name: {i}")
    idNumber += 1
    
for key, value in dictionary.items():
    print(f'key: {key} value: {value}')