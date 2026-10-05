import { useQuery } from '@tanstack/react-query';
import { apiClient, type Todo } from '../api';
import { queryKeys } from '../keys';

export const useTodosQuery = (filter: 'all' | 'done' | 'active') => {
  return useQuery({
    queryKey: queryKeys.todos.filtered(filter),
    queryFn: async () => {
      let params = {};
      if (filter === 'done') params = { done: true };
      if (filter === 'active') params = { done: false };

      const { data } = await apiClient.get<Todo[]>('/todos', { params });
      return data;
    },
  });
};
