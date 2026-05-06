# AI Dungeon Master Pro

AI Dungeon Master Pro is a modular Python-based RPG that uses AI-driven narration, game state management, and interactive player input.

## Features

- Character creation and storage (JSON)
- Turn-based game loop
- AI-generated narration using prompt engineering
- Scenario detection (combat, dialogue, movement, exploration)
- Dice-based mechanics for combat and skill checks
- Game state tracking (HP, location, quests, history)
- Retrieval-Augmented Generation (RAG) for contextual responses
- Save and load system for persistent gameplay
- Memory of recent actions for continuity
- Dynamic NPC generation

## AI Model Setup

This project uses a local LLM via Ollama for narration generation.

### Setup Instructions

1. Install Ollama: https://ollama.com  
2. Pull and run a model:
   ```bash
   ollama run llama3

## How to Run

1. Make sure you have Python 3 installed  
2. Run the program:

```bash
python main.py
