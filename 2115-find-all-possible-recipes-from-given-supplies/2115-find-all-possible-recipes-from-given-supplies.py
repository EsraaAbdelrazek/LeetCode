from typing import List
from collections import defaultdict, deque

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        indegree = {}  # Track how many ingredients are needed for each recipe
        graph = defaultdict(list)  # Ingredient -> list of recipes that need it

        # Initialize indegree and graph
        for i in range(len(recipes)):
            recipe = recipes[i]
            indegree[recipe] = len(ingredients[i])
            for ing in ingredients[i]:
                graph[ing].append(recipe)

        queue = deque(supplies)
        available = set(supplies)
        result = []

        # BFS to process ingredients and recipes
        while queue:
            current = queue.popleft()

            for recipe in graph[current]:
                indegree[recipe] -= 1
                if indegree[recipe] == 0:
                    queue.append(recipe)
                    available.add(recipe)
                    result.append(recipe)

        return result
