import { useState } from 'react';
import { AddTodoForm } from './components/AddTodoForm';
import { TodoList } from './components/TodoList';
import './App.css';

type FilterType = 'all' | 'done' | 'active';

function App() {
  const [filter, setFilter] = useState<FilterType>('all');

  return (
    <div className="app-container">
      <h1>ToDo App (TanStack Query)</h1>
      <AddTodoForm />
      
      <div className="filters">
        <button className={filter === 'all' ? 'active-filter' : ''} onClick={() => setFilter('all')}>Wszystkie</button>
        <button className={filter === 'active' ? 'active-filter' : ''} onClick={() => setFilter('active')}>Do zrobienia</button>
        <button className={filter === 'done' ? 'active-filter' : ''} onClick={() => setFilter('done')}>Ukończone</button>
      </div>

      <TodoList filter={filter} />
    </div>
  );
}

export default App;
