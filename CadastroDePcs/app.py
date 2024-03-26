from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configurações do MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'cadastro'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        start_date = request.form['start_date']
        end_date = request.form['end_date']
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM computers WHERE data_chegada BETWEEN %s AND %s", (start_date, end_date))
        computers = cursor.fetchall()
        cursor.close()
        return render_template('index.html', computers=computers)
    else:
        # Consulta os computadores no banco de dados
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM computers")
        computers = cursor.fetchall()
        cursor.close()
        return render_template('index.html', computers=computers)

@app.route('/search_by_date', methods=['POST'])
def search_by_date():
    start_date = request.form['start_date']
    end_date = request.form['end_date']
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM computers WHERE data_chegada BETWEEN %s AND %s", (start_date, end_date))
    computers = cursor.fetchall()
    cursor.close()
    return render_template('index.html', computers=computers)

@app.route('/edit/<int:computer_id>', methods=['GET', 'POST'])
def edit_computer(computer_id):
    if request.method == 'GET':
        # Lógica para obter os detalhes do computador com o ID fornecido
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT * FROM computers WHERE id = %s", (computer_id,))
        computer = cursor.fetchone()
        cursor.close()
        return render_template('edit.html', computer=computer)  # Renderiza o template edit.html com os detalhes do computador
    else:
        # Lógica para atualizar os detalhes do computador
        patrimonio = request.form['patrimonio']
        funcionario = request.form['funcionario']
        departamento = request.form['departamento']
        data_chegada = request.form['data_chegada']
        problema = request.form['problema']
        data_saida = request.form['data_saida']
        marca = request.form['marca']
        reparo_realizado = request.form['reparo_realizado']

        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE computers SET patrimonio=%s, funcionario=%s, departamento=%s, data_chegada=%s, problema=%s, data_saida=%s, marca=%s, reparo_realizado=%s WHERE id=%s",
                       (patrimonio, funcionario, departamento, data_chegada, problema, data_saida, marca, reparo_realizado, computer_id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))

@app.route('/add', methods=['GET', 'POST'])
def add_computer():
    if request.method == 'POST':
        patrimonio = request.form['patrimonio']
        funcionario = request.form['funcionario']
        departamento = request.form['departamento']
        data_chegada = request.form['data_chegada']
        problema = request.form['problema']
        data_saida = request.form['data_saida']
        marca = request.form['marca']
        reparo_realizado = request.form['reparo_realizado']

        cursor = mysql.connection.cursor()
        cursor.execute("INSERT INTO computers (patrimonio, funcionario, departamento, data_chegada, problema, data_saida, marca, reparo_realizado) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
                       (patrimonio, funcionario, departamento, data_chegada, problema, data_saida, marca, reparo_realizado))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)
