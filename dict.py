import json

obj="""{
    "Tamilnadu":"Chennai",
    "kerala":"thiruvanathapuram",
    "Karnathaka":"Bangalore",
    "Andhra pradesh":"Hyderabad",
    "Maharashtra":"mumbai",
    "madhya pradesh":"bhopal"}"""

    
# obj="""{
#     'Tamilnadu':'Chennai',
#     'kerala':'thiruvanathapuram',
#     'Karnathaka':'Bangalore',
#     'Andhra pradesh':'Hyderabad',
#     'Maharashtra':'mumbai',
#     'madhya pradesh':'bhopal'}"""

data=json.loads(obj)
print(data)
print(type(data))

obj=json.dumps(data)
print(obj)
print(type(obj))