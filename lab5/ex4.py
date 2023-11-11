#Build an employee hierarchy with a base class Employee. Create subclasses for different types of employees like Manager,
# Engineer, and Salesperson. Each subclass should have attributes like salary and methods related to their roles.
class Employee:
    def __init__(self, name, email, salary, address, id):
        if isinstance(name, str) and isinstance(email, str) and isinstance(salary, (int, float)) and isinstance(address, str) and isinstance(id, int):
            self._name = name
            self._email = email
            self._salary = salary
            self._address = address
            self._id = id

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            return "Invalid type of parameter "
    def get_id(self):
        return  self._id
    def set_salary(self, amount):
        if amount > 0 and isinstance(amount, (int, float)):
            self._salary = amount
        else:
            return "Invalid type of parameter "
    def get_salary(self):
        return self._salary



class Manager(Employee):
    def __init__(self, name, email, salary, address, id, department, subordinates, number_sub):
        super().__init__(name, email, salary, address, id)
        if isinstance(department, str) and isinstance(subordinates, (list, set)) and isinstance(number_sub, int):
            self._department = department
            self._subordinates = subordinates.copy()
            self._number_sub = number_sub
    def give_task(self, task, employee):
        if isinstance(employee, Engineer) and employee in self._subordinates:
            employee.add_task(task)
        else:
            return "Something wrong"
    def find_best_engineer(self):
        scores = []
        for employee in self._subordinates:
            if isinstance(employee, Engineer):
                scores.append((employee.get_id(), employee.score()))
        sorted_scores = list(sorted(scores, key=lambda item : item[1], reverse=True))

        best_engineer_id = sorted_scores[0][0]
        return best_engineer_id
    def increase_salary(self, employee, amount):
        if isinstance(employee, Engineer) and employee in self._subordinates:
            employee.set_salary(employee.get_salary() + amount)
        else:
            return "Something wrong"



class Engineer(Employee):
    def __init__(self, name, email, salary, address, id, programming_language, years_experience, evaluation=None, tasks=None):
        super().__init__(name, email, salary, address, id)
        if isinstance(programming_language, str) and isinstance(years_experience, int):
            self._programming_language = programming_language
            self._years_experience = years_experience
            self._evaluation = evaluation if evaluation else []
            self._tasks = tasks if tasks else []
    def score(self):
        result = 0
        for grade in self._evaluation:
            result += grade
        return result
    def add_grade_to_evaluation(self, grade):
        if isinstance(grade, int) and grade > 0 and grade < 11:
            self._evaluation.append(grade)
        else:
            return "Something wrong"
    def add_task(self, task):
        if isinstance(task, str):
          self._tasks.append(task)
        else:
            return "Something wrong"


class SalesPerson(Employee):
    def __init__(self, name, email, salary, address, id, num_sales, target_num_sales, commission_rate, products=None):
        super().__init__(name, email, salary, address, id)
        if isinstance(num_sales, int) and isinstance( target_num_sales, int) and isinstance(commission_rate, float):
            self._num_sales = num_sales
            self._target_num_sales = target_num_sales
            self._commission_rate = commission_rate
            self._products = products if products else {}

    def calculate_commission(self):
        return self._commission_rate * self._num_sales

    def check_target(self):
        if self._num_sales < self._target_num_sales:
            return False
        return True

    def add_product(self, name, price, quantity):
        if isinstance(name, str) and isinstance(price, (float, int)):
            self._products[name] = [price, quantity]

    def take_command(self, command):
        total_sum = 0
        for tpl in command:
            how_many = tpl[1]
            product_name = tpl[0]
            if product_name in self._products:
                if how_many <= self._products[product_name][1]:
                    total_sum += self._products[product_name][0] *  how_many
        return total_sum

if __name__ == '__main__':
    eng = [Engineer("Ana", "ana123@gmail.com", 2500, "Iasi", 39, "Java", 4, [8, 9, 7.5]), Engineer("Bob", "bob123@gmail.com", 3500, "UK", 6, "Python", 8, [9, 10, 10])]
    manager = Manager("Man", "m123@gmail.com", 5500, "Bucuresti", 12, "SoftwareDevelopment", eng, 2)
    best = manager.find_best_engineer()
    print(best)
    manager.increase_salary(eng[1], 500)
    print(eng[1].get_salary())




