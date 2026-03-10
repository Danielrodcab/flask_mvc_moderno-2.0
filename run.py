from app import create_app, db

app = create_app()

with app.app_context():
    db.create_all()   # Crea las tablas en la base de datos si no existen
    # ORM (Object Relational Mapping): Permite interactuar con la base de datos usando objetos en lugar de escribir SQL directamente.

import os

if __name__ == "__main__":
    # Railway asigna un puerto dinámico, lo tomamos de las variables de entorno
    port = int(os.environ.get("PORT", 5000))
    # host='0.0.0.0' permite que el servidor acepte conexiones externas
    # debug=False es lo recomendado para producción en Railway
    app.run(host='0.0.0.0', port=port, debug=False)
