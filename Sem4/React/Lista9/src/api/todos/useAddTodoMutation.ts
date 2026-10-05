import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '../api';
import { queryKeys } from '../keys';

export const useAddTodoMutation = () => {
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: async (text: string) => {
      const { data } = await apiClient.post('/todos', { text, done: false });
      return data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: queryKeys.todos.all });
    },
  });
};
