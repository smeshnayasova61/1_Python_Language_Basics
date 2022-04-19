# 2. Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя: имя, фамилия,
# год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def intro(**data):
    print("Data type of argument: ",type(data))
    for key, value in data.items():
        print("{} is {}".format(key, value))
intro(Firstname="John", Surname="Wood", Email="johnwood@nomail.com", Country="Wakanda", Year_birthday=1995, Phone=9876543210)

print('*'*100)

def personal_info(name, surname, birthday, city, email, phone_number):
    return f"Name - {name}; Surname - {surname}; Birthday - {birthday}; City - {city}; Email - {email}; Phone_number - {phone_number}"
print(personal_info(name='Sova', surname='Smeshnaya', birthday='10.10.1999', city='Moscow', email='sova_smeshnaya@yandex.ru',
                    phone_number='81234567890'))


