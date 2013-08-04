#!/usr/bin/python
# -*- coding: utf-8 -*-

import sqlite3

def connect():
    con = sqlite3.connect('base12.db')
    con.row_factory = sqlite3.Row
    return con
    
def get_ciudades():
    con = connect()
    c = con.cursor()
    query = """SELECT nombre, poblacion, fundacion, superficie, densidad, gentilicio FROM ciudades"""
    result = c.execute(query)
    ciudades = result.fetchall()
    con.close()
    return ciudades

def get_paises():
    con = connect()
    c = con.cursor()
    query = """SELECT paises.nombre FROM paises, ciudades WHERE ciudades.fk_id_pais = paises.id_pais"""
    result = c.execute(query)
    paises = result.fetchall()
    con.close()
    return paises

def obtener_paises(): #paises para el combobox
    con = connect()
    c = con.cursor()
    query = "SELECT id_pais, nombre FROM paises"
    result= c.execute(query)
    paises = result.fetchall()
    con.close()
    return paises

def delete(nombre):
    exito = False
    con = connect()
    c = con.cursor()
    query = "DELETE  FROM ciudades  WHERE nombre = ?"
    try:
        resultado = c.execute(query, [nombre])
        con.commit()
        exito = True
    except sqlite3.Error as e:
        exito = False
        print "Error:", e.args[0]
    con.close()
    return exito
    
 
