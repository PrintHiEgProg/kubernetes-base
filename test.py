import random 
path = 'test'
api_box = ['http://localhost:8080/' , 'http://localhost:8081/' , 'http://localhost:8082/']
api = f'{api_box[random.randint(0 , len(api_box)-1)]}{path}'
print(api)
