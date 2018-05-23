#!/usr/bin/env python
# -*- coding: utf-8 -*-
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.config import Config
from kivy.uix.accordion import Accordion
import time
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
import cv2
import numpy as np
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import FadeTransition
from kivy.properties import StringProperty

import MySQLdb
#cursor = MySQLdb.cursor()
#con = MySQLdb.connect()
#Window.size = (1300,890)
Config.set('graphics', 'width', '1000')
Config.set('graphics', 'height', '670')


class Cargar(Screen):
    pass


class PaginaInicial(Screen):
    pass


class MercanciasCat(Screen):
    pass


class UsuariosCat(Screen):
    pass


class ProveedoresCat(Screen):
    pass


class VentasCat(Screen):
    pass


class InventarioCat(Screen):
    pass


class LabelConfig(Screen):
    def datosImg(self):
        self.parent.nombreMerca = self.ids.ti_nombreM.text

    def total(self):
        total = int(self.ids.ti_cantidad.text) * int(self.ids.ti_precio.text)
        self.ids.ti_total.text = str(total)

    def errorC(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="El precio de venta es menor al mínimo",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint ={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def errorT(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="No hay mercancia suficiente en almacen",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint ={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def errorP(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Uno o más campos estan vacíos",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint ={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def errorL(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Uno o más campos son muy cortos",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def exitoP(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text='Transacción Exitosa',
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Datos Correctos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def validar1(self):
        d1 = self.ids.ti_nombreM.text
        d2 = self.ids.ti_largo.text
        d3 = self.ids.ti_ancho.text
        d4 = self.ids.ti_peso.text
        d5 = self.ids.ti_costo.text
        d6 = self.ids.ti_precioMin.text
        d7 = self.ids.ti_precioOpt.text
        d8 = self.ids.ti_existencias.text
        a1 = (d1, d2, d3, d4, d5, d6, d7, d8)
        al2 = (d2, d3, d4, d5, d6, d7, d8)
        if '' in a1 and (self.ids.bt_insertar1.state == 'down'):
            self.errorP()
        else:
            if '' in al2 and (self.ids.bt_actualizar1.state == 'down'):
                self.errorP()
                self.limpiar1()
            else:
                if (len(self.ids.ti_nombreM.text) < 4
                        or len(self.ids.ti_largo.text) < 2
                        or len(self.ids.ti_ancho.text) < 2
                        or len(self.ids.ti_costo.text) < 3
                        or len(self.ids.ti_precioMin.text) < 3
                        or len(self.ids.ti_precioOpt.text) < 3):
                    self.errorL()
                else:
                    foto = 'LL_{}.png'.format(self.nombreMerca)
                    if (self.ids.bt_insertar1.state == 'down'):
                        sql = ("call insersionMercancia"
                            "(2, 'Fr3', '{0}','{1}','{2}',"
                                "'{3}','{4}','{5}','{6}','{7}','{8}');"
                            .format(self.ids.ti_nombreM.text,
                            self.ids.ti_largo.text,
                            self.ids.ti_ancho.text,
                            self.ids.ti_peso.text,
                            self.ids.ti_costo.text,
                            self.ids.ti_precioOpt.text,
                            self.ids.ti_precioMin.text,
                            self.ids.ti_existencias.text, foto))
                        self.parent.run_query(sql)
                    else:
                        if (self.ids.bt_actualizar1.state == 'down'):
                            sql = ("call actualizarMercancia"
                                "('{0}',2, 'Fr3','{1}','{2}',"
                                    "'{3}','{4}','{5}','{6}','{7}','{8}');"
                                .format(self.ids.ti_nombreM.text,
                                self.ids.ti_largo.text,
                                self.ids.ti_ancho.text,
                                self.ids.ti_peso.text,
                                self.ids.ti_costo.text,
                                self.ids.ti_precioOpt.text,
                                self.ids.ti_precioMin.text,
                                self.ids.ti_existencias.text,
                                foto))
                            self.parent.run_query(sql)
                    self.exitoP()
                    self.limpiar1()

    def borrado1(self):
        sql = "SELECT MERCANCIA.NOMBREP,MERCANCIA.LARGO,MERCANCIA.ANCHO,"
        sql += "MERCANCIA.PESO,MERCANCIA.COSTOPIEZA,MERCANCIA.PRECIOMINIMO,"
        sql += "MERCANCIA.PRECIOOPTIMO,MERCANCIA.EXISTENCIAS,"
        sql += "PROVEEDORES.NOMBREPR,TIPOMERCANCIA.TIPO,MERCANCIA.FOTO "
        sql += "FROM MERCANCIA,PROVEEDORES,TIPOMERCANCIA "
        sql += "WHERE (PROVEEDORES.ID_PROVEEDOR = MERCANCIA.ID_PROVEEDOR) AND"
        sql += "(TIPOMERCANCIA.ID_TIPOMER = MERCANCIA.ID_TIPOMER)"
        sql += " AND NOMBREP='{0}';" .format(self.ids.ti_nombreM.text)
        datos = self.parent.run_query(sql)
        self.ids.ti_largo.text = str(datos[0][1])
        self.ids.ti_largo.text = str(datos[0][2])
        self.ids.ti_ancho.text = str(datos[0][3])
        self.ids.ti_peso.text = str(datos[0][4])
        self.ids.ti_costo.text = str(datos[0][5])
        self.ids.ti_precioOpt.text = str(datos[0][6])
        self.ids.ti_precioMin.text = str(datos[0][7])
        self.ids.ti_existencias.text = str(datos[0][8])
        self.ids.bt_foto.background_normal = str(datos[0][9])
        self.ids.bt_foto.background_disabled_down = str(datos[0][9])
        self.ids.bt_foto.background_disabled = str(datos[0][9])

    def limpiar1(self):
        self.ids.ti_nombreM.text = ''
        self.ids.ti_ancho.text = ''
        self.ids.ti_largo.text = ''
        self.ids.ti_peso.text = ''
        self.ids.ti_costo.text = ''
        self.ids.ti_precioMin.text = ''
        self.ids.ti_precioOpt.text = ''
        self.ids.ti_existencias.text = ''
        self.ids.ti_nombreM.hint_text = "Ingresa Nombre"
        self.ids.ti_largo.hint_text = "Ingresa Largo"
        self.ids.ti_ancho.hint_text = "Ingresa Ancho"
        self.ids.ti_peso.hint_text = "Ingresa Peso"
        self.ids.ti_costo.hint_text = "Ingresa Costo"
        self.ids.ti_precioMin.hint_text = "Ingresa Precio Min"
        self.ids.ti_precioOpt.hint_text = "Ingresa Precio Opt"
        self.ids.ti_existencias.hint_text = "Ingresa Existencias"
        self.ids.bt_insertar1.state = 'normal'
        self.ids.bt_actualizar1.state = 'normal'

    def validar2(self):
        d1 = self.ids.ti_nombreP.text
        d2 = self.ids.ti_direccion.text
        d3 = self.ids.ti_telefono.text
        d4 = self.ids.ti_referencias.text
        a1 = (d1, d2, d3, d4)
        al2 = (d2, d3, d4)

        if '' in a1 and (self.ids.bt_insertar2.state == 'down'):
            self.errorP()
        else:
            if '' in al2 and (self.ids.bt_actualizar2.state == 'down'):
                self.errorP()
                self.limpiar2()
            else:
                if (len(self.ids.ti_nombreP.text) < 4
                    or len(self.ids.ti_direccion.text) < 15
                    or len(self.ids.ti_telefono.text) < 10
                    or len(self.ids.ti_referencias.text) < 10):
                    self.errorL()
                else:
                    if (self.ids.bt_insertar2.state == 'down'):
                        sql = ("call insersionProveedores"
                            "('{0}','{1}','{2}','{3}');"
                            .format(self.ids.ti_nombreP.text,
                            self.ids.ti_direccion.text,
                            self.ids.ti_telefono.text,
                            self.ids.ti_referencias.text))
                        self.parent.run_query(sql)
                    else:
                        if (self.ids.bt_actualizar2.state == 'down'):
                            sql = ("call actualizarProveedores"
                                "('{0}','{1}','{2}','{3}');"
                                .format(self.ids.ti_nombreP.text,
                                self.ids.ti_direccion.text,
                                self.ids.ti_telefono.text,
                                self.ids.ti_referencias.text))
                            self.parent.run_query(sql)
                    self.exitoP()
                    self.limpiar2()

    def borrado2(self):
        sql = "SELECT NOMBREPR,DIRECCION,TELEFONO,REFERENCIAS"
        sql += "FROM PROVEEDORES "
        sql += "WHERE NOMBREP='{0}';" .format(self.ids.ti_nombreP.text)
        datos = self.parent.run_query(sql)
        self.ids.ti_nombreP.text = str(datos[0][0])
        self.ids.ti_direccion.text = str(datos[0][1])
        self.ids.ti_telefono.text = str(datos[0][2])
        self.ids.ti_referencias.text = str(datos[0][3])

    def limpiar2(self):
        self.ids.ti_nombreP.text = ''
        self.ids.ti_direccion.text = ''
        self.ids.ti_telefono.text = ''
        self.ids.ti_referencias.text = ''
        self.ids.ti_nombreP.hint_text = "Ingresa Provedor"
        self.ids.ti_direccion.hint_text = "Ingresa Dirección"
        self.ids.ti_telefono.hint_text = "Ingresa Teléfono"
        self.ids.ti_referencias.hint_text = "Ingresa Referencias"
        self.ids.bt_insertar2.state = 'normal'
        self.ids.bt_actualizar2.state = 'normal'

    def validar3(self):
        d2 = self.ids.ti_cantidad.text
        d3 = self.ids.ti_precio.text
        a1 = (d2, d3)
        if '' in a1:
            self.errorP()
        else:
            if len(self.ids.ti_precio.text) < 3:
                self.errorL()
            else:
                sql = ("SELECT EXISTENCIAS FROM MERCANCIA "
                        "WHERE MERCANCIA.ID_MERCANCIA='Vi0';")
                cantidad = self.parent.run_query(sql)
                print cantidad
                cantidad = cantidad[0][0]
                print cantidad
                if (int(self.ids.ti_cantidad.text)) <= (cantidad):
                    sql = ("SELECT PRECIOMINIMO FROM MERCANCIA "
                            "WHERE MERCANCIA.ID_MERCANCIA='Vi0';")
                    precio = self.parent.run_query(sql)
                    print precio
                    precio = precio[0][0]
                    print precio
                    if (int(self.ids.ti_precio.text)) >= (precio):
                        sql = ("call insersionVentas('Vi0','{0}','{1}','{2}');"
                                .format(self.ids.ti_precio.text,
                                self.ids.ti_cantidad.text,
                                self.ids.ti_total.text))
                        self.parent.run_query(sql)
                        self.exitoP()
                        self.limpiar3()
                    else:
                        self.errorC()
                else:
                    self.errorT()

    def infoCatVentas(self):
        sql = "SELECT *"
        sql += "FROM VENTAS; "
        datos = self.parent.run_query(sql)
        #str(datos[0][0])

    def limpiar3(self):
        self.ids.ti_cantidad.text = ''
        self.ids.ti_precio.text = ''
        self.ids.ti_total.text = ''
        self.ids.ti_cantidad.hint_text = "Ingresa Cantidad"
        self.ids.ti_precio.hint_text = "Ingresa Precio"
        self.ids.ti_total.hint_text = "0"
        self.ids.bt_insertar3.state = 'normal'

    def validar4(self):
        d1 = self.ids.ti_usuario.text
        d2 = self.ids.ti_password.text
        a1 = (d1, d2)
        al2 = (d2)
        if '' in a1 and (self.ids.bt_insertar.state == 'down'):
            self.errorP()
        else:
            if '' in al2 and (self.ids.bt_actualizar.state == 'down'):
                self.errorP()
                self.limpiar4()
            else:
                if (len(self.ids.ti_usuario.text) < 4
                    or len(self.ids.ti_password.text) < 4):
                    self.errorL()
                else:
                    if (self.ids.bt_insertar.state == 'down'):
                        sql = ("call insersionUsuarios('{0}','{1}','AD1');"
                                    .format(self.ids.ti_password.text,
                                    self.ids.ti_usuario.text))
                        self.parent.run_query(sql)
                    else:
                        if (self.ids.bt_actualizar.state == 'down'):
                            sql = ("call actualizarUsuarios('{0}','{1}','AD1');"
                                    .format(self.ids.ti_password.text,
                                    self.ids.ti_usuario.text))
                            self.parent.run_query(sql)
                    self.exitoP()
                    self.limpiar4()

    def borrado4(self):
        sql = "SELECT USUARIO,PASSWORD,NOMBGRUPO"
        sql += "FROM GRUPOS,USUARIOS "
        sql += "WHERE(USUARIOS.ID_GRUPO = GRUPOS.ID_GRUPO) "
        sql += "AND USUARIOS.USUARIO='{0}';" .format(self.ids.ti_usuario.text)
        datos = self.parent.run_query(sql)
        self.ids.ti_usuario.text = str(datos[0][0])
        self.ids.ti_password.text = str(datos[0][1])

    def limpiar4(self):
        self.ids.ti_usuario.text = ''
        self.ids.ti_password.text = ''
        self.ids.ti_usuario.hint_text = "Ingresa Usuario"
        self.ids.ti_password.hint_text = "Password"
        self.ids.bt_insertar.state = 'normal'
        self.ids.bt_actualizar1.state = 'normal'


class CamClick(Screen):
    pass


class Inicio(Screen):
    def errorP(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Uno o más campos vacíos",
                        pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def errorL(self):
        box = FloatLayout(size=(300, 300))
        label = Label(text="Usuario o contraseña incorrectos",
                                pos_hint={'x': 0, 'y': 0.2})
        btn1 = Button(text="Aceptar", size_hint=(0.5, 0.3),
                        pos_hint={'center_x': 0.5, 'center_y': 0.2})
        box.add_widget(label)
        box.add_widget(btn1)
        popup = Popup(title='¡Verificar Datos!', title_size=(20),
                        title_align = 'center', content = box,
                        size_hint=(None, None), size=(280, 180),
                        auto_dismiss = True)
        btn1.bind(on_press=popup.dismiss)
        popup.open()
        self.popup = popup

    def validarIni(self):
        d1 = self.ids.ti_userL.text
        d2 = self.ids.ti_passwordL.text
        a1 = (d1, d2)
        if '' in a1:
            self.errorP()
        else:
            try:
                con = MySQLdb.connect(host="127.0.0.1",
                                    user=self.ids.ti_userL.text,
                                    passwd=self.ids.ti_passwordL.text,
                                    db="lalibertad")
                SSQL = "SELECT ID_GRUPO FROM USUARIOS"
                SSQL += " WHERE USUARIO='{0}';" .format(self.ids.ti_userL.text)
                #sql = (SSQL)
                self.parent.usr = self.ids.ti_userL.text
                self.parent.pwd = self.ids.ti_passwordL.text
                tipoNivel = self.parent.run_query(SSQL)
                tipoNivel = tipoNivel[0]
                if (tipoNivel == 'VE2'):
                    self.parent.bloqueos()
                self.parent.cargarDatos()
                self.parent.menuP()
            except Exception:
                self.errorL()


class ScreenManagement(ScreenManager):
    def capture(self):
        for child in self.children:
            if child.name == 'camClick':
                camera = child.ids['camera']
                camera.export_to_png("LL_{}.png".format(self.nombreMerca))
                self.cambioImg()
                self.opciones_mercancias()

    def cambioImg(self):
        for child in self.children:
            if child.name == 'labelConfig':
                child.ids.bt_foto.background_normal = 'LL_{}.png'.format(self.nombreMerca)
                child.ids.bt_foto.background_disabled = 'LL_{}.png'.format(self.nombreMerca)
                child.ids.bt_foto.background_disabled_down = 'LL_{}.png'.format(self.nombreMerca)
                self.opciones_mercancias()

    def run_query(self, query=''):
        #user, passwd = Inicio().validarIni()
        datos = ["127.0.0.1", self.usr, self.pwd, "lalibertad"]
        conn = MySQLdb.connect(*datos)
        cursor = conn.cursor()
        cursor.execute(query)
        data = None
        if query.upper().startswith('SELECT'):
            data = cursor.fetchall()
        else:
            conn.commit()
            data = None
        cursor.close()
        conn.close()
        return data

    def inicial(self):
        self.current = 'cargar'

    def login(self):
        self.current = 'inicio'

    def opciones(self):
        self.current = 'labelConfig'

    def catalogoMer(self):
        self.current = 'mercanciasCat'

    def catalogoVen(self):
        self.current = 'ventasCat'

    def catalogoUser(self):
        self.current = 'usuariosCat'

    def catalogoProve(self):
        self.current = 'proveedoresCat'

    def catalogoInv(self):
        self.current = 'inventarioCat'

    def bloqueos(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                child.ids.bt_actualizar1.disabled = True
                child.ids.bt_actualizar2.disabled = True
                child.ids.bt_actualizar.disabled = True
                child.ids.bt_borrar1.disabled = True
                child.ids.bt_borrar2.disabled = True
                child.ids.bt_borrar.disabled = True
                child.ids.bt_insertar1.disabled = True
                child.ids.bt_insertar2.disabled = True
                child.ids.bt_insertar.disabled = True
                child.ids.bt_aceptar1.disabled = False
                child.ids.bt_cancelar1.disabled = False
                child.ids.bt_aceptar2.disabled = False
                child.ids.bt_cancelar2.disabled = False
                child.ids.bt_aceptar3.disabled = False
                child.ids.bt_cancelar3.disabled = False
                child.ids.bt_aceptar.disabled = False
                child.ids.bt_cancelar.disabled = False

    def cargarDatos(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                sql = ("SELECT NOMBREP FROM MERCANCIA WHERE STATUSMERCANCIA=1;")
                valores = self.run_query(sql)
                v = [e[0] for e in valores]
                child.ids.sp_nombreM.values = v
                child.ids.sp_producto.values = v
                sql2 = ("SELECT NOMBREPR FROM PROVEEDORES WHERE STATUSPROVEEDOR=1;")
                valores2 = self.run_query(sql2)
                v2 = [e[0] for e in valores2]
                child.ids.sp_proveedor.values = v2
                child.ids.sp_proveedores.values = v2
                sql3 = ("SELECT TIPO FROM TIPOMERCANCIA WHERE STATUSTIPO=1;")
                valores3 = self.run_query(sql3)
                v3 = [e[0] for e in valores3]
                child.ids.sp_tipo.values = v3
                sql4 = ("SELECT USUARIO FROM USUARIOS WHERE STATUSUSUARIO=1;")
                valores4 = self.run_query(sql4)
                v4 = [e[0] for e in valores4]
                child.ids.sp_user.values = v4
                sql5 = ("SELECT NOMBGRUPO FROM GRUPOS WHERE STATUSGRUPO=1;")
                valores5 = self.run_query(sql5)
                v5 = [e[0] for e in valores5]
                child.ids.sp_grupo.values = v5


    def opciones_mercancias(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'MERCANCIAS':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def opciones_proveedores(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'PROVEEDORES':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def opciones_ventas(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'VENTAS':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def opciones_usuarios(self):
        self.current = 'labelConfig'
        for child in self.children:
            if child.name == 'labelConfig':
                for box in child.children:
                    for acor in box.children:
                        for acori in acor.children:
                            if acori.title == 'USUARIOS':
                                acori.collapse = False
                            else:
                                acori.collapse = True

    def menuP(self):
        self.current = 'paginaInicial'

    def camaraAccion(self):
        self.current = 'camClick'


class MainApp(App):
    def build(self):
        self.root = ScreenManagement()
        return self.root

if __name__ in ('__main__', '__android__'):
    MainApp().run()

