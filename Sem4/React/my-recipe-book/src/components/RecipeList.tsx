import { useRecipes } from '../RecipeContext';
import RecipeItem from './RecipeItem';
import './RecipeList.css';

export default function RecipeList() {
  const { state } = useRecipes();
  const { filteredRecipes } = state;

  return (
    <div className="recipe-list">
      {filteredRecipes.map(recipe => (
        <RecipeItem key={recipe.id} recipe={recipe} />
      ))}
    </div>
  );
}
