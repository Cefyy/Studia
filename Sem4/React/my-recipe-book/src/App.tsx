import { RecipeProvider } from './RecipeContext';
import AddRecipeForm from './components/AddRecipeForm';
import FilterBar from './components/FilterBar';
import RecipeList from './components/RecipeList';
import './App.css';

export default function App() {
  return (
    <RecipeProvider>
      <div className="app-container">
        <h1>My Recipe Book</h1>
        <AddRecipeForm />
        <FilterBar />
        <RecipeList />
      </div>
    </RecipeProvider>
  );
}
