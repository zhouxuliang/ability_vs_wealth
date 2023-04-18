import random
import matplotlib.pyplot as plt
import numpy as np

#agent base model
#人有3个属性能力，财富，位置xy
class Person:
    def __init__(self, ability, wealth, x, y):
        self.ability = ability
        self.wealth = wealth
        self.x = x
        self.y = y

    # 按照 ability 属性值进行排序
    def __lt__(self, other):
        return self.ability < other.ability
#好事    
class Opportunity:
    def __init__(self):
        self.x = random.randint(1, 100)
        self.y = random.randint(1, 100)

#坏事    
class Danger:
    def __init__(self):
        self.x = random.randint(1, 100)
        self.y = random.randint(1, 100)

#agent base model 中的人数
person_num = 1000
#agent base model 中的好事次数，坏事次数
challenge_num = 250

person_list = []
for i in range(person_num):
    # 模拟正态分布，均值为50，标准差为15
    ability = int(random.normalvariate(50, 15))
    # 设置wealth初期值为10
    wealth = 10
    # 设置人的位置为随机
    x = random.randint(1, 100)
    y = random.randint(1, 100)
    person = Person(ability, wealth, x, y)
    person_list.append(person)

# 生成Opportunity 对象，存入列表中
opportunity_list = [Opportunity() for _ in range(challenge_num)]

# 生成Danger 对象，存入列表中
danger_list = [Danger() for _ in range(challenge_num)]

# 对 person_list 按照 ability 属性值进行排序
person_list.sort()

# debug用，可以输出人的情报
'''for i, person in enumerate(person_list[:person_num]):
    print(f"Person {i+1}: ability={person.ability}")
'''

# 绘制 ability 属性的直方图, 应该为正态分布
fig, ax1 = plt.subplots()
ax1.set_xlabel('Person')
ax1.set_ylabel('Ability')
#ax1.plot(np.arange(len(person_list)), [person.ability for person in person_list], color='blue')
ax1.hist([person.ability for person in person_list], bins=100, alpha=0.5, color='blue')
ax1.tick_params(axis='y', labelcolor='blue')
plt.title('Distribution of Ability and Wealth')
fig.tight_layout()

# 绘制agent base model 平面图
plt.figure()
x = [p.x for p in person_list]
y = [p.y for p in person_list]
plt.scatter(x, y, c='black', label='Person')
x = [o.x for o in opportunity_list]
y = [o.y for o in opportunity_list]
plt.scatter(x, y, c='red', label='Opportunity')
x = [o.x for o in danger_list]
y = [o.y for o in danger_list]
plt.scatter(x, y, c='blue', label='Danger')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('2D Scatter Plot of Persons')
plt.show()

# 输出实验开始前的wealth,每个人都为初级值
plt.bar(range(len(person_list)), [p.wealth for p in person_list])
plt.title('Before comparison')
plt.xlabel('Person ID')
plt.ylabel('Wealth')
plt.show()

# 重复80次比较处理
for i in range(80):
    # 创建新的Danger和Opportunity
    danger_list = [Danger() for _ in range(challenge_num)]
    opportunity_list = [Opportunity() for _ in range(challenge_num)]
    
    # 遍历person_list和danger_list，如果有位置相同的，则将person的wealth减半
    for person in person_list:
        for danger in danger_list:
            if person.x == danger.x and person.y == danger.y:
                person.wealth /= 2
                break
    # 设置一个运气值，
    success_rate = random.randint(1, 100)
    # 遍历person_list和opportunity_list，如果有位置相同的，能力和运气的和大于某个值时wealth翻倍
    for person in person_list:
        for opportunity in opportunity_list:
            if person.x == opportunity.x and person.y == opportunity.y:
                if person.ability + success_rate > 70:
                    person.wealth *= 2    

# 输出实验开始后的wealth,观察wealth值得分布
plt.bar(range(len(person_list)), [p.wealth for p in person_list])
plt.title('After comparison')
plt.xlabel('Person ID')
plt.ylabel('Wealth')
plt.show()

