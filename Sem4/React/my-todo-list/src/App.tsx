import { useState, useMemo } from 'react';
import type { Todo, FilterType } from './types';
import TodoForm from './components/TodoForm';
import TodoItem from './components/TodoItem';
import FilterBar from './components/FilterBar';
import './App.css';

export default function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [filter, setFilter] = useState<FilterType>('all');
  const [search, setSearch] = useState('');

  const addTodo = (text: string) => {
    setTodos((prev) => [...prev, {
      id: Date.now(),
      text,
      completed: false,
    }]);
  };

  const toggleTodo = (id: number) => {
    setTodos((prev) =>
      prev.map((t) => (t.id === id ? { ...t, completed: !t.completed } : t))
    );
  };

  const deleteTodo = (id: number) => {
    setTodos((prev) => prev.filter((t) => t.id !== id));
  };

  const filteredTodos = useMemo(() => {
    return todos
      .filter((t) => {
        if (filter === 'active') return !t.completed;
        if (filter === 'completed') return t.completed;
        return true;
      })
      .filter((t) => t.text.toLowerCase().includes(search.toLowerCase()));
  }, [todos, filter, search]);

  return (
    <div className="app-container">
      <h1>Lista Zadań</h1>
      <TodoForm onAdd={addTodo} />
      <FilterBar
        filter={filter}
        setFilter={setFilter}
        search={search}
        setSearch={setSearch}
      />
      <ul className="todo-list">
        {filteredTodos.map((todo) => (
          <TodoItem
            key={todo.id}
            todo={todo}
            onToggle={toggleTodo}
            onDelete={deleteTodo}
          />
        ))}
      </ul>
    </div>
  );
}