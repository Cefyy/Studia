import { useEffect } from 'react';
import { useRecipes } from '../RecipeContext';
import './FilterBar.css';

export default function FilterBar() {
  const { state, dispatch } = useRecipes();
  const { showOnlyFavorites, searchTerm } = state;

  useEffect(() => {
    dispatch({ type: 'SET_SHOW_ONLY_FAVORITES', payload: showOnlyFavorites });
  }, [showOnlyFavorites, dispatch]);

  useEffect(() => {
    dispatch({ type: 'SET_SEARCH_TERM', payload: searchTerm });
  }, [searchTerm, dispatch]);


  return (
    <div className="filter-bar">
      <input
        type="text"
        placeholder="Search by keyword..."
        value={searchTerm}
        onChange={e => dispatch({ type: 'SET_SEARCH_TERM', payload: e.target.value })}
      />
      <label>
        <input
          type="checkbox"
          checked={showOnlyFavorites}
          onChange={e => dispatch({ type: 'SET_SHOW_ONLY_FAVORITES', payload: e.target.checked })}
        />
        Show Only Favorites
      </label>
    </div>
  );
}
