from graphics import *

def main():
    win = GraphWin("Celsius Converter", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)
    
    Text(Point(1,3), "Celsius Temp").draw(win)
    Text(Point(1,1), "Fahrenheit Temp").draw(win)
    inputText = Entry(Point(2.25, 3), 5)
    inputText.setText("0.0")
    inputText.draw(win)
    outputText = Text(Point(2.25, 1),"")
    outputText.draw(win)
    button = Text(Point(1.5, 2), "Convert It")
    button.draw(win)
    Rectangle(Point(1, 1.5), Point (2, 2.5)).draw(win)
    
    win.getMouse()
    
    celsius = float(inputText.getText())
    fahrenheit = 9/5 * celsius + 32
    outputText.setText(round(fahrenheit,2))
    button.setText("Quit")
    win.getMouse()
    win.close()
    
main()    
       