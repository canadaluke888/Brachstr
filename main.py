from tree import Tree
from text_similarity import TextSimilarity
from tree_visualizer import TreeVisualizer
from rich.console import Console

class BrachstrApp:
    def __init__(self):
        self.tree = Tree()
        self.similarity_model = TextSimilarity(threshold=0.2)
        self.console = Console()
        self.visualizer = TreeVisualizer()

    def run(self):
        self.console.print("[bold green]Welcome to Brachstr![/bold green]")
        self.console.print("[cyan]Commands:[/cyan] add [word], print, exit")
        while True:
            user_input = self.console.input("[bold blue]>> [/bold blue]").strip()
            if user_input.lower() == 'exit':
                self.console.print("[bold red]Exiting Brachstr. Goodbye![/bold red]")
                break
            elif user_input.startswith('add '):
                word = user_input[4:].strip()
                if word:
                    self.add_word(word)
                else:
                    self.console.print("[bold yellow]Please provide a word to add.[/bold yellow]")
            elif user_input.lower() == 'print':
                self.print_tree()
            else:
                self.console.print("[bold yellow]Unknown command. Please use 'add [word]', 'print', or 'exit'.[/bold yellow]")

    def add_word(self, word):
        """
        Add a word to the tree using the similarity model to determine placement.
        :param word: The word to add to the tree.
        """
        best_match = self.similarity_model.find_best_match(word, self.tree.get_tree())
        if best_match:
            self.tree.add_node(best_match, word)
            self.console.print(f"[bold green]Added '{word}' under '{best_match}'.[/bold green]")
        else:
            self.tree.add_node(None, word)
            self.console.print(f"[bold green]Added '{word}' as a new root node.[/bold green]")

    def print_tree(self):
        """
        Print the current tree structure using the TreeVisualizer.
        """
        self.console.print("[bold magenta]Current Tree Structure:[/bold magenta]")
        self.visualizer.visualize_tree(self.tree.get_tree())

if __name__ == "__main__":
    app = BrachstrApp()
    app.run()
