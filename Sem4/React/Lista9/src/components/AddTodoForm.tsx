import { useState } from 'react';
import { useAddTodoMutation } from '../api/todos/useAddTodoMutation';
import './AddTodoForm.css';

export const AddTodoForm: React.FC = () => {
  const [text, setText] = useState('');
  const addMutation = useAddTodoMutation();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (text.trim()) {
      addMutation.mutate(text, {
        onSuccess: () => setText('')
      });
    }
  };

  return (
    <form onSubmit={handleSubmit} className="add-todo-form">
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Nowe zadanie..."
        disabled={addMutation.isPending}
      />
      <button type="submit" disabled={addMutation.isPending}>
        {addMutation.isPending ? 'Dodawanie...' : 'Dodaj'}
      </button>
      {addMutation.isError && <p className="error">Błąd dodawania zadania.</p>}
    </form>
  );
};
