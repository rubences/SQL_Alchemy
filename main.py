import productos.db
from productos.models import Producto
def run():
    pass
if __name__ == '__main__':
    db.Base.metadata.create_all(productos.db.engine)
    run()