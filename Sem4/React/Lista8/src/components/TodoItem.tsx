import React, { useState } from 'react';
import type { Todo } from '../types';

interface TodoItemProps {
  todo: Todo;
  onToggle: (id: string, done: boolean) => Promise<void>;
  onDelete: (id: string) => Promise<void>;
}

export const TodoItem: React.FC<TodoItemProps> = ({ todo, onToggle, onDelete }) => {
  const [isUpdating, setIsUpdating] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleToggle = async () => {
    setIsUpdating(true);
    setError(null);
    try {
      await onToggle(todo.id, !todo.done);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error updating todo');
    } finally {
      setIsUpdating(false);
    }
  };

  const handleDelete = async () => {
    setIsDeleting(true);
    setError(null);
    try {
      await onDelete(todo.id);
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error deleting todo');
      setIsDeleting(false);
    }
  };

  return (
    <li className={"todo-item "}>
      <div className="todo-content">
        <input
          type="checkbox"
          checked={todo.done}
          onChange={handleToggle}
          disabled={isUpdating || isDeleting}
        />
        <span className="todo-title">{todo.text}</span>
      </div>
      
      <div className="todo-actions">
        {isUpdating && <span className="loading-text">Updating...</span>}
        <button 
          onClick={handleDelete} 
          disabled={isUpdating || isDeleting}
          className="delete-button"
        >
          {isDeleting ? 'Deleting...' : 'Delete'}
        </button>
      </div>
      {error && <div className="error-message item-error">{error}</div>}
    </li>
  );
};
