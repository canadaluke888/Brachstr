import difflib
from typing import Optional

class TextSimilarity:
    def __init__(self, threshold: float = 0.2):
        """
        Initialize the TextSimilarity model with a similarity threshold.
        :param threshold: The similarity threshold to determine braching (defualt is 0.6).
        """
        self.threshold = threshold

    def calculate_similarity(self, word1: str, word2: str) -> float:
        """
        Calculate the similarity between two words using SequenceMatcher from difflib.
        :param word1: The first word.
        :param word2: The second word.
        :return: A float representing the similaritty ration between the two words.
        """
        return difflib.SequenceMatcher(None, word1, word2).ratio()
    
    def find_best_match(self, word: str, tree: dict) -> Optional[str]:
        """
        Find the best match for a given word in the existing tree based on similarity.
        :param word: The word to match.
        :param tree: The current tree structure as a nested dictionary.
        :trturn: The best matching node, or None if no suitable match is found.
        """
        best_match = None
        best_similarity = 0.0

        # Recursively search for the best match in the tree
        def _recursive_search(current_tree, current_best_match, current_best_similariry):
            for node in current_tree:
                similarity = self.calculate_similarity(word, node)
                if similarity > current_best_similariry and similarity >= self.threshold:
                    current_best_match = node
                    current_best_similariry = similarity
                # Recurse into child nodes
                current_best_match, current_best_similariry = _recursive_search(current_tree[node], current_best_match, current_best_similariry)
            return current_best_match, current_best_similariry
        
        best_match, best_similarity = _recursive_search(tree, best_match, best_similarity)
        return best_match