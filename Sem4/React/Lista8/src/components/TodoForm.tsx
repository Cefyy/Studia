import React, { useState } from 'react';

interface TodoFormProps {
  onAdd: (text: string) => Promise<void>;
}

export const TodoForm: React.FC<TodoFormProps> = ({ onAdd }) => {
  const [text, setText] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!text.trim()) return;

    setIsSubmitting(true);
    setError(null);

    try {
      await onAdd(text.trim());
      setText('');
    } catch (err) {
      setError(err instanceof Error ? err.message : 'Error adding todo');
    } finally {
      setIsSubmitting(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="todo-form">
      <input
        type="text"
        value={text}
        onChange={(e) => setText(e.target.value)}
        placeholder="Add a new task..."
        disabled={isSubmitting}
      />
      <button type="submit" disabled={isSubmitting || !text.trim()}>
        {isSubmitting ? 'Adding...' : 'Add'}
      </button>
      {error && <div className="error-message">{error}</div>}
    </form>
  );
};
