import { createContext, useReducer, useContext } from 'react';
import type { Dispatch, ReactNode } from 'react';
import type { Recipe } from './types';

interface State {
  recipes: Recipe[];
  filteredRecipes: Recipe[];
  showOnlyFavorites: boolean;
  searchTerm: string;
}

type Action =
  | { type: 'ADD_RECIPE'; payload: Recipe }
  | { type: 'DELETE_RECIPE'; payload: number }
  | { type: 'TOGGLE_FAVORITE'; payload: number }
  | { type: 'SET_SHOW_ONLY_FAVORITES'; payload: boolean }
  | { type: 'SET_SEARCH_TERM'; payload: string };

const initialState: State = {
  recipes: [
    { id: 1, title: 'Spaghetti Bolognese', content: 'Classic Italian dish.', isFavorite: false },
    { id: 2, title: 'Chicken Curry', content: 'Spicy and flavorful.', isFavorite: true },
  ],
  filteredRecipes: [],
  showOnlyFavorites: false,
  searchTerm: '',
};

const filterRecipes = (state: State): Recipe[] => {
  let recipes = state.recipes;
  if (state.showOnlyFavorites) {
    recipes = recipes.filter(recipe => recipe.isFavorite);
  }
  if (state.searchTerm) {
    const searchTerm = state.searchTerm.toLowerCase();
    recipes = recipes.filter(
      recipe =>
        recipe.title.toLowerCase().includes(searchTerm) ||
        recipe.content.toLowerCase().includes(searchTerm)
    );
  }
  return recipes;
};

const recipeReducer = (state: State, action: Action): State => {
  let newState: State;
  switch (action.type) {
    case 'ADD_RECIPE':
      newState = { ...state, recipes: [...state.recipes, action.payload] };
      break;
    case 'DELETE_RECIPE':
      newState = { ...state, recipes: state.recipes.filter(recipe => recipe.id !== action.payload) };
      break;
    case 'TOGGLE_FAVORITE':
      newState = {
        ...state,
        recipes: state.recipes.map(recipe =>
          recipe.id === action.payload ? { ...recipe, isFavorite: !recipe.isFavorite } : recipe
        ),
      };
      break;
    case 'SET_SHOW_ONLY_FAVORITES':
      newState = { ...state, showOnlyFavorites: action.payload };
      break;
    case 'SET_SEARCH_TERM':
      newState = { ...state, searchTerm: action.payload };
      break;
    default:
      return state;
  }
  return { ...newState, filteredRecipes: filterRecipes(newState) };
};

interface RecipeContextProps {
  state: State;
  dispatch: Dispatch<Action>;
}

const RecipeContext = createContext<RecipeContextProps | undefined>(undefined);

export const RecipeProvider = ({ children }: { children: ReactNode }) => {
  const [state, dispatch] = useReducer(recipeReducer, {
    ...initialState,
    filteredRecipes: initialState.recipes,
  });

  return (
    <RecipeContext.Provider value={{ state, dispatch }}>
      {children}
    </RecipeContext.Provider>
  );
};

export const useRecipes = () => {
  const context = useContext(RecipeContext);
  if (!context) {
    throw new Error('useRecipes must be used within a RecipeProvider');
  }
  return context;
};
