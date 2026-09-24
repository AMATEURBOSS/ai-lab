# ai-lab

My first AI project: a bilingual (English/Spanish) text summarizer that runs
an open-source model (Qwen3 4B) locally on my Mac using Ollama.

## Why I'm building this
This is the first step toward an AI assistant for a real estate company that
manages many properties and tenants in the U.S. and Mexico. Tenants write in
English and Spanish, so the goal is a model that understands and responds
naturally in **Mexican Spanish**: local vocabulary, tone, and phrasing,
not generic or Spain-style Spanish.

**Plan:** test open-source models locally, then fine-tune one on
Mexican Spanish property-management messages using my RTX 4090 PC.

## What it does
Paste in any text, like a tenant email, and it returns a summary in English and Spanish.

## How to run
1. Install [Ollama](https://ollama.com) and [uv](https://docs.astral.sh/uv/)
2. `ollama pull qwen3:4b`
3. `uv run main.py`

## What I learned
- Running open-source LLMs locally
- Calling a model from Python
- Small models make mistakes. The Spanish output had a grammar error
  ("Seré en casa" instead of "Estaré en casa"), so my next step is improving the prompt.

## Next steps
- Improve the prompt for better Spanish summaries
- Compare the local model vs. a cloud API
- Build a dataset of example tenant messages in Mexican Spanish
- Fine-tune a Qwen model for Mexican Spanish property management
