#!C:/Users/treym/AppData/Local/Microsoft/WindowsApps/python3.10.exe
print("Content-Type: text/html\n")

#!C:\Program Files\WindowsApps\C:\Program Files\WindowsApps\PythonSoftwareFoundation.Python.3.10_3.10.752.0_x64__qbz5n2kfra8p0\python3.10.exe
# Import modules for CGI handling
import cgi;
import cgitb; cgitb.enable()
form = cgi.FieldStorage()

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')
school_name = form.getvalue('school_name')


print("")
print("<h1>First Name: "+ first_name + "<br></h1>")
print("<h1>Last name: " + last_name + "<br></h1>")
print("<h1>School name:" + school_name +"<br></h1>")

