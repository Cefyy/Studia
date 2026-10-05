import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '../api';
import { queryKeys } from '../keys';

export const useDeleteTodoMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (id: string) => {
      await apiClient.delete(`/todos/${id}`);
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.todos.all });
    },
  });
};
