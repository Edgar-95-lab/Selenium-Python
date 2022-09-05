from xml.dom import minidom


class xmlReader:
    def __init__(self):
        self.document = minidom.parse('./Config/configuration.xml')

    def obtener_datos(self, dato):
        item = self.document.getElementsByTagName(dato)[0].firstChild.nodeValue
        return item