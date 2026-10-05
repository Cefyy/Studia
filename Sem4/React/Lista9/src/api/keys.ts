export const queryKeys = {
  todos: {
    all: ['todos'] as const,
    filtered: (filter: string) => ['todos', { filter }] as const,
  },
};
