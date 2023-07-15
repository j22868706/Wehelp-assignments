def calculate_sum_of_bonus(data):
    exchange_rate = 30
    weight_bonus = []
    set_weight = []
    

    dict_performance = {"above average" : 2,
                       "average" : 1,
                       "below average:" : 0}
    dict_role = {"CEO" : 2,
                 "Engineer" : 1,
                 "Sales": 1}


    for item in data:
        for index in range(len(data["employees"])):
            performance_level = data["employees"][index]["performance"]
            role = data["employees"][index]["role"]
            salary = data[item][index]['salary']
        
            if isinstance(salary, str):
                 if "USD" in salary:
                     salary_value = int(salary.replace("USD", ""))
                     salary_usd = salary_value * exchange_rate
                     salary = salary_usd

                 else:
                    salary = int(salary.replace(",",""))        

            performance_factor = dict_performance.get(performance_level, 0)
            role_factor = dict_role.get(role, 0)           
            base = salary * (role_factor + performance_factor)
            set_weight.append(base)

    sum_set_weight = sum(set_weight)
    weight_value = 10000 / sum_set_weight
    
    for weight in set_weight:
        bonus = round(weight * weight_value, 0)
        print(bonus)
        weight_bonus.append(bonus)
        sum_bonus = sum(weight_bonus)



    print(sum_bonus)



calculate_sum_of_bonus({
"employees":[
{
"name":"John",
"salary":"1000USD",
"performance":"above average",
"role":"Engineer"
},
{
"name":"Bob",
"salary":60000,
"performance":"average",
"role":"CEO"
},
{
"name":"Jenny",
"salary":"50,000",
"performance":"below average",
"role":"Sales"
}
]
}) # call calculate_sum_of_bonus function