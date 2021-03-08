
from tkinter import *

from place import PlaceModel


class Application:
    def __init__(self, master=None):
        self.fonte = ("Verdana", "8")

        self.container1 = Frame(master)
        self.container1["pady"] = 10
        self.container1.pack()
        self.container2 = Frame(master)
        self.container2["padx"] = 20
        self.container2["pady"] = 5
        self.container2.pack()
        self.container3 = Frame(master)
        self.container3["padx"] = 20
        self.container3["pady"] = 5
        self.container3.pack()
        self.container4 = Frame(master)
        self.container4["padx"] = 20
        self.container4["pady"] = 5
        self.container4.pack()
        self.container5 = Frame(master)
        self.container5["padx"] = 20
        self.container5["pady"] = 5
        self.container5.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()

        self.titulo = Label(self.container1, text="Informe os dados :")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()

        self.lblidusuario = Label(self.container2,
                                  text="idLugar:", font=self.fonte, width=10)
        self.lblidusuario.pack(side=LEFT)

        self.txtidlugar = Entry(self.container2)
        self.txtidlugar["width"] = 10
        self.txtidlugar["font"] = self.fonte
        self.txtidlugar.pack(side=LEFT)

        self.btnBuscar = Button(
            self.container2, text="Buscar", font=self.fonte, width=10)
        self.btnBuscar["command"] = self.buscarPlace
        self.btnBuscar.pack(side=RIGHT)

        self.lblnome = Label(self.container3, text="Nome:",
                             font=self.fonte, width=10)
        self.lblnome.pack(side=LEFT)

        self.txtnome = Entry(self.container3)
        self.txtnome["width"] = 25
        self.txtnome["font"] = self.fonte
        self.txtnome.pack(side=LEFT)

        #####
        self.lblendereco = Label(self.container4, text="Endereço:",
                                 font=self.fonte, width=10)
        self.lblendereco.pack(side=LEFT)
        self.txtendereco = Entry(self.container4)
        self.txtendereco["width"] = 25
        self.txtendereco["font"] = self.fonte
        self.txtendereco.pack(side=RIGHT)
        #####

        self.bntInsert = Button(
            self.container8, text="Inserir", font=self.fonte, width=12)
        self.bntInsert["command"] = self.inserirPlace
        self.bntInsert.pack(side=LEFT)

        self.bntAlterar = Button(
            self.container8, text="Alterar", font=self.fonte, width=12)
        self.bntAlterar["command"] = self.alterarPlace
        self.bntAlterar.pack(side=LEFT)

        self.bntExcluir = Button(
            self.container8, text="Excluir", font=self.fonte, width=12)
        self.bntExcluir["command"] = self.excluirPlace
        self.bntExcluir.pack(side=LEFT)

        self.lblmsg = Label(self.container9, text="")
        self.lblmsg["font"] = ("Verdana", "9", "italic")
        self.lblmsg.pack()

    def inserirPlace(self):
        try:
            place = PlaceModel()

            place.nome = self.txtnome.get()
            place.id = self.txtidlugar.get()
            place.endereco = self.txtendereco.get()

            # self.lblmsg["text"] = place.insertPlace(place)
            place.insertPlace(place)

            self.txtnome.delete(0, END)
            self.txtidlugar.delete(0, END)
            self.txtendereco.delete(0, END)

            self.lblmsg["text"] = "Lugar Cadastrado com Sucesso"
        except Exception as e:
            self.lblmsg["text"] = f"error: {e}"

    def alterarPlace(self):
        old_place = PlaceModel()
        new_place = PlaceModel()
        old_place = PlaceModel.find(self.txtidlugar.get())
        new_place.id = old_place.id
        new_place.nome = self.txtnome.get()
        new_place.endereco = self.txtendereco.get()

        old_place.delete()
        new_place.save()

        self.lblmsg["text"] = "Lugar atualizado com Sucesso"

        self.txtidlugar.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)

    def excluirPlace(self):

        old_place = PlaceModel.find(self.txtidlugar.get())

        old_place.delete()

        self.lblmsg["text"] = "Lugar Excluído com Sucesso"

        self.txtidlugar.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0,END)

    def buscarPlace(self):
        place = PlaceModel()
        placeid = self.txtidlugar.get()

        place = place.find(placeid)
        self.lblmsg["text"] = f"Lugar de Nome: {place.nome}"

        self.txtidlugar.delete(0, END)
        self.txtnome.delete(0, END)
        self.txtendereco.delete(0, END)
        self.txtidlugar.insert(INSERT, f"{place.id}")
        self.txtnome.insert(INSERT, f"{place.nome}")
        self.txtendereco.insert(INSERT, f"{place.endereco}")


root = Tk()
Application(root)
root.mainloop()
