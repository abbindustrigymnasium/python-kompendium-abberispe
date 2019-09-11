import ui
import sys
import time
operationsArray = ["add", "subtract", "divide", "multiply"]

def validateNumbers(num):
    if num.isdigit() == True:
        return int(num)
    else:
        ui.echo("Invalid input")
        return False


def displayMainUI():
    ui.line(False)
    ui.header("Calculator")
    ui.line(False)
    ui.echo("Please select one of these operations:")
    ui.echo("add - Adds two numbers")
    ui.echo("subtract - Subtracts two numbers")
    ui.echo("divide - Divides two numbers")
    ui.echo("multiply - Multiplies two numbers")
    ui.echo("exit - Exits the calculator")

def start(state): # state defines where in the program we would like to start over
    if (state == "main"):
        displayMainUI()
        selectedOperation = ui.prompt("Selection > ")
        makeOperation(selectedOperation)
    if (state == "add"):
        makeOperation(state)
    if (state == "subtract"):
        makeOperation(state)
    if (state == "divide"):
        makeOperation(state)
    if (state == "multiply"):
        makeOperation(state)

def makeOperation(operation):
    try:
        operationIndex = operationsArray.index(operation)
        ui.line(False)
        ui.echo("Please choose two numbers to " + operation + ".")
        a = validateNumbers(ui.prompt("a = "))

        while type(a) == bool and a == False:
            a = validateNumbers(ui.prompt("a = "))

        b = validateNumbers(ui.prompt("b = "))

        while type(b) == bool and b == False:
            b = validateNumbers(ui.prompt("b = "))
        
        ui.line(False)
        if (operation.lower() == "add"):
            ui.echo("Result > " + str(a) + " + " + str(b)+ " = " + str(float(a) + float(b)))
        if (operation.lower() == "subtract"):
            ui.echo("Result > " + str(a) + " - " + str(b) + " = " + str(float(a) - float(b)))
        if (operation.lower() == "divide"):
            ui.echo("Result > " + str(a) + " / " + str(b) + " = " + str(float(a) / float(b)))
        if (operation.lower() == "multiply"):
            ui.echo("Result > " + str(a) + " * " + str(b) + " = " + str(float(a) * float(b)))
        ui.line(False)
        ui.prompt("Press enter to continue")
        ui.line(False)
        start("main")
    except:
        ui.echo("Please select a valid input")
        time.sleep(2)
        start("main")

start("main")