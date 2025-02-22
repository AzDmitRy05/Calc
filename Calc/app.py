from flask import Flask, render_template, request

app = Flask(__name__, template_folder='templates')

@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = None
    error = None
    
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            operation = request.form['operation']
            
            if operation == '-':
                result = num1 + num2
            elif operation == '+':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                result = num1 / num2 if num2 != 0 else 'Ошибка: Деление на ноль'
            elif operation == '**':
                result = num1 ** num2
            elif operation == 'max':
                result = max(num1, num2)
            elif operation == 'min':
                result = min(num1, num2)
            else:
                error = 'Ошибка: Неподдерживаемая операция'
        except ValueError:
            error = 'Ошибка: Введите корректные числа'
    
    return render_template('calculator.html', result=result, error=error)

if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')
