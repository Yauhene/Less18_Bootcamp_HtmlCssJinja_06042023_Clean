from flask import Flask, render_template
from LoginForm import Lf

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
        print(f'form.validate_on_submit(): {form.validate_on_submit()}')
        print(f' form.is_submitted(): { form.is_submitted()}')
        print(f'form.validate(): {form.validate()}')
        print(form.name.data, form.password.data)

    return render_template('register.html', title='Регистрация', form=form) #если кнопка не будет нажата мы в любом 
                                #случае отображаем форму register.html с заголовком "Регистрация" и 
                                #'name' в качестве переменной-имени формы

if __name__ == '__main__':
    app.run()