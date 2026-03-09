import type { FilterType } from '../types';
import './FilterBar.css';

interface FilterBarProps {
  filter: FilterType;
  setFilter: (f: FilterType) => void;
  search: string;
  setSearch: (s: string) => void;
}

export default function FilterBar({ filter, setFilter, search, setSearch }: FilterBarProps) {
  const filters: FilterType[] = ['all', 'active', 'completed'];
  const filterLabels: Record<FilterType, string> = {
    all: 'All',
    active: 'Active',
    completed: 'Done'
  };

  return (
    <div className="filter-bar">
      <input
        type="text"
        placeholder="Filter list..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />
      <div className="filter-group">
        {filters.map((f) => (
          <button
            key={f}
            onClick={() => setFilter(f)}
            className={filter === f ? 'active' : ''}
          >
            {filterLabels[f]}
          </button>
        ))}
      </div>
    </div>
  );
}