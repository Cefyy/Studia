import { useState, useEffect } from 'react';
import type { Todo } from './types';
import { fetchTodos, createTodo, updateTodo, deleteTodo as deleteTodoApi } from './api';
import { TodoForm } from './components/TodoForm';
import { TodoList } from './components/TodoList';
import './App.css';

function App() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const data = await fetchTodos();
      setTodos(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error loading list');
    } finally {
      setIsLoading(false);
    }
  };

  const handleAddTodo = async (text: string) => {
    const newTodo = await createTodo({ text });
    setTodos(prev => [...prev, newTodo]);
  };

  const handleToggleTodo = async (id: string, done: boolean) => {
    const todoToToggle = todos.find(t => t.id === id);
    if (!todoToToggle) return;
    
    // Server expects both text and done for PUT
    const updatedTodo = await updateTodo(id, { text: todoToToggle.text, done });
    setTodos(prev => prev.map(t => t.id === id ? updatedTodo : t));
  };

  const handleDeleteTodo = async (id: string) => {
    await deleteTodoApi(id);
    setTodos(prev => prev.filter(t => t.id !== id));
  };

  return (
    <div className="app-container">
      <header>
        <h1>ToDo App</h1>
      </header>
      
      <main>
        <TodoForm onAdd={handleAddTodo} />
        
        {error && (
          <div className="error-message global-error">
            {error}
            <button onClick={loadTodos}>Retry</button>
          </div>
        )}
        
        {isLoading ? (
          <div className="loading-state">Loading tasks...</div>
        ) : (
          <TodoList 
            todos={todos} 
            onToggle={handleToggleTodo} 
            onDelete={handleDeleteTodo} 
          />
        )}
      </main>
    </div>
  );
}

export default App;
