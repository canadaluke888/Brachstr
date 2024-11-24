# Brachstr

Brachstr is a command-line application that allows users to create and visualize "string trees" interactively by adding words that form a branching structure based on text similarity. It leverages a text similarity model to determine the placement of words within the tree, making it possible to build organized hierarchies of related terms.

## Features
- **Interactive Command-Line Interface**: Add words to the tree, print the tree, and interact with it all from an easy-to-use terminal interface.
- **Text Similarity-Based Tree Structure**: Words are grouped based on their similarity, using a configurable similarity threshold.
- **Tree Visualization**: Visualize the tree structure in a clear, readable way using the `rich` library.

## Installation
To get started with Brachstr, clone this repository and install the necessary Python packages.

### Prerequisites
- Python 3.8 or later
- `rich` for terminal visualization

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/brachstr.git
   cd brachstr
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the main application using Python:
```bash
python main.py
```

Upon starting the application, you will see a welcome message and a list of available commands:
- **add [word]**: Add a word to the tree. The application will determine the best location based on similarity.
- **print**: Print the current structure of the tree.
- **exit**: Exit the application.

### Example Session
```
Welcome to Brachstr!
Commands: add [word], print, exit
>> add music
Added 'music' as a new root node.
>> add dance
Added 'dance' as a new root node.
>> add dancing
Added 'dancing' under 'dance'.
>> print
Current Tree Structure:
music
dance
  └── dancing
>> exit
Exiting Brachstr. Goodbye!
```

## Project Structure
The project is organized into different modules to ensure separation of concerns:
- **`main.py`**: The main application that runs the command-line interface.
- **`tree.py`**: Manages the tree structure, allowing nodes to be added and the entire tree to be retrieved.
- **`text_similarity.py`**: Handles text similarity calculations and helps determine the best node for adding a word.
- **`tree_visualizer.py`**: Uses the `rich` library to print the tree structure in a visually appealing way.

## Requirements
- Python 3.8+
- `rich` (for tree visualization)

You can install the requirements via:
```bash
pip install -r requirements.txt
```

## Contributing
Feel free to contribute to Brachstr! If you encounter any issues or have feature suggestions, please open an issue or submit a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](Brachstr/LICENSE) file for details.

