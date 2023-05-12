from flask import Flask, render_template
from LoginForm import Lf
from AuthForm import AuthF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hello hello hello hello hello world' 

@app.route('/')
#@app.route('/index')
def main():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def reg():
    form = Lf()
    
    #print(form.name.data, form.password.data)
    if form.validate_on_submit(): #функция, обрабатывающая нажатие кнопки "Зарегистрироваться"
        #pass #слово-заглушка, позволяет вначале не прописывать никаких действий в блоке if
        # print(f'form.validate_on_submit(): {form.validate_on_submit()}')
        # print(f' form.is_submitted(): { form.is_submitted()}')
        # print(f'form.validate(): {form.validate()}')
        if form.password_again.data != form.password.data:
            return render_template('register.html', title='Регистрация', form=form,
                                   message="Пароли не совпадают!!!")
        
        with open('file.txt', 'a', encoding='utf-8') as file:
            file.write(f'{form.name.data};{form.email.data};{form.password.data};\n')

        return render_template('register.html', message="Регистрация прошла успешно")

    return render_template('register.html', title='Регистрация', form=form) #если кнопка не будет нажата мы в любом 
                                #случае отображаем форму register.html с заголовком "Регистрация" и 
                                #'name' в качестве переменной-имени формы

@app.route('/log', methods=['GET', 'POST'])
def log():
    form = AuthF()
    if form.validate_on_submit():
        with open('file.txt', 'r', encoding='utf-8') as file:
            data = ' '.join(file.readlines()) # все строки в файле соединятся в одну строчку через пробел
            print(f'data = {data}')
        if form.email.data not in data: #если такого емейла нет в файле
            return render_template('login.html', form=form, message='Вы не зарегистрированы')
        else:
            #print('data.split =', data.split())
            for i in data.split(): # вновь разделяем строчки по пробелу
                #print('поехали....')
                print(i)
                
                if form.email.data in i:
                    #print('i.split(";")[-1] = ', i.split(";")[-1], '****', form.password.data)
                    #print(form.password.data)
                    #if i.split(';')[-1][:-2] == form.password.data:
                    print(i.split(';')[-1])
                    if i.split(';')[-1] == form.password.data:
                    # пароль - последнее значение в строчке, т.е. [-1],
                    # а срез последнего значения [:-2] исключает финальные "\n" в строке
                    # это же можно было бы записать так:
                    # if i.split(';')[-1] == form.password.data + '\n':
                    
                        return render_template('login.html', message='Вы успешно авторизовались')


    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run()