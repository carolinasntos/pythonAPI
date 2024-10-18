from dotenv import load_dotenv
import os

load_dotenv()

# Verifica que DATABASE_URL esté cargado correctamente
print(os.getenv('DATABASE_URL'))