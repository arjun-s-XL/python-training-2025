import json

# with open('emp.json','r') as f:
#     data=json.load(f)
#     print(data)
#     json.dump(data,) 
# json_str='{"name":"jan","dept":"it","dept_id":"3"}'
# data=json.loads(json_str)
# json_out=json.dumps(data)
# print(json_out)


# import json
# def load_json(filename):
#     with open(filename,'r') as f:
#         return json.load(f)
# def filter_by_dept(data,department):
#     filtered=[emp for emp in data if emp.get("department")==department]
#     return  filtered
# db=load_json('emp.json')
# print(db)
# filtered_emp=filter_by_dept(db,'HR')
# print(filtered_emp)



# def average_salary(data):
#     sal=[emp.get('salary') for emp in data]
#     avg=sum(sal)/len(data)
#     return avg
# db=load_jason('emp.json')
# print(average_salary(db))

def assign_level(data):
    for emp in data:
        salary=emp.get('salary',0)
        emp['level']='senior' if salary>100000 else 'mid'


def save_jason(data,filename):
    with open(filename,'w') as f:
        json.dump(data,f)

