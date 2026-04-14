import AddRecipeForm from './components/AddRecipeForm'
import FilterBar from './components/FilterBar'
import RecipeList from './components/RecipeList'
import { useRecipeStore } from './useRecipeStore'
import './App.css'

function App() {
  const recipes = useRecipeStore((state) => state.recipes)
  const totalRecipes = recipes.length
  const favoriteRecipes = recipes.filter((recipe) => recipe.isFavorite).length

  return (
    <main className="app-shell">
      <div className="app-container">
        <header className="app-header">
          <p className="eyebrow">Zustand edition</p>
          <h1>My Recipe Book</h1>
          <p className="app-description">
            Dodawaj przepisy, oznaczaj ulubione i filtruj listę po nazwie lub treści.
          </p>
          <div className="app-stats" aria-label="Recipe statistics">
            <span>{totalRecipes} recipes</span>
            <span>{favoriteRecipes} favorites</span>
          </div>
        </header>

        <AddRecipeForm />
        <FilterBar />
        <RecipeList />
      </div>
    </main>
  )
}

export default App
