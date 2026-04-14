import RecipeItem from './RecipeItem'

import { useRecipeStore } from '../useRecipeStore'

import './RecipeList.css'

export default function RecipeList() {
  const recipes = useRecipeStore((state) => state.recipes)
  const showOnlyFavorites = useRecipeStore((state) => state.showOnlyFavorites)
  const searchTerm = useRecipeStore((state) => state.searchTerm)

  const normalizedSearchTerm = searchTerm.trim().toLowerCase()
  const visibleRecipes = recipes.filter((recipe) => {
    if (showOnlyFavorites && !recipe.isFavorite) {
      return false
    }

    if (!normalizedSearchTerm) {
      return true
    }

    const title = recipe.title.toLowerCase()
    const content = recipe.content.toLowerCase()

    return title.includes(normalizedSearchTerm) || content.includes(normalizedSearchTerm)
  })

  return (
    <div className="recipe-list">
      {visibleRecipes.length === 0 ? (
        <p className="recipe-list-empty">No recipes found</p>
      ) : (
        visibleRecipes.map((recipe) => <RecipeItem key={recipe.id} recipe={recipe} />)
      )}
    </div>
  )
}