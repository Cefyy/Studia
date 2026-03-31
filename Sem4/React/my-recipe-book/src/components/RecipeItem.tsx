import type { Recipe } from '../types';
import { useRecipes } from '../RecipeContext';
import './RecipeItem.css';

interface Props {
  recipe: Recipe;
}

export default function RecipeItem({ recipe }: Props) {
  const { dispatch } = useRecipes();

  return (
    <div className={`recipe-item ${recipe.isFavorite ? 'favorite' : ''}`}>
      <h3>{recipe.title}</h3>
      <p>{recipe.content}</p>
      <div className="recipe-item-actions">
        <button
          className="favorite-btn"
          onClick={() => dispatch({ type: 'TOGGLE_FAVORITE', payload: recipe.id })}
        >
          {recipe.isFavorite ? 'Unfavorite' : 'Favorite'}
        </button>
        <button
          className="delete-btn"
          onClick={() => dispatch({ type: 'DELETE_RECIPE', payload: recipe.id })}
        >
          Delete
        </button>
      </div>
    </div>
  );
}
