# -*- coding: utf-8 -*-

import os
import sqlite3

def create_db(db_name):
    conn = sqlite3.connect(db_name)
    c= conn.cursor()
    
    query = """CREATE TABLE paises (id_pais integer PRIMARY KEY AUTOINCREMENT,
                                    nombre text)"""
      
    c.execute(query)
    
    query1 = """CREATE TABLE ciudades (id_ciudad integer primary key AUTOINCREMENT,
                                       nombre text,
                                       poblacion integer,
                                       fundacion date,
                                       superficie double,
                                       densidad double,
                                       gentilicio text,
                                       fk_id_pais integer,
                                       FOREIGN KEY (fk_id_pais) REFERENCES paises (id_pais))"""
    c.execute(query1)
                                       
    
if __name__ == "__main__":
    db_name = 'base12.db'
    if not os.path.exists(db_name):
        create_db(db_name)
        
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    query= "INSERT INTO paises(id_pais,nombre) VALUES (?,?)"
    
    p1=["1","Alemania"]
    p2=["2","Argentina"]
    p3=["3","Australia"]
    p4=["4","Canada"]
    p5=["5","Chile"]
    p6=["6","Colombia"]
    p7=["7","Egipto"]
    p8=["8","Estados Unidos"]
    p9=["9","Filipinas"]
    p10=["10","Francia"]
    p11=["11","Grecia"]
    p12=["12","India"]
    p13=["13","Israel"]
    p14=["14","Italia"]
    p15=["15","Japon"]
    p16=["16","Marruecos"]
    p17=["17","Mexico"]
    p18=["18","Polonia"]
    p19=["19","Reino Unido"]
    p20=["20","Vaticano"]
    
    c.execute("INSERT into paises VALUES (?,?)",p1)
    c.execute("INSERT into paises VALUES (?,?)",p2)
    c.execute("INSERT into paises VALUES (?,?)",p3)
    c.execute("INSERT into paises VALUES (?,?)",p4)	
    c.execute("INSERT into paises VALUES (?,?)",p5)
    c.execute("INSERT into paises VALUES (?,?)",p6)
    c.execute("INSERT into paises VALUES (?,?)",p7)
    c.execute("INSERT into paises VALUES (?,?)",p8)
    c.execute("INSERT into paises VALUES (?,?)",p9)	
    c.execute("INSERT into paises VALUES (?,?)",p10)
    c.execute("INSERT into paises VALUES (?,?)",p11)
    c.execute("INSERT into paises VALUES (?,?)",p12)
    c.execute("INSERT into paises VALUES (?,?)",p13)
    c.execute("INSERT into paises VALUES (?,?)",p14)	
    c.execute("INSERT into paises VALUES (?,?)",p15)
    c.execute("INSERT into paises VALUES (?,?)",p16)
    c.execute("INSERT into paises VALUES (?,?)",p17)
    c.execute("INSERT into paises VALUES (?,?)",p18)
    c.execute("INSERT into paises VALUES (?,?)",p19)	
    c.execute("INSERT into paises VALUES (?,?)",p20)
    conn.commit()
    	
    	
    query = "INSERT INTO ciudades (id_ciudad,nombre,poblacion,fundacion,superficie,densidad,gentilicio,fk_id_pais) VALUES(?,?,?,?,?,?,?,?,)"
   
    r1 =["22","Berlin","3.531.201","1307","891.85","3.845","Berlines","1"]
    r2 =["23","Mar del Plata","616.142","10-02-1874","79,48","7752,2","Marplatense","2"]
    r3 =["24","Melbourne","4.246.345","1835","17.153","1767.8","Melburniano","3"]
    r4 =["25","Vancouver","603.502","06-04-1886","114,97","5.25","Vancouverense","4"]
    r5 =["26","Valdvia","154.445","09-02-1552","1.016","138.35","Valdiviano","5"]
    r6 =["27","Barranquilla","1.206.946","1627-1637","154","948","Barranquillero","6"]
    r7 =["28","Alejandria","3.917.082","332 a.c","2.679","1.034","Alejandrino","7"]
    r8 =["29","El Cairo","8.259.461","116 a.c","214","38.596","Cairota","7"]
    r9 =["30","New York","8.175.133","1624","1214.4","6731.83","Neoyorkino","8"]
    r10 =["31","Los Angeles","3.792.621","04-09-1781","1290.6","2938.65","Angelino","8"]
    r11 =["32","Manila","1.660.714","24-06-1571","38.55","43079.48","Manileno","9"]
    r12 =["33","Paris","2.257.981","52 a.c","105,40","21.423","Parisino","10"]
    r13 =["34","Versalles","86.110","1789","26.18","3289,15","Versaillais","10"]
    r14 =["35","Atenas","3.158.400","7000 a.c","411.717","19.133","Ateniense","11"]
    r15 =["36","Nueva Delhi","13.800.000","1911","1.483","9.294","Indio","12"]
    r16 =["37","Jerusalen","804.355","3000 a.c","152.2","6424.56","Jerosolimitano","13"]
    r17 =["38","Florencia","378.235","59 a.c","102","3708.19","Florentinos","14"]
    r18 =["39","Venecia","270.884","siglo V","4146","653.41","Veneciano","15"]
    r19 =["40","Londres","8.308.369","43 d.c","1570","5285","Londinenses","19"]
    r20 =["41","Ciudad del Vaticano","932","1929","0.44","2118","Vaticano","20"]
    
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r1)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r2)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r3)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r4)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r5)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r6)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r7)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r8)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r9)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r10)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r11)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r12)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r13)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r14)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r15)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r16)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r17)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r18)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r19)
    c.execute("INSERT INTO ciudades VALUES (?,?,?,?,?,?,?,?)",r20)
    conn.commit()
