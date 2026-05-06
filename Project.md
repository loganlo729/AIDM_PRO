## Dungeon Master Pro

## Use Case Diagram  
[Use Case](UseCase.png)

## 1. Base System Functionality (30 pts)

## Feature Description  
The system acts as a single player AI-powered Dungeon Master. After creating a character, the user enters a loop where they input actions. The system processes each action, rolls dice, retrieves context, and generates a response. Game state is updated after each action, and the game state can be saved and loaded.

## Scenarios Implemented  
The system can handle the following scenarios:

- Combat (attack actions with dice rolls and damage)  
- Dialogue (interacting with NPCs)  
- Movement (changing location, running, moving)  
- Exploration (general environment interaction)  
- Quests (tracking progress based on actions)  
- State tracking (history, enemy HP, location)
- Game termination conditions (player defeat and enemy defeat)

## How This Fits the Project  
These scenarios demonstrate a working AI system that processes input, applies logic, and generates output. This demonstrates AI-based behavior and a structured system design.

## 2. Prompt Engineering & Model Parameter Choice

## Prompt Design  
The system uses structured prompts that include:

- Character information (name, class)  
- Player action  
- Retrieved context (lore and memory)  
- Dice roll result  
- Narration instructions

Example structure:

"You are a Dungeon Master.  
Character: Joe, Fighter  
Context: Goblins are small, aggressive creatures.  
Dice Roll: 15  
Player Action: attack goblin  
Respond with immersive narration."

## Parameter Choices  
- Temperature: ~0.7–0.9 for creative storytelling  
- Max Tokens: ~200–400 to control response length  
- Top-p: 1.0 for diversity  

## Rationale
Different prompt configurations are used depending on the scenario. Combat scenarios prioritize structured responses to ensure consistency with game logic and math, while dialogue and exploration scenarios use higher creativity settings to enhance immersion and world design.
Constraints prevent the model from generating outcomes that conflict with system-calculated results (e.g., avoiding duplicate damage events).

## 3. Tools Usage

## Tools Implemented  
- Dice rolling using Python `random`  
- JSON storage for character data  
- State tracking system

## Example  
Dice rolls determine outcomes:

roll = roll_d20()

Used in combat, skill checks, and decision-making.

## Integration  
Tools are integrated into the action-processing pipeline to simulate game mechanics, demonstrating use of Python libraries and system design.

## 4. Planning & Reasoning

## Multi-Step Reasoning  
The actions below are taken in order on a given turn:
1. Interpret input
2. Classify scenario
3. Roll dice
4. Apply logic (combat, movement, etc.)
5. Retrieve context  
6. Generate prompt
7. Produce narration
8. Update state

## Scenario Classification  
Actions are categorized as:

- Combat  
- Dialogue  
- Movement  
- Exploration  

This determines how the system processes the input.

This pipeline improves consistency, realism, and narrative coherence by enabling the system to plan encounters, maintain context, and generate logical responses throughout gameplay.

## 5. RAG Implementation

## Data Source  
A dictionary is used to store lore such as monsters, environments, and rules.

## Implementation  
- Keywords in user actions trigger relevant lore retrieval
- Retrieved context is injected into prompts

## Example  
Input: "attack goblin"  
Retrieved: "Goblins are small, cunning creatures that prefer ambush tactics."

## Benefit  
This improves context awareness, narrative quality, and consistency. It demonstrates a simplified retrieval-augmented generation system.

## 6. Additional Tools / Innovation

## Features  
- Memory system (stores recent actions and injects into prompts)
- NPC generation (random names and roles for dialogue)
- Quest tracking (updates based on player actions)

## Impact  
These features improve immersion, continuity, and interactivity while demonstrating creative extensions of the system.

## 7. Code Quality & Modular Design

## Structure  
The project is organized into modules:

- main.py (entry point, character creation)
- game_loop.py (core logic)
- prompts.py (prompt construction)
- dice.py (dice rolling)  
- rag.py (context retrieval, NPC generation)
- state.py (game state management)
- llm.py (AI response handling)

## Benefits  
- Clear separation of responsibilities
- Reusable components
- Easy to expand

## Best Practices  
- Clean and readable functions
- Modular file design
- JSON-based persistence

## Conclusion  
The project presents a complete AI Dungeon Master system that uses prompt engineering, tool integration, structured reasoning, and retrieval-augmented generation. The modular design demonstrate a scalable and well-structured application of AI concepts that can be integrated into various iterations of the DnD system. The system emphasizes maintainability, allowing new gameplay features to be easily integrated in future development.