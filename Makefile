deps: requirements.txt
	@echo "Installing Dependecies"
	pip install -r requirements.txt

build:
	@echo "Compiling the software"
	python -m PyInstaller --noconfirm --onefile --windowed --add-data "C:\Users\timot\AppData\Local\Programs\Python\Python311\Lib\site-packages\customtkinter;customtkinter/"  ".\fbpos-welcome.py" --icon icon.ico

clean:
	@echo "Cleaning project directory"
	rm -rf build
	rm -rf dist
	rm -rf __pycache__
	rm fbpos-welcome.spec

