from app.core.config import *

print("App Name :", APP_NAME)
print("Version  :", APP_VERSION)
print("Groq Key :", GROQ_API_KEY[:10] + "..." if GROQ_API_KEY else "Not Found")
print("Uploads  :", UPLOAD_FOLDER)
print("Reports  :", REPORT_FOLDER)
print("Knowledge:", KNOWLEDGE_BASE)
print("ChromaDB :", CHROMA_DB)
print("BASE_DIR:", BASE_DIR)
print("DATABASE_URL:", DATABASE_URL)