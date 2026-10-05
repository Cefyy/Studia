
import { useTodosQuery } from '../api/todos/useTodosQuery';
import { useToggleTodoMutation } from '../api/todos/useToggleTodoMutation';
import { useDeleteTodoMutation } from '../api/todos/useDeleteTodoMutation';
import './TodoList.css';

interface Props {
  filter: 'all' | 'done' | 'active';
}

export const TodoList: React.FC<Props> = ({ filter }) => {
  const { data: todos, isPending, isError, isFetching } = useTodosQuery(filter);
  const toggleMutation = useToggleTodoMutation();
  const deleteMutation = useDeleteTodoMutation();

  if (isPending) return <p>Ładowanie...</p>;
  if (isError) return <p className="error">Błąd pobierania zadań.</p>;

  return (
    <div className="todo-list">
      {isFetching && !isPending && <p className="fetching-indicator">Odświeżanie...</p>}
      
      {toggleMutation.isError && <p className="error">Błąd podczas edycji zadania.</p>}
      {deleteMutation.isError && <p className="error">Błąd podczas usuwania zadania.</p>}

      <ul>
        {todos?.map(todo => (
          <li key={todo.id} className={todo.done ? 'done' : ''}>
            <span onClick={() => toggleMutation.mutate(todo)} style={{ cursor: 'pointer', textDecoration: todo.done ? 'line-through' : 'none' }}>
              {todo.text}
            </span>
            <button 
              onClick={() => deleteMutation.mutate(todo.id)}
              disabled={deleteMutation.isPending}
            >
              Usuń
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
};
