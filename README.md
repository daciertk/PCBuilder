# BuilderPC Builder

PC Builder is a project similar to the popular pcpartpicker.com. PCBuilder allows the user to select from a number of pc parts to build their own PC.

The project is in its early stage, and currently only has functionality to add a CPU and Motherboard to the user’s build. Future features include more part options, compatibility checking and a more intuitive User Interface. 

#Running:  
The program connects to a local mysql database, and uses the Flask and Jinja framework to deploy the site. The program requires Flask and mysql-connector-python to be installed 

pip install Flask  
pip install mysql-connecter-python

The program can be run using

Flask –app app run


Source for data used https://www.kaggle.com/datasets/warcoder/pc-parts
