import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient, type Todo } from '../api';
import { queryKeys } from '../keys';

export const useToggleTodoMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (todo: Todo) => {
      const { data } = await apiClient.put(`/todos/${todo.id}`, {
        ...todo,
        done: !todo.done,
      });
      return data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.todos.all });
    },
  });
};
