import { useRecipeStore } from '../useRecipeStore'

import './FilterBar.css'

export default function FilterBar() {
  const showOnlyFavorites = useRecipeStore((state) => state.showOnlyFavorites)
  const searchTerm = useRecipeStore((state) => state.searchTerm)
  const setShowOnlyFavorites = useRecipeStore((state) => state.setShowOnlyFavorites)
  const setSearchTerm = useRecipeStore((state) => state.setSearchTerm)

  return (
    <div className="filter-bar">
      <input
        type="text"
        placeholder="Search by keyword..."
        value={searchTerm}
        onChange={(event) => setSearchTerm(event.target.value)}
      />
      <label className="filter-toggle">
        <input
          type="checkbox"
          checked={showOnlyFavorites}
          onChange={(event) => setShowOnlyFavorites(event.target.checked)}
        />
        Show Only Favorites
      </label>
    </div>
  )
}