class Carro: #guardar sesiones
    def __init__(self, request):
        self.request=request
        self.session=request.session
        carro=self.session.get("carro")
        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro #continuar agregando si se va
            
    def agregar(self,hamburguesas):
        if(str(hamburguesas.id)not in self.carro.keys()): #si no se encuentra el id del producto que lo agregue
            self.carro[hamburguesas.id]={
                "hamburguesas_id":hamburguesas.id,
                "nombre":hamburguesas.title,
                "precio":str(hamburguesas.precio),
                "cantidad":1,  # Utiliza la cantidad proporcionada
                "imagen":hamburguesas.image1.url,
            }
        else:
            for key, value in self.carro.items():
                if key==str(hamburguesas.id):
                    value["cantidad"]=value["cantidad"]+1 #incrementando en 1
                    value["precio"]=float(value["precio"])+hamburguesas.precio
                    break
        self.guardar_carro()#guardar la sesion  actualizar

    def guardar_carro(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, hamburguesas):
        hamburguesas.id=str(hamburguesas.id)
        if hamburguesas.id in self.carro:
            del self.carro[hamburguesas.id] #eliminar
            self.guardar_carro()     #guardar
        
    def restar_producto(self, hamburguesas):
        for key, value in self.carro.items():
                if key==str(hamburguesas.id):
                    value["cantidad"]=value["cantidad"]-1 #incrementando en 1
                    value["precio"]=float(value["precio"])-hamburguesas.precio
                    if value["cantidad"]<1:
                        self.eliminar(hamburguesas)
                    break
        self.guardar_carro()  

    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True
        


    
       


    
    