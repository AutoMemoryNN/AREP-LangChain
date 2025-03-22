# LangChain LLM Chain Tutorial

Este repositorio contiene una implementación del tutorial básico de LangChain LLM Chain utilizando OpenAI y siguiendo los conceptos fundamentales de la documentación oficial.

## Arquitectura y Componentes

Este proyecto implementa un simple traductor de texto de inglés a otros idiomas utilizando LangChain y OpenAI. La arquitectura se compone de:

1. **Modelo de Lenguaje (LLM)**: Utilizamos el modelo `gpt-4o-mini` de OpenAI como nuestro modelo de chat.
2. **Plantilla de Prompts**: Implementamos una plantilla de prompts para estructurar las instrucciones de traducción.
3. **Integración con LangSmith**: Para el seguimiento y la depuración de las llamadas al modelo.

## Requisitos

- Python 3.8+
- Cuenta de OpenAI con API key
- (Opcional) Cuenta de LangSmith para trazabilidad

## Instalación

1. Clonar este repositorio:
```bash
git clone https://github.com/tu-usuario/langchain-llm-chain-tutorial.git
cd langchain-llm-chain-tutorial
```

2. Instalar las dependencias:
```bash
pip install -r requirements.txt
```

3. Configurar las variables de entorno:
- Crea un archivo `.env` en el directorio raíz con el siguiente contenido:
```
OPENAI_API_KEY=tu_clave_api_de_openai
LANGSMITH_API_KEY=tu_clave_api_de_langsmith (opcional)
LANGSMITH_TRACING=true (opcional)
```

## Uso

Ejecuta el script principal:

```bash
python translate.py
```

También puedes ejecutar el notebook de Jupyter:

```bash
jupyter notebook LLM_Chain_Tutorial.ipynb
```

## Estructura del Repositorio

```
├── README.md
├── requirements.txt
├── .env.example
├── translate.py
└── LLM_Chain_Tutorial.ipynb
```

## Ejemplos

### Funcionamiento de la aplicación

![Ejemplo de Traducción](screenshots/traduccion_ejemplo.png)

Este ejemplo muestra la traducción de "Hello, how are you?" del inglés al español.

## Recursos Adicionales

- [Documentación de LangChain](https://python.langchain.com/docs/)
- [Tutorial oficial de LLM Chain](https://python.langchain.com/docs/tutorials/llm_chain/)
- [Documentación de OpenAI](https://platform.openai.com/docs/api-reference)