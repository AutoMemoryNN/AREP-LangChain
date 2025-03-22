# translate.py
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# Cargar variables de entorno desde el archivo .env
load_dotenv()

def main():
    # Verificar que la API key está configurada
    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: API key de OpenAI no encontrada. Por favor, configura la variable de entorno OPENAI_API_KEY.")
        return
    
    # Configurar LangSmith si está habilitado
    if os.environ.get("LANGSMITH_API_KEY") and os.environ.get("LANGSMITH_TRACING") == "true":
        print("LangSmith tracing habilitado para depuración y monitoreo.")
    
    print("🔹 Inicializando modelo de chat...")
    # Inicializar el modelo de chat
    model = init_chat_model("gpt-4o-mini", model_provider="openai")
    
    # Crear una plantilla de prompt para la traducción
    print("🔹 Creando plantilla de prompt...")
    system_template = "Translate the following from English into {language}"
    prompt_template = ChatPromptTemplate.from_messages(
        [("system", system_template), ("user", "{text}")]
    )
    
    # Interacción con el usuario
    print("\n🌐 Traductor de Idiomas con LangChain 🌐")
    print("----------------------------------")
    
    while True:
        text = input("\n📝 Texto en inglés (o 'salir' para terminar): ")
        if text.lower() in ["salir", "exit", "quit"]:
            print("👋 ¡Hasta pronto!")
            break
        
        language = input("🌍 Idioma de destino (e.g., Spanish, French, Italian): ")
        
        print("\n🔄 Traduciendo...")
        
        # Formatear el prompt con los valores proporcionados
        prompt = prompt_template.invoke({"language": language, "text": text})
        
        # Invocar el modelo para obtener la traducción
        try:
            response = model.invoke(prompt)
            print(f"\n✅ Traducción ({language}):")
            print(f"🗣️ {response.content}")
            
            # Mostrar información de tokens si está disponible
            if hasattr(response, 'response_metadata') and 'token_usage' in response.response_metadata:
                usage = response.response_metadata['token_usage']
                print(f"\nℹ️ Tokens utilizados: {usage.get('total_tokens', 'N/A')}")
        
        except Exception as e:
            print(f"\n❌ Error durante la traducción: {str(e)}")

if __name__ == "__main__":
    main()