# -*- coding:utf-8 -*-

class amount_to_text:
    """
    Transforma de una cantidad numerica a cantidad en letra
    ej. 200 -> doscientos
    """

    def __init__(self):
        self._n1 = ( "un","dos","tres","cuatro","cinco","seis","siete","ocho",
            "nueve","diez","once","doce","trece","catorce","quince",
            "dieciseis","diecisiete","dieciocho","diecinueve","veinte")

        self._n11 =( "un","dos","tres","cuatro","cinco","seis","siete","ocho","nueve")

        self._n2 = ( "dieci","veinti","treinta","cuarenta","cincuenta","sesenta",
                "setenta","ochenta","noventa")

        self._n3 = ( "ciento","dosc","tresc","cuatroc","quin","seisc",
                "setec","ochoc","novec")
    
    def amount_to_text_cheque(self, nNumero, intermedio="pesos ", sufijo="M. N." ):
        nNumero = round( nNumero , 2)
        strCantEntera = self.amount_to_text(nNumero)
        intCantDecimal = self.extraeDecimales( nNumero )
        if intCantDecimal<=9:
            strCantDecimal="0%d"%(intCantDecimal)
        else:
            strCantDecimal="%d"%(intCantDecimal)
        strCantDecimal += "/100"
        return strCantEntera+' '+intermedio+' '+strCantDecimal+' '+sufijo
    
    def extraeDecimales(self, nNumero, max_digits=2):
        strDecimales = str( round(nNumero%1, 2) ).replace('0.','')
        strDecimales += "0"*max_digits
        strDecimales = strDecimales[0:max_digits]
        return long( strDecimales )
    
    def amount_to_text(self, nNumero, lFemenino=False):
        """
        NOTA: Solo numeros ENTEROS, omite los DECIMALES.
        amount_to_text(nNumero, lFemenino) --> cLiteral
            Convierte el numero a una cadena literal de caracteres
        P.e.:       201     -->   "doscientos uno"
                    1111     -->   "mil ciento once"

            <nNumero>       Numero a convertir
            <lFemenino>     = 'true' si el Literal es femenino
                            P.e.:   201     -->    "doscientas una"
        """
        # Nos aseguramos del tipo de <nNumero>
        # se podria adaptar para usar otros tipos (pe: float)
        nNumero = long(nNumero)
        if nNumero<0:       cRes = "menos " + self._amount_to_text(-nNumero, lFemenino)
        elif nNumero==0:    cRes = "cero"
        else:               cRes = self._amount_to_text(nNumero,lFemenino)
        
        # Excepciones a considerar
        if not lFemenino and nNumero%10 == 1 and nNumero%100!=11:
            cRes += "o"
        #cRes = cRes.upper()
        #cRes = cRes.capitalize()
        return cRes
    
    # Funcion auxiliar recursiva
    def _amount_to_text(self, n, lFemenino=0):
    
        # Localizar los billones    
        prim, resto = divmod(n, 10L**12)
        if prim != 0:
            if prim == 1:
                cRes = "un billon"
            else:
                cRes = self._amount_to_text(prim, 0) + " billones" # Billones es masculino

            if resto!=0:
                cRes += " " + self._amount_to_text(resto, lFemenino)
    
        else:
        # Localizar millones
            prim,resto = divmod(n, 10**6)
            if prim != 0:
                if prim == 1: cRes = "un millon"
                else: cRes = self._amount_to_text(prim, 0) + " millones" # Millones es masculino
                if resto != 0: cRes += " " + self._amount_to_text(resto, lFemenino)
    
            else:
            # Localizar los miles
                prim,resto = divmod(n,10**3)
                if prim!=0:
                    if prim==1: cRes="un mil"
                    else:       cRes=self._amount_to_text(prim,lFemenino)+" mil"
    
                    if resto!=0: cRes += " " + self._amount_to_text(resto,lFemenino)
    
                else:
                # Localizar los cientos
                    prim,resto=divmod(n,100)
                    if prim!=0:
                        if prim==1:
                            if resto==0:        cRes="cien"
                            else:               cRes="ciento"
                        else:
                            cRes=self._n3[prim-1]
                            if lFemenino:       cRes+="ientas"
                            else:               cRes+="ientos"
    
                        if resto!=0:  cRes+=" "+self._amount_to_text(resto,lFemenino)
    
                    else:
                    # Localizar las decenas
                        if lFemenino and n==1:              cRes="una"
                        elif n<=20:                         cRes=self._n1[n-1]
                        else:
                            prim,resto=divmod(n,10)
                            cRes=self._n2[prim-1]
                            if resto!=0:
                                if prim==2:                 cRes+=self._n11[resto-1]
                                else:                       cRes+=" y "+self._n1[resto-1]
    
                                if lFemenino and resto==1:  cRes+="a"
        return cRes
    
# Crear una demo interactiva
if __name__=="__main__":
    """
    lFemenino=(raw_input("En masculino o femenino? ( [M] / F ) ") in "Ff")
    num=raw_input("Dame un numero: ")
    print amount_to_text(num,lFemenino)
    raw_input("Presione cualquier tecla para continuar....")
    """
    #print amount_to_text().amount_to_text(5001)
    letra = amount_to_text().amount_to_text_cheque(1500.25, 'pesos', 'M. N.')
    letra = amount_to_text().amount_to_text(1500.25)
    print letra.upper()
