from rich.tree import Tree as RichTree
from rich.console import Console

class TreeVisualizer:
    def __init__(self):
        self.console = Console()

    def visualize_tree(self, tree_data: dict):
        """
        Visualize the tree structure using the Rich library.
        :param tree_data: The tree data as a nested dictionary.
        """
        if not tree_data:
            self.console.print("[bold red]The tree is empty. Nothing to visualize.[/bold red]")
            return

        # Create the root of the visualization
        root_key = next(iter(tree_data))
        rich_tree = RichTree(f"[bold cyan]{root_key}[/bold cyan]")
        self._add_branches(tree_data[root_key], rich_tree)

        # Print the rich tree
        self.console.print(rich_tree)

    def _add_branches(self, current_branch: dict, rich_node):
        """
        Recursively add branches to the Rich tree node.
        :param current_branch: The current branch as a dictionary.
        :param rich_node: The rich node to add branches to.
        """
        for key, sub_branch in current_branch.items():
            # Add each branch to the tree
            new_node = rich_node.add(f"[bold green]{key}[/bold green]")
            self._add_branches(sub_branch, new_node)

# Example usage
if __name__ == "__main__":
    tree_data = {
        'animal': {
            'mammal': {
                'dog': {},
                'cat': {}
            },
            'reptile': {
                'lizard': {}
            }
        }
    }

    visualizer = TreeVisualizer()
    visualizer.visualize_tree(tree_data)
