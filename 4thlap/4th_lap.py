from flask import Flask

app = Flask(__name__)


#home page 

@app.route('/')
def home():
	return("<html><p>welcome to my photo gallery press the button to see the pic </p><a href = '/first_'>first page </a></html>")

	#art gallery 

@app.route('/first_')
def home():
	return("<html><a href=''></a><a href='/second'>second page</a></html>")

@app.route('/second')
def home():
	return("<html><a href='' ></a><a href='/third'>third page </a><a href='/second'>second page</a></html>")

@app.route('/third')
def home():
	return("<html><a href='' ></a><a href='/'>fourth page</a></html>")



	@app.route('/first_food')
def home():
	return("<html><a href='/home/student/Documents/GitHub/Y2-Summer-Labs/4thlap/download (4).jpeg'></a><a href='/second'>second page</a></html>")

@app.route('/second_food')
def home():
	return("<html><a href='/home/student/Documents/GitHub/Y2-Summer-Labs/4thlap/download (5).jpeg' ></a><a href='/third_food'>third page </a><a href='/second_food'>second page</a></html>")

@app.route('/third_food')
def home():
	return("<html><a href='/home/student/Documents/GitHub/Y2-Summer-Labs/4thlap/ultra-detailed-nebula-abstract-wallpaper-4_1562-749.avif' ></a><a href='/'>fourth page</a></html>")



@app.route('/first_space')
def home():
	return("<html><a href='/home/student/Documents/GitHub/Y2-Summer-Labs/4thlap/download (6).jpeg'></a><a href='/second_space'>second page</a></html>")

@app.route('/second_space')
def home():
	return("<html><a href='/home/student/Documents/GitHub/Y2-Summer-Labs/4thlap/download (7).jpeg' ></a><a href='/third_space'>third page </a><a href='/first_space'>second page</a></html>")

@app.route('/third_space')
def home():
	return("<html><a href='/home/student/Documents/GitHub/Y2-Summer-Labs/4thlap/download (8).jpeg' ></a><a href='/'>fourth page</a></html>")



    
if __name__ == '__main__':
    app.run(debug=True)
