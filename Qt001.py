from PyQt4.QtCore import QObject, SIGNAL

class A:
    # метод, который будем использовать в качестве слота:
    def main_slot(self,text):
        print ("Объектом класса A получено сообщение с текстом:",text)

class B(QObject):
    def send_signal(self,text):
        print ("Из объекта класса B отправляется сообщение с текстом:",text)
        self.emit( SIGNAL("main_signal(PyQt_PyObject)"), text )
        
if __name__=="__main__":
    a = A()
    b = B()
    # а вот, собственно, и соединение (Источник,Сигнал,СлотПриемника):
    QObject.connect( b, SIGNAL("main_signal(PyQt_PyObject)"), a.main_slot )
    # и теперь пошлем сигнал:
    b.send_signal("Траляля")
