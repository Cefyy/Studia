import type { Recipe } from '../types'
import { useRecipeStore } from '../useRecipeStore'

import './RecipeItem.css'

interface Props {
  recipe: Recipe
}

export default function RecipeItem({ recipe }: Props) {
  const toggleFavorite = useRecipeStore((state) => state.toggleFavorite)
  const deleteRecipe = useRecipeStore((state) => state.deleteRecipe)

  return (
    <article className={`recipe-item ${recipe.isFavorite ? 'favorite' : ''}`}>
      <div className="recipe-item-header">
        <h3>{recipe.title}</h3>
        {recipe.isFavorite ? <span className="favorite-chip">Favorite</span> : null}
      </div>
      <p>{recipe.content}</p>
      <div className="recipe-item-actions">
        <button type="button" className="favorite-btn" onClick={() => toggleFavorite(recipe.id)}>
          {recipe.isFavorite ? 'Unfavorite' : 'Favorite'}
        </button>
        <button type="button" className="delete-btn" onClick={() => deleteRecipe(recipe.id)}>
          Delete
        </button>
      </div>
    </article>
  )
}